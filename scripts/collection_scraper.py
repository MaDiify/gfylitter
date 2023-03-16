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

r = requests.get(QUERY_USER_PRIVATE_ALBUMS_ENDPOINT, headers=headers)

with open("everything.json", "wb") as f:
	f.write(str(r.json())[38:-2].replace("'","\"").encode('utf-8'))

m = open('everything.json', encoding='utf-8')
js = json.load(m)
ids = ""
res_str = ""
PATTERN = r'(https)(:\/\/)(giant.)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

for x in js:
	u_id = x.get('id')
	u_title = x.get('title')
	ids += f"{str(u_id)}\n"
	r2 = requests.get(QUERY_ALBUM_ENDPOINT + str(u_id), headers=headers)

	res_str_nobytes = str(r2.text).replace("\\","").replace(".webm",".mp4")
	whole_txt = "".join(res_str_nobytes)

	matches = re.findall(PATTERN, whole_txt, flags=re.MULTILINE)
	matched = ["".join(x) for x in matches]

	res_str += f"{u_title}: {matched}\n" 

with open("ids.txt", "wb") as f:
	f.write(ids.encode('utf-8'))


with open("links.txt", "wb") as f:
	f.write(str(res_str).encode('utf-8'))

m.close()