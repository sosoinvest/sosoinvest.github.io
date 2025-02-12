---
layout: single
title:  "[투자전략-17] 섹터 ETF 변동성 돌파전략 최적의 변동폭 값 찾기"
description: 섹터 ETF에 변동성 돌파전략을 적용할 때 최적의 변동폭 값에 대해 정리한 글
categories: 투자
tag: [주식, 퀀트]
toc: true
author_profile: false
header:
 teaser: /images/2025-02-13-best-vol-definition-for-sector-etf/vol-band-cagr.webp
 og_image: /images/2025-02-13-best-vol-definition-for-sector-etf/vol-band-cagr.webp
# sidebar:
#     nav: "docs"
# search: true
---
이 글에서는 변동성 정의에 따른 섹터 ETF의 성과를 비교했다. 변동성 돌파 전략에서 언급되는 변동성은 일반적으로 전일의 고가와 저가 차이를 기준으로 정의된다. 그러나 이 계산 방법은 수학적으로 엄밀히 정의된 것이 아니며, 다양한 방식으로 변동성을 측정할 수 있다.

본 글에서는 OHLC(Open, High, Low, Close) 데이터를 활용해 네 가지 변동성 정의를 제시하고, 이를 바탕으로 섹터 ETF를 대상으로 한 변동성 돌파 전략의 매매 성과를 분석했다. 각 변동성 계산 방식이 실제 전략 성과에 미치는 영향을 비교함으로써, 투자자들이 전략을 보다 효과적으로 활용할 수 있는 통찰을 제공하고자 한다.

**변동성 정의**
1. 전일 고가 - 전일 저가
2. 전일 시가 - 전일 저가
3. 전일 고가 - 전일 시가
4. True range =max(전일 고가 - 전일 저가, abs(전일 고가-전전일 종가), abs(전일 저가-전전일종가)) 

돌파전략의 로직은 이미 많이 다뤘으므로, 자세한 내용은 다음 글들을 참고하기 바란다. 특히, [국장에서 단타치기 가장 좋은 섹터](/투자/sector-etf-short-term-strategy)는 이 글에서 다루는 11가지 섹터 etf의 백테스트 성과를 다루고 있으므로 참고할만하다.

- [래리 윌리엄스의 변동성 돌파전략 (파이썬 코드 있음)](/투자/volatility-break-out-strategy/)
- [절대로 지지않는 롱 전략](/투자/never-losing-long-strategy)
- [곱버스를 우상향시키는 방법](/투자/upward-sloping-inverse-double)
- [변동성 돌파전략 포지션 청산방법의 효과](/투자/vol-brk-out-close-method)
- [변동성 정의에 따른 돌파전략 성과](/투자/vol-definition)

# 백테스트 결과
백테스트에서는 etf의 상장일부터 2025년 2월 현재까지의 기간을 고려했다. 세금은 없고 수수료는 한국투자증권의 국장 거래수수료인 0.0036%를 고려했다.

## CAGR
<p align="center">   
    <img src="/images/2025-02-13-best-vol-definition-for-sector-etf/vol-band-cagr.webp" alt="변동성 정의에 따른 섹터 ETF들의 CAGR">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 CAGR</span>
</p>
고가-저가(High-Low)로 정의한 변동성보다 고가-시가(High-Open), 시가-저가(Open-Low)로 정의한 변동성이 더 높은 CAGR을 기록했다. 전반적으로 가장 성과가 좋은 변동성 정의는 고가-시가(High-Open)이고, 가장 성과가 저조한 것은 True Range로 나타났다.

고가와 시가의 차이로 정의한 변동성이 더 좋은 이유는 두 가지로 설명할 수 있다.
- 첫 번째로, 전일의 장 시작부터 종료까지 하락하는 날에는 시가와 고가의 차이가 좁아진다. 이 경우, 다음 날 가격이 시가보다 조금만 오르더라도 매매가 이루어지므로, 폭락 후 반등하는 상황에서 빠르게 진입할 수 있다.
- 두 번째로, 고가-저가로 정의한 변동성보다 값이 절반 수준으로 작기 때문에, 추세에 더 빨리 진입할 수 있으며, 이로 인해 수익의 폭을 늘릴 수 있다.

## MDD
<p align="center">   
    <img src="/images/2025-02-13-best-vol-definition-for-sector-etf/vol-band-mdd.webp" alt="변동성 정의에 따른 섹터 ETF들의 MDD">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 MDD</span>
</p>
전반적으로 MDD는 True Range와 고가-저가(High-Low)로 정의한 변동성에서 더 작았다. 반면, 고가-시가(High-Open) 또는 시가-저가(Open-Low)로 정의한 변동성은 조기에 진입해 큰 수익을 추구할 수 있는 장점이 있지만, 신호의 신뢰도가 떨어지는 상황에서도 진입해야 하므로 손실이 더 큰 경향이 있다.
