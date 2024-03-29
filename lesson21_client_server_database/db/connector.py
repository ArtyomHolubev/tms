import sqlalchemy.exc
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select, delete
from asyncpg.exceptions import UniqueViolationError

from lesson21_client_server_database.db.models import User, Post, Comment, Like
from lesson21_client_server_database.structures import OperationStatus


class DatabaseConnector:

    def __init__(self, db_url):
        self._url = db_url
        self._engine = create_async_engine(self._url, echo=True)
        # *async_sessionmaker* call returns AsyncSession class object
        self._session = async_sessionmaker(self._engine)

    @staticmethod
    async def _get_user(
            session: AsyncSession,
            user_name: str,
            user_age: int
    ) -> User | None:
        return (
            await session.execute(
                select(User)
                .where(
                    User.name == user_name,
                    User.age == user_age
                )
            )
        ).unique().scalar_one_or_none()

    @staticmethod
    async def _get_post(
            session: AsyncSession,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str
    ) -> Post | None:

        return (
            await session.execute(
                select(Post)
                .join(User)
                .where(
                    User.name == user_name,
                    User.age == user_age,
                    Post.title == post_title,
                    Post.description == post_description
                )
            )
        ).unique().scalar_one_or_none()

    @staticmethod
    async def _get_post_by_title(
            session: AsyncSession,
            post_title: str,
            post_description: str
    ) -> Post | None:

        return (
            await session.execute(
                select(Post)
                .where(
                    Post.title == post_title,
                    Post.description == post_description
                )
            )
        ).unique().scalar_one_or_none()

    @staticmethod
    async def _delete_like_by_id(
            session: AsyncSession,
            id: int
    ) -> None:

        await session.execute(
            delete(Like)
            .where(
                Like.id == id
            )
        )

    @staticmethod
    async def _delete_comment_by_id(
            session: AsyncSession,
            id: int
    ) -> None:

        await session.execute(
            delete(Comment)
            .where(
                Comment.id == id
            )
        )

    @staticmethod
    async def _delete_post_by_id(
            session: AsyncSession,
            id: int
    ) -> None:

        await session.execute(
            delete(Post)
            .where(
                Post.id == id
            )
        )

    @staticmethod
    async def _add_post_avoid_conflict(
            session: AsyncSession,
            user: User,
            post: Post,
    ) -> OperationStatus:
        try:
            async with session.begin_nested():
                user.posts.append(post)
                return OperationStatus.SUCCESS
        except sqlalchemy.exc.IntegrityError as exc:
            match exc.orig and exc.orig.__cause__:
                case UniqueViolationError() as exc:
                    print(repr(exc))
                    return OperationStatus.NOT_UNIQUE
                case _:
                    raise exc

    async def add_post(
            self,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str
    ) -> OperationStatus:

        # here (and in all methods bellow) we use *async with self._session()*
        # instead of *async with self._session*
        # because *self._session* stores the reference to
        # the AsyncSession class, NOT AsyncSession class Instance!
        async with self._session() as session:
            async with session.begin():
                user = await self._get_user(
                    session, user_name, user_age
                )
                if not user:
                    return OperationStatus.NOT_EXIST

                post = Post(title=post_title, description=post_description)
                return await self._add_post_avoid_conflict(session, user, post)

    async def add_comment(
            self,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str,
            comment_title: str
    ) -> OperationStatus:

        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session,
                    user_name, user_age,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                post.comments.append(
                    Comment(
                        title=comment_title,
                        user_id=post.user_id  # required
                    )
                )
                return OperationStatus.SUCCESS

    async def add_like(
            self,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str,
    ) -> OperationStatus:

        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session,
                    user_name, user_age,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                post.likes.append(
                    Like(
                        user_id=post.user_id  # required
                    )
                )
                return OperationStatus.SUCCESS

    # TODO: Implement methods bellow as Homework

    async def edit_post(
            self,
            user_name: str,  # for Select!
            user_age: int,  # for Select!
            post_title: str,  # for Select!
            post_description: str,  # for Select!
            new_post_title: str,  # for UPDATE!
            new_post_description: str  # for UPDATE!
    ):
        """
        To update the record from DB you need to
        SELECT this record firstly! And this is NOT
        required to build the query using *update* function
        - you just need to update the Python Object retrieved by SELECT query!
        """

    async def edit_comment(
            self,
            user_name: str,  # for Select!
            user_age: int,  # for Select!
            post_title: str,  # for Select!
            post_description: str,  # for Select!
            comment_title: str,  # for Select!
            new_comment_title: str  # for UPDATE!
    ):
        """
        Please read *edit_post* method documentation
        """

    async def delete_post(
            self,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str,
    ):
        async with self._session() as session:
            async with session.begin():
                post = await self._get_post(
                    session,
                    user_name, user_age,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                await self._delete_post_by_id(session=session, id=post.id)

                return OperationStatus.SUCCESS

    async def delete_comment(
            self,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str,
            comment_title: str
    ):
        async with self._session() as session:
            async with session.begin():
                post = await self._get_post_by_title(
                    session,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                user = await self._get_user(session, user_name, user_age)
                if not user:
                    return OperationStatus.NOT_EXIST

                comment_to_delete = [c for c in post.comments if c.user_id == user.id and c.title == comment_title]

                if not comment_to_delete:
                    return OperationStatus.NOT_EXIST

                await self._delete_comment_by_id(session=session, id=comment_to_delete[0].id)

                return OperationStatus.SUCCESS

    async def delete_like(
            self,
            user_name: str,
            user_age: int,
            post_title: str,
            post_description: str,
    ):
        async with self._session() as session:
            async with session.begin():
                post = await self._get_post_by_title(
                    session,
                    post_title, post_description
                )
                if not post:
                    return OperationStatus.NOT_EXIST

                user = await self._get_user(session, user_name, user_age)
                if not user:
                    return OperationStatus.NOT_EXIST

                like_to_delete = [l for l in post.likes if l.user_id == user.id]

                if not like_to_delete:
                    return OperationStatus.NOT_EXIST

                await self._delete_like_by_id(session=session, id=like_to_delete[0].id)

                return OperationStatus.SUCCESS
