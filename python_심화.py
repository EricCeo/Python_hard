
#외부모듈 실행 Pip install request
#request 라는 모듈은 조립해주는 기계이다 get함수를 꺼내서 요청을 보내줘 (get은 return응답값)
#클라이언트는 요청, 서버는 응답
#200은 리스폰스
import requests
response = requests.get(url) 

from bs4 import BeautifulSoup

url = "http://www.daum.net/"
response = requests.get(url)
# print(response.text)

print(BeautifulSoup(response.text, 'html.parser'))