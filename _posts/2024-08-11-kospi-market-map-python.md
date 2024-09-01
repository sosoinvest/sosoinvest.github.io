---
layout: single
title:  "파이썬으로 코스피 마켓맵 그리는 4단계 방법"
description: 파이썬으로 주식시황을 표현하는 마켓맵을 그리는 방법을 설명합니다.
categories: 투자
tag: [주식,파이썬]
toc: true
author_profile: false
header:
 teaser: /images/2024-08-11-kospi-market-map-python/marketmap-marketcap.webp
 og_image: /images/2024-08-11-kospi-market-map-python/marketmap-marketcap.webp

# sidebar:
#     nav: "docs"
# search: true
---
주식 시황을 한눈에 분석하는 방법인 마켓맵 그리는 방법에 대해 알아보자.

주식 시황을 한눈에 보는 방법으로 마켓맵을 이용할 떄가 많습니다. 여기서는 파이썬을 이용하여 마켓맵을 코스피 시장을 표현하는 마켓맵을 그리는 방법에 대해 소개합니다.

<p align="center">   
    <img src="/images/2024-08-11-kospi-market-map-python/marketmap-marketcap.webp" alt="코스피 마켓맵">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 코스피 마켓맵 작성 결과</span>
</p>

# 마켓맵(Market map)이란?
주식시장의 마켓맵(Market map)은 특정시점에서 주식 시장의 전반적인 상태를 시각적으로 보여주는 도구입니다. 주로 주식들의 시가총액, 거래량, 주가 변동률 등의 지표를 기준으로 시각적으로 배열하여, 시장 내 주요 종목들의 상대적 크기와 성과를 직관적으로 파악할 수 있습니다. 이를 통해 투자자와 애널리스트는 특정 종목의 시장 내 위치, 섹터 간의 동향, 그리고 전체 시장의 흐름을 빠르고 효율적으로 이해할 수 있습니다. 마켓맵은 특히 시장의 전반적인 상태를 요약하여 보여주고, 시장 변동에 대한 실시간 반응을 확인하는 데 유용합니다.

## 주요 특징

- 색상: 마켓 맵에서는 종종 주식의 가격 변동을 색상으로 나타냅니다. 일반적으로 주가가 상승한 주식은 파란색으로, 하락한 주식은 빨간색으로 표시됩니다. 색상의 농도나 밝기에 따라 상승 또는 하락의 정도를 시각적으로 구분할 수 있습니다.

- 크기: 개별 사각형이나 셀의 크기는 회사의 시장 가치(시가총액)를 반영하는 경우가 많습니다. 즉, 대형 기업일수록 셀의 크기가 더 크며, 이를 통해 어떤 기업이 시장에서 큰 비중을 차지하고 있는지 쉽게 파악할 수 있습니다.

- 섹터 및 산업 분류: 마켓 맵은 종종 시장을 다양한 섹터(예: 기술, 금융, 헬스케어, 에너지 등)로 분류하여 보여줍니다. 이를 통해 특정 섹터가 전체 시장에서 어떤 성과를 보이는지, 또는 특정 섹터 내에서 어떤 주식이 특히 강세나 약세를 보이는지를 쉽게 확인할 수 있습니다.

## 볼 수 있는 곳

국외시장은 Finviz, TradingView, Yahoo finance 같은 곳에서 볼 수 있으며, 국내시장은 [한국경제에서 제공하는 웹페이지](https://markets.hankyung.com/marketmap/kospi)에서 확인할 수 있습니다. 

# 파이썬으로 코스피 시장의 마켓맵 그리는 방법
물론 한국경제 웹사이트에서 코스피 시장의 마켓맵을 제공하지만, 파이썬을 이용해 직접 그릴 수도 있습니다. 파이썬을 이용해 마켓맵을 그리는 코드를 작성하는 것은 여러가지 장점이 있습니다. 

첫번째로, 파이썬을 사용하면 마켓맵의 색상, 크기, 레이아웃 등 다양한 요소를 사용자의 요구에 맞게 자유롭게 커스터마이징 할 수 있습니다. 

게다가, 간단한 주가 변동 외에도 거래량, 펀더멘털 데이터(순이익) 등 여러 요소를 포함한 복잡한 분석을 시각화할 수 있습니다.

또한, 파이썬을 사용하면 원하는 주기에 데이터를 업데이트하고 마켓맵을 생성할 수 있습니다. 이를 통해 반복 작업을 줄이고, 실시간으로 최신 데이터를 반영할 수 있습니다.

아래에서는 마켓맵을 그리는 방법을 4단계로 구분하여 설명합니다.

## 1단계. 필요한 라이브러리 불러오기
먼저 코드에 필요한 라이브러리를 불러와야합니다. 다음과 같은 라이브러리들이 필요합니다.
- matplotlib: 그래프 생성
- numpy: 데이터 계산
- yfinance: 종목정보 불러오기
- datetime: 시간 데이터 다루기
LinearSegmentedColormap은 matplotlib의 객체로 컬러맵을 커스터마이징하기 위해 필요합니다.

company_list는 코스피 시가총액 상위 종목에 대한 리스트를 나타내며, tikr_list는 각 종목의 종목코드를 나타내는 딕셔너리입니다. 저는 [네이버 금융에서 시가총액 상위 종목](https://finance.naver.com/sise/sise_market_sum.nhn)들을 검색해서 수기로 작성했습니다. 데이터 수집은 웹크롤링이나 [한국거래소 웹페이지](https://data.krx.co.kr/contents/MDC/MDI/outerLoader/index.cmd?screenId=MDCEASY017&locale=ko_KR&kosdaqGlobalYn=1)에서 제공하는 시가총액 상위 종목 데이터 파일을 이용하실 수도 있습니다. 주의 할점은 yfinance에서 종목정보를 얻기 위해서는 종목코드(tikr) 마지막에 .KS를 추가해야 하는 것 입니다.

```python
# BLOCK: Step 1 - Import libraries
import matplotlib.pyplot as plt
import squarify
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams["font.family"] ="Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# companies
company_list = ["삼성전자", "SK하이닉스", "LG에너지솔루션", "삼성바이오로직스",
                "현대차", "셀트리온", "기아", "KB금융", "POSCO홀딩스", "신한지주",
                "NAVER", "삼성물산", "삼성SDI", "LG화학", "현대모비스", "HD현대중공업", "삼성생명", "하나금융지주"]
tikr_list = {
    "삼성전자": "005930.KS",
    "SK하이닉스": "000660.KS",
    "LG에너지솔루션": "373220.KS",
    "삼성바이오로직스": "207940.KS",
    "현대차": "005380.KS",
    "삼성전자우": "005935.KS",
    "셀트리온": "068270.KS",
    "기아": "000270.KS",
    "KB금융": "105560.KS",
    "POSCO홀딩스": "005490.KS",
    "신한지주": "055550.KS",
    "NAVER": "035420.KS",
    "삼성물산": "028260.KS",
    "삼성SDI": "006400.KS",
    "LG화학": "051910.KS",
    "현대모비스": "012330.KS",
    "HD현대중공업": "329180.KS",
    "삼성생명": "032830.KS",
    "하나금융지주": "086790.KS",
}
```
## 2단계. yfinance로 종목정보 불러오기
2단계에서는 yfinance를 이용하여 종목정보와 주가정보를 불러와서 마켓맵 작성에 필요한 데이터 리스트에 저장합니다. 여기서 정의한 데이터 리스트는 다음과 같습니다.
- labels: 종목명과 등락율
- sizes: 시가총액
- change_list: 등락율 리스트

시가총액(marketcap)은 yf.Tiker 객체의 info에서 얻을 수 있습니다. 등락율(change)은 종가 정보를 불러와서 계산할 수 있습니다. 주말이나 휴일에는 장이 열리지 않아 종가 데이터가 없는 문제를 방지하기 위해, 과거 5일치의 주가를 불러와서 4일간의 등락율을 계산하고 마지막 값만 취했습니다.

```python
# BLOCK: Step 2 - Import data
labels = []
sizes = []
change_list = []
for company in company_list:
    TIKR = tikr_list[company]
    ticker = yf.Ticker(TIKR)
    marketcap = ticker.info["marketCap"]

    hist = ticker.history(start=datetime.now() - timedelta(days=5), end=datetime.now(), period="1d")
    close_data = hist.iloc[:]["Close"].to_numpy()
    change = (close_data[-1:1:-1] - close_data[-2:0:-1])/close_data[-2:0:-1]*100
    change = np.round(change[0],2)

    change_list.append(change)
    labels.append(f"{company}\n{change}%")
    sizes.append(marketcap)
```

## 3단계. squarify로 사각형 트리맵 생성하기
3단계는 squarify를 이용하여 사각형 트리맵을 생성합니다. 여기서 컬러맵(colormap)은 한국경제의 마켓맵에서 색상을 추출하여 7단계로 커스터마이징 했습니다. 등락율을 표현하는 색상의 최소값(vmin)과 최대값(vmax)은 -3과 3으로 설정했는데, 원하는 값으로 수정할 수 있습니다.

아래의 코드에서 rects는 squarify로 생성한 시가총액으로 크기를 정규화한 종목들의 사각형 객체입니다.

```python
# BLOCK: Step 3 - Treemaps generation
# colormap
colors_list = ["#4B87FF", "#4675F0", "#4162C4", "#414654", "#8A414E", "#BD3945", "#F3243B"]
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors_list)

norm = plt.Normalize(vmin=-3, vmax=3)
colors = [custom_cmap(norm(value)) for value in change_list]

# 크기를 정규화하여 squarify 레이아웃에 맞추기
sizes_normalized = squarify.normalize_sizes(sizes, 100, 100)
rects = squarify.squarify(sizes_normalized, 0, 0, 100, 100)
```

## 4단계. matplotlib으로 마켓맵 그리기
마지막으로 matplotlib을 이용하여 마켓맵을 그립니다. 여기서 종목의 트리맵은 ax.add_patch로 종목명과 등략을을 나타내는 텍스트는 ax.text로 작성됩니다.

```python
# BLOCK: Step 4 - Drawing a market map
fig, ax = plt.subplots(figsize=(12, 8))

# draw rectangle and add label
for rect, label, color in zip(rects, labels, colors):
    x, y, w, h = rect['x'], rect['y'], rect['dx'], rect['dy']
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=color, alpha=1.0, edgecolor="black"))
    ax.text(x + w/2, y + h/2, label, ha="center", va="center", color="white", fontsize=12, fontweight="bold")

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

plt.show()
```
# 코드를 수정하여 마켓맵 커스터마이징 하기
## 주간/월간 변동율 마켓맵 
코드에서 변동율 (change)를 주간 또는 월간단위로 계산하면 주간/월간 변동율 마켓맵을 작성할 수 있습니다. 2024년 08월 09일 주간으로는 대부분의 종목들이 상승한 반면, 월간으로는 대부분의 크게 떨어진 것을 한눈에 볼 수 있습니다.

<p align="center">   
    <img src="/images/2024-08-11-kospi-market-map-python/marketmap-week.webp" alt="코스피 주간 변동율 마켓맵">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 코스피 주간 변동율 마켓맵</span>
</p>

<p align="center">   
    <img src="/images/2024-08-11-kospi-market-map-python/marketmap-month.webp" alt="코스피 월간 변동율 마켓맵">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 코스피 월간 변동율 마켓맵</span>
</p>


## 거래량 마켓맵
코드에서 size를 거래량(volume)값으로 수정하면 코스피 시장에서 거래량 기준으로 종목의 크기를 표현하는 마켓맵을 그릴 수 있습니다.

<p align="center">   
    <img src="/images/2024-08-11-kospi-market-map-python/marketmap-volume.webp" alt="코스피 거래량 마켓맵">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 코스피 거래량 마켓맵</span>
</p>


## 순이익 마켓맵
코드에서 size를 순이익(income)값으로 수정하면 회사의 순이익을 기준으로 마켓맵을 작성할 수 있습니다. 다만, 섹터별로 순이익의 규모가 차이가 나는 점은 참고해야합니다.

그림을 시가총액 기준 마켓맵과 비교해보면, 현대차와 기아는 순이익이 높은 만큼 시가총액이 크기 않음을 알 수 있습니다.

<p align="center">   
    <img src="/images/2024-08-11-kospi-market-map-python/marketmap-income.webp" alt="코스피 순이익 마켓맵">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 코스피 순이익 마켓맵</span>
</p>


# 결론
정리하면, 앞에서 보았듯이 마켓맵을 활용한 데이터 분석은 시장 데이터를 직관적으로 시각화하여 복잡한 정보를 빠르게 이해할 수 있는 강력한 도구입니다. 코스피 시장의 경우 한국경제에서 제공하는 것 외에는 마켓맵을 볼 수 있는 소스가 거의 없었습니다.

파이썬을 이용하면, 마켓맵을 자유자재로 커스터마이징 할 수 있기 때문에 원하는 방식으로 데이터를 시각화 할 수 있습니다. 위에서 제공한 코드를 활용한다면 한국경제에서 제공하는 것 외에도 다양한 재밌는 그래프를 그릴 수 있다는 점에서 장점이 있습니다.