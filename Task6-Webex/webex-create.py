import requests
import json

access_token = 'YTM0OGE1ZjgtNmQ5OS00Y2ZmLTk1YjMtOTUyMTIxZTRhNzZlNDk2YTViZDgtZjkx_PF84_consumer'

url = 'https://webexapis.com/v1/rooms'

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params={'title': 'netacad_devasc_skills_sergek'}

res = requests.post(url, headers=headers, json=params)

jresp = res.json()
print(jresp)
print('\n\n---------------')


room_id = jresp['id']
person_email = 'yvan.rooseleer@biasc.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
 }
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)

jresp = res.json()
print(jresp)
print('\n\n---------------')
