import requests
import json

access_token = 'YTM0OGE1ZjgtNmQ5OS00Y2ZmLTk1YjMtOTUyMTIxZTRhNzZlNDk2YTViZDgtZjkx_PF84_consumer'

room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMmZkM2RkZDAtM2E1NC0xMWViLWE4MzYtMWRjZGZkOTI1YmM0'

message = 'Hello Here are my screenshots of of netacad-devasc skills-based exam'

url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)

print(res.json())