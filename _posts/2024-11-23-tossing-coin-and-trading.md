---
layout: single
title:  "내 트레이딩 전략은 정말 이길 확률이 있는가"
description: 동전던지기 문제의 통계적 기법을 이용해 트레이딩 전략이 정말 이길 확률이 있는지 추론하는 방법
categories: 투자
tag: [주식,퀀트]
toc: true
author_profile: false
header:
 teaser: /images/2024-11-23-tossing-coin-and-trading/a-trader-tossing-coin.webp
 og_image: /images/2024-11-23-tossing-coin-and-trading/a-trader-tossing-coin.webp
# sidebar:
#     nav: "docs"
# search: true
---
<style>
  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.9em;
  }
  th {
    background-color: #51555D;    
    padding: 10px;    
  }
  td {
    padding: 10px;
  }
</style>

어떤 트레이딩 전략을 백테스팅해서 승률을 계산했다고 할 때, 이 결과를 그대로 믿을 수 있을까? 이러한 문제를 풀 수 있는 통계적 접근법이 있다.

# 트레이딩과 동전던지기 게임
트레이딩은 명백히 승패가 있는 게임이다. 한번의 매매에서 이득을 얻으면 승리, 손실을 보면 패배다. 이렇게 승패가 가려지는 문제는 동전던지기와 유사하다. 동전을 던져서 앞면(head)이면 승리, 뒷면(tail)이면 패배에 대응될 수 있다. 

만약 동전을 10번 던져서 앞면이 5번, 뒷면이 5번 나왔다고 해보자. 이 동전은 편심되지 않은 공정한 동전이라고 할 수 있을까? 공정하다고 확신하기에는 아직 미심쩍은 부분이 있다. 왜냐하면 시행횟수가 너무 적기 때문이다. 

반대로 만약 앞면이 7번, 뒷면이 3번 나왔을 때, 이 동전은 불공정한 동전이라고 할 수 있을까? 전자와 같은 이유로 그것도 어렵다. 

공정한 동전인지 확인하는 가장 단순한 방법은 시행횟수를 늘리는 것이다. 시행횟수를 10000번으로 늘려서 앞면과 뒷면이 거의 5대 5의 비율로 나왔다면, 공정하다고 인정할 수 있다. 반대로 7 대 3의 비율이라면 불공정하다고 확신할 수 있다.

그런데 문제는 10000번이나 동전을 던지는 것은 현실적으로 많은 노력과 비용이 든다는 것이다. 구체적으로 얘기하자면 우선 동전을 던지는 시간과 체력이 소모되고, 만약 여기에 돈이라도 걸었다면 동전이 사기인지 아닌지 판단하기 까지 너무 오랜 시간이 걸린다. 만약 사기라면 10000번을 반복하기 전에 가진 돈이 먼저 바닥날 것이다.

이러한 이유로, 너무 많지 않은 현실적인 시행횟수에서 확률이 얼마나 신뢰할 수 있는지 판단하는 것이 중요하다. 이러한 문제를 다루는 통계적 접근법은 여러가지가 있는데, 여기서는 대표적인 베이지안 접근법과 빈도주의 접근법을 다룬다. 이 글은 위키피디아의 [동전이 공정한지 판단하기](https://en.wikipedia.org/wiki/Checking_whether_a_coin_is_fair) 문서를 참고해서 정리한 것이다. 

<p align="center">   
    <img src="/images/2024-11-23-tossing-coin-and-trading/a-trader-tossing-coin.webp" alt="동전 던지기하는 트레이더 사진">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 트레이딩은 성공과 실패가 갈리는 동전던지기다.</span>
</p>

## 베이지안 접근법: 사후 확률 밀도 함수
베이지안(Bayesian) 접근법은 사전 확률 밀도 함수(Prior probability density function)와 시행결과를 이용하여 사후 확률 밀도 함수(Posterior probability density function)를 유도하고 이를 적분하여 동전이 공정한지 판단하는 방법이다. 

예를 들면 동전을 던지기 전에 동전이 앞면이 나올 확률을 p%로 알고있다고 할 때, N번 던져서 앞면이 h번, 뒷면이 t번 나왔다고해보자. 베이지안 접근법은 조건부 확률, 앞면이 나올 확률이 X% 일 때, N번의 시행에서 앞면이 h번 나올 확률을 계산하는 것이다. 여기서 앞면이 나올 확률 X%는 동전던지기 전의 사전(Prior) 확률이고, 시행후 계산한 조건부 확률은 사후(Posterior) 확률이다.

좀 더 엄밀히 말하면, 사전 확률 p는 상수가 아닌 확률 밀도 함수로 표현된 불확정 변수로 가정한다. 

구체적으로 동전을 N번 던진다고 해보자. 앞면이 나온 회수는 h, 뒷면은 t로 그리고 각각에 대응되는 확률 변수는 H와 T라고 하자. 즉, $N=H+T=h+t$. 여기서 문자는 변수고 소문자는 값을 나타낸다.

$r$을 한번의 시행에서 앞면이 나올 실제 확률이라고 하자. 이 값은 변하지 않는 동전 자체의 특성이다.

베이즈 이론을 이용하면, 앞면이 h번, 뒷면이 t번 나온경우의 사후 확률 밀도 함수는 다음과 같다. 

$$
f(r|H=h, T=t)=\frac{Pr(H=h|r,N=h=t)g(r)}{ \int_{0}^{1}Pr(H=h|p,N=h+t)g(p)dp}
$$

여기서 $g(r)$은 $r$의 사전 확률 밀도 함수를 의미한다. 

동전에 대한 정보가 전혀 없을 때, 사전 확률 밀도 함수가 $[0,1]$ 구간에서 균일(uniform)하다고 가정해보자. 즉, $g(r)=1$. 실제 우리가 사용하는 동전은 앞면이 나올 확률이 50%에 가까울 것이기 때문에, 확률 밀도 함수는 $r=0.5$에 가중된 모양일 것이다. 그런데, 동전이 전혀 정보가 없는 순수한 블랙박스라면, 확률 밀도 함수가 균일하다는 가정에서 출발해서 동전던지기에 새로 얻는 정보를 이용하여 베이즈 이론으로 계속해서 업데이트 해나갈 수 있다. 

예를 들어, 첫번째 세트에서 동전을 10번 던진 후 얻은 사후 확률 밀도 함수를 두번째 세트의 사전 확률 밀도 함수에 입력해서 새로운 사후 확률 밀도 함수를 유도해 낼 수 있다. 이렇게 업데이트 하는 접근법은 승률을 전혀 알 수 없는 트레이딩에서 유용하게 쓰일 수 있다.

다시 수식으로 돌아가서, 위의 식에서 분자에 해당하는, 실제 앞면이 나올 확률이 r일 때, N번의 시행에서 앞면이 h번 나올 확률은 이항분포를 이용하여, 

$$
Pr(H=h|r,N=h+t)=\binom{N}{h}r^h(1-r)^t.
$$

이 확률식을 위의 사후 확률 밀도 함수 식에 넣으면 $g=1$ 이므로, 

$$
f(r|H=h, T=t)=\frac{\binom{N}{h}r^h(1-r)^t}{\int_{0}^{1}\binom{N}{h}p^h(1-p)^tdp}=\frac{r^h(1-r)^t}{\int_{0}^{1}p^h(1-p)^tdp}.
$$

위의 식의 우항은 분모가 [베타 함수($B$)](https://en.wikipedia.org/wiki/Beta_function)로 표현되는 [베타 분포(Beta distribution)](https://en.wikipedia.org/wiki/Beta_distribution)라고 불린다. 

베타 함수로 표현하면, 

$$
f(r|H=h, T=t)=\frac{r^h(1-r)^t}{B(h+1,t+1)}.
$$
여기서 h와 t는 정수이기 때문에, 위의 사후 확률 밀도식은 팩토리얼을 이용해 다음과 같이 표현된다.

$$
f(r|H=h, T=t)=\frac{(h+t+1)!}{h!t!}r^h(1-r)^t.
$$

이렇게 유도된 사후 확률 밀도 함수를 동전이 공정하다고 할 수 있는 판정 범위의 r(예를 들면, $0.45<r<0.55$)에 대해 적분하면, N번의 시행 후 추정한 r이 판정 범위 안에 들어갈 확률을 알 수 있다.

### 예제
N=10, h=7 인경우, 즉, 10번 동전을 던져서 앞면이 7번 나온 경우 사후 확률 밀도 함수는,

$$
f(r|H=7, T=3)=\frac{(10+1)!}{7!3!}r^7(1-r)^3=1320r^7(1-r)^3.
$$

계산한 사후 확률 밀도 함수를 그래프로 그리면,

<p align="center">   
    <img src="/images/2024-11-23-tossing-coin-and-trading/pdf.webp" alt="사후 확률 밀도 함수 그림">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 사후 확률 밀도 함수 (N=10, h=7, t=1); 사전 확률 밀도 함수는 균일(g=1)하다고 가정했다.</span>
</p>

r이 45%에서 55% 사이에 있을 때 동전이 공전하다고 판정한다면, 시행결과를 바탕으로 추정한 이 범위에 들어가 확률은, 

$$
Pr(0.45<r<0.55>)=\int_{0.45}^{0.55}f(p|H=7,T=3)dp \approx 13\%.
$$

즉, 10번의 시행에서 7번 앞면이 나왔으면, 13%의 확률로 동전이 공정하다고 볼 수 있다는 것이다. 사실 13%의 확률은 균일하다고 가정한 사전 확률 밀도 함수의 10%($g$의 $0.45<r<0.55$ 구간에서의 면적)보다 조금 더 높다. 사전 확률 밀도 함수를 실제와 맞게 0.5에 가중된 것을 쓰거나, 여기서 얻은 사후 확률 밀도 함수를 새로운 세트의 시행에서 사전 확률 밀도 함수로 업데이트 한다면, 추론의 정확도를 높여갈 수 있다.

균일한 사전 확률 밀도 함수에서, 사후 확률 밀도 함수의 피크 값은 $r=h/(h+t)=0.7$에서 발생한다. 이 값을 r의 maximum a posteriori (MAP) estimate라고 한다. 

또한, 이 예제에서 r의 기댓값은,

$$
E[r]=\int_{0}^{1}rf(r|H=7,T=3)dr =\frac{h+1}{h+t+2}=\frac{2}{3}.
$$

## 빈도주의 접근법: 진짜 확률 추정하기 
빈도주의 접근법은 실험자가 신뢰 구간과 허용 오차의 범위를 지정하고, 이러한 파라미터을 이용하여, 추정 확률이 실제 확률과 오차범위에 들어오려면 동전을 몇번 던져야 하는지 계산하는 방법이다. 베이지안 접근법이 사전 경험에 가중치를 두는 것과 다르게, 빈도주의 접근법은 그렇지 않다는 차이가 있다.

여기서는 실제 확률 $r$의 최적의 추론 값 $p$는 단순히 앞면의 횟수를 전체 시행횟수로 나눈것으로 본다. 

$$
p=\frac{h}{h+t}.
$$

이 추론값은 특정 신뢰구간에서 오차의 마진 (Margin of error) $E$를 갖는다.

$$
|p-r|<E.
$$

여기서, 빈도주의 접근법을 이용하여 얼마나 많이 동전을 던져야하는지 결정하려면 두가지 파라미터가 필요하다. 첫번쨰는 신뢰도 Z이고, 두번째는 최대허용오차 E이다.

여기서 신뢰도 Z는 표준 정규분포의 Z 값으로 주어진다. 아래의 표는 표준 정규분포의 신뢰도별 Z 값을 보여준다. 

*표 1: 신뢰도 Z값*

|Z 값| 신뢰도 | 비고 |
|:---:|:---:|:---:|
|0.6745 | 50.000% | Half |
|1.0000 | 68.269% | One std dev |
|1.6449 | 90.000% | "One nine" |
|1.9599 | 95.000% | 95 percent |
|2.0000 | 95.450% | Two std dev |
|2.5759 | 99.000% | "Two nines" |
|3.0000 | 99.730% | Three std dev |
|3.2905 | 99.900% | "Three nines" |
|3.8906 | 99.990% | "Four nines" |
|4.0000 | 99.993% | Four std dev |
|4.4172 | 99.999%| "Five nines" |

통계학에서 표준 오차는 다음과 같이 정의된다.

$$
s_p=\sqrt{\frac{p(1-p)}n}.
$$

여기서, n은 총 시행횟수를 의미한다.

위의 수식에서 $s_p$는 $p=0.5$일 때 최대가 된다. 위의 식에 $p=0.5$를 대입해서 최대 오차를 구하면,

$$
s_p=\sqrt{\frac{p(1-p)}n}\leq \sqrt{\frac{0.5\times 0.5}n}=\frac{1}{2\sqrt{n}}
$$

따라서 신뢰되 Z에 해당하는 최대 허용오차는, 

$$
E=Zs_p=\frac{Z}{2\sqrt{n}}
$$

위의 식을 n에 대해서 정리하면, 

$$
n=\frac{Z^2}{4E^2}.
$$

위의 수식을 이용하면, 신뢰도 Z와 허용오차 E가 주어졌을때, 시행횟수 n을 구할 수 있다.

### 예제
1. 최대 허용오차가 0.01이라고 할 때, 동전을 몇번 던져야 하는가?

위의 수식에 $E=0.01$을 대입하면, $n=2500Z^2$.

\- 신뢰도 68.27%(Z=1) 일 때, n=2500,

\- 신뢰도 95.45%(Z=2) 일 때, n=10000, 

\- 신뢰도 99.90%(Z=3.3) 일 때, n=27225, 

2. 동던던지기를 10000회를 시행했다고 할 때, 추정한 확률 p의 최대 오차는 얼마인가?

최대 허용오차 수식에서 n=10000를 대입하면, $E=\frac{Z}{200}$

\- E=0.0050, 신뢰도 68.27% (Z=1)

\- E=0.0100, 신뢰도 95.45% (Z=2)

\- E=0.0165, 신뢰도 99.90% (Z=3.3)

3. 동전을 12000회 던져서 앞면이 5961번 나왔을 때, 신뢰도 99.999%의 앞면이 나올 확률 r의 구간을 얼마인가?

추정 확률 $p=5961/12000=0.4968$, 신뢰도 99.999%의 Z=4.4172 일 때, E를 계산하면, $E=0.0202$.

추정 확률 r과 최대오차 E일 때, 실제 확률 r의 범위는,
$p-E<r<p+E$ 따라서,

$0.4766<r<0.5170$

# 백테스팅 결과를 얼마나 믿을 수 있는가
## 베이지안 접근법
이전의 트레이딩 결과를 가져와서 얼마나 신뢰할 수 있나 판단해보자. [섹터 ETF에 적용한 변동성 돌파 전략](/투자/sector-etf-short-term-strategy)의 트레이딩 결과를 가져와보자. KODEX 헬스케어가 가장 성과가 좋았는데, 대략 725회의 트레이딩에서 461번 이기고 264번 졌다. 베이지안 접근법으로 승률 r의 사후 확률 밀도 함수를 구해보면 아래 그림과 같다.

<p align="center">   
    <img src="/images/2024-11-23-tossing-coin-and-trading/pdf-trading.webp" alt="KODEX 헬스케어 트레이딩 결과의 사후 확률 밀도 함수">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 KODEX 헬스케어 트레이딩 결과의 사후 확률 밀도 함수; 사전 확률 밀도 함수는 균일하다고 가정했다.</span>
</p>

승률이 X 이상일 확률은 위의 그래프를 구간[X,1]에서 적분해서 얻어진다. 아래의 표는 그렇게 얻은 승률별 확률을 나타낸다. 이 트레이딩은 승률이 60%가 넘을 확률이 97.5%이고, 65% 부터는 급감해서 70%가 넘을 확률을 거의 없다. 

*표 2: 승률이 X 이상일 확률*

|승률| 확률 |
|:---:|:---:|
|50% | 99.99% |
|55% | 99.99% |
|60% | 97.5% |
|65% | 20.38% |
|70% | 0.01% |

## 빈도주의 접근법
다시 KDOEX 헬스케어의 결과를 가져오면, 725번의 트레이딩에서 461번 이겼으므로, 승률의 추정값은 0.636이다. 

최대 추정오차는 $E=Z/2\sqrt{725}$ 이므로, 승률(r)의 범위는 신뢰도에 따라서 다음과 같다.

\- E=0.0185, 신뢰도 68.27% (Z=1)  

$61.75\%<r<0.65.45\%$

\- E=0.0371, 신뢰도 95.45% (Z=2) 

$59.89\%<r<67.31\%$

\- E=0.0612, 신뢰도 99.90% (Z=3.3) 

$57.48\%<r<69.72\%$

이 방법을 이용하면 신뢰도에 따른 최대/최소 승률의 범위를 얻을 수 있다.

## Appendix: 사후 확률 밀도 함수 파이썬 코드

```python
from matplotlib import pyplot as plt
import numpy as np
import my_colors
from scipy.special import comb


def prob(h,t,r):
    return comb(h+t,h)*r**h*(1-r)**t


def g(r):
    return 1


def pdf(h, t, r):
    p_array = np.linspace(0,1,100)
    dp = np.mean(np.diff(p_array))
    denom = 0
    for p in p_array:
        denom += prob(h, t, p)*g(p)*dp
    numer = prob(h, t, r)*g(r)

    return numer/denom

n = 725
h = int(0.636*725)
t = n-h

r_array = np.linspace(0,1,500)

pdf_ = []
for r in r_array:
    pdf_.append(pdf(h,t,r))

# BLOCK: Import modules for plot
plt.rcParams["font.family"] ="Times New Roman"
plt.rcParams["axes.unicode_minus"] = False

# Create a figure object
fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)

# Plot the data
ax.plot(r_array, pdf_,
        linestyle="-", linewidth=2, color=my_colors.color[0],
        marker="none", markersize=8, markerfacecolor="white", markevery=10,
        label="n=725, win=461, lose=264")

# Set legend and axis
# plt.legend() # Show the legends
plt.xticks(fontname="Times New Roman", fontsize=12)  # Rotate the xticks by 15 degree
plt.yticks(fontname="Times New Roman", fontsize=12) # Set the yticks
ax.grid(True) # Show grids

# Add texts
plt.title("Posterior probability density function",  fontdict={"fontsize":16, "fontweight": "normal"})
plt.xlabel("r", fontsize=16, color="black", fontname="Times New Roman")
plt.ylabel("pdf", fontsize=16, color="black", fontname="Times New Roman")

# Save figure and show
plt.tight_layout() # Tight layout
plt.savefig(f"pdf.png", dpi=300)
plt.show()

``` 

