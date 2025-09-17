import requests

url = "https://appapi.chengan.tech/openapi/v1/appapi/user/sendOTP"
headers = {
  "Accept": "application/json; charset=utf-8",
  "X-ZAXD-sign": "de96b7c47667c1a17e419fdd639d0eeb",
  "X-ZAXD-appKey": "tX7pvHYOxoWuvXEc4Yvx8FiyGA63PNSk",
  "X-ZAXD-timestamp": "20250917084410131",
  "X-ZAXD-signType": "APPMD5",
  "X-ZAXD-version": "1.0.0",
  "X-ZAXD-nonce": "069c713f-4ff6-4f92-bdc9-37b7ca6b42b2",
  "Content-Type": "application/json; charset=UTF-8",
  "Host": "appapi.chengan.tech",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip",
  "User-Agent": "okhttp/3.12.1"
}
data = """KRb7zpnIMNfhLgzYb/cLDIEP6+cffqtKX46jywWjA9KjNoo9L7SX87UjgBqp3kGg0KqdQeIPwHDlhPH6aYl4lYGarhhF13HoA9nQHI2qDw+Pnkyz0i5sAwpFbE0yfVIqT2RlyESuyIH8phZcWvujS4gdII0oIPgAJK4lengBv7yA2tA73y20EPw9IFsdDAFAueWQ2QaKyCddKEa7vx8vsItTFYCMQqU9+UoSLh+WhL1pqwrElquhVKVekFGquvzsCsq8DDq3RNVI1DOycZiGboTkJJUxx7T2bpd1GoBgV4F4ktP3KX1SiYvgMuO9rNM47eVpvlc5dH6WNLShWcTF91HJE64wgLG8e4icl+Sv57gUpLL9pPm1iXxatgBYRcNkEP9Oo2PtdNILtAkLIHnG0aUoc8Tk/YXpiOsL6LHbPbvgFsso5rZdqhNbV0df9BuUB2e8Qh8PpLnLoUXLYZZW+oKOfOJ7nY3FXA03Gu4DdYgeV0d6O+2J+tZa+VY52rCtSZSCsL+v9XKLWx26KnDU0JT1wLpJAx+Rum6FyqqXePUyuS29eC+HPa5E4w3U1Olflv9sxJL72zY2bRi84PCZX6cIvGjb8D+3mbp6IoTFiNo2J/uWlXMALNp0V3w0qkEluzvAof38jyzxzlJnzE0dzx4wD0cvhYdYt4y3UbCzAntjZ6fw8kHKHjTMGiUIfvTqdIOb7NwaWMFtjxXQkQFSf/cWy4lQbzgIcBGEUiJ1v/7l2S52MlX7K9xNanr/lJA0oJT34FiapkvTqbrE7r4KoQ=="""

res = requests.post(url, headers=headers, data=data)
print(res.text)
