## 1. 프로젝트 배경

> 가족들과 집콕하던 아무개씨. 내일 출근하려면 미리 주유소는 갔다와야한다. 자주 가는 주유소는 있지만, 과연 그 곳이 제일 싼게 맞을까? NUGU Speaker에서 현재 위치에서 가깝고, 가장 저렴한 순으로 정렬해서 바로 알려주면 어떨까?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/00409fbc-435e-4884-8257-d257c4751301/jean-christophe-gougeon-t8bDFvkhNQY-unsplash.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/00409fbc-435e-4884-8257-d257c4751301/jean-christophe-gougeon-t8bDFvkhNQY-unsplash.jpg)

NUGU 오일 서비스는 기름값을 조금이라도 줄이고자 하는 사회초년생, 자신 단골 집으로 갔으면 더 싸게 살 수 있었다고 말다툼하는 부부 혹은 친구 사이를 위해 만들어졌다. 

우리 팀이 서비스하고자하는 항목은 다음과 같다 

- 사용자의 현재 위치를 기반으로 **최저가 주유소** 추천
- 해당 주유소 경유/휘발유 가격 정보 제공
- 2007년 경유/휘발유 가격부터 현재까지의 가격을 수집해 다음주 예측 가격 정보 제공

---

## 2. 원하는 결과

사용자가 NUGU Speaker에게 최저가 주유소를 알려달라는 요청을 말하면, 해당 데이터를 서버에서 가져와 사용자에게 전달한다. 다음은 NUGU 오일 서비스를 사용할 때의 사용자와 NUGU의 대화 흐름이다. 

---

**사용자** : 아리야, 최저가 주유소 찾아줘 

**NUGU** : 경유를 원하시면 1번, 휘발유를 원하시면 2번을 말씀해주세요 

**사용자** : 2번 

**NUGU** : 반경 5km이내에 주유소 3곳을 알려드릴게요. 현대오일뱅크(주)직영 토평 1호 셀프주유소, 1387원, 푸른 주유소, 1399원, 현대오일뱅크(주)직영 토평 2호주유소, 1427원이에요 

---

서비스 제공을 위해 필요한 데이터셋은 다음과 같다 

- **유가 정보 API**

한국석유공사에서 제공하는 API로 주유소 판매 가격, 주유소 위치, 부가 서비스 등 전국 주유소 정보 및 평균 유가를 제공한다

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3cf082b7-9135-46da-89f5-de4522e649d1/_2020-11-28__11.29.57.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3cf082b7-9135-46da-89f5-de4522e649d1/_2020-11-28__11.29.57.png)

사진 출처 : [http://www.opinet.co.kr/user/main/mainView.do](http://www.opinet.co.kr/user/main/mainView.do)

## 3. 서비스 flow

NUGU 오일의 서비스 구조는 다음과 같다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5fa6e6a-b8e1-4ad3-89e3-7e0597ec95eb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5fa6e6a-b8e1-4ad3-89e3-7e0597ec95eb/Untitled.png)

 자세한 내용은 다음 포스팅에서 확인할 수 있다. 

Photo by [Jean-christophe Gougeon](https://unsplash.com/@alien_crafted?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/gas-station?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
