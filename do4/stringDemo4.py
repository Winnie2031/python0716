report = "台積電每股315.5元,可賣出4000股,目前我的庫存有6000股"
# 求庫存賣出後的總值
amount = int(report[15:19])
price = float(report[5:10])
stock = int(report[28:32])
print(price, amount, stock)
cost = (amount * (stock-amount))
print(cost)