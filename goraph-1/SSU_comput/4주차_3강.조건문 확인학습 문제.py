#1
#정수를 입력받아 양수인지, 음수인지, 0인지 판단하는 프로그램을 작성하시오

integer = int(input("정수를 입력하시오. "))
if integer > 0:
    print("양수")
elif integer < 0:
    print("음수")
else:
    print("0")

#2
# 출생연도를 입력받아 나이를 계산하여 알려주는 프로그램을 작성하시오.
# "당신은 올해 23살 입니다." 라는 형식으로 출력하시오.
# 또한 나이가 20세 이상이면 "당신은 성인입니다."라고 안내하시오.

birth = int(input("출생연도를 입력하시오. "))
k_birth = 2022 - birth + 1
print("당신은 올해 %d살입니다." % k_birth)
if k_birth >= 20:
    print("당신은 성인입니다.")

#3
# 한국과 프랑스의 시차는 8시간이다. 한국이 프랑스보다 8시간 빠르다.
# 즉, 한국이 10시 30분이라면 프랑스는 2시 30분이다.
# 한국 시각(시간,분)을 입력받아 프랑스 시간을 알려주는 프로그램을 작성하시오.
# 시간은 24시간 단위로 입력받는다. (오후2시 = 14시)

k_hour = int(input("한국은 몇 시인가요?"))
k_minute = int(input("한국은 몇 분인가요?"))

if k_hour < 8:
    k_hour += 24

f_hour = k_hour - 8

print("프랑스의 시간은 %d시 %d분입니다." % (f_hour,k_minute))

#9
# 출생연도를 입력받아 나이를 계산 후 나이에 따라 ~을 예측하는 프로그램을 만드시오
birth_pre = int(input("출생연도를 입력하시오. "))
job = 2022 - birth_pre + 1

if job > 27 :
    print("직장인")
elif 20 <= job <= 26 :
    print("대학생")
elif 16 < job <= 19 :
    print("고등학생")
elif 13 < job <= 16 :
    print("중학생")
elif 7 < job <= 13 :
    print("초등학생")
elif 1 < job < 7:
    print("어린이")
else:
    print("아직 태어나지 않았습니다.")

#4
# 점수를 입력받아 80점 이상이면 A등급, 60점 이상 80점 미만이면 B등급, 60점 미만이면 C등급

score = int(input("점수를 입력하시오. "))

if score > 100 or score < 0:
    print("점수를 정확히 입력해주십시오.")
elif score >= 80:
    print("A등급입니다.")
elif score < 80 and score >= 60:
    print("B등급입니다.")
else:
    print("C등급입니다.")

#5
# 양의 정수를 입력받아 3의 배수인지 아닌지 판단해주는 프로그램을 만드시오
# 만약 0이나 음의 정수를 입력하면 잘못된 입력이라고 안내하고 프로그램을 종료하시오

plus = int(input("양의 정수를 입력하시오. "))
check = plus % 3


if plus == 0 or plus < 0:
    print("잘못된 입력입니다.")
elif check == 0:
    print("3의 배수입니다.")
elif check != 0:
    print("3의 배수가 아닙니다.")

#6
# 양의 정수를 입력받아 2의 배수, 3의 배수, 5의 배수를 판단해주는 프로그램을 작성하시오
# 만약 10을 입력했다면 '10은 2의 배수입니다.','10은 3의 배수는 아닙니다','10은 5의 배수입니다.'라는 3줄의 문장을 출력

plus_int = int(input("양의 정수를 입력하시오. "))

plus_int2 = plus_int % 2
plus_int3 = plus_int % 3
plus_int5 = plus_int % 5

if plus_int < 0 or plus_int == 0:
    print("잘못된 입력입니다.")
else:
    if plus_int2 == 0:
        print("%d는 2의 배수입니다." % plus_int)
    else:
        print("%d는 2의 배수가 아닙니다." % plus_int)
    
    if plus_int3 == 0:
        print("%d는 3의 배수입니다." % plus_int)
    else:
        print("%d는 3의 배수가 아닙니다." % plus_int)
    
    if plus_int5 == 0:
        print("%d는 5의 배수입니다." % plus_int)
    else:
        print("%d는 5의 배수가 아닙니다." % plus_int)

#7
# 퀴즈, 중간고사, 기말고사 점수를 받아 최종 점수를 계산 후
# 최종 점수가 70 이상이면 PASS, 아니면 FAIL로 안내하시오
# 각 점수는 모두 100점 만점으로 입력받으며, 퀴즈, 중간고사, 기말고사는 각각 2,3,5할 비중

quiz = int(input("퀴즈 점수를 입력하시오. "))
mid_exam = int(input("퀴즈 점수를 입력하시오. "))
fin_exam = int(input("퀴즈 점수를 입력하시오. "))

tot_exam = quiz * 0.2 + mid_exam * 0.3 + fin_exam * 0.5

if quiz > 100 or quiz < 0 or mid_exam > 100 or mid_exam < 0 or fin_exam > 100 or fin_exam < 0:
    print("점수가 잘못 입력되었습니다.")
elif tot_exam >= 70:
    print("PASS")
else:
    print("FAIL")

#8
# 봄(3~4월) 또는 가을(10~11월) 정도의 시기라고 가정해보자.
# 현재 기온을 입력받아 입고 나갈 옷을 추천하라.

# 온도 : ~ 10 , 날씨안내 : 날씨가 춥습니다. , 옷 추천 : 두꺼운 외투를 챙기세요.
# 온도 : 11 ~ 15 , 날씨안내 : 날씨가 신선하네요. , 옷 추천 : 가벼운 외투를 챙기세요.
# 온도 : 16~19 , 날씨안내 : 생활하기 좋습니다. , 옷 추천 : 가볍게 입으세요.
# 온도 : 20 ~ , 날씨안내 : 덥게 느껴지네요. , 옷 추천 : 반팔티도 괜찮습니다.

temp = int(input("현재 기온은?" ))
if temp <= 10:
    clim = "날씨가 춥습니다"
    clot = "두꺼운 외투를 챙기세요"
elif temp > 10 and temp <= 15:
    clim = "날씨가 신선하네요"
    clot = "가벼운 외투를 챙기세요"
elif temp > 15 and temp <= 20:
    clim = "생활하기 좋습니다"
    clot = "가볍게 입으세요"
elif temp > 20:
    clim = "덥게 느껴지네요"
    clot = "반팔티도 괜찮습니다"

print(clim,clot)

# 근데 좀 복잡하게 한 것 같다. 그냥 바로 print() 써도 될 뻔 했네 ㅎㅎ