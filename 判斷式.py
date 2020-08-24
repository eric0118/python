'''score = int(input("請輸入成績:"))
if score >= 60:
    print("pass")
else:
    print("fail")'''

'''score = int(input("請輸入成績:"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif  score >= 70:
    print("C")
elif  score >= 60:
    print("D")
else:
    print("E")'''

math = int(input("請輸入數學成績:"))
eng = int(input("請輸入英文成績:"))
if math > 90 and eng > 90:
    print('你有獎品')
elif math < 60 and eng < 60:
    print('你要被懲罰')
else:
    print('沒事')
    