a = 10
if a == 9 :
    print("T")
else :   # else 다음은 조건문 X
    print("F")

score = int(input("점수는? "))
if score >= 90 :
    print("장학금 대상자입니다. \n축하합니다.")
else :
    print("장학금 대상자가 아닙니다. \n다음 학기를 노려봅시다.")
print("수고하셨습니다.")

score2 = int(input("점수2는? "))
if score2 >= 90 :
    print("장학금 대상자입니다.")
    print("축하합니다.")
else :
    print("장학금 대상자가 아닙니다.")
    print("다음 학기를 노려봅시다.")
print("수고하셨습니다.")

score3 = int(input("점수3은? "))
if score3 >= 90 :
    pass
else :
    print("공부를 열심히 ..")
print("수고하셨습니다.")