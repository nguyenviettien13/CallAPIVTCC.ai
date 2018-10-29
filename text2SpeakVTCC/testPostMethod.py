import os, ssl
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from click_package.commands import verify

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundarycKo3dQoclhhOhdK1",
    'Cookie': "WEBSVR=1; _ga=GA1.2.212854641.1539595551; _gid=GA1.2.1663307608.1539595551; XSRF-TOKEN=eyJpdiI6Im90MTBoOUJvUzhpQTRua2tkYlBrWXc9PSIsInZhbHVlIjoiTFdsYUFsc3lYUk9NTEU0UXRlZlIydkpBMWE4ZCs5bGQ4VFdwQlkyZXdobk14QWwxdVVYTXZMMGFTZjZGbnBBMyIsIm1hYyI6IjFiYjYwNDM4Y2UzMWZiYzY2MDUwOTY0MmMxYTkxZWIxZDYxNTlhMDUzNTcxYjkxOTA1NDc5MWFhM2NjN2MwYmUifQ%3D%3D; voice_ai_session=eyJpdiI6InlpdjVPZm50ZnZZQjlOT0NWVFVpa0E9PSIsInZhbHVlIjoibHpjQk1oeno0VVcySjI0c2h1V0pGc3pSeFVGOWZQNG41WXIzZ1JFMG91ekZLZkg0bk9YXC95dlBKak5aeTA4c1EiLCJtYWMiOiI5NzIwOTMxMmJmN2E4YzU5YmRhMmNmNjkwYThmZTliNTY0OGE4NDlhYzc1MjUyMDg4OGJhZGVhYmZlZjg2NjNiIn0%3D",
    'cache-control': "no-cache"
    }

url = "https://vtcc.ai/voice/api/asr/v1/rest/decode_file"
files={'file':('FPTOpenSpeechData_Set001_V0.1_000001.mp3',open('FPTOpenSpeechData_Set001_V0.1_000001.mp3', 'rb'),'audio/mp3')}

#normal_multipart_req = requests.Request('POST',url,files= files).prepare()
#print("Body: " , normal_multipart_req.body)
#print("Header: ",normal_multipart_req.headers)

#if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
#         getattr(ssl, '_create_unverified_context', None)):
#     ssl._create_default_https_context = ssl._create_unverified_context
# urllib.requests.urlopen(normal_multipart_req)

r = requests.request('POST', url, files=files, verify= False)
print(r.status_code)
print(r.text)