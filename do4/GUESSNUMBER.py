import random
ans = random.randint(1, 100)
min, max = 0, 100
amount = 5
while amount > 0:
    amount -=1
    guess = int(input('請在%d~%d之間猜一數字:' % (min, max)))
    if guess >= max or guess <= min:
        print("輸入錯誤, retry again")
        continue
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('恭喜答對了')
        break

    if amount == 0:
        print ("your dead, the answer is :" , str(ans))
