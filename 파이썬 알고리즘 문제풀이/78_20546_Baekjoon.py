'''
백준 20546번 기적의 매매법 - 구현
준현 : 주식을 살 수만 있다면 무조건 많이 삼
성민 : 주식 거래 프로그램 - 33 매매법 이용, 전량 매수 or 전량 매도로 이루어짐. 
3일 연속 가격이 전일 대비 상승 시 -> 다 팔아버림 [전량 매도] (동일한건 상승으로 안침)
3일 연속 가격이 저전일 대비 하락 시 -> 다 사버림 [전량 매수] (동일한건 하락으로 안침)
14일동안 주가가 주어짐

14일 후 누가 더 높은 자산을 가지고 있는지 비교해서 이긴 사람 출력

J-준현 이김 : BNP 출력
S-성민 이김 : TIMING 출력
둘이 비김 : SAMESAME 출력

자산 : 현금 + (마지막 14일날의 주가 * 보유 주식수)

--
입력
첫째줄 :준현이와 성민이에게 주어진 현금 수
둘째줄 : 14일 간의 MachineDuck의 주가
100
10 20 23 34 55 30 22 19 12 45 23 44 34 38
'''
import sys

input = sys.stdin.readline

cash = int(input()) # 주어진 현금 입력 받음
stock_price = list(map(int, input().strip().split())) # 14일간의 주가를 입력받음
j_cash = cash # 준현 현금에 넣어줌
j_stock_count = 0 # 준현 가진 주식 수
s_cash = cash # 성민 현금에 넣어줌
s_stock_count = 0 # 성민 가진 주식 수
# 준현 매매법 : 살수있는 한도 내에서 최대한 삼. 주가가 40이면 40*2가 100이하의 최대 숫자이므로 주식 2개 사고 20현금 남은 것..
# 성민 매매법 : 3일째 하락장일때 살 수 있는 최대한 삼, 3일간 상승장일때 팔 수 있는 최대한을 팜
'''
100
10 20 23 34 55 30 22 19 12 45 23 44 34 38
'''
for i in range(14): # today_price = 10
    price = stock_price[i]
    if j_cash >= price:
        buy = j_cash // price
        j_stock_count += buy # 총 주식 매매수 저장
        j_cash = j_cash - (price * buy) # j_cash = 100 - 10*10 = 0, 주식 사고 남은 현금 계산해서 저장시킴

#상승장과 하락장을 어떻게 코드로 구현할 것인가.. 인덱스로 비교해서 전보다 상승이거나 하락이면 count +1해주고 아니면 count초기화 0으로 해줘서 count가 3이 되는 날?
up = 0
down = 0
for k in range(1, 13):
    if stock_price[k-3] > stock_price[k-2] > stock_price[k-1]: # 3일 연속 하락
        if s_cash >= stock_price[k]:
            buy = s_cash // stock_price[i]
            s_stock_count += buy
            s_cash = s_cash - buy * stock_price[k]
     # 3일 연속 상승
    elif stock_price[i-3] < stock_price[i-2] < stock_price[i-1]:
        s_cash += s_stock * stock_price[i]
        s_stock = 0       


j_money = j_stock_count*stock_price[13] + j_cash
s_money = s_stock_count*stock_price[13] + s_cash

if j_money > s_money:
    print("BNP")
elif j_money < s_money:
    print("TIMING")
else:
    print("SAMESAME")

'''
[문제 흐름]
- 첫 줄에서 `cash` 입력 받음
- 둘째 줄에서 `stock_price` 리스트 입력 받음 (14일치)
- 변수 초기화
    - `j_cash`, `j_stock_count` : 준현의 현금, 보유 주식 수
    - `s_cash`, `s_stock_count` : 성민의 현금, 보유 주식 수
- 준현 계산
    - 0일부터 13일까지 반복
    - 매일 현재 가격으로 최대한 주식 매수
    - 매수한 수량만큼 현금 차감, 주식 수량 증가
- 성민 계산
    - 3일부터 13일까지 반복
    - 현재 날짜 기준으로 바로 전 3일 가격 확인
        - `stock_price[k-3] > stock_price[k-2] > stock_price[k-1]`이면 하락 3일
            - 오늘 가격으로 전량 매수
        - `stock_price[k-3] < stock_price[k-2] < stock_price[k-1]`이면 상승 3일
            - 오늘 가격으로 전량 매도
- 각각 총 자산 계산
    - `j_money = j_cash + j_stock_count × stock_price[13]`
    - `s_money = s_cash + s_stock_count × stock_price[13]`
- 정답 출력
    - `j_money > s_money` → BNP
    - `j_money < s_money` → TIMING
    - 같으면 → SAMESAME
'''