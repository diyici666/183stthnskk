import requests

url = "https://hdttapi.hstloan.com/api/user/sms/send"
headers = {
  "Accept": "application/json",
  "mchUuid": "HST-TTFQ",
  "appPath": "com.jiwind.loan",
  "insideVersion": "24",
  "channelId": "40019",
  "deviceVersion": "35",
  "deviceId": "889A1ABB73C0BD51F4B38D68F3643F0C2D29EB93",
  "deviceType": "2",
  "Content-Type": "application/json;charset=utf-8",
  "Host": "hdttapi.hstloan.com",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "User-Agent": "okhttp/3.12.0"
}
data = """{\"mobile\":\"18300702132\",\"scene\":\"2\"}"""

res = requests.post(url, headers=headers, data=data)
print(res.text)
