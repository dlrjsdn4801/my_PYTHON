absent = [2, 5]
no_book = [7]

for student in range(1,11): # 1~10번
    if student in absent:
        print("{0}번이 없네".format(student))
        continue
    elif student in no_book:
        print("{0} 따라와".format(student))
        break
    print("{0}야, 책읽어봐".format(student))
