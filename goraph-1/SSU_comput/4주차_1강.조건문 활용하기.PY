# if : 조건이 맞는 경우 실행할 명령을 정의
# if .. else .. : 조건에 맞는 경우와 아닌 겨웅에 대해 다른 명령을 정의
# if .. elif .. else: 여러가지 조건에 따라 다른 명령을 정의

score = int(input("점수를 입력하시오. "))

if score >= 90:
    print("장학금 대상자입니다.")
elif 80 <= score < 90:
    print("장학금 대상자가 아닙니다.")
elif score < 80:
    print("지원대상이 아닙니다.")

