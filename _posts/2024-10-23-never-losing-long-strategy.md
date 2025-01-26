---
layout: single
title:  "[투자전력] 절대로 지지않는 롱 전략 (5)"
description: 한국, 미국, 일본, 중국, 유럽 주식 시장에서 절대지지 않는 롱 매매 전략을 분석한 글
categories: 투자
tag: [주식,퀀트,백테스트,파이썬]
toc: true
author_profile: false
header:
 teaser: /images/2024-10-23-never-losing-long-strategy/result-kospi200.webp
 og_image: /images/2024-10-23-never-losing-long-strategy/result-kospi200.webp

# sidebar:
#     nav: "docs"
# search: true
---
전 세계 주식시장에서 절대 지지않은 롱 매매 전략을 알아보자.

이 글은 한국, 중국, 일본, 미국, 유럽 주식시장의 지난 10년간 데이터를 바탕으로 [변동성 돌파전략](/투자/volatility-break-out-strategy/)을 적용한 백테스트 결과를 다룬다. 놀랍게도 이 단순한 매매 전략은 모든 시장에서 손실을 보지 않았으며, 심지어 우상향한 미국 시장은 물론, 우하향한 중국 시장과 박스피에 갇힌 한국, 유럽 시장에서도 높은 수익을 기록했다.

# 백테스트 조건
- 백테스트 대상: 한국(코스피200), 중국(항셍), 일본(Nikkei225), 미국([S&P500](/투자/snp-historical-return-since-1871), [Nasdaq100](nasdaq100-since-1985)), 유럽(Eurostoxx50) 
: *지수를 대상으로 잡은 이유는 실적과 산업의 시황의 위험에 노출된 개별주 보다는 전체 시장을 평균한 값으로, 급등락의 영향을 피할 수 있기 떄문이다. 지수 데이터는 야후파이낸스에서 불러왔다. 코스닥150 지수는 야후파이낸스에 없어서 백테스트에서 제외하였다.

- 백테스트 기간: 2014.10.23 ~ 2024.10.18
: *최근 10년

- 세금: 0%
: *투자 방법마다 세금이 달라질 수 있기 때문에 공평한 비교를 위해 고려하지 않았다.

- 거래 수수료: 0%
: *국내주식과 해외주식의 수수료가 다르기 때문에 공평한 비교를 위해 고려하지 않았다.

## 계산 조건
변동성 돌파전략의 매매조건은 아래와 같다. 

<div class="notice--primary">
<ul>
    <li style="font-size: 1.25em;">전일 고가에서 저가를 빼서 변동폭을 구한다.</li>
    <li style="font-size: 1.25em;">시가+K*변동폭으로 타겟 매수가를 정하고, 오늘 장중 가격이 이 가격을 초과하면 매수한다.</li>
    <li style="font-size: 1.25em;">다음날 시가에 모두 매도한다.</li>
</ul>
</div>

K값은 0.5로 동일하게 사용했다. 

[백테스트 코드 구성의 자세한 내용은 지난글을 참고바란다.](/투자/volatility-break-out-strategy/)

# 백테스트 결과
아래의 표는 계산에 고려한 모든 주식시장의 최근 10년간(2014.10.23~2024.10.18) 변동성 돌파전략을 적용한 결과이다. 

*표 1: 변동성 돌파전략 백테스트 결과*

| 구분 | KOSPI200 | HSI | Nikkei225 | S&P500 | NASDAQ100 | EUROSTOXX 50 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 최종 수익률 | <span style="color: red;">110.3%</span> | <span style="color: red;">177.9%</span> | <span style="color: red;">93.9%</span> | <span style="color: red;">86.0%</span> | <span style="color: red;">124.3%</span> | <span style="color: red;">78.7%</span> |
| Buy and hold | <span style="color: red;">41.9%</span> | <span style="color: blue;">-10.8%</span> | <span style="color: red;">157.5%</span> | <span style="color: red;">200.6%</span> | <span style="color: red;">406.6%</span> | <span style="color: red;">63.8%</span> |
| CAGR | 7.3% | 10.0% | 6.2% | 5.8% | 7.2% | 5.3% |
| MDD | -13.1% | -13.7% | -10.9% | -14.8% | -17.2% | -13.3% |
| 매매일수  | 712 | 708 |  758 | 775 | 799 | 802 |
| 승률  | 57.2% | 57.8% | 54.5% | 58.7% | 59.5% | 54.6% |
| 수익 시 평균 수익률 | 0.66% | 0.83% |  0.76% | 0.54% | 0.73% | 0.59% |
| 손해 시 평균 손실률  | -0.65% | -0.82% | -0.73% | -0.60% | -0.85% | -0.57% |
| 샤프지수  | 0.94 | 1.03 | 0.70 | 0.79 | 0.68 | 0.68 |
| 샤프지수(Buy and hold)  | 0.03 | -0.26 | 0.27 | 0.45 | 0.54 | 0.06 |

백테스트 결과, 모든 주식시장에서 최종 수익률이 마이너스가 된 경우는 없었다. 가장 좋은 성과를 낸 시장은 중국으로, 177.9%의 수익을 올렸다. 반면 가장 저조한 성과는 유럽 시장으로, 78.7%의 수익률을 기록했다. 한국 코스피도 110.3%의 수익률로 괜찮은 성과를 보였다.

특히 한국, 중국, 유럽 시장에서는 매수 후 보유(Buy and Hold) 전략보다 변동성 돌파전략이 더 높은 수익률을 보였다. 중국 항셍지수는 10년간 -10%로 하락했지만, 변동성 돌파전략을 적용한 결과는 오히려 가장 높은 수익을 기록했다.

각 시장의 MDD(최대 손실 폭)를 살펴보면, 한국, 중국, 유럽 모두 약 13% 수준으로 비슷했고, 일본이 10.9%로 가장 낮았으며, 미국의 S&P500은 14.8%, Nasdaq100은 17.2%로 다소 높았다.

승률은 모든 주식시장에서 54% 이상으로, 매매 횟수의 절반 이상이 성공적인 거래였다. 샤프지수는 중국이 1.03으로 가장 높았고, 그 뒤를 한국이 따랐으며 나머지 시장들은 비슷한 수준이었다. 중요한 점은 매수 후 보유 전략의 샤프지수와 비교했을 때, 모든 시장에서 변동성 돌파전략의 샤프지수가 더 높았다는 것이다. 특히 한국과 유럽은 샤프지수가 거의 0에 가까웠고, 중국은 오히려 마이너스였으나 변동성 돌파전략의 결과는 훨씬 우수했다. 우상향한 일본과 미국 시장에서도 변동성 돌파전략이 매수 후 보유보다 샤프지수가 높았다.

아래의 그림은 모든 백테스트 결과를 종합하여 보여준다. 미국, 일본은 물론 한국, 중국, 유럽 모두 우상향하는 모습을 보인다.

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-in-total.webp" alt="전체 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 백테스트 결과 종합; 한국, 미국, 일본, 중국, 유럽 </span>
</p>

## 한국
한국의 코스피200은 지난 10년간 크게 오르지도, 내리지도 않은 박스권에 머물렀지만, 변동성 돌파전략은 꾸준히 우상향했다.

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-kospi200.webp" alt="코스피200의 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 코스피200의 백테스트 결과 </span>
</p>

## 미국
미국의 S&P500과 Nasdaq100은 10년간 꾸준히 상승했으나, 변동성 돌파전략은 2020년 이후 급등 구간에서 지수 대비 언더퍼폼했다. 이는 변동성 돌파전략이 급등하는 시장에서는 성과가 다소 제한적임을 보여준다. 

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-snp500.webp" alt="S&P500의 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 S&P500의 백테스트 결과 </span>
</p>

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-nasdaq100.webp" alt="Nasdaq100의 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 Nasdaq100의 백테스트 결과 </span>
</p>

## 일본
일본의 Nikkei225도 미국과 유사하게 꾸준히 상승해왔으며, 변동성 돌파전략도 지수를 따라왔지만 최근 급등장에서는 지수에 뒤처졌다.

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-nikkei225.webp" alt="Nikkei225의 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 Nikkei225의 백테스트 결과 </span>
</p>

## 중국
반면 중국의 항셍지수는 지난 10년간 우하향했지만, 변동성 돌파전략은 지수와 상관없이 우상향했다. 이 결과는 인버스 ETF에 전략을 적용해도 좋은 성과를 낼 수 있다는 가능성을 보여준다.

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-hsi.webp" alt="항셍지수(HSI)의 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 6 항셍지수(HSI)의 백테스트 결과 </span>
</p>

## 유럽
유럽도 10년간 미약하게 우상향했지만, Eurostoxx50에 적용한 변동성 돌파전략은 대체로 지수를 따라갔고, 최근에는 약간 더 나은 성과를 보였다.

<p align="center">   
    <img src="/images/2024-10-23-never-losing-long-strategy/result-eurostoxx50.webp" alt="Eurostoxx50의 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 7 Eurostoxx50의 백테스트 결과 </span>
</p>

# 결론
요약하자면,
- 변동성 돌파전략은 백테스트한 어느 시장에서도 손실을 보지 않았다.
- 변동성이 큰 시장에서 시장을 초과하는 수익을 올렸다.
- 우상향한 시장에서는 지수보다 다소 낮은 수익률을 기록했다.
- 급등하는 시장에서는 변동성 돌파전략이 지수를 따라가지 못하는 경향이 있다.
- 모든 시장에서 매수 후 보유 전략보다 샤프지수가 뛰어나다.

다른 지역의 모든 주식시장에서 변동성 돌파전략이 효과적이었다는 점은 매우 놀라운 결과다. 확률론에서 '[에르고딕성(Ergodic)](https://namu.wiki/w/%EC%97%90%EB%A5%B4%EA%B3%A0%EB%94%95%20%EA%B0%80%EC%84%A4)'이라는 개념이 이를 설명할 수 있다. 에르고딕성은 시간 평균과 공간 평균이 일치하는 특성을 말하며, 여기서 '공간'은 물리적 공간을 넘어 가능한 모든 상태를 포괄하는 개념이다. 즉, 특정 시스템의 장기적인 시간 평균이 그 시스템의 모든 가능한 상태를 고려한 평균인 앙상블(Ensemble) 평균과 동일하다는 의미다.

이 개념을 변동성 돌파전략에도 적용할 수 있을 것이다. 여러 주식시장에서 유효했던 전략이 한 시장에서도 장기적으로 성공할 수 있다는 뜻이다. 이번 분석 결과는 변동성 돌파전략이 에르고딕성을 가진다는 것을 시사하며, 이는 주식시장이 열려 있는 한, 미래에도 이 전략이 효과적일 가능성이 크다는 점을 보여준다.