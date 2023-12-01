import requests,m3u8

m3_url = ''
r = requests.get(m3_url)

m3u8_master = m3u8.loads(r.text)
print(m3u8_master.data)