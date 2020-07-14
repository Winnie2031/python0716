def add(x, y):
    print('執行到 add() 方法', x, y)
    result = x + y
    return result

def info():
    print("執行到 info() 方法")
    print("本程式是由 Python 所填寫")

def checkSex(id):

    sex = id[1]
    if sex == "1":
        print("boy")
        return
    if sex == "2":
        print(girl)
        return


sum = add(10, 30)
print(sum)
info()
checkSex(H12)