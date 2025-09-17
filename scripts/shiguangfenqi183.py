import requests

url = "https://fastlend.shiguangjk.com/yzd/v676/account/loginvcode"
cookies = {
}

headers = {
  "Content-Type": "application/x-www-form-urlencoded",
  "Host": "fastlend.shiguangjk.com",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "User-Agent": "okhttp/3.12.0"
}
data = """sec_level=2&data=w%2BIwMibOEaBjQ3RhR7pSKEJoRjTcGNTE8X59Xxp%2BQQddBxMUelSGnnXCKAhlrsRoQBURYljxoVXCkyOjLOhUI64bVV1dWudu0CpT8FRFBdkjUEY5baL%2BjTdPFfsVY15FYk4y4API1m5t7g9PKltZjhmb5uUa6DnvCVjYB3dLoSrxKHL0IpVMz7XHBkEXHIc2JswlmQRG1N%2BoRgPPySqhsxD0lPeWQwYsFT9cWLaM8c4hgI1lvE1LcjUbUnGBL%2BBUfeRUHjJhCUj78amTonoHLthsoPRjKwFj6KDvgpZrXhJO0VXaSQvlOHMHOZoAl%2BDgOSMtS9GkUrnEdSJEiVGrxyLKIklVIMj1U6poJkcCHpvviMvtl6ZwHZqh50zOff%2FnQGHIubNfxfVCyeQDy9kvYp9KLaDiXJEFMqdggfg1ySCDSUj7CbJWb8L3xXRlFLmX41dwmMnc0vA1e7S7mzYaWivuKZcjcSY7RLZ6UW1OA9h7VQ8XO6IyBtiDweqg%2FjWv7ABspil08hh5ADVEGxe666s%2FEJy%2FGnVk7c7TDJtAyDpY%2BN7ZT%2FSvAziGB%2FAZD3nqjfl0DmmleXa7nWHILIRE0zax0IqEN603RHXybMAd3P%2Fomz%2Bsl81XBssv43eoFgJ5Avp2h%2ByoFJkgkhRod8%2FRgIfDuXhR7XvCLR3wXbv5QEakr6rbuLRUnJeG3udpd6LoOyIYUEM55hXt2VtqD9T4M%2BBB0Fkw%2FGoTpJGAullzYzHjnR1SZrDVDEPeuWEHIbX3PVsqLybAt1SjgdZDEXJqliUuv7SHOfeGrT3dTc5IrVW1Cz%2BDSqlJ4%2F0uFXcxFOp5ZN4RwphqPN%2FQmyJX3t7gEax1C0EQKWqq3W67frWkSrjdYAUh5%2B0DbZMcjCk%2FiyW7fkaqyl3L29kgO4NMe%2BOwM10K2JpYAwHycn1NiTJUUFCe9vPzrEtTg5rbD4pIrKrRy3xBuE5T4GOS%2BfIfru1PKZp9e4Uz2bdqiUiERPJFdx0%3D&uid=0&ticket=&appid=2"""

res = requests.post(url, headers=headers, cookies=cookies, data=data)
print(res.text)
