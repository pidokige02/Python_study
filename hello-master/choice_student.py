import random, time
import mysys

g_students = ['엄희진', '이준수', '한진선', '배준홍', '김건우', '김도혜', '성재현', '백영래', '이현주', '김정민', '김주동', '이현욱', '김영모']

idx = 0
while idx < 100:
    idx += 1
    mysys.clear()
    print("\n\n\n")
    c = random.choice(g_students)
    print("choosing one....................................", idx, '%', '---->', c)
    time.sleep(0.05)
