###############################################################################################################################################################
#AI 개발 실무 1차 레포트과제
#---------------------------
#
# 상장 기업의 재무제표를 크롤링하여 당기순이익 증감률 구하기
#
# 5주차 실습 자료를 참고하여,
# 상장기업 중 3곳을 선택하여 전년도 대비 당기순이익 증감률을 구하고, 증감률이 높은 순으로 내림차순 정렬하시오.
#
# 대상 데이터 (예: 삼성전자 :  http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN=
#
#과제 상세 설명:
#---------------
#1. 상장 기업 3곳의 재무제표를 Pandas 데이터 프레임으로 적재
#2. 전년도 대비 당기 순이익 증감률 계산
#3. 3 곳의 당기 순이익 증감률을 파이썬 Pandas Series로 적재
#4. 당기 순이익의 증감률이 높은 순으로 내림차순 정렬 뒤 출력
#
#과제 조건
#---------
#1. 과제를 수행했던 코드와 결과화면의 캡처본이 모두 word 파일에 있어야 함 (모두 제출했다면 100점)
#2. 워드 파일이 제출되지 않으면 이것을 압축하여 zip파일로 업로드하여도 됨
#3. 절대로 타인과 과제를 공유하지 말 것 (캡처본 파일을 검사하여 동일 파일일 경우 0점 처리)
#6. 과제를 제대로 수행하지 못했지만, 제출만 했을 경우, 제출 점수 20점
#
#과제 기한 : 4월 8일 23시 55분까지
#힌트 : 6주차 강의
###############################################################################################################################################################

import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

#종목 리스트 = {'종목명' : '종목코드'}
stock_codes = {
               '삼성전자': 'A005930',
               'SK하이닉스': 'A000660',
               'LG에너지솔루션': 'A373220'
              }

#
# 증권종목 요청 URL 생성
#
def make_url(stock_code):
    url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=' + stock_code + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN='
    return url

#
# 증권종목에 대한 당기순이익 증감률 산출
#
def find_current_incomming_rate(stock_code):
    url = make_url(stock_code)

    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    current_incomming_rate = get_current_incomming_rate(soup)

    return current_incomming_rate

#
# 당기순이익 증감률 parsing
#
def get_current_incomming_rate(soup):
    current_incomming_0 = soup.select('#highlight_D_A > table> tbody > tr:nth-of-type(4) > td:nth-child(4)')
    current_incomming_1 = soup.select('#highlight_D_A > table> tbody > tr:nth-of-type(4) > td:nth-child(5)')
    current_incomming_rate = (int(current_incomming_1[0].string.replace(",", "")) - int(current_incomming_0[0].string.replace(",", ""))) / int(current_incomming_0[0].string.replace(",", "")) * 100.

    return current_incomming_rate

#
# 종목리스트에 대한 당기순이익 증가율 산출
#
def call_incomming_rate(stock_codes):
    results = []   
    for stock_name, stock_code in stock_codes.items():
        curr_inc_rate = find_current_incomming_rate(stock_code)
        results.append([stock_code, stock_name, curr_inc_rate])

    column_name = ['stock_name', 'stock_code', 'incomming_rate']
    df = pd.DataFrame.from_records(results, columns=column_name)
    return df

response_df = call_incomming_rate(stock_codes)
print(response_df.sort_values('incomming_rate'))
