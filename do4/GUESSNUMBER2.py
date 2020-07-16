import random
import sys

ans = random.randint(1, 100)
min, max = 0, 100
amount = 50
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
        print('恭喜玩家答對了')
        break

    print(' %d~%d guess a number,press enter to let computer guess' % (min, max))
    sys.stdin.read(1)

    guess = random.randint(min+1, max-1)
    print('電腦在%d~%d之間猜一數字:%d' % (min, max, guess))
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('恭喜電腦答對了')
        break


    if amount == 0:
        print ("your dead, the answer is :" , str(ans))
