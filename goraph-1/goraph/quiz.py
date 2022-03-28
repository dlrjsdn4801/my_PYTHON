# 나도코딩 퀴즈용
from random import *

#비슷하게는 한 것 같기는 한데 하ㅏㅏ 복습해야겟다

guest = list(range(1,51))
time = randrange(5,51)
for t in time:
    for i in guest:
        if t <= 15:
            print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i,t))
        else:
            print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,t))
