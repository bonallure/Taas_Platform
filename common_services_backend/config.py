import os

config = {

    'password': os.getenv('Team11_developer'),
    'raise_on_warnings': os.getenv('DB_DATABASE', 'true') == 'true',
}
