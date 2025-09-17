import requests

url = "https://emapp.emoney.cn/user/platformlogin/getloginsmscode"
headers = {
  "AppClientGuid": "194cb6fe-99b0-43ca-ac60-89653fb47817",
  "Authorization-AccessToken": "U5N2xMKKVUw3KO0gxVH%2FHxCk6gJEfq%2F%2FLlzwF7jwa9LwTL95QJZutU1CAznIOcxUspwnmy6%2Fwy1VkT1byg9tsPieFb6Y3QfiTgw3FT3vHENTBUPRmbJaaOD%2FnpFHAk6JxBpDUuhWI1sGAd2aYojGR1kE7qaI0O9Sb%2FImnD5T0Qg%3D",
  "Content-Type": "application/x-www-form-urlencoded",
  "Host": "emapp.emoney.cn",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "User-Agent": "okhttp/3.10.0"
}
data = """is2pt=false&ar=10&pd=2&pkgName=cn.emoney.level2&mv=9.4.8&accId=18300702132&accType=2&emoneyToken=ED519166B1953A8EE12F4ADD801D33D6&vd=551"""

res = requests.post(url, headers=headers, data=data)
print(res.text)
