from urllib.parse import urlparse

ENV = "dev"

if ENV == 'dev':
    DATABASE_CONFIG = {
        'host': "pic4calcetto_db",
        'database': "pic4calcetto",
        'user': "pic4calcetto",
        'password': "1234",
    }
else: 

    uri = "****"
    parsed_uri = urlparse(uri)

    DATABASE_CONFIG = {
        'host': "****",
        'database': "****",
        'user': "****",
        'password': "****",
        'port': "****"
    }
