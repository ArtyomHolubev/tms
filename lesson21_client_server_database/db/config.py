db_user = "admin"
db_pass = "postgres"
db_host = "127.0.0.1"
db_port = 5432
db_name = "postgres"

DB_URL = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
print(DB_URL)
