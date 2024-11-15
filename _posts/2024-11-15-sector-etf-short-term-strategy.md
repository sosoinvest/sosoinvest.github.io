---
layout: single
title:  "국장에서 단타치기 가장 좋은 섹터"
description: 국장 섹터 ETF를 단타해서 성공할 수 있는 변동성 돌파전략 결과를 정리한 글
categories: 투자
tag: [주식,퀀트,백테스트,파이썬]
toc: true
author_profile: false
header:
 teaser: /images/2024-11-15-sector-etf-short-term-strategy/sector-total.webp
 og_image: /images/2024-11-15-sector-etf-short-term-strategy/sector-total.webp

# sidebar:
#     nav: "docs"
# search: true
---
국장에서 단타로 먹기 가장 좋은 섹터는 어디일까? 

지난 10년간의 주가 데이터를 기반으로 섹터별로 [변동성 돌파전략](/투자/volatility-break-out-strategy/)을 적용해봤다.

먼저 섹터에 대해 정리하고 출발하자.

# 섹터(Sector)
섹터(Sector)는 섹터는 유사한 비즈니스 특성, 경제적 특성, 또는 시장 특성을 공유하는 기업들의 그룹을 의미한다.

이렇게 섹터를 구분하는 목적은 경제 활동을 체계적으로 분류하고 분석하기 위함에 있다. 이를 통해 투자자들이 시장을 쉽게 이해하고 분석할 수 있다.

섹터는 대표적으로 GICS(Global Industry Classification Standard) 분류기준에 따라 11개(IT, 금융, 헬스케어, 소비재, 에너지, 산업재, 소재, 유틸리티, 부동산, 통신서비스, 필수소비재)로 구분된다. 국가별로 자체 구분체계가 있기도 한데, 세계 표준은 GICS다. 

각 섹터는 고유한 경제적 특성, 성장 동인, 위험 요소를 가진다. 그렇기 때문에 경제 주기에 따라 각 섹터의 성과가 다르게 나타날 수 있다.

이러한 특성 때문에 다양한 분야에서 섹터가 활용되고 있다. 대표적으로 투자자들은 섹터 분산을 통해 포트폴리오의 위험을 관리할 수 있고, 섹터의 성과를 통해 전반적인 경제 상황을 파악할 수도 있다. 또한 정부나 중앙은행은 경제정책 수립에 섹터별 분석을 이용하기도 한다.

## GICS(Global Industry Classification Standard)
[GICS는 1999년 MSCI와 S&P가 공동개발한 산업분류체계이다](https://www.msci.com/our-solutions/indexes/gics). 개발 당시에는10개 섹터로 시작했는데, 2016년에 부동산이 금융 섹터에서 분리되어 11번째 섹터로 추가되었다.

GICS는 고정된 것이 아니라 정기적으로 검토되어 시장 변화에 맞춰 조정된다. 떄문에 다양한 이유로 새로운 섹터가 생기기도 하고 기존의 섹터에 속한 기업의 리스트가 바뀌기기도 한다.

2024년 현재 기준으로 국장의 11개 섹터들의 특징을 정리하면 다음과 같다.

### 소재
2000년대 중국의 고성장 시기에 강세를 보였으며, 최근에는 2차전지 관련 소재 기업들의 성장이 두드러진다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/materials.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">경제 성장과 연동된 실적</td>
      <td style="padding: 10px;">경기 변동에 민감</td>
      <td style="padding: 10px;">포스코홀딩스</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">원자재 가격 상승 시 수혜</td>
      <td style="padding: 10px;">원자재 가격 변동성</td>
      <td style="padding: 10px;">현대제철</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">다양한 산업에 필수적</td>
      <td style="padding: 10px;">환경 규제 리스크</td>
      <td style="padding: 10px;">동국제강</td>
    </tr>
  </tbody>
</table>

### 필수소비재 
경기 방어적 특성으로 안정적인 흐름을 보이고 있으며, 최근 언택트 소비 확대로 온라인 유통 기업들의 성장이 두드러진다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/consumer-discretionary.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">안정적인 수요</td>
      <td style="padding: 10px;">낮은 성장성</td>
      <td style="padding: 10px;">농심</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">경기 방어적 특성</td>
      <td style="padding: 10px;">원자재 가격 변동 리스크</td>
      <td style="padding: 10px;">롯데칠성</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">브랜드 파워</td>
      <td style="padding: 10px;">경쟁 심화</td>
      <td style="padding: 10px;">빙그레</td>
    </tr>
  </tbody>
</table>

### 경기소비재
경제 성장기에 강세를 보이며, 특히 2000년대 이후 글로벌 브랜드로 성장한 기업들을 중심으로 꾸준한 성장세를 보이고 있다.

<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/consumer-staples.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">안정적인 수요</td>
      <td style="padding: 10px;">경기 변동에 민감 (자유소비재)</td>
      <td style="padding: 10px;">현대백화점</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">브랜드 파워</td>
      <td style="padding: 10px;">원자재 가격 변동 리스크</td>
      <td style="padding: 10px;">이마트</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">경기 방어적 특성</td>
      <td style="padding: 10px;">경쟁 심화</td>
      <td style="padding: 10px;">CJ제일제당</td>
    </tr>
  </tbody>
</table>

### 산업재
경제 성장기에 강세를 보이며, 특히 조선, 자동차 등 한국의 주력 산업 성장과 함께 발전해왔다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/industrials.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">경제 성장과 연동된 실적</td>
      <td style="padding: 10px;">경기 변동에 민감</td>
      <td style="padding: 10px;">현대중공업</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">다양한 산업 포트폴리오</td>
      <td style="padding: 10px;">원자재 가격 변동 리스크</td>
      <td style="padding: 10px;">두산중공업</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">기술 혁신 기회성</td>
      <td style="padding: 10px;">글로벌 무역 정책 영향</td>
      <td style="padding: 10px;">한국항공우주</td>
    </tr>
  </tbody>
</table>

### 에너지
국제 유가 변동에 민감하게 반응하며, 2000년대 중반 고유가 시기에 강세를 보였으나, 최근에는 신재생 에너지 기업들의 성장이 두드러진다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/energy.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">높은 배당 수익률</td>
      <td style="padding: 10px;">원자재 가격 변동성</td>
      <td style="padding: 10px;">S-Oil</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">원유 가격 상승 시 수혜</td>
      <td style="padding: 10px;">환경 규제 리스크</td>
      <td style="padding: 10px;">GS</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">필수 자원 산업</td>
      <td style="padding: 10px;">대체 에너지 위협</td>
      <td style="padding: 10px;">한국전력</td>
    </tr>
  </tbody>
</table>

### 유틸리티
안정적인 실적을 바탕으로 꾸준한 흐름을 보이고 있으며, 최근 ESG 투자 확대로 주목받고 있다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/utilities.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">안정적인 현금 흐름</td>
      <td style="padding: 10px;">성장성 제한</td>
      <td style="padding: 10px;">한국전력기술</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">높은 배당 수익률</td>
      <td style="padding: 10px;">규제 리스크</td>
      <td style="padding: 10px;">서울가스</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">경기 방어적 특성</td>
      <td style="padding: 10px;">금리 상승 시 불리</td>
      <td style="padding: 10px;">대성홀딩스</td>
    </tr>
  </tbody>
</table>

### IT
IT는 빠른 기술 혁신과 높은 성장 잠재력을 가진 섹터이다. 2000년대 초반 IT 버블 붕괴 이후 회복세를 보이며, 특히 2010년대 이후 삼성전자, SK하이닉스 등 대형주 중심으로 강세를 보이고 있다. 그러나 2020년 판데믹과 AI의 발달 이후 국제적으로 뒤쳐지는 모습을 보이고있다. 

<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/information-technology.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">높은 성장 잠재력과 혁신성</td>
      <td style="padding: 10px;">높은 변동성</td>
      <td style="padding: 10px;">SK하이닉스</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">디지털 전환 트렌드의 수혜</td>
      <td style="padding: 10px;">기술 변화에 따른 위험</td>
      <td style="padding: 10px;">네이버</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">높은 수익성</td>
      <td style="padding: 10px;">규제 리스크</td>
      <td style="padding: 10px;">카카오</td>
    </tr>
  </tbody>
</table>

### 통신서비스
1990년대 말~2000년대 초 이동통신 보급 확대 시기에 강세를 보였으며, 최근에는 5G 상용화로 다시 주목받고 있다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/communication-services.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">안정적인 현금 흐름</td>
      <td style="padding: 10px;">높은 설비 투자 비용</td>
      <td style="padding: 10px;">SK텔레콤</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">필수 서비스 산업</td>
      <td style="padding: 10px;">규제 리스크</td>
      <td style="padding: 10px;">LG유플러스</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">5G 등 신기술 성장 기회</td>
      <td style="padding: 10px;">경쟁 심화</td>
      <td style="padding: 10px;">KT</td>
    </tr>
  </tbody>
</table>

### 헬스케어
2010년대 이후 바이오 기업들의 성장으로 주목받기 시작했으며, 특히 코로나19 팬데믹 이후 더욱 강세를 보이고 있다.

<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/health-care.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">인구 고령화에 따른 수요 증가</td>
      <td style="padding: 10px;">규제 리스크</td>
      <td style="padding: 10px;">셀트리온</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">경기 방어적 특성</td>
      <td style="padding: 10px;">연구개발 비용 부담</td>
      <td style="padding: 10px;">유한양행</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">높은 진입 장벽</td>
      <td style="padding: 10px;">특허 만료에 따른 위험</td>
      <td style="padding: 10px;">녹십자</td>
    </tr>
  </tbody>
</table>

### 금융
경제 성장과 밀접하게 연관된 섹터로, 1997년 외환위기와 2008년 글로벌 금융위기 때 큰 타격을 받았지만, 이후 꾸준한 회복세를 보이고 있다. 최근 기준금리인상과 벨류업 정책으로 수혜를 입었다.

<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/financials.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">안정적인 배당 수익</td>
      <td style="padding: 10px;">경기 변동에 민감</td>
      <td style="padding: 10px;">신한지주</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">금리 상승기에 수혜</td>
      <td style="padding: 10px;">규제 리스크</td>
      <td style="padding: 10px;">하나금융지주</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">경제 성장과 연동된 실적</td>
      <td style="padding: 10px;">금융 위기 시 큰 타격</td>
      <td style="padding: 10px;">삼성생명</td>
    </tr>
  </tbody>
</table>

### 부동산
한국의 부동산 시장 변화와 밀접하게 연관되어 움직이며, 2000년대 이후 리츠(REITs) 상장으로 투자 접근성이 높아졌다.
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color: #51555d; border-bottom: 2px solid #ddd;">
      <th style="padding: 10px;"></th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">장점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">단점</th>
      <th style="padding: 10px; text-align: center;font-weight: bold;">대표종목</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #ddd;">
      <td rowspan="3" style="padding: 10px;">
        <img src="/images/2024-11-15-sector-etf-short-term-strategy/real-estate.webp" alt="IT sector icon" width="100" />
      </td>
      <td style="padding: 10px;">안정적인 임대 수익</td>
      <td style="padding: 10px;">금리 변동에 민감</td>
      <td style="padding: 10px;">신한알파리츠</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">인플레이션 헤지</td>
      <td style="padding: 10px;">경기 변동 리스크</td>
      <td style="padding: 10px;">롯데리츠</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
      <td style="padding: 10px;">높은 배당 수익률</td>
      <td style="padding: 10px;">지역별 편차</td>
      <td style="padding: 10px;">맥쿼리인프라</td>
    </tr>
  </tbody>
</table>

## 섹터 ETF

*표 1: 섹터 ETF*

| 구분 | ETF종목명 | 종목코드 | 기초지수 | 상장일 |
|:---:|:---:|:---:|:---:|:---:|
| 소재 | KODEX 철강 | 117680 | KRX Steel | 2009.10.30 | 
| 필수소비재 | KODEX 필수소비재 | 266410 | KRX 필수소비재 | 2017.03.28 |
| 경기소비재 | TIGER200 경기소비재 | 139290  | KOSPI200 경기소비재| 2011.04.06|
| 산업재 | TIGER200 산업재 | 227550 | KOSPI200 산업재  | 2015.09.23 |
| 에너지  | TIGER200 에너지화학  | 117460  | KRX Enegy&Chemicals  | 2009.10.12 |
| 유틸리티 | KODEX 운송 | 140710 | KRX Transportation | 2011.04.26 |
| IT | TIGER200 IT | 139260 | KOSPI200 정보기술  | 2011.04.06 |
| 통신서비스  | TIGER 방송통신 | 098560 | KRX Media&Telecom | 2007.09.07 |
| 헬스케어 | TIGER 헬스케어 | 143860 | KRX Health Care | 2011.07.18 |
| 금융  | TIGER200 금융 | 139270 | KOSPI200 금융 | 2011.04.06 |
| 부동산  | TIGER 리츠부동산인프라 | 329200 | FnGuide 부동산인프라고배당지수 | 2019.07.19 |

위의 표는 각 섹터별로 대표적인 국장 ETF를 선정하여 정리한 것이다. 일부 섹터의 경우 여러 ETF가 존재할 수 있으며, 여기서는 각 섹터를 대표하는 ETF를 선정했다. 관심가는 섹터에 투자하고 싶으면 위에 정리한 ETF를 매수하면 된다.

### 섹터 ETF에 투자하면 좋은 점
섹터 ETF에 투자하면 다음과 같은 장점이 있다. 
먼저 경기 상황에 따라 수혜를 받는 섹터와 그렇지 못한 섹터 간 수익률 차이가 발생할 때 유리한 섹터에 집중 투자할 수 있다. 

회복기, 확장기, 둔화기, 침체기 등 경기 사이클별로 유리한 섹터가 있는데, 여기에 맞춰서 전략적으로 투자할 수 있다. 마지막으로 시장 상황에 따라 섹터의 비중을 조정하며 유연하게 투자할 수 있다.


# 백테스트 조건
- 백테스트 대상: [KODEX 철강](https://m.stock.naver.com/domestic/stock/117680/total), [KODEX 필수소비재](https://m.stock.naver.com/domestic/stock/266410/total), [TIGER200 경기소비재](https://m.stock.naver.com/domestic/stock/139290/total), [TIGER200 산업재](https://m.stock.naver.com/domestic/stock/227550/total), [TIGER200 에너지화학](https://m.stock.naver.com/domestic/stock/117460/total), [KODEX 운송](https://m.stock.naver.com/domestic/stock/140710/total), [TIGER200 IT](https://m.stock.naver.com/domestic/stock/139260/total), [TIGER 방송통신](https://m.stock.naver.com/domestic/stock/098560/total), [TIGER 헬스케어](https://m.stock.naver.com/domestic/stock/143860/total), [TIGER200 금융](https://m.stock.naver.com/domestic/stock/139270/total), [TIGER 리츠부동산인프라](https://m.stock.naver.com/domestic/stock/329200/total)
: *국장에 상장된 GICS 산업분류체계의 11개 섹터 ETF를 대상으로했다.

- 백테스트 기간: 2014.11.11 ~ 2024.11.12
: *최근 10년 (ETF가 상장한지 10년이 되지 않은 경우에는 상장일부터 2024.11.12까지를 기간으로 잡았다.)

- 세금: 0%
: *거래세와 ETF의 배당소득세는 계산에서 제외했다.

- 거래 수수료: 0%
: *거래수수료는 계산에서 제외했는데, 증권사들이 경쟁적으로 수수료를 내리고 있어서 거의 영향을 미치지 않는다.

## 계산 조건
변동성 돌파전략의 매매조건은 아래와 같다.

<div class="notice--primary">
<ul>
    <li style="font-size: 1.25em;">전일 고가에서 저가를 빼서 변동폭을 구한다.</li>
    <li style="font-size: 1.25em;">시가+K*변동폭으로 타겟 매수가를 정하고, 오늘 장중 가격이 이 가격을 초과하면 매수한다.</li>
    <li style="font-size: 1.25em;">다음날 시가에 모두 매도한다.</li>
</ul>
</div>

변동성 돌파전략은 이미 이전에 많이 다뤘기 때문에 간략하게 정리하고만 넘어간다. 자세한 것은 다음 글들을 참고하기 바란다.

- **[래리 윌리엄스의 변동성 돌파전략 (파이썬 코드 있음)](/투자/volatility-break-out-strategy/)**
- **[절대로 지지않는 롱 전략](/투자/never-losing-long-strategy)**
- **[곱버스를 우상향시키는 방법](/투자/upward-sloping-inverse-double)**

# 백테스트 결과
아래의 표는 백테스트한 모든 ETF에 최근 10년간(2014.11.11~2024.11.12) 변동성 돌파전략을 적용한 결과이다. 여기서는 K값은 0.5로 고정한 후 섹터 ETF간의 결과를 비교했다.

*표 1: 변동성 돌파전략 백테스트 결과 (K=0.5)*

| 구분 | 소재 | 필수소비재 | 경기소비재 |산업재 |에너지 |유틸리티 |IT |통신서비스 |헬스케어 |금융 |부동산|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 최종 수익률 | <span style="color: red;">596.7%</span> | <span style="color: red;">376.9%</span> | <span style="color: red;">943.4%</span> |<span style="color: red;">598.5%</span> |<span style="color: red;">1000.9%</span> |<span style="color: red;">421.3%</span> |<span style="color: red;">570.2%</span> |<span style="color: red;">505.2%</span> |<span style="color: red;">1501.4%</span> |<span style="color: red;">664.3%</span> |<span style="color: red;">117.8%</span> |
| Buy and hold | <span style="color: red;">19.8%</span> | <span style="color: blue;">-28.2%</span> | <span style="color: blue;">-2.3%</span> |<span style="color: red;">7.0%</span> |<span style="color: red;">74.8%</span> |<span style="color: red;">15.4%</span> |<span style="color: red;">104.6%</span> |<span style="color: blue;">-2.7%</span> |<span style="color: red;">176.1%</span> |<span style="color: red;">66.2%</span> |<span style="color: red;">7.1%</span> |
| CAGR | 20.2% | 23.1% | 25.7% | 23.5% | 26.4% | 16.8% | 20.7% | 19.9% | 30.9% |22.3% |16.2% |
| MDD | -23.0% | -5.3% | -9.7% | -9.8% | -11.0% | -21.2% | -11.9% | -7.0% | -11.4% | -13.6% | -3.4% |
| 매매일수  | 690 | 475 | 684 | 577 | 700 | 696 | 712 | 608 | 725 | 658 | 306 |
| 승률  | 58.0% | 64.8% | 61.1% | 62.6% | 61.9% | 57.5% | 62.4% | 61.5% | 63.6% |63.1% |68.3% |
| 수익 시 평균 수익률 | 1.14% | 0.84% | 1.00% |1.04% | 1.13% | 1.05% | 0.90% | 0.83% |1.20% |0.94% |0.51% |
| 손해 시 평균 손실률  | -0.95% | -0.66% | -0.74% | -0.91% | -0.98% | -0.94% | -0.80% | -0.60% | -1.09% | -0.81% | -0.37% |
| RR비율 | 1.20 | 1.27 | 1.35 | 1.14 | 1.15 | 1.12 | 1.12 | 1.38 | 1.10 | 1.16 | 1.38 |
| 샤프지수  | 1.53 | 2.79 | 2.15 | 2.17 | 2.19 | 1.30 | 2.13 | 2.57 | 2.27 | 2.15 | 3.09 |
| 샤프지수(Buy and hold)  | -0.19 | -0.41 | -0.22 | -0.18 | -0.05 | -0.20 | 0.11 | -0.18 | 0.04 | 0.03 | -0.03 |

결과를 보면, KODEX 인버스는 최종 수익률이 -13.3%로 손실을 기록했지만, KODEX 200선물 인버스 2X와 KODEX 코스닥 선물 인버스는 각각 34.4%와 79.3%의 수익을 냈다. KODEX 인버스가 손실을 기록하긴 했지만, 매수 후 보유 전략(Buy and Hold)과 비교했을 때는 모든 경우에서 더 나은 성과를 보였다.

연평균 복리 수익률(CAGR)을 보면, KODEX 인버스는 -2.1%, KODEX 200선물 인버스 2X(곱버스)는 0.8%, KODEX 코스닥 선물 인버스는 6.0%로, KODEX 코스닥 선물 인버스의 성과가 가장 높았다. 코스피보다 코스닥의 성과가 더 높은 이유는 지난 10년간 코스닥의 변동성이 코스피보다 더 컸기 때문으로 보인다.

그림을 보면, KODEX 인버스와 곱버스의 손실은 대부분 2022년부터 최근 2년 사이에 발생했다. 이 기간 동안 코스피 지수는 2500선에서 크게 오르지도 내리지도 않았는데도 손실이 발생한 것을 보면, 변동성이 큰 장세에서는 숏 포지션으로 수익을 내기가 쉽지 않다는 것을 알 수 있다. 이는 주가가 하락하는 추세는 비교적 짧게 유지되는 반면, 상승하는 추세는 더 오래 지속되는 경향 때문으로 보인다. 

상승 추세는 길고 하락 추세는 짧다는 설명은 아래의 격언과 들어맞는 결과이다.
>["상승할 때는 쌓아 올리고 하락할 때는 무너진다"](/투자/trading-edge-book-in-out-rule/#매수-밖에-하지-못하는-시장과-종목)

최대 낙폭(MDD)을 살펴보면, 코스피, 코스닥, 곱버스 모두 약 30% 수준으로 비슷한 수준의 손실 위험을 보였다.

승률은 코스피에서 약 45%, 코스닥에서 약 50%로, 코스닥이 더 나은 성과를 보였다. 50% 이하의 승률에서 수익을 내려면 [RR 비율(=평균 수익률/평균 손실률)](/투자/trading-edge-book)이 약 1.1 이상이어야 하는데, KODEX 인버스는 이 조건을 충족하지 못했다.

샤프지수는 전부 1미만으로 형편없었다. 

아래의 그림은 모든 백테스트 결과를 종합한 것이다. 

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/sector-total.webp" alt="11개 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 11개 섹터 백테스트 결과; K는 0.5로 모두 동일하다. </span>
</p>

## 소재

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-materials.webp" alt="소재 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 2 백테스트 결과: 소재 섹터 </span>
</p>

## 필수소비재

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-consumer-discretionary.webp" alt="필수소비재 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 3 백테스트 결과: 필수소비재 섹터 </span>
</p>

## 경기소비재

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-consumer-staples.webp" alt="경기소비재 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 4 백테스트 결과: 경기소비재 섹터 </span>
</p>

## 산업재

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-industrials.webp" alt="산업재 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 5 백테스트 결과: 산업재 섹터 </span>
</p>

## 에너지

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-materials.webp" alt="소재 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 6 백테스트 결과: 소재 섹터 </span>
</p>

## 유틸리티

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-utilities.webp" alt="유틸리티 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 7 백테스트 결과: 유틸리티 섹터 </span>
</p>

## IT

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-it.webp" alt="IT 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 8 백테스트 결과: IT 섹터 </span>
</p>

## 통신서비스

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-communication-services.webp" alt="통신서비스 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 9 백테스트 결과: 통신서비스 섹터 </span>
</p>

## 헬스케어

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-health-care.webp" alt="헬스케어 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 10 백테스트 결과: 헬스케어 섹터 </span>
</p>

## 금융 

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-financials.webp" alt="금융 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 11 백테스트 결과: 금융 섹터 </span>
</p>

## 부동산

<p align="center">   
    <img src="/images/2024-11-15-sector-etf-short-term-strategy/result-real-estate.webp" alt="부동산 섹터 백테스트 결과">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 12 백테스트 결과: 소재 섹터 </span>
</p>

# 결론
백테스트 결과를 요약하자면,
- 롱 전략과 달리, 숏에 변동성 돌파 전략을 적용했을 때는 손실이 발생할 수 있다.
- 그 이유는 하락 추세는 상승 추세보다 상대적으로 짧게 유지되기 때문이다.
- 전략의 최종 수익과 손실은 K값에 따라 달라지지만, 그 결과는 일관적이지 않았다.
- 코스닥 인버스에 적용했을 때 가장 좋은 성과를 보였으며, 이때 최적의 K값은 0.4였다.
- 모든 경우에서 매수 후 보유 전략보다 샤프 지수는 높았고 최대 낙폭(MDD)은 낮았다.
- 전략의 성과가 고르지 못한 이유는 국내 주식시장의 지수가 일관된 추세를 보이지 않고 변동성이 크기 때문인 것으로 보인다.