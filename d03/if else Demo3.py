def calcBMI():
    h = float(input('你的身高(cm)'))
    w = float(input('你的體重(kg)'))
    bmi = w / ((h/100)**2)
    result = "過重" if(bmi > 23) else "過輕" if (bmi<18) else "正常"
    print("身高: %.1f 體重: %.1f BMI: %.2f (%s)" % (h, w, bmi, result))

def menu():
    print("BMI 計算系統")
    print("__________")
    print("1. 開始系統")
    print("2. 離開系統")
    id = int(input("請選擇:"))
    if id ==1:
        print('你選擇的是1')
        calcBMI()
        print(input('請輸入任意鍵重新開始...'))
        menu()
    elif id ==2:
        print('你選擇的是2')
        print('再見掰掰')
        print(input('請輸入任意鍵重新開始...'))
        print('還敢玩啊')
        menu()
    else:
        print('選擇錯誤')
        menu()
menu()