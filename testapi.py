import requests

api_url = 'http://10.142.36.136:49003/hub/api'

token = '4f4149bced8268566ba0e0c96461a0841e3bd23d6d5d96aacbf85fe08f7eeabb'

r = requests.get(api_url + '/users',
    headers={
        'Authorization': f'token {token}',
    }
)
print(r.content)

r = requests.post(api_url + '/users/admin/servers/server1',
    headers={
        'Authorization': f'token {token}',
    }
)
print(r.content)

# r = requests.delete(api_url + '/users/admin/servers/server2',
#     headers={
#         'Authorization': f'token {token}',
#     }
# )
# print(r.content)

