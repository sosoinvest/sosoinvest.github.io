---
layout: single
title:  "래리 윌리엄스의 변동성 돌파전략 (파이썬 코드 있음)"
description: 트레이더 래리 윌리엄스(Larry Williams)의 변동성 돌파전략을 설명하고 과거의 데이터에 기반하여 분석한 글
categories: 투자
tag: [주식,퀀트,백테스트]
toc: true
author_profile: false
header:
 teaser: /images/2024-10-10-volatility-break-out-strategy/vol-brk-out.webp
 og_image: /images/2024-10-10-volatility-break-out-strategy/vol-brk-out.webp

# sidebar:
#     nav: "docs"
# search: true
---
10000%의 수익률로 선물 투자대회에서 우승한 래리 윌리엄스의 변동성 돌파전략에 대해 알아보자.

# 래리 윌리엄스
## 생애
[래리 윌리엄스(Larry Williams, 1942.10.06~)](https://en.wikipedia.org/wiki/Larry_R._Williams)는 성공한 트레이더이자 투자 전문가로 1942년 미국 몬태나주에서 태어났다. 1964년 오리건 대학교 언론학과를 졸업했는데, 대학생이던 1962년부터 주식과 선물 시장에 관심을 갖기 시작했다고 한다. 사실 그의 아버지도 증권 브로커였고 1960년대 후반에는 아버지의 중계회사에서 애널리스트로서 경력을 쌓는 등 투자를 하기 좋은 환경에서 자랐다.

<p align="center">   
    <img src="/images/2024-10-10-volatility-break-out-strategy/larry-williams.webp" alt="래리 윌리엄스 사진">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 래리 윌리엄스(출처: Wikipedia) </span>
</p>

래리 윌리엄스는 11권의 책을 쓰고, Williams %R지표를 개발하고, [트레이더를 양성하는](https://www.ireallytrade.com/)등 폭넓은 투자활동을 해오고있다. 그중에서도 그를 가장 유명하게 만들어준 것은 1987년 선물투자 대회에서 우승시켜준 변동성 돌파전략이다.

## 투자대회 우승
1987년 미국의 Robbins Financial Group LTD은  World Cup Champions of Futures Trading이라는 선물 투자대회를 열었다. 래리 윌리엄스는 이 대회에서 11,376%의 수익률로 우승했다.

대회는 전 세계의 트레이더들이 참가할 수 있으며, 10,000달러의 초기 자금으로 1년간 올린 총 수익률로 우승자를 결정한다. 참고로 이 대회는 1983년 처음 열려서 현재까지 지속되고있다.

래리 윌리엄스는 1987년 10,000달러를 1,100,000로 불려서 우승할 수 있었다. 대회에서 그가 거래한 대상은 S&P500 선물, 채권 선물, 금 선물, 커피 선물 등이었다. 투자 전략은 기본적으로 변동성 돌파에 기반하고, 시장간 관계와 계절성등의 다양한 요소를 고려한 것으로 알려졌다. 

그의 딸 미셸 윌리엄스(Michelle Williams) 또한 아버지에게 배운 변동성 돌파전략으로 1997년 같은 대회에서 900%의 수익률로 우승했다. 이 결과는 래리 윌리엄스의 변동성 돌파전략이 본인만 할 수 있는게 아니라, 다른 사람에게도 전수될 수 있다는 것을 보여준다.

# 변동성 돌파전략
변동성 돌파전략의 원리는 단순하다. 다음의 3단계로 구성된다.

<div class="notice--primary">
<ul>
    <li style="font-size: 1.25em;">전일 고가에서 저가를 빼서 변동폭을 구한다.</li>
    <li style="font-size: 1.25em;">시가+K*변동폭으로 타겟 매수가를 정하고, 오늘 장중 가격이 이 가격을 초과하면 매수한다.</li>
    <li style="font-size: 1.25em;">다음날 시가에 모두 매도한다.</li>
</ul>
</div>

변동폭과 타겟 매수가의 개념을 그림으로 표현하면 아래와 같다.

<p align="center">   
    <img src="/images/2024-10-10-volatility-break-out-strategy/vol-brk-out-concept.webp" alt="변동성 돌파전략 개념">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 변동성 돌파전략 개념(출처: 파이썬 증권데이터 분석, (출판사: 한빛미디어, 저자: 김황후)); 이 그림에서는 당일 종가에 매도한다. 또 어떤 자료에서는 다음날 시가에 매도하는 것으로 나온다. 직접해본 백테스트 결과는 다음날 시가에 매도하는 것이 더 성과가 좋았다.  </span>
</p>

여기서 K는 매개변수로 보통 0.5의 값을 설정한다. K 값이 작으면 거래가 너무 빈번하게 일어나며, 크면 거의 거래가 일어나지 않는다. 즉, K값은 매수신호를 만드는 문턱값을 조절하는 역할을 한다. 

참고자료의 출처마다 다른데, 매도는 다음날 시가 또는 매수 당일 종가에 한다. 이렇게 짧게 매매하는 이유는 갑작스러운 뉴스 등의 이벤트의 영향을 제거하기 위해서다.

래리 윌리엄스의 변동성 돌파전략은 가격이 오르는 추세에서 매수한다는 점에서 모멘텀 전략과 유사하다. 다만 일반적인 모멘텀 전략이 시간 간격을 연간 또는 분기간으로 상대적으로 길게 보는 반면에 변동성 돌파는 일간으로 짧게 가져간다는 점에서 차이가 있다. 게다가 매수 신호의 기준을 결정하는 파라미터가 있고, 종가에 매도함으로써 수익(만약 있다면)을 확정한 후 이후에 발생하는 변동성을 회피할 수 있다는 점에서 모멘텀 전략과 차이가 있다. 

한가지 변동성 돌파전략에 긍정적인 것은 국내 주식시장에서는 모멘텀 전략이 기존에 잘 먹혀왔다는 것이다. 심지어 [최근 3년간은 S&P 500 지수 보다 국장 모멘텀 ETF가 더 성과가 좋았다](/투자/quant-way-book). 따라서 모멘텀 전략과 유사한 변동성 돌파 전략이 국장에서도 잘 먹힐 것으로 기대하는 것은 그럴듯하게 보인다. 정말 그런지는 백테스트를 해봐야하지만 말이다.

아래는 전략의 장점과 단점을 정리한 것이다. 

## 장점
- 변동성 확장 시기를 포착하여 큰 움직임을 잡을 수 있다.
- 명확한 진입/퇴출 규칙으로 감정적 거래를 방지한다.

## 단점
- 1일 단타 전략으로 거래비용이 크다.
- 횡보장이나 큰 일중 변동성 시장에서는 휩소(whipsaw, 가격이 한 방향으로 급격히 움직인 후 갑자기 반대 방향으로 전환되는 현상)에 휘말릴 수 있다.
- 지속적인 상승장이 아닐 경우 수익을 내기 어려울 수 있다.


# 백테스트
래리 윌리엄스의 변동성 돌파전략을 파이썬 코드로 구현해서 백테스트 해보았다.

## 코드의 구조
코드의 구조를 순서도로 그리면 아래와 같다. 일반적으로 장중 기록되는 모든 가격을 기록하지 않기 때문에, 종가가 타겟 매수(=오늘 시가 + K*(전일 변동폭))가 보다 높은 경우에만 그 타겟 매수가로 매수하는 것으로 가정했다. 즉, 장시작 후 타겟 매수가에 매수를 걸어놓았다고 가정하고, 종가가 그 매수가보다 높을 때만 걸어놓은 매수 주문이 체결된 것으로 가정한 것이다. 실제로는 정확히 이 가격에 전량 매수할 수 없기 때문에 계산을 위한 어느정도 이상적인 가정이라고 할 수 있다.

<p align="center">   
    <img src="/images/2024-10-10-volatility-break-out-strategy/flowchart.webp" alt="변동성 돌파전략 코드의 순서도">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 코드의 순서도 </span>
</p>

## 백테스트 조건
백테스트 대상은 Tiger 코스닥150 레버리지 ETF다. 이것을 대상으로 잡은 것은 장기 하락 또는 상승하지 않고 큰 변동성을 보여서 변동성 돌파 전략이 잘 먹힐 것이라 생각했기 때문이다. 또한, 이전에 [다른 블로그](https://mproject2017.tistory.com/entry/%EB%B3%80%EB%8F%99%EC%84%B1-%EB%8F%8C%ED%8C%8C-%EC%A0%84%EB%9E%B5-%EB%8B%A8%EC%A0%90-%EC%A0%A0%ED%8F%AC%ED%8A%B8-%EB%B0%B1%ED%85%8C%EC%8A%A4%ED%8A%B8?t&utm_source=perplexity)에서 젠포트를 이용해서 백테스트 대상으로 다루었기 때문에 두 결과를 비교해 보는 것도 재밌을 거라고 생각했다.

- 백테스트 기간: 2015.12.17 ~ 2024.10.04 (ETF 상장 후 현재까지)

- 세금: 매매 차익에 대해 15.4% 
: *국내주식 ETF는 거래세가 없다. 그러나 레버리지 ETF는 기타 ETF로 분류돼서 매매차익에대해 배당소득세 15.4%가 붙는다. 왜 양도세가 아니라 배당소득세인지는 모르지만, 아무튼 그렇다. 참고로 배당소득세는 원천징수돼서 매도하자마자 납부하게 된다. 즉, 증권사에서 매도 이익에 대해 알아서 세금을 차감해서 돌려준다.

- 거래 수수료: 0.015%
: *거래 수수료는 증권사마다 다르다. 현재 최저 수수료는 토스증권의 0.015%로 백테스트에서도 이 값을 사용했다.

- 벤치마크: S&P 500
: *참고로 [S&P 500의 역사적인 연평균 수익률은 9.25%](/투자/snp-historical-return-since-1871/)이다.

## 백테스트 결과

### 세금의 영향
아래의 그림은 변동성 돌파전략을 코스닥 레버리지 2배 ETF에 적용한 결과를 보여준다. 세금 유무에 따른 결과와 비교군으로 Buy and hold 전략과 S&P 500 지수를 고려하였다. 

세금이 없는 경우 변동성 돌파전략은 9년간 756%의 수익률을 보였고, 세금을 고려하면 이 값은 192%로 낮아진다. 세금을 고려한 전략의 결과는 S&P500 지수의 결과와 비슷했다. 연평균 수익률(CAGR)은 각각 26.9%, 12.6%이며 벤치마크인 S&P500은 12.2%이다. Buy and hold가 9년간 -0.3%로 역성장한 것과 비교하면 변동성 돌파전략이 굉장히 잘 작동한것으로 보인다. 아래의 표 1은 이 결과들을 정리한 것이다.

<p align="center">   
    <img src="/images/2024-10-10-volatility-break-out-strategy/vol-brk-out.webp" alt="변동성 돌파전략 백테스트 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 변동성 돌파전략 백테스트 </span>
</p>

*표 1: 변동성 돌파전략 백테스트 결과*

| 전략 | 변동성 돌파(세금 X) | 변동성 돌파(세금O) | Buy and hold | S&P500 |
|:---:|:---:|:---:|:---:|:---:|
| 최종 수익률 | 756.2% | 192.2% | -0.3% | 181.6% |
| CAGR | 26.9% | 12.6% | -0.05% | 12.2% |
| MDD | -31.8% | -36.3% | -85.7% | -33.9% |
| 매매횟수  | 628 | 628 |  0 | 0 |
| 승률  | 58.0% | 58.0% | - | - |
| 수익 시 평균 수익률 | 2.0% | 1.7% |  - | - |
| 손해 시 평균 손실률  | -1.8% | -1.8% | - | - |

위의 표에서 정리했듯이, 세금 유무에 따라서 최종 수익률이 약 4배까지 결과 차이가 난다. 세금은 매매 이익에 대해 15.4% 밖에 안되는데 이렇게 큰 차이가 나는 이유는 복리의 마법에 있다. 매매로 수익을 실현해나가면, 차익에 대해 양도세를 내는 경우 다음번 매수에서 더 적은 물량을 사게 돼서 복리효과가 줄어들기 때문이다. 수익 시 평균 수익률을 보면 그 차이를 알 수 있다. 세금이 없는 경우 이익 거래에서 발생한 평균 수익률은 2.0%인 반면에, 세금이 있는 경우에는 이보다 작은 1.7%다. 0.3%의 차이가 복리로 굴러가니 최종적으로 4배의 수익률 차이를 만드는 것이다.

심지어 국내상장 ETF들은 세금이 원천징수되니 더욱 불리하다. 반면에 해외상장 ETF들은 양도세가 부과되는데 원천징수되지 않고 1년에 한번 5월에 자진신고하면 된다. 세금을 납부하기 전의 기간동안 복리효과를 누릴 수 있는 것이다. 게다가 양도차익 250만원까지 공제되는데, 대신 양도세율은 22%로 더 높다.

이러한 이익 실현에서 발생하는 세금을 아껴서 변동성 돌파 전략의 효과를 극대화할 수 있는 방법이 있는데 그것은 아래에서 다뤄보고자 한다.

### K값의 영향
아래의 그림은 0.5가 아닌 다른 K값을 사용할 때 투자 결과를 보여준다. 0.1부터 0.9까지 0.2 간격으로 5개의 케이스를 고려하였다. 여기서 세금은 고려하지 않았다.

K값이 너무 작으면 너무 자주 매매하게 되고, 반대로 크면 너무 보수적으로 매매하게 된다. 백테스트 결과를 보면, 작은 경우와 큰 경우 모두 중간값(=0.5)보다 안좋은 결과를 보였다. 특히 K가 가장 작은 0.1의 결과는 최종 수익률 48.7%로 가장 안좋았다. 너무 자주 매매하다 보니 승률이 떨어지고 평균적으로 더 많이 잃기 때문이다.  

아래의 표2는 K 값에 따른 변동성 돌파전략의 백테스트 결과를 정리했다. 가장 성과가 좋은 것은 K=0.5로 756.2%의 수익률과 -31.8%의 MDD를 보였다. 이보다 K가 높으면, MDD가 낮아지고 승률이 높아지지만, 최종 수익률은 낮아진다. K가 0.5보다 낮으면 최종 수익률과 MDD, 승률 모두 안좋아졌다.

여기서 보여주는 결과는 K가 0.5인 것이 최적으로 보이지만, 다른 주식, ETF 또는 채권, 상품과 같은 투자대상에서는 다른 결과가 나올 수 있다. 또한 투자 시점과 기간에 따라서도 다른 결과가 나올 수 있음을 감안해야한다.

<p align="center">   
    <img src="/images/2024-10-10-volatility-break-out-strategy/vol-brk-out-K_study.webp" alt="변동성 돌파전략 K값에 따른 백테스트 결과 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 변동성 돌파전략 K값에 따른 백테스트 결과 차이 </span>
</p>

*표 2: K값에 따른 변동성 돌파전략 백테스트 결과*

| 전략 | K=0.1 | K=0.3 | K=0.5 | K=0.7 | K=0.9 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 최종 수익률 | 48.7% | 399.4% | 756.2% | 414.3% | 286.9% |
| CAGR | 4.5% | 19.6% | 26.9% | 19.9% | 16.2% |
| MDD | -52.1% | -51.5% | -31.8% | -35.8% | -29.0% |
| 매매횟수  | 983 | 811 | 628 | 469 | 319 |
| 승률  | 53.6% | 55.0% | 58.0%| 58.4% | 61.4% |
| 수익 시 평균 수익률 | 2.2% | 2.2% | 2.0% | 1.9% | 1.7% |
| 손해 시 평균 손실률  | -2.3% | -2.1% | -1.8% | -1.7% | -1.6% |

# 죽음과 세금은 피할 수 없다.
앞에 결과에서 봤듯이 세금의 유무에 따라 전략의 결과가 천지차이다. 이러한 결과의 기저에는 세금으로 인한 복리의 마법이 힘을 못쓰는 이유가 있다.

세금이 없으면 좋겠지만, 벤자민 플랭클린이 말했듯이, 

>"누구도 피할 수 없는 것은 죽음과 세금뿐이다." 

피할 수 없다면 최대한 미루거나 줄여야한다. 이것이 변동성 돌파전략에 있어서 핵심이라고 생각한다.

## 세금을 절약하는 방법
### 1. 세금이 없는 투자대상
첫번째는 매매차익에 대한 세금이 없는 상품을 거래하는 것이다. 국내상장 주식 ETF는 증권 거래세가 없고, 매매차익에 대한 양도세도 없다. 대신 레버리지 없이 지수 1배 추종이라 좀 심심한 느낌이 있긴하다. 변동성이 큰 핫한 섹터 ETF를 고른다면 결과가 나쁘지 않을 수도 있다.

### 2. ISA 절세계좌 이용
두번째 방법은 ISA계좌를 이용하는 것이다. ISA는 개인종합자산관리계좌로 예금, 주식, ETF, 펀드를 종합해서 관리할 수 있으며 결정적으로 세금혜택이 있다. 

일반형과 서민형/농어민형이 있는데, 일반형의 경우 수익금 200만원까지 비과세되고 비과세 초과 수익에 대해 9.9%분리과세 된다. 게다가 세금은 과세 이연이 돼서 만기해지시 그동안 발생한 모든 금융소득을 합산하여 계산된다. 즉, 만기까지 복리의 마법 효과를 누릴 수 있는 것이다. 만기가 끝나면 새로 가입하면 된다

대신에 가입조건이 있다. ISA의 가입조건은 다음과 같고 증권사 모바일 앱을 이용하면 누구나 쉽게 만들 수 있다.
- 가입기간: 3년 의무 (최대 5년)
- 납입한도: 연간 2000만원, 총 납입한도 1억원

# 결론
- 래리 윌리엄스의 변동성 돌파 전략을 코스닥 2배 레버리지 ETF에 대해 테스트했다.
- 9년간(세금제외) 총 수익률은 756% 연간 평균 수익률은 26.9%로 벤치마크 S&P500을 4배 아웃퍼폼했다.
- 코스닥 2배 레버리지의 과거 데이터는 K값이 0.5일때 가장 잘 작동했다.
- 세금을 고려하면 성과가 1/4로 줄어들었는데, 복리효과가 감소했기 때문이다.
- 세금을 줄이려면, 1) 세금이 없는 국내상장 주식형 ETF를 이용하거나, 2) ISA계좌를 이용할 수 있다.

## 부록
### 변동성 돌파전략 파이썬 코드
```python
# BLOCK: Import modules
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
from datetime import datetime, timedelta
pd.set_option('display.max_rows', None)

# BLOCK: Import data from the csv file
df = pd.read_csv("tiger_kosdaq150_x2.csv")
df_bm = pd.read_csv("s&p500.csv")

# BLOCK: Vol. Break-out strategy
# Set initial condition
Account = {
    "Cash": [100],
    "Asset": [0],
    "Total": [100],
    "Open": [df["Open"][0]],
    "Close": [df["Close"][0]],
    "High": [df["High"][0]],
    "Low": [df["Low"][0]],
    "Price to buy": [0],
    "Buy sign": [0],
    "Return": [0],
}

buy_sign = 0
K = 0.5
is_end_of_data = False
day_index = 0

fee_when_buy = 0.015*0.01
fee_when_sell = 0.015*0.01
tax_on_earning = 15.4 * 0.01 * 0

file_name = "vol_brk_out_kosdaq_x2_reseult_k05_without_tax.csv"
while not is_end_of_data:
    # Move to the next day
    day_index += 1
    if day_index > len(df)-1:
        is_end_of_data = True
        break

    # Get the price data
    high_yesterday = df["High"][day_index-1]
    low_yesterday = df["Low"][day_index-1]

    open_today = df["Open"][day_index]
    close_today = df["Close"][day_index]
    high_today = df["High"][day_index]
    low_today = df["Low"][day_index]

    Account["Return"].append(0)

    # Sell if buy yesterday
    if buy_sign:
        buy_sign = 0
        price_sell = open_today
        asset_new = 0

        # Tax on the earning
        if price_sell > price_buy:
            cash_new = (Account["Asset"][-1] * (price_sell - price_buy)
                        * (1 - tax_on_earning)) # Return after tax
            cash_new += Account["Asset"][-1] * price_buy
            return_new = np.round((price_sell-price_buy)*(1 - tax_on_earning)
                                  /price_buy*100, 2)
        else:
            cash_new = (Account["Asset"][-1] * price_sell) * (1 - fee_when_sell)
            return_new = np.round((price_sell-price_buy)
                                  /price_buy * 100, 2)

        Account["Cash"].append(cash_new)
        Account["Asset"].append(asset_new)
        Account["Return"][-1] = return_new

        price_buy = 0
    # Check sign if did not buy yesterday
    else:
        # Check volatility break-out signal
        price_width = high_yesterday - low_yesterday
        price_buy = open_today + K * price_width

        # If the buy signal occurs
        if high_today > price_buy:
            buy_sign = 1

            asset_new = Account["Cash"][-1] * (1 - fee_when_buy) / price_buy
            cash_new = 0

            Account["Asset"].append(asset_new)
            Account["Cash"].append(cash_new)

        # If the buy signal do not occur
        else:
            price_buy = 0
            cash_new = np.round(Account["Cash"][-1], 2)
            asset_new = np.round(Account["Asset"][-1], 2)
            Account["Asset"].append(asset_new)
            Account["Cash"].append(cash_new)

    Account["Total"].append(np.round(Account["Cash"][-1]
                                     +Account["Asset"][-1]*close_today, 2))

    Account["Price to buy"].append(price_buy)
    Account["Open"].append(open_today)
    Account["Close"].append(close_today)
    Account["High"].append(high_today)
    Account["Low"].append(low_today)
    Account["Buy sign"].append(buy_sign)

date = []
for dates in df["Date"]:
    date.append(dates.split(" ")[0])

df_account = pd.DataFrame(Account, index=date)
print(df_account)
df_account.to_csv(file_name, index=True)

```






