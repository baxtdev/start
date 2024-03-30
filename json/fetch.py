import requests

response=requests.get("https://www.turmush.kg/news:573729")
print(response.text[:20])
