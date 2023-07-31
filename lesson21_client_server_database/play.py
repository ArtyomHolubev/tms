import asyncio

from lesson21_client_server_database.client_and_server.client import Client
from lesson21_client_server_database.structures import User
from lesson21_client_server_database.client_and_server.config import SERVER_PORT


SERVER_HOST = f"http://0.0.0.0"
SERVER_URL = f"{SERVER_HOST}:{SERVER_PORT}"


async def main():
    user = User(
        name="Alex",
        age=34,
    )
    post_tile, post_description = f"{user.name} new post", "I love you!"
    # post_tile, post_description = f"Alex 1st post", "Hello! I am Alex, I am 34 years old "
    client = Client(server_url=SERVER_URL)
    # add_post_result = await client.add_post(user, post_tile,
    # post_description)Alex 1st post', 'Hello! I am Alex, I am 34 years old
    # print(add_post_result)
    #
    # add_comment_result = await client.add_comment(user, post_tile, post_description, comment_title="Great Post!")
    # print(add_comment_result)

    # add_like_result = await client.add_like(user, post_tile, post_description)
    # print(add_like_result)

    # delete_like_result = await client.delete_like(user, 'Alex 2nd post',
    # 'My favourite programming language is Python!')
    # print(delete_like_result)

    # user_with_comment = User(name="Ann", age=32)
    # delete_comment_result = await client.delete_comment(user_with_comment, "Ann 1st post",
    # "Hello! I am Ann, I am 32 years old", "I am 32 years old too!")
    # print(delete_comment_result)

    delete_post_result = await client.delete_post(user, "Alex 1st post", "Hello! I am Alex, I am 34 years old")
    print(delete_post_result)


if __name__ == '__main__':
    asyncio.run(main())
