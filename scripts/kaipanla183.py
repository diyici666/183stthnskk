import requests

url = "https://applhb.longhuvip.com/w1/api/index.php"
headers = {
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; M2007J3SC Build/AQ3A.240912.001)",
  "Host": "applhb.longhuvip.com",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip"
}
data = """a=PwlSendVerify&c=PwlMob&PhoneOSNew=1&DeviceID=a20d1394-a252-30d5-896b-ccddb5ecee3a&VerSion=5.20.0.8&Token=0&apiv=w41&SType=1&UserID=0&Phone=mGUui8sYXiRwpdCOIzHZILM%2B5rkuzQV54KMMSSkNNrVK3gmOMjRgFUN7tqj3KRj7Cx5O9FKfYRLQ%0Ax5ZIZ6QScN4puZZu2CY%2B5VLxt%2BXZo9ExvGTwAu%2F8DReSiNNo4%2BrgWTaXwPBnuhs4disRrgWHUmFY%0An0kh%2Fv1PL3Nps1vUtNqTjFUClde17KjQVOqKOK3HQHgyGtO1kIUn2G4yMxPr8wD2O6kZXKMDtBCV%0ALj1E657rgfzuFACqjPMnbQSO3RO5RfSvmjHHvcOKlIHxTKxQBnXPbuN9ZnziOaPtAEZacL5b85cy%0AhqrRGxrMsgTBLGaD1oLjptPdm3Is6BkV6cg7vw%3D%3D%0A&CheckCode=bdc3cbd2b5410dd3d528a7e678346f81&"""

res = requests.post(url, headers=headers, data=data)
print(res.text)
