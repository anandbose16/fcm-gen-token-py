import json
import argparse
from oauth2client.service_account import ServiceAccountCredentials

argparser = argparse.ArgumentParser(description = 'Generate bearer token for Firebase APIs')
argparser.add_argument(
        '-f', 
        '--service-account-file', 
        help='Path to service-account.json file',
        required=True
)
args = argparser.parse_args()
service_account_file = args.service_account_file

scopes = ['https://www.googleapis.com/auth/firebase.messaging']

print('')

credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scopes)
access_token_info = credentials.get_access_token()
print(access_token_info.access_token)

print('')
