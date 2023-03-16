import requests
import time
import json
import re

QUERY_USER_PRIVATE_ENDPOINT = 'https://api.gfycat.com/v1/me/gfycats'

QUERY_USER_PRIVATE_ALBUMS_ENDPOINT = 'https://api.gfycat.com/v1/me/album-folders'
QUERY_ALBUM_ENDPOINT = 'https://api.gfycat.com/v1/me/albums/'

OAUTH_ENDPOINT = 'https://api.gfycat.com/v1/oauth/token'

payload = {'grant_type': 'client_credentials', 'client_id': '{insertclientid}', 'client_secret': "{insertclientsecret}"}
payload_oauth = {"code":"{insertoauthcode}", "client_id":"{insertclientid}", "client_secret": "{insertclientsecret}", "grant_type": "authorization_code","redirect_uri":"http://localhost"}

r = requests.get(OAUTH_ENDPOINT, data=json.dumps(payload_oauth), headers={'content-type': 'application/json'})

response = r.json()
print(r.text)

token_type = response['token_type']
access_token = response['access_token']
expires_in = response['expires_in']
expires_at = time.time() + expires_in - 5
headers = {'content-type': 'application/json', 'Authorization': token_type + ' ' + access_token}

simple_header = {'Authorization': 'Bearer ' + access_token}

first = True
second = True

r = requests.get(QUERY_USER_PRIVATE_ENDPOINT + "?count=100", headers=headers)
response = r.json()
initcursor = response['cursor']
print(initcursor)

while True:
    if first:
        res_str = r.content
        first = False
    elif second:
        res_str = res_str + r.content
        second = False
    else:
        res_str = res_str + r.content
        if cursor == initcursor:
            break
    
    response = r.json()
    cursor = response['cursor']
    print(cursor)

    r = requests.get(QUERY_USER_PRIVATE_ENDPOINT + "?count=100&cursor=" + cursor, headers=headers)

res_str_nobytes = str(res_str)
whole_txt = "".join(res_str_nobytes)

PATTERN = r'(https)(:\/\/)(giant.)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

matches = re.findall(PATTERN, whole_txt, flags=re.MULTILINE)
expenses = ["".join(x) for x in matches]

with open("links.txt", "a") as f:
    f.write(str(expenses[:]).replace(".webm",".mp4"))