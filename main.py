import requests
from random import randint
url=f"http://numbersapi.com/{randint(1,100)}"
request=requests.get(url)
text=(request.content)