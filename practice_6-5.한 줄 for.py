# 출석번호가 1, 2, 3, 4, 앞에 100 붙이기로 함 -> 101, 102 ...

student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)


# 학생 이름을 길이로

students = ["kim cheol soo", "lee geon woo", "jeon tae woong"]
print(students)
students = [len(i) for i in students]
print(students)


# 학생 이름을 대문자로

stu = ["kim cheol soo", "lee geon woo", "jeon tae woong"]
print(stu)
stu = [i.upper() for i in stu]
print(stu)
