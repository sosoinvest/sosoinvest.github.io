---
layout: single
title:  "[서평-13] 퀀트: 물리와 금융에 대한 회고"
description: 이매뉴얼 더만의 자서전과 함께 퀀트에 대해 정리한 글
categories: 투자
tag: [주식,퀀트,책]
toc: true
author_profile: false
header:
 teaser: /images/2024-10-24-quant-and-physics-book/quant-physics-book.webp
 og_image: /images/2024-10-24-quant-and-physics-book/quant-physics-book.webp

# sidebar:
#     nav: "docs"
# search: true
---
월스트리트에서 정점을 찍은 퀀트가 바라본 금융 업계는 어떤 모습일까.

[퀀트: 물리와 금융에 대한 회고](https://www.aladin.co.kr/m/mproduct.aspx?ItemId=939964&srsltid=AfmBOoq8Gj7PTeednmhzyw5ckifSdiX1rwXLhOKvenD_qFs3K5iSLZ5g)는 이론 물리학자 이자 금융공학자, 그리고 골드만삭스에서 성공한 퀀트인 이매뉴얼 더만(Emanual Derman, 1945~)의 자서전이다.

# 퀀트란 무엇인가
일반적으로 퀀트(Quant)는 Quantative와 Analyst가 합쳐져 탄생한 단어로 정량적 분석을 이용해 투자결정을 내리는 방식 또는 사람을 말한다. 

좀 더 형식적인 옥스포드 영어사전은 퀀트를 투자 방식보다는 수학적 모델을 이용해 금융 시장을 분석하는 사람으로 정의한다. 

<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/quant-oxford-dict.webp" alt="옥스포드 사전의 Quant의 정의 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 퀀트의 정의(출처: Oxford dictionary) </span>
</p>

수학과 통계를 이용한다는 점 때문에 대중들에게는 퀀트가 뭔가 신비한 엄청난 일을 하는 것으로 비춰지는 것 같다. 서점이나 도서관에서 구할 수 있는 많은 책들도 퀀트의 이름을 빌려서 다양한 투자법들을 제시한다. 그러한 책들을 보면 이러 저러한 방법에 따라 꾸준히 투자하면 이정도의 수익을 얻을 수 있다는 내용들이 담겨있다.

즉, 사전에서 정의하는 퀀트와 대중이 인식하는 퀀트에는 관점의 차이가 있다. 이러한 관점을 구분해서 따라서 퀀트의 의미를 정리해보면, 기술적 분석, 기본적 분석, 그리고 금융공학의 관점으로 나눌 수 있다.

## 기술적 분석의 관점
기술적 지표를 이용해 투자하는 투자기법을 말한다. 예를 들면 [래리 윌리엄스의 변동성 돌파전략](/투자/volatility-break-out-strategy), 알렉산더 엘더의 세개의 창 전략, 또는 존 볼린저의 볼린저 밴드를 이용한 전략들이 있다. 가장 성공한 헤지펀드인 [르네상스 테크놀로지의 짐 사이먼스](/투자/jim-simons-book)도 이러한 기술적 분석에 중심을 두고 있다.

국내에도 퀀트를 표방하여 어떠한 규칙에 따라 매매하는 투자법들이 책으로 나와있다. 사실 이런 방식의 투자법들은 퀀트라기 보다는 알고리즘 트레이딩이라는 용어가 더 정확한 것 같다.

## 기본적 분석의 관점
이 관점은 PBR, PBR, 배당수익률 등 기업의 재무 데이터에 기반한 투자법을 말한다. 예를들면, PBR이 낮은 주식 몇개를 포트폴리오에 담아서 분기별로 비중을 조절하는 것을 꾸준히하면 장기적으로 어느정도의 수익이 난다는 것이다. 

[퀀트의 정식](/투자/quant-way-book)에서 말하는 팩터 모델링 기반 투자법도 이러한 관점이다.

이 방식은 수학적 모델과 가장 거리가 먼, 문과적 기법이지만 몇몇 투자책에서는 이러한 투자법을 퀀트라고 부르기고 한다.

## 금융공학의 관점
수학적 모델과 통계에 기반해서, 옵션, ELS 같은 복잡한 금융 상품을 설계하고 채권 또는 주식의 가치평가 모델을 만드는 사람들을 뜻한다. 옥스포드 사전의 정의에 가장 잘 맞는 관점이다.

금융공학의 관점이야말로 퀀트의 원조라고 할 수 있다. 이매뉴얼 더만에 따르면 1970-1980년대 학계에는 교수나 연구직 자리가 부족해서 많은 물리학자들이 산업계에서 일자리를 찾아야 했다. 컴퓨터의 발전과 블래-숄즈 방저식의 발견으로 미분방정식과 수치해석에 능한 사람들을 월스트리트가 원했고, 그러한 시대적 흐름에 따라 많은 이공계 박사들이 뉴욕으로 흘러들어갔다고 한다.

이공계 출신이 생소한 금융계에서는 그들을 뭐라고 불러야 할지 몰라서 비꼬는 의미에서 로켓 과학자(Rocket Scientist)로 불렀다. 아마도 실제로 많은 사람들이 로켓 과학자였을 것이다. 시간이 흐르면서 계량금융(Quantitative Finance)에서 따온 Quant라는 말로 부르기 시작했다.

이러한 관점은 앞의 두가지, 즉, 기술적 분석과 기본적 분석에 기반한 것과 공통점이 거의 없는 전혀 다른 관점이다. 앞의 두 방식은 기반은 다르지만 어디까지나 규칙을 통한 매매차익을 추구한다. 그러나 금융공학적 방식은 아니다. 금융공학적 관점이 가진 근본적인 차이점을 열거해보면,

- 직접 트레이딩 하지 않고 트레이더를 보조하는 도구를 만든다.

- 수학적 이론을 이용해 금융상품을 설계한다.

- 미분방정식을 사용한다.

- 주가와 채권 수익률 같은 불확시한 변수들을 통계적 방법을 이용해서 처리한다.

이러한 차이점에 기반해서 보면, 대중이 인식하고 기대하는 퀀트와 실제 월스트리트의 퀀트는 물로켓과 스페이스X의 팔콘9 만큼의 거리가 있다고 느껴진다. 일정한 규칙에 따라 매매하는 것은 일반인에게 물로켓만큼 실행하기 쉽지만, 금융상품을 설계하고 매매하는 것은 팔콘9을 발사하는 것 만큼 어렵다.

# 책소개
[퀀트: 물리와 금융에 대한 회고]는 금융공학적 관점의 월스트리트의 프로 퀀트들에 대한 책이다. 한국어판은 금융위기가 발생하기 전인 2007년에 나왔다.

기본적으로 자서전 형식의 글이다. 문장이 명료하고 번역도 깔끔해서 소설처럼 쉽게 읽힌다. 저자의 인생이 시간 순서로 열거되어 있어서 따라가는 재미가 있다.

책의 분량은 물리학자 시절과 퀀트 시절로 반반씩 나뉜다. 쉽게 쓰려고 노력했지만 다루는 금융공학적 내용이 일반인에게는 꽤 전문적이어서 정확히 이해하기는 어렵다. 게다가 실질적으로 도움이되는 투자 얘기는 거의 없다. 대신에 직장을 옮기거나 직장내 정치에서 살아남는 방법 등 인생을 살아가는데 참고할만한 내용이 많다.

책의 서문은 이런 문장으로 끝난다.
> 이 책은 내가 과학자로, 퀀트로, 그리고 때로는 괴짜들의 여정에 함께 나선 동행으로 겪은 경험담을 모은것이다.

<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/quant-physics-book.webp" alt="퀀트:물리와 금융에대한 회고 책 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 퀀트: 물리와 금융에 대한 회고 </span>
</p>

## 책의 저자
저자 이매뉴얼 더만은 현재 콜롬비아 대학에서 금융공학을 가르치는 교수다. 남아프리카 공화국에서 태어나 이론 물리학을 전공하기 위해 미국으로 이주했다. 

### 물리학자
그는 케이프타운 대학에서 물리학을 전공했고 콜롬비아 대학에서 이론 물리학으로 박사학위를 받았다. 당시에 콜롬비아 대학은 이론물리학 분야에서 노벨상을 받은 교수들이 많이 근무하고 있었다. 대표적으로 중국계 교수인 리정다오(Tsung-Dao Lee)와 양전닝(Yang Chen-Ning)이 있다. 더만의 시선에서는 리정다오가 리오넬 메시와 같은 인간계를 초월한 신계의 인물로 보였던 것 같다. (서양에서 존경받는 중국계 물리학자라니.. 게다가 둘은 중국에서 태어나 학사까지는 중국대학에서 공부했다.)

박사학위 후 펜실베니아 대학, 옥스포드 대학, 록펠러 대학에서 박사후 연구원을 거쳤다. 그에 따르면 1960-1970년대에는 앞세대에서 이론 물리학 교수를 많이 뽑은 탓에 자리를 얻기가 어려운 시기였다. 때문에 오랜 기간 떠돌이 생활을 하다가 1979년 콜로라도 대학에서 교수직을 얻게 된다. 

그러나 얼마지나지 않아서 뉴욕에 있는 가족과 떨어져서 박봉의 교수직을 이어가는 것에 염증을 느껴 벨 연구소로 이직한다. 교수로 근무하며 2만5천 달러 수준의 연봉을 받았는데 벨 연구소에서는 5만 달러로 점프한다. 지금으로부터 40년 전인 것을 생각하면, 엄청난 연봉이다. 한국의 아파트 시세와 비교해보자. 아래 그림은 1980년대 강남아파트 가격이다. 가장 비싼 압구정 현대 아파트가 1억원 남짓이다. 벨연구소에서 2년만 일하면 압구정 현대 아파트 1채를 살 수 있었다.

<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/1980-gangnam-apt.webp" alt="1980년대 강남아파트 가격 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 1980년대 강남아파트 가격 </span>
</p>

### 벨 연구소
그는 벨 연구소를 유배지라고 표현했다. 당시 벨 연구소에는 학계에서 자리를 잡지 못한 물리학 박사들이 몰려들었다. 그런데 회사는 지나치게 관료적이어서 무언가 새로운 것을 배우고 만드는 일과는 거리가 먼 관리적인 일만 하게했다. 과거에는 클로드 섀넌(Claude Elwood Shannon)을 포함해 많은 기라성 같은 학자 또는 개발자가 일하던 곳이지만 1980년대의 상황은 달랐던 것 같다. 때문에 5년만에 월스트리트의 골드만삭스로 이직한다.

### 골드만삭스의 퀀트가 되어서
1980년대 월스트리트에는 과학자에 대한 수요가 넘쳤는데, 블랙-숄즈 방정식의 발견과 컴퓨터의 발전 때문이다. 더만도 이러한 시류를 탄 인물 중 하나였다. 

그에 따르면 당시 벨 연구소에서 5만달러의 연봉을 받고 있을 때 헤드헌터들이 15만 달러의 연봉을 받을 수 있는 면접자리를 소개해준다고 전화를 돌렸다고 한다. 더만은 어찌저찌 헤드헌터의 소개로 골드만삭스 고정수익부증권 부서에 퀀트로서 합류하게 된다.

더만은 골드만삭스에서 블랙-숄즈 방정식을 발견한 [피셔 블랙(Fischer Black)](https://ko.wikipedia.org/wiki/%ED%94%BC%EC%85%94_%EB%B8%94%EB%9E%99)과 함께 금융상품의 가치 평가 모델을 만드는 일을 했다. 골드만삭스에서 3년 일한 뒤 살로몬 브라더스를 거쳐서 다시 골드만삭스에 돌아와 전무자리까지 오르게된다. 

그에 따르면 골드만삭스의 업무 분위기는 금융업계보다는 학계에 가까워 보인다. 거기서는 새로운 모델을 만드는 일에 투자하며 피셔 블랙같은 거물 학자를 고용하고 논문도 자유롭게 낼 수 있었다. 공학계의 벨 연구소가 관료적이고 금융계의 골드만삭스가 학구적인 것은 아이러니하다.

당시의 퀀트는 어디까지나 트레이더를 보조하는 지원자였다. 높은 연봉과 직급으로 올라가려면 트레이더가 돼야했다. 퀀트는 트레이더들이 편하게 거래를 할 수 있도록 옵션등 금융상품의 가치평가 모델과 소프트웨어를 만들어주는 역할만 할 뿐이었다. 이 점에서 오늘날 대중에 퀀트에게 가지는 인식은 환상에 가깝다고 느낀다. 수학적 방법으로 시장의 비밀을 풀어내서 돈을 쓸어모으는 것과는 거리가 꽤 많이 멀다.

더만은 골드만삭스에서 옵션의 내재적 변동성이 잔존기간에 따라 달라지는 변동성 스마일을 다룰 수 있는 금융 이론을 만들었다. 이 공로로 2000년에는 올해의 금융공학자상을 받게된다. 학계가 아닌 업계 인물로서 상을 받은 유일한 사람이다. 이 업적으로 2002년 골드만삭스를 떠나 박사학위를 받은 콜롬비아 대학으로 돌아가 금융공학 교수직을 얻게된다.

# 책에서 참고할 내용
자전적인 책이기 떄문에 저자가 인생을 살아가며 깨달은 점들을 고스란히 느낄 수 있다. 저자 시대의 학계와 업계 환경을 이해하는 재미도 있고, 학계에서 살아남기 위해 노력한 모습 그리고 회사의 정치와 이직에 대해 고민한 모습들은 누구에게나 도움이 될만한 내용들이다.

아래에는 이러한 것들 중 두고두고 참고할 만한 내용을 발췌한 것이다.

## 물리학자

### 학계에 있으며 한계를 느낀 순간
>열예닐곱일 때에는 아인슈타인 같은 사람이 되기를 원했다. 스물한 살일 때에는 파인만 같은 사람이 된다면 아주 기뻐했을 것이다. 스물네 살이 되자 리정다오 정도면 만족하겠다고 생각했다. 1976년 무렵, 옥스퍼드에서 또 한 사람의 박사후연구원과 함께 사무실을 나눠 쓰면서, 바로 옆 사무실에 있는 박사후연구원이 프랑스에서 열리는 세미나에서 발표자로 초대받았다는 사실을 부러워하는 수준에 다다랐다. 금융의 주식 옵션 역시 이와 아주 비슷한 방식으로 만기 일이 다가옴에 따라 잠재 가치를 잃어버린다. 옵션 이론가는 이를 '노후화' 현상이라 부른다.

### 대학원생의 삶
>나는 몇 년 전 하버드의 노벨상 수상자 엘리아스 코리 교수의 연구실 에서 공부하던 대학원생 두 명이 자살했다는 내용의 〈뉴욕타임스〉 기사를 읽게 됐다. 이 기사에 대한 독자 편지가 1998년 12월 20일자 일요판 〈뉴욕타임스>에 실렸는데, 편지에서 뉴욕 주 어퍼나이악의 린다 록버그는 대학원생의 생활에 대해 다음과 같이 논평했다.

* >"대학원 교육은 사춘기의 연장이다. 어쩌면 그때보다 지금이 더 그럴 것 같은데, 대단히 명석한 청년이라도 이 기간을 지나는 동안 자신의 세계가 담당 지도교수의 연구실 크기에 맞게 찌부러지는 것을 보게 된다. 자신의 정체성이 논문 프로젝트의 결과물에 매여 있는 이들 대학원생은 다른 가능성(교직, 산업체, 또는 완전히 다른 유형의 직업)을 경멸의 눈으로 바라보는 분위기에 익숙해진다. 주당 예를 들면, 50시간만 일하면 되는 의미있는 일을 하면서 일정 수준의 급료를 원하는 것을 배신이라 여긴다".

> 정확한 표현이다. 우리는 과학에 대한 사랑 때문에 과학에 뛰어들었고, 그래서 그 나머지는 반눈에도 차지 않았다. 일부는 박사 논문 자격시험에서 떨어져 1년 만에 떠났다. 또 일부는 시험은 통과했지만 지도교수를 찾지 못해 포기했다. 많은 수의 대학원생은 논문이 진행되는 도중에 수건을 던졌다. 그 나머지는 겨우겨우 빠져나와 박사 후 연구직이라는 떠돌이 생활로 옮겨 갔다. 우리 가운데 편안한 시간을 보낸 사람은 거의 없었다. 이상의 추구를 포기하고 좀 덜 야심찬 목표를 향해 떠나가는 친구들은 마치 수녀원에서 낙오한 수련수녀처럼 부끄러운 얼굴이 되어 떠났다. 떠나는 그들을 깔보는 눈으로 바라보는 우리가 느낀 무언의 자기혐오를 인정했다는 점에서 록버그는 특히 정확하게 꿰뚫어 보았다. 블레이크가 쓴 「지옥의 격언」에서 "부끄러움은 자존심의 외투"라는 구절을 읽었을 때 나는 그 의미를 정확하게 이해할 수 있었다. 그렇지만 나중의 일이다.

### 노벨상 수상자의 허영심과 경쟁심
> 시간이 지나면서 나는 리정다오와 양전닝의 천재성에 어두운 구석이 있음을 알아차렸다. 1960년대 말에 어느 미국 물리학회 모임에 참석했는데, 이들 두 사람이 모두 같은 위원회 소속이었지만 둘이 서로의 존재를 외면하는 것을 보았다. 컬럼비아에서 티디의 수업을 들을 때에도, 그는 양전닝과 공동으로 발표한 발견의 핵심 부분을 설명할 때 자신의 공로에 초점을 맞추는 것 같았다. 나중에 어떤 사람이 내게 귀띔해 주었는데, 알고 보니 이 분야의 사람 치고 두 사람의 반목을 모르는 사람이 거의 없었다. 리정다오와 양전닝이 함께 일하지 않기 시작한게 벌써 몇 년이나 됐으며 이제는 서로 말도 하지 않는다는 것이었다. 훗날 물리학을 그만둔 뒤에야 나는 양전닝의 회고록을 보고 화가 난 티디가 쓴 회고록을 읽게 됐다. 복수심에 불타 쓴 그 글에는 두 사람이 논쟁 끝에 갈라선 사연과 양전닝이 그의 사무실에서 울었다는 내용이 기록돼 있었다.
 
> 나는 어느 쪽이 옳은지 전혀 알지 못한다. 지금 이 글에서 티디에게 초점을 맞추는 것은 오로지 그가 가장 내 눈에 잘 띄었고 그렇게 부러운 발견을 했고 또 우리가 푸핀 홀에서 들이쉬는 공기에 너무나 강력한 영향을 끼쳤기 때문이다. 노벨상을 받고 거의 불멸이라 할 수 있는 명성까지 얻고서도 허영심과 경쟁심을 극복할 수 없다는 사실을 알고 나니 실망을 금할 수 없었다.

### 박사학위의 의미
> 논문을 마치기까지 그토록 오랜 시간이 걸렸지만 그래도 나는 별다른 후회는 없다. 어떻게 보면 그런 고투를 이겨 낸 나 자신이 자랑스럽다. 그 시절 내가 배운 것-수학만큼이나 끈기까지-은 학계에서뿐 아니라 월 스트리트에서도 내게 큰 보탬이 돼 왔다. 어떤 분야에서 뭔가 새로운 것을 발견하려 할 때에는 여러 해 동안에 걸쳐 생각하고, 엉뚱한 곳도 파헤 치고, 막다른 골목에서 헤매고, 수렁에 빠지기도 하면서 다시 일어서서 계속 앞으로 나아가야 한다. 이런 목적이라면 박사 공부는 고통스럽기는 해도 좋은 훈련 과정이다.

> 오래 뒤 월스트리트에서 일할 때, 난생 처음 보는 학위인 'ABD'를 퀀트의 이력서에서 보고 황당해했다. 알고 보니 사회에서 흔히 쓰이는 약어로 "논문만 남겨 두었다(Al But Dissertation)"는 뜻이었다. 박사 학위 공부를 했지만 논문을 완성하기 전에 학계를 떠난 사람을 나타내는 말이었다. 박사라는 것은 정의상 논문에 소개된 독창적 연구를 마치는 것을 위주로 하는 연구 학위이고, 따라서 나는 ABD를 촌극 속의 박사 정도로 바라 보았다. 그것이 연구에서 필요로 하는 혁신과 노력의 가치를 깎아내린다는 점에서 마음에 들지 않았다.

### 박사후연구원의 삶
> 나는 박사후연구원 생활을 일종의 성직자 생활로 상상하고 있었다. 지식에 바친 더없이 행복한 삶으로 미화하고 있었던 것이다. 일류 대학교의 경우 이론 물리학을 연구하는 박사후연구원에게는 일반적으로 부과되 는 세속적인 의무가 전혀 없었다. 강의도, 행정 업무도, 정해진 출퇴근 시간도 없었다. 그것을 빼면 남는 것은 초월 자체였다. 연구원은 연구에 대한 재능으로 채용됐다. 할 일이라고는 오로지 자신의 흥미를 끄는 것 중 뭔가 개념적으로 가치있는 대상을 찾아 연구하는 일뿐이었다. 중요한 것은 나의 성취뿐이었다. 간단했지만 한편으로 위험부담도 컸다. 내가 아는 누구도 부자가 된다거나 장차 얼마를 벌게 될 거라는 생각은 별로 하지 않았다. 다들 뭔가 원대한 것을 성취하기를 바랐고 그것을 위해 일생을 기꺼이 바칠 수 있었다. 우리는 종신 지위를 얻고 나서 '물리학 하기' 를 그만두는 교수들을 경멸했다. 나이가 들면서 우리는 서른이 넘어 위대한 발견을 한 사람들에 대한 이야기를 들으며 위안을 얻었다.  

> 가을에 2년 기한의 연구원직을 시작하면 1년간의 유예 기간을 갖게 되는데, 그 기간에 뭔가 흥미로운 연구를 시작하고 마무리하여 출판해야만 2년째에 전 세계 다른 연구소나 학과의 박사후연구원직에 지원할 수가 있었다. 

>카오스 이론에 끼친 공로로 유명한 미첼 파이겐바움이 이를 잘 묘사해 주 었다. "이런 2년 연한의 연구직에서는 본격적 연구가 거의 불가능했다. 1 년이 지나고 나면 다음에는 어디로 갈지 고민이 시작되기 때문이다." 운이 나빠 1년짜리 박사후연구직밖에 못 구할 경우에는 유예 기간이 없었는데, 그것도 그리 드문 일이 아니었다. 그러면 연구원 생활을 시작하자 마자 다음 일자리를 찾아 지원을 시작해야 했다. 빠져나올 수 있는 유일한 길은 -학계 내에서 물리학 하기를 포기하는 일 말고- 크게 인정받을 수 있는 논문을 쓴 다음 몇 안 되는 교수직을 제의받는 것이었다.

> 내 박사 친구 중 몇몇은 열정은 있으나 물리학을 계속해야 한다는 절박감 때문에 "무보수직" 연구원이 됐다. 이들은 아무 곳에서도 일자리를 찾을 수 없어, 최고 수준의 연구소에 가서 책상과 초보적인 연구 설비만을 허락받아 무보수로 연구를 계속했다. 이들의 목표는 자극적 환경에 들어가 좋은 인맥을 쌓고, 그러다가 보수가 있는 일자리를 얻을 만한 연구 결과를 내놓는 것이었다. 그중 한 친구는 이류 연구소이기는 하나 보수도 있는 연구원직을 거절하고 하버드에서 무보수직으로 일했다. 그리고 하버드에서 쓸 만한 연구를 해냈고, 그것으로 일류에 속하는 연구소인 스탠퍼드 선형 가속기 센터에서 유급 연구원직을 따냈다.

### 대학이 박사후연구원이 필요한 이유
> 박사후연구원 생활은 하나의 격세유전으로, 오랜 과거로부터 전해 내려온 유물이었다. 박사후연구직은 대학원생과 교수 사이에 잠시 동안의 쉴 참을 마련하기 위해 만들어진 자리이다. 그렇지만 스푸트니크 이후 미 국이 과학을 바라보는 시각은 사실상 전쟁이나 마찬가지로 변했고, 이로 인해 젊은 과학자가 양산됐다. 이제 종신 교수직에 오른 이들이 모든 교수직을 다 차지하고 있었다. 은퇴하려면 앞으로 30년은 더 있어야 했다.
 
> 교수에게는 학생이 필요한 법, 그래서 물리학자를 꿈꾸는 사람은 계속해서 박사 과정으로 들어가지만 과정의 끝을 빠져나와 보면 갈만한 곳이 거의 없었다. 이 문제를 일시적으로나마 해결해 주는 게 바로 박사후연구원 자리였다. 연구원직은 2년 정도 머물러 있을 수 있었고 보수는 아주 적었다. 그럼에도 이런 방식은 대학교 입장에서는 잘 굴러갔다. 매년 젊은 물리학 연구원을 새로 한 무더기씩 확보할 수 있었고, 어쩌다 교수직 자리가 나면 그중 특별히 뛰어난 사람을 골라 뽑을 수 있었던 것이다.

### 과학적 발견에 대한 고찰
> 내 친구 중에는 물리학과 금융 분야에서 있었던 여러 가지 위대한 발견이 당연하다는 식으로 곧잘 말하는 이가 있다. 당연해 보이기는 하겠지만 그것은 망상이다. 역사적인 맥락에서 일단 배우고 나면 그런 발견이 대개 명백해 보인다. 그렇지만 그런 발견 뒤에는 언제나 온갖 편견과 혼란, 경쟁 중인 수많은 이론이 자리잡고 있다. 금융이든 이론 물리학이든, 아무리 작은 발견이라 해도 그것은 오랫동안의 열중과 노고와 고역 끝에 얻어낸 것이다.

### Publish or Perish
> 학계에 대해 알지 못하는 내 친구는 우리같은 박사후연구원이 지키며 살고 있는 규칙을 이해하지 못했다. 한번은 어느 남아프리카 친구에게 내가 쓴 글이 물리학계에서 가장 권위 있는 정기간행물 중 하나인 〈물리 학 리뷰 레터>에 채택됐다고 자랑한 적이 있다. 그랬더니 그는 그걸로 그쪽에서 내게 원고료를 얼마나 지불하는지 물었다. 당황스러웠지만 나는 그게 그 반대로 돌아간다는 사실을 설명해 주었다. 내가 소속한 물리학과에서 그 논문이 인쇄될 수 있도록 지면 사용료 수백 달러를 미국 물리학회에다 지불해야 했다. 그 친구는 도무지 이해하지 못했다. 내가 공명을 알리기 위한 출판에 맛을 들인 것으로 생각했다.

> 첫 학사년도가 끝나는 1974년 5월에 이르러 나는 막다른 길로 나아가고 있었다. 앞으로 세 달이면 다음 연구직을 물색하기 시작해야 하는데 아직 논문을 출판하지 못한 것이다. 그보다 더 심각한 문제는 출판할 수 있을 만한 그 어떤 활동에도 관여하지 못하고 있다는 사실이었다. 나는 "논문을 내놓느냐, 자리 를 내놓느냐" 하는 말의 의미를 피부로 느낄 수 있었고, 친구와 친지에게 앞날이 암담하다는 말을 꺼내기 시작했다.

### 의대로 전향한다면
> 1978년 어느 날, 갑자기 의과대학에가서 의사가 되면 어떨까 하는 생각을 머릿속에서 굴리게 됐다. 요약하면 이런 식이었다 -물리학은 가혹 한 능력주의다, 그 능력은 대부분 상위의 몇몇 전설적 인물에 집중돼 있다, 파인만 정도의 인물이 되지 못하면 아무것도 아니다. 유능하지만 뛰어나지는 않은 연구직 물리학자는 자부심을 느낄 거리가 거의 없었다. 내 가 제공하는 것을 누가 필요로 하겠는가? 어디선가 자그마한 대학에서 그 귀한 전임 강사 자리를 얻으려 노력해 볼수도 있지만, 매주 그렇게 많은시간을 가르치며 보내려면 가르치는 일을 나보다는 좋아해야 한다. 그래서 초월에 대한 추구라 생각하는 것에 내가 일생을 바치고 있다고 생각하니 좋기는 했지만, 뭔가가 부족하다는 생각이 들기 시작했다. 그와는 대조적으로 의학에서는 단지 유능하기만 한 것으로도 뭔가를 뚜렷하고 구체적으로 기여할 수 있으리라는 생각이 들었다.
 
> 이런 식으로 생각한 사람이 나뿐이 아니었다. 최근 여러 의과대학에서 의예과 학위가 없는 지원자도 자연과학 방면에 박사 학위가 있으면 받아 들이기 시작했다. 코럴게이블스에 있는 플로리다 대학교에서는 박사 학위 소지자를 여름학기 포함 2년 만에 의학박사로 바꿔 줄 수 있었지만, 지원할 수 있으려면 대학원 입학 자격시험(GRE)에 합격해야 했다. 그런데 나는 그 자격시험을 치렀던 적이 없었다. 내가 컬럼비아에 지원한 1966년 남아프리카에서는 이 시험을 시행하지도 않았다. 나는 노크 없이는 들어 오지 못하는 록펠러의 내 사무실 안에 틀어박혀, 내가 무엇을 하고 있는 지 아무에게도 말하지 않은 채 한두주 동안 자격시험 모의고사 문제를 풀며 공부했다. 대학 시절 배운 물리학 지식을 되살리고, 자연계의 상수 값과 원자 물리학의 에너지 준위 값을 외웠다. 대학원 첫해 이후 공부하지 않았던 모든 과목을 다시 들추어 보았다. 그러다가 조수아가 고열로 앓았기 때문에 뜬눈으로 밤을 지새운 다음 날인 어느 토요일, 드디어 컬럼비아 대학교 캠퍼스에서 하루 종일 일반 시험과 물리학 시험을 치렀다. 시험 결과는 좋았다. 코럴게이블스 측에서 내 면접을 위해 록펠러 근처의 슬론케터링 암센터에서 인턴으로 근무하고 있는 졸업생 한명을 보냈고, 그러고는 입학 허가가 났다.

### 운은 죄를 갚는 기계
>톨스토이는 운을 죄를 갚는 기계 장치라 했는데, 그 무렵 나는 그 말의 의미를 이해할 것 같았다. 우주는 우리가 허영과 야심과 자존심을 버리고 하느님을 받아들이기를 원하고 있었다. 자발적으로 그렇게 하는게 가장 바람직했다. 그렇지만 스스로 그렇게 하지 않을 경우, 우주의 일상적 작용인 운이 우리가 항복할 때까지 마치 감자 껍질 벗기는 기계처럼 기계적으로 우리의 허영심을 조금씩 갈아내 버리고 자존심과 자만심이라는 껍데기를 조금씩 벗겨 내는 것이다.

## 벨 연구소
### 관료적인 벨 연구소
> 우리는 일을 해내고 싶어 한다는 게 문제였다. 값비싼 첨단 장비를 만지작거리는 것만으로 즐겁게 지낼 수 있는 성격이라면 벨 연구소는 재미있는 곳이 될 수 있었겠지만 그런 생활은 우리 직성에 맞지 않았다. 나는 뭔가를 만들어내는 데에서 오는 뿌듯함을 느끼고 싶었다. 그러나 제 5관 건물 내에서 내가 손댄 프로젝트 중에는 막다른 길에서 지리멸렬한 상태로 끝나버린 게 많았다. 약간의 연구를 하고, 내부용 서류를 만들고, 그러면 할리가 다운스에게 보고하고, 그러면 다운스는 뭔가 도무지 이해할 수 없는 애매모호한 이유를 내세워 실패 내지는 성공으로 끝맺어 버리는 것이다. 연구 결과는 회사 소유이기 때문에 우리에게는 출 관할 권한이 없었다. 그렇지만 그런 연구 결과는 회사 내의 누구에게도 쓸모가 없는 때가 많았다. "정보는 자유를 원한다." 누가 만들어 냈는지는 몰라도 나는 이 구호에 점점 더 동조하게 됐다.

> 나는 연구소의 관리직 숭배 풍토를 혐오했다. 거기 들어갔을 때 나는 서른다섯 살이었는데, 제90구역에서는 관리자가 아닐 경우 아무런 존중도 받지 못한다는 사실을 금방 깨달았다. 그때까지 물리학을 하며 보낸 세월 동안에는 무엇보다도 재능과 기술이 중요했다. 뭔가를 만들어 내는 생활을 접고 행정직을 맡는 사람을 보면 측은하다는 생각이 들기까지 했다.

> 그러나 벨 연구소에 오니 재능은 관리자가 사들여 재판매하는 상품에 지나지 않아 보였다. 과장은 실제로 "기술적인 일"을 하지 못하도록 금지 돼 있었는데, 그런 일을 하느라 하급자와 경쟁하면 사기 저하가 야기될 수 있다는 이유에서였다. 그래서 관리직에 있는 사람은 사내의 정치에 대한 전문가로 변신했다. 이들은 스스로의 능력을 내버리고, 그 시기 그 조직에서만 가치가 있는 체제와 지나치게 밀접한 관계에 들어가버린 것 같 았다
 
> 나중에 골드만삭스로 이직했는데 그곳에서는 실질적 기술과 재능을 중시한다는 사실을 알고 마음이 놓이는 동시에 생기마저 느낄 수 있었다. 거래사, 판매사, 프로그 래머, 옵션 전문가 등 모두가 자신의 능력으로 일했고 게다가 돈도 아주 잘 벌고 있었다.

### 프로그래밍에 대하여
>나는 모든 것을 고스란히 처음부터 만들어 내야 직성이 풀리는 영리한 프로그래머를 많이 보아왔다. 그런 시도에 매달리는 프로그래머는 대개 끝 모를 구렁텅이에 빠져 헤어나지 못한다. 당연하게 거저 얻을 수 있는 것을 모든 기계에서 돌아가도록 새로 만들다 보면 안으로 안으로 자꾸자꾸 파고 들어가게 되는 것이다. 집을 짓기에 앞서 망치, 톱, 대패를 스스로 만들어야 직성이 풀리는 고집스런 다른 사람과 데이브의 차이는 어디까지 파고 들어가야 할지를 안다는 점이었다 . 그는 꼭 필요한 도구만 완성되면 그것만 가지고 시스템 자체를 만들어 내곤 했다.

## 월스트리트
### 퀀트의 관점
> 지난 20년 동안 월스트리트와 런던의 시티를 통틀어, 대부분의 대형 금융 기관과 다수의 소형 금융기관에서 소수의 전직 물리학자와 응용 수학자가 자신의 기술을 증권시장에 적용하려는 노력을 기울여 왔다. 로켓 공학이 과학에서 가장 발전한 분야인 것으로 착각한 사람들이 이들을 예전에 "로켓 공학자"라 부르기도 했는데, 지금은 흔히 "퀀트"라는 이름으로 불린다.

### 금융공학
> 퀀트와 동료들은 "금융공학"에 종사하고 있는데, 이는 "정량적 금융"이라는 이름이 더 어울릴 잡다한 활동을 가리키는 괴상한 신조어다.
 
> 이 분야는 물리학에서 영감을 받은 모델, 수학적 기법, 그리고 컴퓨터 과학이라는 학제 간 활동으로, 모두 금융 증권의 가치 평가를 목적으로 하고 있다. 가치와 불확실성 간의 관계를 제대로 꿰뚫어 볼 수 있는 최고 수준에 이르면, 금융공학은 진짜 과학에 근접한다. 최악의 경우에는 복잡한 수학을 이렇다 할 이유 없이 동원하여 뒤죽박죽 섞어 놓은 사이비 과학이다.

### 1980년대 물리학자들이 퀀트가 된 배경
> 물리학자가 다른 분야로 흘러들어 간 것은 전통적으로 이들을 흡수해왔던 취업시장, 즉 학계의 일자리가 1970년대에 붕괴된 것에도 기인한다. 그 30년 전 제2차 세계대전 동안 레이더와 원자폭탄이 발명됐고, 이에 따라 전쟁이 끝난 후의 미국 정부는 물리학이 쓸모 있는 학문임을 인식했다. 스푸트니크의 우주여행이 성공한 데 충격을 받은 미국 국방에너지부는 순수 연구 활동을 위한 자금을 좀 더 풍족하게 대주기 시작했고, 그런 방면의 연구를 하기 위해 보조금을 찾아다니는 물리학자는 자신의 연구 결과가 가져다줄 부수적 효과를 부풀리지 않을 정도로 고매하지는 않았다. 1960년대 동안에는 대학교의 물리학과가 성장하고 일자리가 늘어났다. 장학금 지원이 늘어나자 이 분야에 흥미를 느끼는 열렬한 학생들이 대학원으로 물밀 듯 몰려들었다.

> 호시절은 그리 오래 가지 않았다. 베트남 전쟁이 끝날 무렵 경제사정이 악화된 데다 과학이 전쟁을 섬기는 데에 대한 대중의 혐오감이 확산되면서 연구 기금이 대폭 줄어들었다. 1970년대와 1980년대가 지나는 동안, 기초 과학 연구에 일생을 바치기를 바랐던 이론 물리학자 중 많은 수가 학계에 남아 있으려면 여기저기 떠돌아다니는 노동자가 되는 수밖에 다른 도리가 없었다. 대학교든 국가의 연구소든 자리가 나는 곳이면 어디서든 단기간의 임시 직책을 맡아 일했다. 우리 중에는 결국 급료가 낮은 학계의 반영구직조차 찾기를 포기하고 다른 분야로 눈길을 돌린 사람이 많다.

### 월스트리트가 물리학자들을 필요로한 이유
> 우연한 일이지만, 물리학자를 학계에서 몰아낸 바로 그 변화의 흐름 때문에 월스트리트는 그들을 받아들이기 시작했다. 1973년 아랍의 석유금수 때문에 에너지 가격이 폭등하고 금리가 상승했다. 인플레이션이 닥쳐 올 거라는 두려움으로 인해 금값이 금세 온스당 8백 달러를 상회했다. 갑자기 금융시장이 예전보다 더 불안정해 보이기 시작했다. 전통적으로 보수적 투자 대상이라 생각했던 채권이 어느 날 갑자기 그 누구도 상상하지 못한 정도로 위험도가 높은 대상으로 간주됐다. 예전의 주먹구구는 더이상 먹혀들지 않았다. 금융기관에서는 금리와 주가의 움직임을 이해하는 일이 과거 어느 때보다도 중요해졌다. 위험관리와 헤지가 새로운 절대명령이 됐고, 새로 인지된 너무나도 많은 위험 앞에 노출되고 보니, 변동으로부터 보호받을 수단을 제공해 주는 정교한 새로운 금융상품이 급증했다.

> 게다가 물리학자와 공학자는 만능이었다. 수학, 모델링, 컴퓨터 프로그래밍에 동시에 능하면서 새로운 분야에 대한 적응력과 자신의 지식을 활용하는 능력에 대한 자부심이 대단한 사람이었다. 월스트리트는 이들을 불러들이기 시작했다.

> 1980년대에는 얼마나 많은 물리학자가 투자은행으로 몰려들었는지, 내가 아는 어느 헤드헌터는 이들을 POW  부르기까지 했다. 월스트리트의 물리학자(Physicists on Wall Street) 라는 뜻이다.

### 물리학자들이 월스트리트에서 무엇을 하는가
> 물리학자는 그러면 월스트리트에서 무엇을 하는가? 주로 증권의 가치를 판별하기 위한 모델을 만든다. 투자은행이나 헤지펀드, 또는 블룸버그 나 선가드 같은 금융 소프트웨어 회사에 파묻혀, 기존 모델을 만지작거려 새 모델을 개발해 내는 것이다.

### 파생증권의 존재이유
> 그것은 파생증권을 이용하면 투자은행, 자산 관리사, 법인, 투자자, 투기업자 등과 같은 고객이 떠맡거나 회피하고자 하는 위험을 정밀하게 조절할 수 있기 때문이다. 아이비엠 주식을 사는 투자자는 그 주식을 소유하는 위험을 전부 떠맡는다. 그가 소유하는 주식의 가치는 아이비엠의 주가에 비례하여 늘고 준다. 그와는 달리, 아이비엠 콜 옵션은 손실에는 제한을 걸어 주는 한편(주가가 100달러 아래로 떨어질 경우 옵션을 사들이는 데에 들어간 비용 말고는 아무것도 잃지 않으므로), 얻을 수 있는 잠재 이득에는 한계가 없다 (주가가 100달러를 넘김에 따라). 이득이라는 긍정적 부분과 손실이라는 부정적 부분 사이가 이처럼 대칭적이지 않은 것이 파생 증권의 특징이다.

### 옵션과 과일샐러드
> 블랙-숄스 모델은 기초 주식으로부터 옵션을 만들어 내는 방법을 알려 주고 또 그렇게 하는 데에 들어갈 추정 비용을 거의 기적처럼 알려 준다. 블랙과 숄스에 따르면 옵션을 만드는 과정은 과일 샐러드를 만드는 것과 아주 비슷하고 주식은 과일과 약간 비슷하다.

> 사과와 오렌지만으로 만든 간단한 과일 샐러드를 팔고 싶다고 하자. 500그램 통조림 한 개에 얼마를 받아야 할까? 합리적으로 보면, 먼저 원재료인 과일의 시장 가격과 통조림 제조 및 유통 비용을 살펴본 다음, 그같은 단순한 재료를 섞어 혼합물을 제조하는 총비용을 계산할 것이다. 1973년, 블랙과 숄스는 사과와 오렌지를 섞어 과일 샐러드를 만드는 것과 비슷한 방법으로 얼마간의 아이비엠 주식과 현금을 혼합함으로써 아이비엠 옵션을 만들 수 있다는 사실을 보여 주었다. 물론 옵션을 만드는 작업은 과일 샐러드를 만드는 작업보다 약간 더 복잡하다. 그렇지 않다면 그보다 일찍 누가 알아냈을 것이다. 한편 과일 샐러드의 혼합 비율은 제 조 과정이 반복돼도 일정하게 유지되지만 (예를 들면 사과 50%, 오렌지 50%), 옵션의 비율은 끊임없이 바뀌어야 한다. 옵션에서는 주가가 변화함에 따라 혼합물 내의 주식과 현금 비율을 지속적으로 조정해 주어야 한다. 과일 샐러드에 비유해 보면, 처음에는 사과 50%와 오렌지 50%에서 시작했지만, 사과 값이 올라가면 사과 40%, 오렌지 60%로 바뀐다. 그러다가 사과 값이 떨어지면 사과 70%에 오렌지 30% 비율로 바꿔 주어야 하기도 한다. 어떻게 보면 시간이 지나면서 원료의 가격 변동에 따라 비율을 조절 하여 혼합물의 가격을 일정하게 유지해 주기 위해 애쓰고 있다고 볼 수 있다. 이때 적용해야 하는 정확한 조리법을 블랙-숄스 방정식으로 산출 하는 것이다. 이 조리법에 따라 혼합물을 섞을 때 들어가는 비용은 블랙-숄스 공식의 해답을 통해 알 수 있다. 

### 블랙-숄즈 방정식의 혁명
> 이제 거래사는 온갖 종류의 기초 증권을 바탕으로 고객이 원하는 수준의 위험도에 정확하게 맞춰 옵션을 제조, 판매하면서 그 위험을 자신이 떠맡지는 않을 수 있게 된 것이다. 그것은 산소와 수소가 가득한 목마른 세계에서 누군가가 드디어 물을 합성하는 방법을 발견한 것과 같았다.

> 거래사는 블랙-숄스 모델을 이용하여 고객에게 팔 옵션을 제조(또는 '합성', 또는 '금융 공법으로 가공')한다. 이들은 시장에서 사들이는 일반 주식을 바탕으로 옵션을 구성한다. 역으로, 이들은 다른 사람으로부터 사들이는 옵션을 해체해서 일반 주식으로 환원시켜 시장에 내다 팔 수 있다. 이런 방법으로 거래사는 자신이 떠맡을 위험을 경감시킨다. (블랙-숄스 모델은 모델에 지나지 않기 때문에, 그리고 금융에서 100% 정확한 모델은 없기 때문에 이들이 위험을 완전히 상쇄시킬 방법은 없다.) 이와 같은 합성 및 해체 작업에 거래사는 수수료를 (옵션의 웃 돈을) 매긴다. 고급 레스토랑의 요리사가 손님에게 원재료 값만 요구하는 게 아니라 그가 사용한 조리법과 조리 기술에 대한 값도 청구하는 것이 나, 양재사가 고급 양복을 맞춰 주고 원단 값과 공임을 모두 청구하는 것과 마찬가지이다.

### 물리학자와 퀀트의 차이
> 증권 거래업체에서 일하는 실무자 퀀트의 삶은 물리학자와는 판이하게 다르다. 나는 오랫동안 물리학 연구 분야에서 종사하다가 1985년 말에 처음으로 월스트리트에 발을 디뎠는데, 그때 내 새 상사는 1년 전에 자신이 만든 모델이 안고 있는 문제점을 바로잡는 작업을 내게 맡겼다. 채권 옵션용으로 블랙-숄스 모델을 본떠 만든 모델이었다. 나는 물리학자답게 차근차근 신중하게 작업을 시작했다. 해당 논문을 읽고, 이론을 익히고, 문제를 분석하고, 그런 다음 모델을 적용한 컴퓨터 프로그램을 재작성하기 시작했다. 그렇게 몇 주가 지나자 내 상사는 나를 한쪽으로 따로 불렀다. 일의 진행이 더딘 것을 보고 더 이상 견딜 수가 없었던 것이다. 그러더니 약간은 가시 돋친 어조로 이렇게 말했다. "이봐, 이 일에서는 네 가지 만 알면 돼. 덧셈, 뺄셈, 곱셈, 나눗셈 말이야. 게다가 나눗셈은 필요도 없는 때가 거의 대부분이란 말씀이야!"

> 나는 무슨 말인지 알아들었다. 물론 모델에 사용되는 수학은 산수보다는 차원이 높다. 그렇지만 그의 말은 옳았다. 옵션 거래사는 대부분 고객이 필요로 하는 상품을 최대한 효율적으로 제조하는 일, 즉 서비스를 제공하고 수수료를 받는 일을 생업으로 삼고 있다. 그들에게는 간단하고 이해하기 쉬운 모델이 복잡하고 더 나은 모델보다 더 쓸모가 있는 것이다.

> 커다란 이윤폭에 최대한 많은 거래를 성사시키는 것이 관건인데, 완벽하게 처리하기가 불가능한 세밀한 부분을 붙들고 씨름하는 일은 방해가 될 수 있다. 게다가 "더 나은" 모델의 조건이 뭔지를 정확하게 정의내리기 란 쉽지 않은 때가 많다. 시장이라는 환경에서 통제된 실험은 희귀하기 때문이다. 결론적으로 내가 그 모델을 개선시키기는 했지만, 거래사는 내가 짜넣은 편리한 화면 구성 덕을 가장 많이 봤다. 단순히 인체공학적으로 바꿔 주었을 뿐이지만, 그것이 약간의 모순점을 잡아내는 것보다 그들의 업무에 훨씬 더 큰 영향을 미쳤다. 이제 거래를 원하는 고객의 요구를 더 많이 소화할 수 있게 됐기 때문이다.

### 채권 vs 주식
> 옵션이 생겨난 곳은 주식 세계이지만 더 널리 이용되고 있는 곳은 고정 수익형 증권이라는 더 넓은 세계이다. 주식에는 (적어도 언뜻 보기에는) 수학 이라는 세부조건이 없다. 주식 한 주를 소유하고 있다면 그에 따른 보장은 아무것도 없다. 아는 것이라고는 가격이 올라갈 수도 내려갈 수도 있다는 사실뿐이다. 그와는 달리 채권같은 고정수익형 증권은 장차 정기적으로 이자를 지불하고 또 최종적으로는 원금을 상환한다는 부수적 조건이 딸린 화려한 장치이다. 이런 세부조건 때문에 고정수익형 증권은 보통주보다 훨씬 더 많은 부분에서 수학을 필요로 하며, 그런만큼 수학적 분석에 훨씬 더 적합하다. 모든 고정수익형 증권 -몇 가지 예를 들면 채권, 담보부 채권, 전환사채, 스왑 등-은 어떤 가치를 기반으로 삼고 있고, 따라서 편의상 시장의 기초 금리에서 파생된 증권으로 간주한다. 금리 파생 상품은 성격상 정상적 업무의 일부분으로서 채권을 발행해 돈을 빌려야만 하는 각종 법인에게 매력적인 상품인데, 이 채권의 가치는 금리나 환율 변동에 따라 바뀐다. 금리의 움직임을 현실적인 모델로 만들기는 훨씬 더 어렵다. 주가에 비해 더 복잡한 방식으로 변화하기 때문이다. 따라서 금리를 모델화하는 작업은 지난 20년 동안 파생 증권 이론을 만들어 내는 어머니 역할을 해 왔다. 이 분야에서는 어디를 가나 퀀트가 일하고 있다. 

> 그와는 대조적으로, 보통주 세계에서는 퀀트가 비교적 드문 존재이다. 이곳에서 투자자는 대부분 어떤 주식을 매입할지에 관심이 쏠려 있는데, 이 문제를 해결하는 데에는 파생 증권을 다루는 고등 수학이 거의 도움이 되지 않는다. 고정수익형 증권과 보통주는 초점부터 근본적으로 다르다.

> 고정수익형 거래에서는 보통주 거래에서보다 정량적 기법 과 방법에 대해 더 잘 이해할 필요가 있다. 한번은 거래사로 일하고 있는 내 친구에게, 내가 아는 고정수익형 거래사들은 보통주 거래사들보다 더 똑똑해 보이더라는 말을 한 적이 있다. 그는 이런 대답으로 알기 쉽게 요 약해 주었다. "그건 보통주 방면에서는 똑똑해 봐야 경쟁력에는 아무 도 움도 되지 않기 때문이지."

### 블랙-숄즈 방정식 바깥의 퀀트
#### 통계적 차익거래
> 퀀트가 모두 블랙-숄스 모델을 가지고 작업하고 있다는 뜻으로 하는 말은 아니다. 일부는 과거의 주가 변동 패턴에서 규칙과 예측 가능한 부분을 찾아 활용하는, 즉 과거로부터 미래를 점치는 '통계적 차익거래' 라 는 분야에서 활동하고 있는데 점점 더 그 수가 늘어나고 있다. 헤지펀드는 시장 한쪽 귀퉁이의 아무도 찔러 보지 않은 부분에서 가격상의 작은 모순점을 찾아 그것을 활용하는 일종의 사설 펀드인데, 이들은 통계적 차익거래를 위해 지난 5년 동안 퀀트를 대거 고용해 왔고 지금도 계속해서 퀀트를 고용하고 있다.

#### 위험관리(Risk Management)
> 위험관리 또한 유행하고 있다. 그럴 만한 이유가 있다. 10여 년 전인 1994년에 전 세계 금리가 예기치 않게 갑자기 오르면서 수많은 투자은행의 채권 거래 영업장에서 막대한 손실이 일어났다. 이 때문에 이들은 그 때까지 초보적 수준으로 유지해 오던 위험관리 노력을 확대하게 됐고 또 증권 산업에서 종사하는 감사는 자기 회사가 떠안는 위험을 제한하는 방법에 초점을 맞추게 됐다. 이제 퀀트는 각 투자은행 내에서 회사 전체를 총괄하는 위험관리 팀의 일원으로 일한다. 이들의 임무는 회사 전체의 포 지션을 취합하여 현재의 위험과 미래의 있을 수 있는 손실을 정량적으로 산출하는 일이다. 그러나 확률이란 과거의 사건을 바탕으로 추정해야 하기 때문에, 이런 확률을 바탕으로 앞으로 막대한 손실이 일어날 수 있는 가능성을 계산한다 한들 신뢰할 만한 결과를 얻을 수 없다는 사실이 잘 알려져 있다. 시장의 붕괴는 벼락처럼 아무렇게나 떨어지는 게 아니다. 지난번의 붕괴를 피하느라 여념이 없는 군중의 광기가 만들어 내는 결과물인 것이다. 군중은 이런 광기에 휩쓸려 현재 진행형인 붕괴를 만들어 낸다. 1994년에 손실을 겪었지만, 1998년에 러시아의 채무 불이행 이후 전 세계적으로 채무 회수 바람이 불면서 또다시 크나큰 손실을 본 회사가 많다. 그래서 퀀트의 시장은 위험 감시와 관리 쪽으로 점점 더 바뀌고 있다.

### 트레이더 vs 퀀트
> 거래사와 퀀트는 원래부터 종족이 다르다. 거래사는 강하고 직선적이라는 점을 자랑으로 생각한다. 한편 퀀트는 비교적 신중하고 삼가는 편이다. 이런 개성 차이의 밑바탕에는 문화적 취향 차이가 자리 잡고 있다. 거래사는 행동을 위해 고용된다. 이들은 하루 종일 화면을 들여다보고, 경제 정보를 습득하고, 각종 자료표를 마구 뒤적거리며 미친듯이 살펴보고, 퀀트가 작성한 프로그램을 돌리고, 거래에 들어가고, 영업 담당과 중개사와 대화하고, 키보드를 두들긴다. 업무 시간에는 거래사와 진득하게 대화를 나누기가 어렵다. 띄엄띄엄 즉답형으로 대화할 수밖에 없고, 거래사 옆에 한 시간을 서 있어도 대화 시간이 도합 5분을 넘기기가 어렵다. 거래사가 하는 일에는 전자오락 같은 측면이 있다. 결과적으로 이들은 자 기주장이 강해지고, 본능적이며, 생각이 빠르고, 반드시 옳지만은 않지만 과단성이 있는 성격이 된다. 이들은 여러 가지 일을 동시에 진행시킨다.

> 퀀트는 다르다. 연구 활동에 익숙한 학자처럼 이들은 한 가지 일을 처음부터 끝까지 몰두하여 잘 해내는 쪽을 좋아한다. 직장 세계는 많은 일을 동시에 진행시켜야 하기 때문에 그와 같은 사치를 누리기가 어렵다. 내가 월스트리트로 옮겨 갔을 때 적응하기가 가장 어려웠던 부분은 다수의 임무를 나란히 진행시키는 법을 익히는 일이었다. 급하게 진행 중인 한 가지 일을 잠시 중단하고 그보다 더 급한 일을 먼저 진행시키고, 그 일을 마무리 짓고 나면 다시 원래의 우선순위로 돌아가는 것이다.

### 블랙-숄즈 방정식

> 1970년대 초에 이르기까지는 옵션의 가치를 딱 부러지게 산정하는 방법을 아무도 알지 못했다. 주가가 올라갈 때 이익을 보는 콜옵션은 경마와 비슷해 보였다. 해당 주식의 전망에 대해 낙관적이 되면 될수록 옵션 가격을 많이 지불하게 될 것이다. 공정가격은 생각하는 사람에 따라 달랐다.

> 그러다가 1973년에 피셔 블랙과 마이런 숄스가 옵션 가치 평가를 위해 그들 자신의 이름을 딴 블랙-숄스 방정식을 발표했다. 같은 해에 로버트 머턴은 두 사람이 발표한 방정식 이면에서 작용하는 논리를 이해할 수 있는 좀 더 엄정하고 통찰력 있는 방법을 내놓았다. 최종적으로는 그가 내놓은 형식론이 두 사람의 공식을 밀어내고 표준으로 자리 잡게 됐다. 머턴과 숄스는 1997년에 노벨 경제학상을 받았지만, 똑같은 공로가 있음이 확실한 피셔는 1995년에 세상을 떠나고 말았다. 2년만 더 살았어도 그는 분명 노벨상을 공동수상했을 것이다.

> 하버드에서 응용 수학 박사 학위를 받았던 피셔는 아서디리틀 회사에서 경영 자문으로 있는 동안 블랙-숄스 모델을 개발했다. 경영 자문이라는 일이 획기적 이론을 개발해 낼 최적의 환경으로 보기는 어려웠지만, 피셔는 언제나 자신의 배경이 실질적이면서 비정통적이라는 점을 자랑스레 여겼다. 공로가 인정되자 그는 시카고 대학교에서 또 매사추세츠 공과 대학에서 금융 담당 교수가 됐고, 마침내 1984년에는 학계를 떠나 골드만삭스에 들어갔다. 비록 머턴과 숄스는 한쪽 발은 학계에 담고 있었지만, 두 사람 역시 모두 잘로몬브라더즈에서 자문사로 또는 직원으로 일했고, 그러다가 1994년에는 롱텀 캐피털매니지먼트의 파트너가 돼 자본을 끌 어들이는 일을 했다.
 
> 피셔는 일생 동안 평형이라는 개념에 진정으로 심취해 있었고, 1960년대 말에는 평형 조건을 시장 자체에 적용함으로써 블랙-숄스 방정식을 만들어냈다. 물리학에서 평형은 평범하면서도 대단히 강력한 개념이다. 평형에서, 안정을 이룬 계 안에서 우리가 관측하여 얻으려는 양적 수치는 두 가지 힘이 서로 반대로 작용하여 서로 정확히 상쇄되게 하는 수치이다. 예를들면 한 물체의 온도는 평형 온도에 다다르면 더 이상 올라가지 않는데, 이때 그 물체로 흘러들어 가는 열은 그 물체에서 빠져나오는 열과 상쇄된다. 피셔는 시장 가격이 이와 비슷한 상쇄 작용에 의해 결정된 다고 믿었다. 피셔는 먼저 주식에 대한 옵션과 해당 주식 자체는 서로 평형을 이루어야 한다는 - 각기 안고 있는 단위 위험당 똑같은 기대 수익률이 각각의 가격을 통해 투자자에게 제공되어야 한다는 뜻에서 - 조건을 제시함으로써 블랙-숄스 방정식을 얻었다. 그러면 투자자는 주식을 사느냐 옵션을 사느냐 하는 문제를 공평하게 바라볼 수 있다. 이 조건을 수식으로 적은 것이 블랙-숄스 방정식이었으며, 이 방정식을 통해 옵션의 가치가 결정됐다. 블랙과 숄스가 이 방정식의 해법을 제공하기까지는 몇 년이 더 걸렸다. 이들과는 따로 연구 중이던 머턴은 더 깊이 파고들어 갔다. 그는 주식과 현금을 혼합함으로써 주식 옵션을 합성하는 방법이 있음을 증명했는데, 이 혼합물은 주식을 현금으로 또는 그 역으로 교환하는 방법으로 구성비를 지속적으로 재조정해 주어야 했다. 투자자가 처음에 하나의 혼합물을 매입한 후 거기에 이 재조정 비법을 적용시키면 주식 옵션과 똑같은 결과를 얻게 될 것이며, 따라서 이 옵션의 가치는 최초의 혼합물을 매입하는 비용과 정확히 일치해야 한다. 옵션을 합성하는 비법은 동적 복제라 불렀다. '복제' 인 것은 옵션을 재 생산하기 때문이고, '동적' 인 것은 복제하기 위해 혼합물을 계속해서 바꿔 주어야 하기 때문이다. 옵션을 동적으로 복제할 수 있다는 사실은 거의 당혹스러운 결론이었다. 블랙, 숄스, 머턴이 나타나기 전에는 단순한 증권을 가지고 옵션을 만들어 낼 수 있으리라고는 아무도 상상하지 못했다. 이제 옵션은 단순한 증권, 주식, 현금을 잘 혼합한 것으로 간주된다. 지속적으로 바뀌기는 하지만 비례는 알려져 있다.

### 변동성 스마일
>옵션은 대개 주식보다는 유동성이 떨어지며, 따라서 내재 변동성이라는 시장 자료는 조야한 어림에 지나지 않는다. 그럼에도 불구하고 데이브는 내가 이미 어렴풋이 인식하고 있던 부분을 지적했다. 즉 내재 변동성에 심한 뒤틀림이 있어서, 행사 가격이 낮은 3개월 옵션이 행사 가격이 높 은 3개월 옵션보다 훨씬 더 내재 변동성이 높다는 사실이었다. <그림 14.1>에 이와 같은 비대칭을 대략적으로 나타냈다. 한쪽으로 기울어진 형태를 대개는 미소, 즉 "스마일"이라 불렀지만 실상은 능글맞은 웃음에 더 가까웠다.
<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/vol-smile-nikkei.webp" alt="1980년대 니케이지수의 변동성 스마일 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 1980년대 니케이지수의 변동성 스마일 (출처: 퀀트:물리과 금융에 대한 회고, 이매뉴얼 더만, 승산) </span>
</p>
>뒤틀리는 현상은 3개월 내재 변동성에서만 나타나는 게 아니었다. 이와 비슷한 효과는 어떠한 만기에서도 나타났으며, 따라서 내재 변동성은 행사가격뿐 아니라 만기에 따라서도 달라졌다. 우리는 시간축과 행사 가격 모두에 따른 내재 변동성의 이와 같은 변화를 2차원의 내재 변동성 곡면 으로 그려내기 시작했다. 스탠더드앤푸어 500 지수에 대한 옵션 곡면 그림을 〈그림 14.2>에 나타냈다. 수익률 곡선과 마찬가지로 이 곡면은 매일 시시각각 변화한다
<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/vol-smile-snp500.webp" alt="S&P500의 변동성 스마일 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 S&P500의 변동성 스마일 (출처: 퀀트:물리과 금융에 대한 회고) </span>
</p>

>우리는 블랙-숄스 모델이 주가 변화를 지나치게 단순화하고 있다는 사실을 알고 있었다. 주가가 현재 가치로부터 미래로 갈수록 임의적이고도 연속적 형태로 조금씩 더 확산한다고 간주했다. 불붙은 담배 끝에서 연기 가 구름처럼 방 안으로 퍼지는 모습을 연상하면 될 것이다. 담배 끝에서 가까운 곳에서는 진하고 멀어질수록 엷어진다. 한 지점의 구름 농도는 구름 입자가 그 위치로 확산될 가능성을 나타낸다. 이와 비슷하게, 블랙-숄 스 모델에서는 구름이 주가가 미래 어느 시점에 특정 위치에 다다를 확률 을 나타낸다. 〈그림 14.4〉는 블랙-숄스 모델에서 하나의 주식이 띠는 확률 구름을 보여 주고 있다. 구름이 퍼질수록 미래의 주가는 불확실해진다. 주식의 변동성은 전통적으로 그리스 문자 시그마로 나타내는데, 이 변수 하나가 확산 비율과 구름의 폭을 결정한다. 주식의 변동성이 클수록 구름폭이 넓다.

<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/stock-price-diffusion-model.webp" alt="주가의 확산 현상을 나타내는 그림 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 6 시간에 따른 주가의 확산 (출처: 퀀트:물리과 금융에 대한 회고); 주가가 시간에 따라 랜덤하게 퍼져나가는 것을 보여준다. </span>
</p>

<p align="center">   
    <img src="/images/2024-10-24-quant-and-physics-book/stock-price-diffusion-after-big-drop.webp" alt="1980년대 강남아파트 가격 ">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 7 폭락 후 주가의 확산 (출처: 퀀트-물리과 금융에 대한 회고); 주가가 큰 폭락 후 다시 시간에 따라 랜덤하게 퍼져나가는 것을 보여준다. </span>
</p>

### 자리를 옮기는 방법
> 그런데 어떻게 옮길 것인가? 1988년에 내가 잘로몬브라더즈에 들어가기 위해 골드만을 그만두던 날, 스코트 핑커스는 회사 내의 다른 자리로 옮겨 가면 어떻겠느냐고 제안했다. 왜 좀 더 일찍 그런 얘기를 꺼내지 않았는지 물었더니, 그랬으면 남의 부서에서 사람을 빼내 가는 꼴이 되지 않았겠느냐고 설명했다. 다른 부서에서 사람을 뽑아가는 일은 나쁜 행위 였다. 

> 그 역도 마찬가지였다. 다른 영역으로 자리를 옮기고 싶은 사람은 그런 의사를 드러내 놓고 타진해서는 안 되었다. 그것은 회사 일보다도 자신의 일을 우선시하는 행위로, 좋지 못한 성격으로 간주되는 것이다. 이런 행 위를 용납하면 너도나도 그렇게 했을 것이다. 회사 내의 문화에 맞는 적절한 행동은 자신의 윗사람을 찾아가 다른 가능성을 생각해 봐야 하는 사유를 정중하게 설명한 다음 이렇게 물어보는 것이었다 - 다른 자리를 찾아봐도 괜찮을까요? 

> 그렇지만 이렇게 하면 자신의 패를 다 드러내 보여주는 셈이었다. 당신 밑에서 더 이상 일하고 싶지 않다는 이야기를 꺼내기는 쉽지 않다. 그래서 실제로는 이와는 반대로 정말로 밑에서 일하고 싶은 사람을 먼저 찾아가. 그쪽에 혹시 자신이 일할 만한 자리가 있는지 넌지시 물어보는 쪽이 일반적이었다. 그런 다음 그가 관심을 보이면 몇 차례 더 만나면서 가능성을 논의했다. 그래서 결국 두 사람 모두 자리를 옮기는 쪽으로 일을 진행하자는 결론에 이르면 그때 현재의 윗사람을 찾아가서 이렇게 묻는 것이다 - 다른 자리를 찾아봐도 괜찮을까요?

### 모델은 모델일 뿐
> 모델은 모델일 뿐이며, 이상화된 세계를 묘사하는 장난감 역할을 할 뿐이다. 간단한 모델은 간단한 미래를 그려낸다. 더 복잡한 모델에서는 실제 시장에 좀 더 근접할 수 있는 더 복잡한 일련의 미래 시나리오를 포함한다. 그러나 인간의 복잡한 심리를 잡아낼 수 있는 수학 모델은 없다. 거래사가 형식주의와 수학의 능력을 너무 많이 믿는 것을 이따금 볼 수 있었다. 그런 모습을 지켜보면서, 사이렌처럼 유혹적인 모델의 노래를 너무 오랫동안 듣고 있다 보면 바위에 좌초하거나 소용돌이에 휘말리게 될 수도 있음을 알게 됐다. 

> 나처럼 금융에 새로 발을 들어놓는 물리학자는 통일장 이론을 발견할 수 있다고 상상한다. 그래서는 안 될 금융학자 중에도 그것을 발견할 수 있다고 상상하는 사람이 많이 있는 것같다. 그들은 현실 세계에서 살고 있지 않기 때문이다. 그 발견은 실제로 가능하지 않다. 그리고 그것은 연산 능력 문제가 아니다. 한 없이 빠른 컴퓨터도 소용이 없다. 문제는 그보다 더 깊은 곳에 있다. 

> 물리학 기법은 금융에서 진실에 가장 가까운 근사치를 만들어 내는 수준 이상의 역할을 하지 못하는데, 금융에서 말하는 "진정한" 가치 자체가 의심스러운 개념이기 때문이다. 물리학에서는 행성의 미래 궤도나 겔만 의 오메가 마이너스 같은 새로운 입자의 존재와 성질을 정확히 예측하는 모델은 올바른 모델이다. 금융에서는 그런 관측을 통해 모델이 옳다는 것 을 쉽사리 증명할 수 없다. 자료가 거의 없는 데다가, 또 그보다도 시장은 작용과 반작용, 정-반-합의 변증법이 이루어지는 투기장이기 때문이다. 사람들은 과거의 실수에서 배워 새로운 실수를 저지른다. 한 시절에는 옳았던 것이 다음 시절에는 틀리게 된다. 

> 경제학자는 진짜 일류 모델을 본 적이 없다. 물리학이 더 낫기 때문이 아니라 금융이 더 어렵기 때문이다. 물리학에서는 하느님을 상대로 경합을 벌이는데, 하느님은 자신이 세운 법칙을 그리 자주 바꾸지 않는다. 그래서 하느님을 외통수로 몰아붙이면 그분은 패배를 시인한다. 금융에서는 하느님의 피조물을 상대로 경합을 벌이는데, 그들은 자산을 자신의 덧없는 의견을 기반으로 평가한다. 이들은 패배해도 패한 줄 모르고, 그래서 시도를 계속한다. 

> 그럼에도 불구하고, 금융의 가치를 결정하는 것은 이처럼 예측할 수 없는-여러분과 나 같은- '나'이다. 피셔 블랙은 금융 이론에 대해 다음과 같이 쓴 적이 있다. 
* > "결국 하나의 이론이 받아들여지는 것은 경험이라는 관습적 시험을 통해 입 증되기 때문이 아니라, 그 이론이 옳고 적합하다고 서로 설득하기 때문이다."

> 내 생각에 금융에서 수학 모델을 쓰는 올바른 방법은 이런 것 같다. 모델은 모델일 뿐, 그 자체가 실물은 아니다. 따라서 우리는 모델이 진정으로 올바르기를 기대할 수 없다. 모델은 우리가 탐색할 수 있는 평행한 생각우주의 집합체로 생각하는 것이 좋다. 각 우주는 모순이 없어야 하지만, 현실의 금융 및 인간 세계는 물질 세계와는 달리 우리가 만드는 그 어떠한 모델보다도 무한히 더 복잡하다. 우리는 현실 세계를 하나의 모델 안에 끼워 넣어, 그 모델이 얼마나 쓸모있는 어림인지 늘 보고자 하는 것 이다.

# 느낀점
## 학계의 삶
대학원생의 고생은 미국이든 한국이든 다르지 않다는 걸 깨달았다. 학위를 마친 후 박사후 연구원 생활에 대한 저자의 이야기는, 과거를 떠올리게 하며 크게 공감되었다. 저자는 미래에 대한 불안과 잠깐의 자유 사이에서 느끼는 감정을 정확히 표현해냈다.

누군가 박사 유학을 고민하고 있다면, 나는 미국보다는 유럽을 추천하고 싶다. 유럽에서는 연구과제가 있어야 학생을 받는 경우가 많고, 박사과정생에게도 비교적 괜찮은 급여를 제공한다. 보통 3년 정도 진행되는 연구과제가 마무리될 때 학위도 함께 끝난다.

## 매매를 할 것인가 금융상품을 팔 것인가
퀀트에도 다양한 분야가 있다는 것을 이 책을 통해 처음 알았다. 저자처럼 금융상품의 모델을 개발할 수도 있고, 통계적 차익거래를 통해 매매 이익을 추구할 수도 있다. 이 두 방식은 수익을 얻는 방식에서 큰 차이가 있다. 전자는 옵션 같은 금융상품을 판매해 수수료를 얻는 것이고, 후자는 매매 차익을 기반으로 한다.

개인 투자자(혹은 투기자)가 할 수 있는 것은 시장에 나와 있는 상품을 사고파는 것뿐이다. 그래서 일반인들은 퀀트를 주로 특수한 주식 매매 전략으로 이해하는 경우가 많다. 하지만 이러한 방식은 '알고리즘 트레이딩'이라는 더 정확한 용어로 불린다.

## 퀀트 모델을 알면 좋은 점
예를 들어, 블랙-숄즈 방정식을 활용하면 옵션의 시장 가격과 현재 주가를 바탕으로 변동성을 역산할 수 있는데, 이를 '내재 변동성'이라고 한다.

일반적으로 변동성은 과거 주가 데이터를 기반으로 계산할 수밖에 없지만, 과거 데이터를 미래 예측에 적용하는 데는 한계가 있다. 반면, 옵션 가격을 통해 역산한 내재 변동성은 시장 참여자들이 예측하는 미래 변동성을 반영한다. 항상 정확하다고 할 수는 없지만, 과거 데이터의 한계를 어느 정도 보완해줄 수 있다고 본다.

변동성을 구하면 이를 바탕으로 통계 모델을 통해 주가 예측 모델을 만들 수 있다. 주로 정규분포, 라플라스 분포, 혹은 t-분포 같은 분포들이 사용된다.
