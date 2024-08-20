import calendar
from datetime import datetime

data = {} # 각 날짜 저장 딕셔너리

yy = datetime.today().year  # 현재 연도
mm = datetime.today().month  # 현재 달

class colors:
    BLUE = '\033[94m'  # 토요일 색상
    RED = '\033[91m'   # 일요일 색상
    END = '\033[0m'    # 색상 초기화

def CAL(year, month): # 캘린더 세팅
    cal = calendar.Calendar(firstweekday=6) # 일요일 첫 요일
    month_days = cal.monthdayscalendar(year, month) # 선택날짜 리스트로 생성
    header = calendar.month_name[month] + ' ' + str(year)  # 월과 연도 헤더
    print(f"{header:^20}")  # 중앙 정렬 헤더
    print("Su Mo Tu We Th Fr Sa")  # 요일 헤더
    
    for week in month_days:
        week_str = ""
        for i, day in enumerate(week):
            if day == 0:  # 빈 날짜 공백처리
                week_str += "   "
            elif i == 0:  # 일요일 빨간색표시
                week_str += f"{colors.RED}{day:2}{colors.END} "
            elif i == 6:  # 토요일 파란색표시
                week_str += f"{colors.BLUE}{day:2}{colors.END} "
            else:
                week_str += f"{day:2} "
        print(week_str)

def select_date(): # 날짜 세팅
    while True:
        year = int(input(f"연도를 입력하세요 (예: {yy}): "))
        month = int(input("월을 입력하세요 (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("다시 입력해주세요.")
    
    CAL(year, month) # 달력 표시
    
    while True:
        day = int(input("날짜를 입력하세요 (1-31): "))
        try:
            selected_date = datetime(year, month, day)
            break
        except ValueError:
            print("다시 입력해주세요.")
    
    return selected_date.strftime("%Y-%m-%d") # 날짜 문자열 변환

def _main_():
    while True: # 메뉴 출력
        print("\n메뉴:")
        print("1. 수입 입력")
        print("2. 지출 입력")
        print("3. 수입, 지출 확인")
        print("4. 종료")
        choose = input("원하는 작업을 선택하세요 (1-4): ")

        if choose == "1": # 수입 입력
            date = select_date()
            IMP = int(input(f"{date}의 수입 금액을 입력하세요: "))
            if date not in data:
                data[date] = {"income": 0, "expense": 0}
            data[date]["income"] += IMP
            print(f"{date}에 {IMP}원이 수입으로 추가되었습니다.")
            print("---------------------------------------\n")

        elif choose == "2": # 지출 입력
            date = select_date()
            SPD = int(input(f"{date}의 지출 금액을 입력하세요: "))
            if date not in data:
                data[date] = {"income": 0, "expense": 0}
            data[date]["expense"] += SPD
            print(f"{date}에 {SPD}원이 지출로 추가되었습니다.")
            print("---------------------------------------\n")

        elif choose == "3": # 특정 날짜 확인
            date = select_date()
            if date in data:
                income = data[date]["income"]
                expense = data[date]["expense"]
                balance = income - expense
                print(f"\n{date}의 수입: {income}원")
                print(f"{date}의 지출: {expense}원")
                print(f"{date}의 잔액: {balance}원")
            else:
                print(f"{date}에 대한 기록이 없습니다.")
            print("---------------------------------------\n")

        elif choose == "4": # 프로그램 종료
            print("\n--가계부를 종료합니다--")
            break

        elif choose == "5": # 테스트
            print(data)

        else:
            print("잘못된 입력입니다.")

_main_() # 프로그램 시작