# for = 반복

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# 더 편하게 

for wait_num in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(wait_num))

for wait_no in range(1,6):  # 1~5
    print("대기번호 : {0}".format(wait_no))

starbucks = ["이건우","잔나비","너드커넥션","혁오"]
for customer in starbucks :
    print("{0} 고객님, 커피가 준비되었습니다.".format(customer))