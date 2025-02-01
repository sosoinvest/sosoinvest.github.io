---
layout: single
title:  "[투자전략-1] 주가의 변동은 정규분포를 따른다: 한국, 미국, 일본, 중국의 주가 지수 비교"
description: 주가 일간 변동율의 히스토그램을 분석하여 정규분포를 따르는지 확인합니다.
categories: 투자
tag: [주식,파이썬,퀀트]
toc: true
author_profile: false
header:
 teaser: /images/2024-08-16-stock-return-normal-distribution/kospi200-histogram.webp
 og_image: /images/2024-08-16-stock-return-normal-distribution/kospi200-histogram.webp

# sidebar:
#     nav: "docs"
# search: true
---

주가의 변동을 분포로 표현하면 어떤 모양으로 나타날까?

# 서론
> "내일 주식시장은 오르거나 내릴겁니다."

어떤 책에서 본 글이다. 아마 제레미 시겔의 [주식에 장기투자하라](https://product.kyobobook.co.kr/detail/S000001490332)에서 본 글로 기억한다. 주식시장은 항시 내리거나 오르기 때문에 틀릴 수가 없는 말이다. 가끔 가격변동이 없는 경우도 있지만 그런 경우는 관심이 없으니 무시하자. 

주가의 변화는 랜덤성과 비선형성이 크기 때문에 예측하는 것은 매우 어렵다. 그러나 주식시장에서 돈을 벌기 위해서는 주가를 예측해야만한다. 그래야만 워런 버핏처럼 쌀 때 사서 비싸게 팔거나, 또는 [제시 리버모어](/투자/jesse-livermore-book/) 처럼 비쌀 떄 사서 더 비싸게 팔 수 있기 때문이다. 

<p align="center">   
    <img src="/images/2024-08-16-stock-return-normal-distribution/wallstreet-cartoon.webp" alt="주식 시장의 변동성을 표현한 만화 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 주식 시장의 랜덤한 변동성을 풍자한 만화; 하워드 막스의 투자와 마켓사이클의 법칙에 나오는 만화다. (BobMankoff.com)</span>
</p>

주가를 예측하기 위해서는 우선 주가의 변화가 어떤 형태인지 알아야 한다. 지피지기면 백전백승이라는 옛말이 있듯이 주가의 변화가 그동안 어떤 모습을 하고 있어왔는지 안다면 조금 더 주식시장에 대해 이해할 수 있을 것이다.

금융공학 모델에서는 주가의 변동율을 정규분포를 따른다고 가정한다. 쉽게 말해 주가는 작은 폭으로 자주 오르내리고 가끔 큰 폭으로 오르거나 내린다는 것이다. 큰 폭락이나 폭등은 자주 볼 수 없기 때문에 말이되는 가정이라고 생각한다. 이러한 가정이 타당한지 우선 주가의 변동율이 정말로 정규분포의 형태를 하고 있는지 확인해보자. 

# 이항분포
어떤 시행의 결과를 0(실패) 또는 1(성공)로 구분할 수 있는 것을 [베르누이 시행](https://ko.wikipedia.org/wiki/%EB%B2%A0%EB%A5%B4%EB%88%84%EC%9D%B4_%EC%8B%9C%ED%96%89)이라고 한다. 대표적으로 동전 던지기가 있다. 동전 던지기는 결과가 앞면 또는 뒷면 두가지로만 나온다. 

만약 베르누이 시행의 시행 횟수가 매우 크다면 성공 횟수를 분포의 형태로 그릴 수 있다. 이러한 분포를 이항분포라고 한다. 이항분포는 중심이 가장 크고 가장자리로 갈수록 작아지는 것은 상식적으로 말이된다. 즉, 모든 시행횟수에서 실패할 경우보다 적절히 성공하고 실패할 경우가 더 많을 것이다.

Galton board는 이러한 이항분포를 가시화 하는 장치이다. 이 장치는 떨어지는 공이 장애물과 부딪혀 결정된 최종 위치를 분포로 표시한다. 아래의 그림은 [Galton board의 시뮬레이션](https://javalab.org/en/galton_board_en/) 결과를 보여주는 애니메이션이다.

<p align="center">   
    <img src="/images/2024-08-16-stock-return-normal-distribution/binomial-distribution.gif" alt="이항분포를 가시화 할 수 있는 Galton board 사진">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 Galton board 시뮬레이션 애니메이션; 이항분포를 가시화 할 수 있다.</span>
</p>

주가가 오로지 수요와 공급의 법칙에 따라 결정된다고 가정한다면, 시장 참여자의 심리를 이산화하여 베르누이 시행으로 볼 수 있다. 즉, 매수하려하는 심리의 사람(1에 대응)과 매도하려하는 심리의 사람(0에 대응)으로 이분법적으로 구분할 수 있다. 어느날 주식시장에 나온 사람들 중 매수하려는 사람 수와 매도하려는 사람 수의 차이를 카운트 해서 그 결과를 분포로 그리면 이항 분포가 될 것이다. 그 결과를 변동율에 대응할 수있는 함수가 있다고 해보자. 이 함수는 매수하려는 사람이 매도하려는 사람보다 많으면, 양수(+)가 되고 반대로 적으면 음수(-)가 된다. 이렇게 하면 주가의 변동율을 이항분포로 표현할 수 있다.

## 이항분포는 정규분포에 근사된다
통계이론에 따르면 [이항분포는 확률이 50%에 가깝고, 시행횟수가 많을 때 정규분포로 근사화 할 수 있다](https://ko.wikipedia.org/wiki/%EC%9D%B4%ED%95%AD_%EB%B6%84%ED%8F%AC). 즉, 이산 확률변수를 연속 확률변수로 근사화 할 수 있다는 것이다. 

즉, 주가의 변동율을 이항분포로 표현할 수 있으면, 주가가 오르고 내릴 확률이 50%에 가깝고 데이터가 많다는 가정과 함께 이를 다시 정규분포로 근사화 할 수있다. 

# 주가지수의 일간 변동율은 정규분포를 따를까
## 코스피 일간 변동율 분포
주가의 일간 변동율의 분포가 정규분포를 따른다는 가정을 확인해보기 위해서는 먼저 주가 데이터를 불러오고, 일간 변동율을 계산해서 히스토그램으로 표현해야한다. 

아래의 그림은 코스피 200 지수의 10년간 일간 변동율을 히스토그램으로 표현한 것이다. 0% 에 가까운 낮은 변동율이 가장 많고, 변동율이 클 수록 횟수가 적어지는 전형적인 정규분포의 모습을 따른다. 신기한 점은 히스토그램이 거의 대칭이라는 점이다. 다시 말해 오르고 내리는 것이 거의 같은 횟수로 나타났다는 것이다. 코스피 지수가 크게 오르거나 내리지 않고 박스권에서 장기간 갖혀있는 것과 정확히 일치한다. 

박스권에 갖혀있는 것은 아쉽지만 그림은 코스피의 일간 변동율이 거의 정규분포를 따른다는 것을 보여준다. 그러나, 히스토그램은 일간 변동율 0을 기준으로 살짝 오른쪽으로 치우쳐있다. 이는 약하지만 지난 10년간 주식시장이 우상향 했다는 것을 보여준다. 우리 주식시장이 바닥권을 조금씩 높여오고 있다는 것이다. 

흥미로운 점은, 1% 이상 떨어지는 경우가 같은 변동폭만큼 오르는 경우보다 빈번하게 발생했다는 점이다. 반면에 3% 이상 변동하는 경우는 거의 없었다. 이러한 현상은 국장이 외부충격에 민감하게 반응한다는 것을 보여준다. 수출기업 중심의 외부충격에 민감한 경제상황을 고려하면 어쩔 수 없는 결과라고 생각한다. 

이러한 관찰을 근거로 생각을 정리해보면 국장에서는 박스권의 변동성을 노려서 트레이딩 하는 전략이 장기보유하는 것보다 유리할 수 있다.

<p align="center">   
    <img src="/images/2024-08-16-stock-return-normal-distribution/kospi200-histogram.webp" alt="Kospi 200 지수의 분포를 나타내는 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 코스피 200 지수의 10년 일간 변동율 분포 (2014.08.16 ~ 2024.08.16)</span>
</p>

## 미국 지수는 어떨까?
미국을 대표하는 S&P 500 지수의 10년간 일간 변동율을 구해봤다. 아래의 그림은 그 결과를 보여준다.

코스피와 마찬가지로 0을 중심으로 일간 변동율이 대칭적으로 분포한 것처럼 보인다. 그러나 자세히 보면, 오르는 빈도가 내리는 빈도보다 더 컸다. 흥미로운 점은 빠질 때는 크게 빠진 다는 점이다. 국장과 다르게 -2% 이상 떨어지는 경우가 같은 폭으로 오르는 경우보다 더 많았다. 그럼에도 불구하고 0~0.5% 오르는 경우가 내리는 경우보다 더 자주 있었기에 미국 주식은 지난 10년간 장기 우상향한 것을 확인할 수 있다. 여기서, 작은 수익률이더라도 누적되면 기하급수적으로 커지는 복리의 마법을 확인할 수 있다.

국장과 반대로 미장은 중단기 등락폭을 이용한 트레이딩 보다는 사서 오래 보유하는 것이 더 유리한 것으로 보인다.

<p align="center">   
    <img src="/images/2024-08-16-stock-return-normal-distribution/snp500-histogram.webp" alt="S&P 500 지수의 분포를 나타내는 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 S&P 500 지수의 10년 일간 변동율 분포 (2014.08.16 ~ 2024.08.16)</span>
</p>

## 한국 vs 미국 vs 일본 vs 중국
이제 한국, 미국, 일본, 그리고 중국의 주가 지수의 변동율을 비교해보자. 비교는 국내에 상장된 지수추종 ETF의 데이터를 기준으로 했다. 주가지수를 직접 불러올 수도 있겠지만, 파이썬 코드가 ETF 가격을 불러와서 처리하는 것을 기반으로 했기 때문이다. 코드를 고치는 것은 어렵지 않지만 쉬운 방법을 택했다. 

비교에 사용한 ETF는 아래 표와 같다. 일본 지수 추종 ETF가 2016년 3월 3일 상장했기 때문에, 비교는 이 시점을 기준으로 했다. 미국과 일본 지수는 관찰한 기간동안 각각 162% 그리고 152.7% 올랐다. 흥미로운 점은 코스피도 82.6%나 올랐다는 것이다. 반면에 중국 지수는 8년의 시간을 고려하면 거의 오르지 않았다.

이 비교에서는 주가지수 자체가 아니라 환율과 ETF 함께 들어갔다는 것을 감안해야한다. 일본, 미국 지수는 환헤지 ETF를 사용해서 환차손익이 없지만, 중국 지수는 위안화 환율의 영향을 받았다. 

|    지수    |          종목          |     상장일     | 변동율 (2016.03.03~2024.08.16) |
|:----------:|:----------------------:|:--------------:|:-----------------------------:|
| KOSPI 200  |       ACE 200           | 2008. 09. 25   |            +82.6 %            |
| NIKKEI 225 | ACE 일본 Nikkei225(H)   | 2016. 03. 03   |           +152.7 %            |
|  S&P 500   |  Tiger 미국 S&P500선물(H)      | 2020. 08. 07   |           +162.0 %            |
|  CSI 300   | ACE 중국 본토 CSI300    | 2012. 11. 29   |            +24.4 %            |

일간 수익률의 히스토그램을 보면 아래 그림과 같다. 여기서는 비교를 쉽게하기 위해 히스토그램을 바(bar) 그래프가 아니라 선으로 그렸다. 

<p align="center">   
    <img src="/images/2024-08-16-stock-return-normal-distribution/total-market-histogram.webp" alt="Kospi200, Nikkei225, S&P500, CSI300 지수의 분포를 나타내는 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 한국, 일본, 미국, 중국 지수의 일간 변동율 분포 (2016.03.03 ~ 2024.08.16)</span>
</p>

### 미국은 가운데가 뾰족하고 오른쪽으로 치우쳐진 히스토그램을 보였다. 
이를 해석하면 작은 폭으로 자주 오르고 적게 떨어졌다고 볼 수 있다. 변동율이 음수인 영역에서 다른 시장들 보다 그래프가 안쪽으로 말려들어가 있다.

### 일본은 미국보다 넓은 형태의 분포를 보였다. 
변동율이 양수인 영역에서 미국보다 그래프가 위쪽에 있다. 즉, 일본의 주가 상승은 작은 폭으로 자주 오른것에 기인한 것이 아니라 큰 폭으로 오르는 경우가 많았기 때문으로 해석할 수 있다.

### 한국은 일본과 비슷한 모양의 그래프를 보였다. 
다른 지수와 비교하여 변동폭이 작은 날이 큰 날보다 더 많았다. 전날 미국 시장이 오르더라도 국장은 이를 따라가지 못하는 경우가 많았는데 그러한 모습을 여기에서도 확인할 수가 있다. 

### 중국은 가장 특이한 그래프를 보인다. 
종모양의 분포지만 변동율이 음수인, 즉, 내리는 날이 다른 나라들 보다 눈에 띄게 많았다. 다른 나라들과 비교하여 변동율 양수의 분포는 아래로 말려들어가 있지만, 음수의 분포는 가장 위에 올라와 있다. 

중국시장에 장기 투자하는 것이 유리하지 않음은 이 그래프에서도 확인할 수 있다. 신기한 점은 지난 8년간 중국의 GDP는 다른 나라보다 큰 폭으로 꾸준히 성장했다는 것이다. 주식시장은 경제 성장과 반대의 결과를 보여줬다. 중국은 비교한 다른 나라와 다르게 사회주의 체제를 따른다. 주식에 투자하는 것은 그 나라의 경제 성장만 가지고 판단할 것이 아니라 체제, 정치, 그리고 문화와도 깊은 관계가 있다는 것을 명심해야한다.

# 정리하면
여기서 알아낸 것을 다음과 같이 정리할 수 있다. 
- 주가 지수의 일간 변동율은 정규분포를 따르는 것처럼 보인다.
- 주가지수가 우상향 하는 것은 큰 폭의 상승이 아니라, 작은 폭의 상승이 누적된 복리의 마법에 의한 것이다.
- 일간 변동율 분포의 모양은 국가별로 조금씩 다르다.

## 부록
### 주가 변동율 파이썬 코드
```python
# BLOCK: Step 1 - Import libraries
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from datetime import datetime
from matplotlib import colors

plt.rcParams["font.family"] = "Malgun Gothic"
# plt.rcParams["font.family"] = "Times"
plt.rcParams["axes.unicode_minus"] = False

# BLOCK: Get close price of ACE 200 and compute the change per day
TIKR = "105190.KS" # KOSPI 200
# TIKR = "238720.KS" # NIKKEI 225
# TIKR = "360200.KS" # S&P500
# TIKR = "168580.KS" # CSI300

ticker = yf.Ticker(TIKR)
start = datetime(2014, 8, 16)
end = datetime.now()

hist = ticker.history(start=start, end=end, period="1d")
close_price = hist.iloc[:]["Close"].to_numpy()
change = np.diff(close_price)/close_price[0:-1]*100
# print(change)

# BLOCK: Draw histogram
n_bins = 71
fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True, figsize=(8, 6))
axs.hist(change, bins=n_bins)

plt.xlabel("Change per day [%]", fontsize=12, color="black")
plt.ylabel("Counts", fontsize=12, color="black")
plt.title("KOSPI 200 Histogram\n(2014-08-16 ~ 2024-08-16)", fontsize=14, color="black")
plt.xticks(color="black", fontsize=12)
plt.yticks(color="black", fontsize=12)

plt.xlim(-5, 5)
axs.grid(True)

## BLOCK: Color the histogram
# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs.hist(change, bins=n_bins)

# We'll color code by height, but you could use any scalar
fracs = N/N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.savefig("KOSPI200_HISTOGRAM.png")
plt.show()

```
