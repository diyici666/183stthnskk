import requests

url = "https://app.dewu.com/api/v1/app/user/ice/user/sendCaptcha?newSign=c7e183de3766ee0c0907b6b430cdb779"
cookies = {
  "HWWAFSESTIME": "1758069487011",
}

headers = {
  "ltk": "EIyJUBUh6ZJod8Dv3Pi4LYIbpGOZdqfERZZxXy4B6",
  "app_build": "5.73.0.10",
  "ipvx": "182.118.232.158",
  "cookieToken": "",
  "webua": "Dalvik/2.1.0 (Linux; U; Android 15; M2007J3SC Build/AQ3A.240912.001)/duapp/5.73.0(android;15)",
  "duplatform": "android",
  "appId": "duapp",
  "duchannel": "vivo",
  "humeChannel": "",
  "duv": "5.73.0",
  "duloginToken": "",
  "dudeviceTrait": "M2007J3SC",
  "dudeviceBrand": "Redmi",
  "timestamp": "1758069580713",
  "shumeiid": "20250917083805a2bae2560769ecf92bcb7023a7ccf51400a0eb50b50e1c36",
  "User-Agent": "duapp/5.73.0(android;15)",
  "X-Auth-Token": "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NTgwNjk0OTAsImV4cCI6MTc4OTYwNTQ5MCwiaXNzIjoiZjdhMGFhYmE3MDkxNzZlYSIsInN1YiI6ImY3YTBhYWJhNzA5MTc2ZWEiLCJ1dWlkIjoiZjdhMGFhYmE3MDkxNzZlYSIsInVzZXJJZCI6MjY0MDgxODk2MCwidXNlck5hbWUiOiLlvpfniallci1QNkYxQzVLNSIsImlzR3Vlc3QiOnRydWV9.myw3QtPe1xzQAv18DxC41_grRvwJSsrjHjNTEQr7tLMJHee2JqOgUdKC8r8x-_Xp0nJJMVKr5ioTst1fIBHlQG0gCuG0ndhiHJQxhKFpaIhEnDCbq30QuFK3_lNQSimgBtnJJJFDMFThtDuqRfT83BqOEbVqiTJKv1m4uGOpbpPbUs3CDMNvpT5uk8xTgfyDJMdML_PlI1SJkm3TtWVHTIKxZxPTWjPqwI_BYGT9emLNSb3dcOhm60wBf69MQWp8bRndNzpP6Y9yTBovF2AOfYJuJxgMk-4YolClX80_hDOtEja6C7Jt1ULANf1jfBtYy2CL3sABa6dI-xniNWZgfQ",
  "isRoot": "0",
  "emu": "0",
  "isProxy": "0",
  "SK": "9RXTDHmjAq3Ij9tMo4ake9YtLJptZVubz3p4adUvNt4cGXTrK9lnYNjNaXWzGFzb4iN2rIDzgN7gPDwQc5etV1e8Es1y",
  "edk": "6C7D61656D61352E6C7D7D7D616C356E3F693869696A693F3831393F3E6D692E6769616C35",
  "dps": "1",
  "sks": "1,adwx",
  "skt": "adr1",
  "skc": "tQ4qttCNie0Qb8AuM8fwlJhidehr4Hnhh3h4",
  "adi": "LLNgaHhKmOzx1_BuPXM6BVvkIwcIkNrdI074hJvhzEI=",
  "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
  "Host": "app.dewu.com",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip"
}
data = """data=NkY2ODY3RjgxNEQ5MzQ0NkUyQkNCMzdGNjc5QTUwMTAuY0dGeVlXMGZNRGcwT0ROalpUQXRZVEZpTkMwMFltVTRMV0l3Tm1VdFlUVm1OVEkzT1dKa09XWmtIblpsY25OcGIyNGZNUjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS64mzTAUr_gVw1VTnxxnMND3IKB1fu4y_1EA19MZcS7AW5M6UwkPBeoWUADPGXOv0IqMhcYv240MA5KA2A0nLwRocZ0qE30sBAMVVlqdJf-VYBNQiIWfr8UGxBTdWmc-HffsxLNaepBSFQfXyNykO1JZYsCoIsBrQEJQw4wM8-5FNA6i1SKQ1rkXBEINWTL6RAl7SNRI9XNSj1zOgUB-YonLLNgaPknigE="""

res = requests.post(url, headers=headers, cookies=cookies, data=data)
print(res.text)
