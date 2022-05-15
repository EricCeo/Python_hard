
# 외부모듈 실행 Pip install request
# request 라는 모듈은 조립해주는 기계이다 get함수를 꺼내서 요청을 보내줘 (get은 return응답값)
# 클라이언트는 요청, 서버는 응답
# 200은 리스폰스
import json
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
response = requests.get(url)


url = "http://www.daum.net/"
response = requests.get(url)
# print(response.text)


print(type(BeautifulSoup(response.text, 'html.parser')))

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)


# 날씨 출력하기

city = "Seoul"
apikey = "################################"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

result = requests.get(api)
data = json.loads(result.text)

print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
print("습도는 ", data["main"]["humidity"], "입니다.")
print("기압은 ", data["main"]["pressure"], "입니다.")
print("풍향은 ", data["wind"]["deg"], "입니다.")
print("풍속은 ", data["wind"]["speed"], "입니다.")


# 번역하기

translator = Translator()
# sentence = "좋은 아침이에요"
sentence = input("번역을 원하는 문장을 입력하세요 : ")
result = translator.translate(sentence, dest="en")
detect = translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detect.lang, ":", result.origin)
print(result.dest, ":", result.text)
print("\n====================================\n")
