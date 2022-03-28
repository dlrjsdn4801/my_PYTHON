# while?

customer = "이건우"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")


# cust = "김정은"
# time = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(cust, time))
#     time += 1


name = "이건우"
person = "Unknown"

while person != name:
    print("{0}, 커피가 준비되었습니다.".format(name))
    person = str(input("이름이 어떻게 되세요? "))
    print(person)

b = 1
a = 1

while a == b :
    a = int(input())