import os

if "POSTGRES_HOST" not in os.environ:
    raise Exception("'POSTGRES_HOST' env var not found in environment")
else:
    POSTGRES_HOST = os.environ['POSTGRES_HOST']

if "POSTGRES_PORT" not in os.environ:
    raise Exception("'POSTGRES_PORT' env var not found in environment")
else:
    POSTGRES_PORT = os.environ['POSTGRES_PORT']

if "POSTGRES_DB" not in os.environ:
    raise Exception("'POSTGRES_DB' env var not found in environment")
else:
    POSTGRES_DB = os.environ['POSTGRES_DB']

if "POSTGRES_USER" not in os.environ:
    raise Exception("'POSTGRES_USER' env var not found in environment")
else:
    POSTGRES_USER = os.environ['POSTGRES_USER']

if "POSTGRES_PASSWORD" not in os.environ:
    raise Exception("'POSTGRES_PASSWORD' env var not found in environment")
else:
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

if "SQLALCHEMY_DATABASE_URI" not in os.environ:
    raise Exception("'SQLALCHEMY_DATABASE_URI' env var not found in environment")
else:
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']