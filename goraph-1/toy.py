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