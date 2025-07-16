import os

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "db"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "example"),
    "database": os.getenv("MYSQL_DATABASE", "hola_mundo"),
}
