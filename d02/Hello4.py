# 資料的轉換
x = input("請輸入一個數字 x :")
y = input("請輸入一個數字 y :")
print(x,y)
sum = x + y
print(sum)

# 觀察 x, y 都是 str 字串
print(x, tyoe(x), y, type(y))
#經過觀察結果發現 x, y都是 str字串
# 所以要透過 int(字串變數) 來進行字串的程序
sum = int(x) + int(y)
print(sum)