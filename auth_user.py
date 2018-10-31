import json


def retrieve_access_token(file_name):
    with open(file_name, 'r') as credentials:
        credentials = json.load(credentials)
        if 'OAUTH_TOKEN' in credentials:
            return credentials['OAUTH_TOKEN']
