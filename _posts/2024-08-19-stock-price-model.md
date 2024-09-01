---
layout: single
title:  "주식이 오를 확률 계산하기: 로그 정규분포 모델을 이용하여"
description: 로그 정규분포 모델을 이용하여 주식이 오를 확률을 계산합니다.
categories: 투자
tag: [주식,파이썬,퀀트]
toc: true
author_profile: false
header:
 teaser: /images/2024-08-19-stock-price-model/kodex200-pdf.webp
 og_image: /images/2024-08-19-stock-price-model/kodex200-pdf.webp

# sidebar:
#     nav: "docs"
# search: true
---

내일 주식이 오를 확률을 계산할 수 있을까?

# 서론
주가는 무작위적으로 오르고 내리는 것처럼 보이지만 자세히 들여다보면 통계적인 규칙이 있다. [주가의 변동율을 히스토그램으로 나타내면 평균을 기준으로 대칭인 종 모양의 정규분포를 따른다](/투자/stock-return-normal-distribution/). 이를 해석하면, 최근에 주가가 많이 올랐으면 내일은 내릴 확률이 크고, 반대로 많이 내렸으면 내일은 오를 확률이 더 크다는 직관적인 사실을 알 수있다. 

주식 투자는 쌀 때사서 비쌀 떄 팔아야 한다는 것은 누구나 다 알고있다. 그런데 도대체 주가가 얼마여야 싼지 또는 비싼지 판단하는 기준은 다양하고 모호하다. 게다가 시장과 주식은 시간에 따라 계속 변한다. 같은 가격이라도 지금은 싸고 그떄는 비쌀 수도 있고, 그 반대로 판단 될 수도 있다. 때문에 많은 사람들이 틀린 예측을 내놓는다.

 주가의 변동율이 정규분포를 따르는 것을 이용해서 어떤한 통계적 방법으로 주가를 모델링 할 수 있다면, 이러한 가격의 높고 낮음을 판단할 수 있는 기준을 제시할 수 있을 것이다.

여기서는 주가를 예측하기 위해 어떤 통계 모델을 쓸 수 있는지 알아보자.

# 주가는 로그정규분포로 모델링 할 수 있다
금융공학에서는 일반적으로 주가에 로그를 취한 것이 정규분포를 따른다고 가정한다. 그 주된 이유는 주가의 로그 수익률이 정규분포를 따르기 때문이다. 로그 수익률은 과거와 현재의 주가의 비에 로그를 취한 것으로, 테일러 전개를 이용하여 변동율(수익률과 같은 말이다. 음수(-)의 수익률이 모순처럼 느껴져서 여기서는 변동율로 표현했다.)로 근사할 수 있다. 이를 수식으로 표현하면 아래와 같다. 아래의 수식은 2차까지 테일러 전개했다.

$$ 
\ln\left(\frac{x_{i+1}}{x_i}\right) = \ln(1 + x_i) \approx R_i - \frac{1}{2} R_i^2 
$$

여기서, x는 주가를 의미하고 R은 시간 i와 i+1 사이의 주가 변동율을 나타낸다. 일반적으로 변동율은 1보다 매우 작으므로, 테일러 전개의 2차항을 무시하면 로그 수익률은 주가 변동율에 근사할 수 있다.
즉,

$$ 
\ln\left(\frac{x_{i+1}}{x_i}\right) \approx R_i
$$

주가의 로그 수익률이 정규분포를 따른다면 주가는 로그를 취했을 때 정규분포가 되는 로그 정규분포를 따른다고 가정할 수 있다. 이와 더불어, 주가는 0이 될 수 없고 시간에 따라 지수적으로 무한대로 커질 수 있으므로 로그 정규분포의 특성과 잘 맞는다.

이러한 이유로 많은 금융모델, 특히 [블랙-숄즈(Black-Scholes) 옵션 가격모델](https://namu.wiki/w/%EB%B8%94%EB%9E%99-%EC%88%84%EC%A6%88%20%EB%AA%A8%ED%98%95)은 주가가 로그 정규분포를 따른다고 가정한다.

## 로그 정규분포
주가의 로그가 평균 μ와 표준편차 σ의 로그 정규분포를 따른다고 해보자. 즉, 수식으로 표현하면,

$$
\ln (x) \sim N(\mu, \sigma^2)
$$

### 확률밀도함수
이떄, 로그 정규분포의 확률밀도함수(Probability density function, PDF)는 아래 수식과 같다. 

$$ 
 PDF(x) = \frac{1}{x\sigma \sqrt{2\pi }}\exp(-\frac{(\ln x-\mu )^2}{2\sigma^2})
$$

<p align="center">   
    <img src="/images/2024-08-19-stock-price-model/log-normal-pdfs.webp" alt="로그 정규분포의 확률밀도함수 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 로그 정규분포 확률밀도 함수 (출처: 위키피디아)</span>
</p>

### 누적분포함수
확률밀도함수를 0 부터 x까지 적분한 누적분포함수(Cumulative distribution function, CDF)는 아래 수식과 같다. 

$$ 
CDF(x) = \frac{1}{2}[1+\mathrm{erf}(\frac{\ln x -\mu}{\sigma\sqrt{2}})]
$$

여기서 erf는 오차함수라는 복잡한 함수를 의미하는데, 어차피 컴퓨터가 다 계산해줄 것이니 크게 신경쓰지 않아도 된다.

<p align="center">   
    <img src="/images/2024-08-19-stock-price-model/log-normal-cdfs.webp" alt="로그 정규분포의 누적분포함수 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 로그 정규분포 누적분포 함수 (출처: 위키피디아)</span>
</p>

## 주가가 오를 확률
내일 주가가 오늘 종가(x)보다 높을 확률(P)을 계산해 보자. 누적분포함수를 이용한 수식으로 표현하면 아래와 같다.

$$ 
P=1-CDF(x)
$$

따라서, 주가의 로그 평균과 표준편차를 안다면 위의 수식을 이용해서 다음 시간에서 주가가 현재 주가보다 높을 확률을 계산해낼 수 있다. 

# 코스피에 적용해보자
이제 로그 정규분포 모델을 코스피에 적용해보자. 분석에는 코스피 200지수를 추종하는 ETF인 KODEX 200의 주가 데이터를 사용했다.

아래의 그림은 한달(20일), 한분기(60일), 반기(120일), 그리고 연간(200일) 시간 간격의 통계치로 계산한 확률밀도함수를 보인다. 한달은 최근 뉴스가 반영되며, 한분기는 기업들의 분기실적, 반기는 금통위의 금리결정, 그리고 연간은 인플레이션 같은 장기적인 요소들의 영향이 반영된다.

현재의 주가는 한달의 시간 간격에서는 거의 평균에 있는데, 시간 간격이 넓어지면 분산커져서 평균에서 벗어나는 모습을 보인다.

<p align="center">   
    <img src="/images/2024-08-19-stock-price-model/kodex200-pdf.webp" alt="KODEX200 ETF의 최근 주가 데이터로 계산한 확률밀도함수 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 KODEX200 최근 1년 (2023.08.20~2024.08.20) 데이터로 계산한 확률밀도함수; 계산에 사용한 시간 간격은 20일, 60일, 120일, 200일을 사용했다.</span>
</p>

## 주가가 오를 확률
시간 간격에 따라 주가가 현재 가격보다 높을 확률을 계산해보면 아래와 같다. 

- 한달(20일): 49.64%
- 한분기(60일): 73.67%
- 반기(120일): 61.36%
- 연간(200일): 30.78%

반기보다 짧은 시간 간격의 통계 데이터 기준으로 주가가 오를 확률이 큰 반면에, 연간 통계로는 주가가 내릴 확률이 더 높았다. 

따라서, 확률을 기준으로 현재의 주가는 중단기적으로 저평가인 반면에 장기적으로 고평가라고 판단할 수 있다. 

# 과거 데이터를 분석해보자
최근 3년간의 데이터로 로그 정규분포로 계산한 주가가 오를 확률이 실제 주가의 움직임과 어떤 관련이 있는지 확인해봤다. 아래에는 2021년 부터 2024년 까지의 데이터로 계산한 결과이다. 여기서 시간 간격은 20일을 사용했다.

아래에 나오는 그림들에서 검은색 실선은 주가이며 파란색 실선은 확률을 나타낸다.

## 2021-2022: 금리 인상기
주식이 게속 빠지던 2021년에는 주가의 변동성이 심했다. 때문에 모델이 예측한 오를 확률이 높음에도 불구하고 주가의 흐름을 따라가지 못하는 모습을 보였다.

<p align="center">   
    <img src="/images/2024-08-19-stock-price-model/prob-2021-2022.webp" alt="KODEX200 ETF의 2021-2022 1년간 주가가 오를 확률과 실제 주가 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 KODEX200 2021.08.20~2022.08.20 데이터로 게산한 주가가 오를 확률과 실제 주가</span>
</p>

## 2022-2023: 금리 동결기
2022년에는 기준금리를 동결하며 주가가 저점을 다지고 반등했다. 이때에는 오를 확률이 60% 이상일 때 매수했으면 저점을 잘 잡았을 것으로 보인다.

<p align="center">   
    <img src="/images/2024-08-19-stock-price-model/prob-2022-2023.webp" alt="KODEX200 ETF의 2012-2023 1년간 주가가 오를 확률과 실제 주가 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 KODEX200 2022.08.20~2023.08.20 데이터로 게산한 주가가 오를 확률과 실제 주가</span>
</p>

## 2023-2024: 금리 인하기대기
최근 1년간 연준이 금리를 내릴거라는 기대로 주가가 잘 올라왔다. 이때는 50% 이상의 확률일 때 매수했으면 저점을 잡고 어느정도 수익을 올릴 수 있었을 것으로 보인다. 

그러나 모델이 제시한 확률만 믿고 배팅한다면 주가가 32000원에서 38000원 까지 약 18% 오른 수익은 놓칠 수 밖에 없었다. 주가가 오르내리지 않고 꾸준히 우상향 하는 경우에는 로그 정규분포 모델을 사용하는 것이 적합하지 않았다는 것을 확인할 수 있다. 

<p align="center">   
    <img src="/images/2024-08-19-stock-price-model/prob-2023-2024.webp" alt="KODEX200 ETF의 2023-2024 1년간 주가가 오를 확률과 실제 주가 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 6 KODEX200 2023.08.20~2024.08.20 데이터로 게산한 주가가 오를 확률과 실제 주가</span>
</p>

# 정리하면
여기서 알아낸 것을 다음과 같이 정리할 수 있다. 
- 주가의 변동율이 정규분포를 따른다면 주가는 로그 정규분포로 모델링 할 수 있다.
- 주가의 로그 평균과 표준편차를 이용하면 주가가 오를 확률을 계산할 수 있다.
- 최근 3년간 코스피 시장은 로그 정규분포로 계산한 확률을 이용하면 저점을 잡을 수 있었다.
- 그러나 이 방법은 주가가 우상향 하는 경우에는 큰 폭의 상승은 놓칠 수 있다.

## 부록
### 주가의 로그 정규분포 모델 파이썬 코드
```python
# Block: Stock price low pass filtering
import numpy as np
import scipy, os, requests, time
import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd
import openpyxl
plt.rcParams["font.family"] ="Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

TIKR = "069500.KS"


# BLOCK: Function to compute mean and standard deviation within the window
def std_and_mean(close, open, high, low, window_size):
    new_close = close[-window_size:]
    new_open = open[-window_size:]
    new_high = high[-window_size:]
    new_low = low[-window_size:]

    mean = np.mean(np.log(np.append(np.append(np.append(new_close, new_open), new_low), new_high)))
    std = np.std(np.log(np.append(np.append(np.append(new_close, new_open), new_low), new_high)))

    return mean, std


def calc_pdf(x, mean, std):
    pdf = 1 / (x * std * np.sqrt(2 * np.pi)) * np.exp(-(np.log(x) - mean) ** 2 / (2 * std ** 2))

    return pdf


# BLOCK: Import stock price data
ticker = yf.Ticker(TIKR)
start = datetime(2023, 8, 20)
end = datetime(2024, 8, 20)

data = ticker.history(start=start, end=end, period="1d")
date = data.index.values
date = [pd.to_datetime(on_day).to_pydatetime().strftime("%Y-%m-%d") for on_day in date]

close = data.iloc[:]["Close"].to_numpy()
close[np.argwhere(np.isnan(close))] = 0

open = data.iloc[:]["Open"].to_numpy()
open[np.argwhere(np.isnan(open))] = 0

high = data.iloc[:]["High"].to_numpy()
high[np.argwhere(np.isnan(high))] = 0

low = data.iloc[:]["Low"].to_numpy()
low[np.argwhere(np.isnan(low))] = 0

# BLOCK: Compute the probability density function (PDF)
x = np.arange(25000, 50000, 50)
ind = (np.abs(x-close[-1])).argmin()

# BLOCK: Plot the PDF
fig, ax = plt.subplots(1, 1, figsize=(8, 8), tight_layout=True)
for window_size in [20, 60, 120, 200]:
    mean, std = std_and_mean(close, open, high, low, window_size)
    pdf = calc_pdf(x, mean, std)

    ax.plot(x, pdf, label=f"Window size: {window_size}", linewidth=2)
ax.grid(True)

ax.set_xlabel("주가", fontsize=16, color="black")
ax.set_ylabel("Probability density", fontsize=16, color="black")

ax.tick_params(axis="x", color="black", labelsize=14)
ax.tick_params(axis="y", color="black", labelsize=14)

ax.axvline(x=x[ind], color="black", linestyle="--", linewidth=1.5, label="Current price")
ax.legend(prop={"size": 14})

plt.savefig(f"kodex200-pdf.png")
plt.show()

# BLOCK: Compute the probability
target_price = close[-1]*1.00
for window_size in [20, 60, 120, 200]:
    mean, std = std_and_mean(close, open, high, low, window_size)
    prob = 1 - 0.5 * (1 + scipy.special.erf((np.log(target_price) - mean) / (std * np.sqrt(2))))
    prob = np.round(prob * 100, 2)
    print(f"The probability of the close price is higher than current price is: {prob}%")

```
