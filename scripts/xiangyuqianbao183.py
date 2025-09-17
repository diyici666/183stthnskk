import requests

url = "https://sjdre-xyqb.xycredit.com.cn/api/user/login/sendVCodeByLogin"
headers = {
  "Host": "sjdre-xyqb.xycredit.com.cn",
  "Connection": "keep-alive",
  "deviceInfo": "{\"deviceId\":\"\",\"idfa\":\"\",\"mobileType\":\"\",\"operator\":\"\",\"operationtime\":\"\",\"imei\":\"\",\"appversion\":\"\",\"channel\":\"\",\"childChan\":\"\",\"latitude\":\"\",\"resolution\":\"\",\"uuid\":\"\",\"rootStatus\":\"\",\"apiid\":\"\",\"manufacturer\":\"\",\"longitude\":\"\",\"apiversion\":\"\",\"idfv\":\"\",\"osversion\":\"Android 15\",\"ostype\":\"01\",\"ip\":\"\",\"mac\":\"\",\"androidId\":\"\"}",
  "ticket": "terror_1006_2035992808_1758070669",
  "sec-ch-ua-platform": "\"Android\"",
  "randstr": "@6pl5rjugo1",
  "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Android WebView\";v=\"140\"",
  "sec-ch-ua-mobile": "?1",
  "deviceType": "Android",
  "chanCode": "306",
  "typeCompany": "TENCENT_CLOUD",
  "User-Agent": "Mozilla/5.0 (Linux; Android 15; M2007J3SC Build/AQ3A.240912.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.51 Mobile Safari/537.36/phd_native_app/xyebank",
  "Content-Type": "application/json; charset=UTF-8",
  "Accept": "*/*",
  "Origin": "https://sjdre-xyqb.xycredit.com.cn",
  "X-Requested-With": "xybank.com.rainbowcredit.vest",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": "https://sjdre-xyqb.xycredit.com.cn/",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
data = """{\"singleParam\":\"18300702132\"}"""

res = requests.post(url, headers=headers, data=data)
print(res.text)
