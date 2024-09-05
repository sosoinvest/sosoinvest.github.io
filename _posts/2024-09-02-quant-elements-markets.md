---
layout: single
title:  "퀀트의 필수 요소 (2/7): 금융시장"
description: 퀀트 투자에 필요한 요소인 금융시장에 대하여 정리하였다.
categories: 투자
tag: [주식,책,퀀트]
toc: true
author_profile: false
header:
 teaser: /images/2024-09-01-quant-elements-markets/quant-elements-markets-thumbnail.webp
 og_image: /images/2024-09-01-quant-elements-markets/quant-elements-markets-thumbnail.webp

# sidebar:
#     nav: "docs"
# search: true
---
금융시장이라는 도메인 지식이 있어야 퀀트 투자의 타겟을 결정할 수 있다.

여기서 도메인 지식은 시장, 플레이어, 그리고 자산군으로 구분된다.

{: .notice--primary}
<span style="font-size: 1.25em;">이 글은 [퀀트의 정석] 책에 나오는 금융시장 부분을 정리한 것이다.</span>

[퀀트의 정석](/투자/quant-way-book/)

# 시장의 구분
## 장내시장과 장외시장: 거래소의 유무에 따라서
장내시장은 중앙에 매수자와 매도자가 동시에 호가를 제출할 수 있는 거래소가 존재한다. 주로, 주식, 선물, 옵션같이 거래소에 상장된 상품이 거래되는 시장이다. 이 시장은 규격화가 잘되어 있어서 거래가 활발하고 따라서 유동성이 풍부하다.

반대로 장외시장은 거래소가 존재하지 않고 거래 상대방들끼리 직접만나서 일대일 거래를 성사해야하는 시장이다. 직접적인예로 부동산이 있으며 비상장 주식 또한 장외시장에서 거래된다. 장외시장은 다른 이름으로 OTC(Over-The-Counter)시장이라고 불린다. 이 시장에서는 매수 또는 매도를 원한다면 그것을 받아줄 상대를 직접 찾아야한다. 일반적으로 거래 상대를 찾아주는 브로커가 매수자와 매도자를 연결해줘서 거래를 성사시킨다. 장외시장은 거래소가 없기 때문에 규격화가 되어 있지않다.

## 발행시장과 유통시장: 상품의 발행 유무에 따라서
발행시장은 기존에 존재하지 않던 새롭게 발행되는 상품이 판매되는 시장이다. IPO(Initial Public Offering) 즉, 주식공모 이벤트가 발생하는 시장이다.

유통시장은 이미 발행된 증권들이 중고로 나와서 거래되는 시장이다. 주식시장은 대표적인 유통시장이다. 이 시장에서는 뉴스와 유동성에 따라서 실시간으로 상품의 가격이 메겨진다.

## 자금시장과 자본시장: 돈을 빌려주는 기간에 따라서
자금시장은 단기적으로 돈을 빌리거나 빌려주기 위해 존재하는 시장이다. 일반적으로 1년 이내의 짧은 기간동안 자금을 빌리거나 빌려주기 때문에 유동성이 매우 풍부하다. 돈을 빌려주는 기간이 단기이기 떄문에 자금시장에서 거래되는 상품은 리스크는 낮고 변동서이 작다. 자금시장에서는 예금, 양도성예금증서(CD), 기업어음(CP), MMF(Money Market Fund), 환매조건부 채권(Repo) 등이 거래된다.

자본시장은 장기 자금 조달을 위해 존재하는 시장이다. 일반적으로 기업이 사업의 목적으로 안정적으로 자금을 조달하기 위한 시장으로 주식과 채권이 거래된다.

# 플레이어의 구분
## 바이사이드(Buy side)
바이사이드는 시장에서 수익을 얻기위해 실제로 자금을 투입하여 투자 행위를 하는 주체다. 즉, 바이사이드라는 용어는 금융상품과 서비스를 구매하는 입장이라는 뜻이다. 여기에는 대표적으로 뮤추얼 펀드, 연기금, 보험사, 국부펀드, 그리고 헤지펀드가 있다.

## 셀사이드(Sell side)
셀사이드는 투자자가 투자행위를 순조롭게 할 수 있도록 도와주는 역할을 하는 주체이다. 즉, 셀사이드라는 용어는 자신들의 고객인 바이사이드에게 금융상품과 서비스를 판매한다는 의미이다. 여기서는 좋은 투자상품을 조달하여 고객에게 제공하는 과정에서 발생하는 여러가지 실무적 이슐르 효율적으로 처리해주는 역할을 한다. 대표적으로 브로커리지, 딜러(시장조성자), ELS(Equity-Linked Securities, 주가연계증권) 같은 상품을 만드는 구조화상품부서, 자금조달 과정을 처리해준느 투자은행(IB)등이 있다.

# 자산군 구분
## 채권
채권은 금리에 기반한 금융상품이다. 시장의 금리가 올라가면 채권의 가격이 떨어지고 반대로 금리가 내려가면 채권의 가격이 올라간다.

채권은 주식과 다르게 만기라는 것이 항상 존재한다. 만기는 하루부터, 1년, 3년, 5년, 10년, 30년, 50년 심지어 영구채까지 다양하게 존재한다. 만기에 따라 감수해야하는 위험이 다르기 때문에, 동일한 주체가 발행했다 하더라도 만기에 따라 채권의 금리 수준은 달라진다.

또한, 채권은 발행주체에 따라 특성이 다르다. 국채는 중앙정부가 발행한 것이며, 회사채는 일반 기업이 발행한 것이다. 같은 회사채라도 은행체, 카드채, 공사채 등 다양한 상품이 있다.

서로 다른 채권이 다른 금리를 갖고 있는 이유는 각 채권이 내포하고 있는 위험 수준이 다르기 때문이다. 특히 회사채의 경우 파산의 위험 때문에 지급불가능의 위험을 반영하여 금리수준이 결정된다. 때문에 신용평가사에서는 신용등급을 메겨서 회사채의 지급불가능 위험을 추정한다. 글로벌 채권시장에서는 회사채의 신용등급에 따라 투자등급(Investment Grade, IG)과 투기등급(High Yield, HY)으로 구분한다.

## 주식
주식은 회사에 자금을 투자한 대가로 기업의 부분적 소유를 얻는 금융상품이다. 주식을 소유했다면 기업활동으로 나온 이익에 대한 분배를 요구할 수 있는 권리와 의결권을 얻을 수 있다. 주가를 결정하는 것은 기업의 수익성, 즉, '미래에 어느정도 돈을 벌 수 있는가' 이다. 주주들은 회사가 많은 이익을 내서 높은 배당금을 받거나 시장에서 좋은 평가를 받아 보유지분의 가치가 높아지기를 기대한다.

주식은 의결권의 유무에 따라 보통주와 우선주로 구분된다. 우선주는 의결권이 없는 대신에 배당을 조금 더 준다. 

일반적으로 주식은 아래의 표와 같이 11개의 섹터로 구분된다.

*표 1: 섹터별 대표기업 리스트*

| 섹터 | 대표기업 |
|:---:|:---:|
| 기술 (Technology) | AAPL, MSFT, NVDA |
| 커뮤니케이션 서비스 (Communication Service) | ALPHABET, META, NFLX |
| 임의 소비재 (Consumer Cyclical) | AMZN, TSLA, HD |
| 부동산 (Real Estate) | AMT, O |
| 에너지 (Energy) |  XOM, CVX |
| 금융 (Financial) | V, MA, BOA |
| 헬스케어 (Health Care) | JNJ, PFE, UNH |
| 필수 소비재 (Consumer Defensive) | KO, PSX |
| 산업재 (Industrials) | UPS, UNP, HON |
| 유틸리티 (Utilities) | DUK, ED, SO |
| 소재 (Basic Materials) | DD, SHW |

## 통화
통화는 사전적으로 각국의 법정화폐를 의미한다. 각 나라는 저마다의 통화 시스템을 가지고 있으며 이러한 통화들은 서로 일정 비율로 교환이 가능하다. 여기서 통화들 간의 교환비율을 '환율'이라고 부른다. 환율의 결정은 각국의 경제적, 정치적 상황에 영향을 받는다. 환율에 영향을 주는 거시지표로는 경제성장률, 국제수지, 금리, 물가 등이 있다.

통화의 교환이 일어나는 외환시장의 특징은 언제나 하나의 통화를 매수하고 다른 하나의 통화를 매도해야 한다는 것이다. 

전 세계에서 가장 거래가 많이되는 주요 통화는 선진국 통화로 불리는 G10 통화와 개발도상국 통화인 이머징 통화로 구분된다. 아래의 표는 이러한 구분에 따른 대표적인 20개의 통화를 보여준다. 여기서 괄호 안의 알파벳은 외환시장에서 표현하는 가국 통화의 기호를 의미한다. 

*표 2: 각국의 통화 리스트*

| G10 통화 | 이머징 통화 |
|:---:|:---:|
| 미국 달러(USB) | 한국 원(KRW) |
| 유로화(EUR) | 싱가포르 달러(SGD) |
| 일본 엔(JPY) | 대만 달러(TWD) |
| 영국 파운드(GBP) | 중국 위안(CHY) |
| 스위스 프랑(CHF) | 브라질 헤알(BRL) |
| 캐나다 달러(CAD) | 러시아 루블(RUB) |
| 호주 달러(AUD) | 인도 루피(INR) |
| 뉴질랜드 달러(NZD) | 남아공 랜드(ZAR) |
| 노르웨이 크로나(NOK) | 멕시코 페소(MXN) |
| 스웨덴 크로나(SEK) | 태국 바트(THB) |

## 원자재
원자재는 원유, 천연가스, 금, 구리와 같이 어떤 상품을 만들기 위해 필요한 천연자원 또는, 우리의 의식주 생활에 필수적인 상품들을 의미한다. 원자재 가격의 움직임은 1차적으로 물가와 경제성장에 영향을 주고 이는 금리를 변화시키며, 종국에는 모든 자산의 가격에 영향을 미칠 수 있다. 

원자재의 거래가 활발히 이루어지는 대표적인 장소는 바로 미국와 유럽의 선물거래소이다. 이러한 선물거래소에는 CME(Chicago Mercantile Exchange), ICE(Intercontinental Exchange), LML(The London Metal Exchange) 등이 있다. 

원자재 자체의 특성상 옮기는 것이 쉽지 않기 떄문에 대부분의 원자재 상품들은 현물이 아닌 선물의 형태로 거래가 이루어진다. 즉, 실제 원자재를 주고 받기 훨씬 전부터 언제 얼마에 거래를 할지 미리 계약해 놓는 것이다. 투자자들은 언제든이 선물 거래를 통해 원자재를 매매할 수 있다. 다만, 선물의 만기가 도래하면 실제 현물에 대한 인수도가 발생한다. 만약 현물을 인수하고 싶지 않다면 만기가 도래하기 전에 자신의 현재 선물 계약을 청산하고 다음 월물을 매수하면 된다. 이러한 갈아타기를 '롤오버'라고 부른다. 

원자재는 일반적으로 에너지, 금속, 곡물, 소프트, 그리고 가축의 5가지 범주로 분류가 가능하다. 아래의 표는 각 범주의 대표적인 원자재 상품들을 보여준다.

*표 3: 섹터별 원자재 상품 리스트*

| 섹터 | 상품 |
|:---:|:---:|
| 에너지(Energy) | WTI, 브렌트유, 난방유, 천연가스, 가솔린 |
| 금속(Metals) | 금, 은, 구리, 알루미늄, 니켈, 아연 |
| 곡물(Grains) | 옥수수, 밀, 대두, 대두박, 대두유 |
| 소프트(Softs) | 설탕, 면화, 코코아, 커피 |
| 가축(Livestocks) | 돈육, 생우, 비육우 |

원자재 시장을 이해하기 위해서는 수요와 공급 메카니즘에 대한 이해가 필수적이며 이 또한 글로벌 경제의 영향을 받는다. 원자재는 다른 자산군과 다르게 단기간에 탄력적으로 공급을 늘릴 수 없기 때문에 공급충격에 의한 가격의 방향성이 한 방향으로 꽤 오랜시간 동안 지속될 수도 있다.

옥수수, 밀, 대두같은 곡물은 기후 변화에 민감하다. 특히 농산물이 생산되는 지역에 급작스러운 가뭄이나 홍수 같은 자연재해가 발생하면 즉각적으로 원자재 가격에 반영된다. 때문에 원자재는 계절성에 영향을 많이 받는 자산이다.