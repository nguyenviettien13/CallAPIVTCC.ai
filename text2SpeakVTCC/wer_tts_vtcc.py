import http.client
import ssl

conn = http.client.HTTPSConnection("vtcc.ai",
context=ssl._create_unverified_context()
)

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"FPTOpenSpeechData_Set001_V0.1_014122.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {
'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
'cookie': "XSRF-TOKEN=eyJpdiI6InlqWlJPd1pIODRtT2FQUkdMOEE2WXc9PSIsInZhbHVlIjoiQ212cDBXZ3VySW5wMVEwaDltYnNjM1paeURhS3BqT3hmMlk5SmtHcVdCakIrZlFuRmp3VlZOeFVheDg4SzZpTSIsIm1hYyI6IjMxYzZjNzYwODY5MDEyNzgzN2Q3MDY2YmY2YzRkYWVmZTM0MmVhNDZmMmVhZWUwYzE3YmU5YjJhMDgyNjEzMmUifQ%3D%3D; voice_ai_session=eyJpdiI6IksxMHd6MVhRR3k1YU40T0pcL0VtNjhBPT0iLCJ2YWx1ZSI6IkdoTDNKUEpZQjlcL1lwbURwdUlZRUFkUFV2MU1JeEEyNHBzMW5HdnU1enBGNlE0VnZxQ3BScEo4UjN1OW05OGx4IiwibWFjIjoiMzc1NDI1MGQ0MzhiZmVlMTA5ZjEzOWI0MGYyMzRhNDE2NmUxNzVhZWI1MzAyNDgyOGVkZTUwZTA4MzhiZDYyNyJ9; WEBSVR=1; ga=GA1.2.595491308.1539577929; gid=GA1.2.1029939479.1539577929; _gat_gtag_UA_127323561_1=1",
'cache-control': "no-cache",
'postman-token': "0739b9f2-dd7c-b846-e811-385898cf703e"
}

conn.request("POST", "/voice/api/asr/v1/rest/decode_file", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))