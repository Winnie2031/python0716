report = "台積電目前價格每股300元, 非常適合買進"
amount = 1000
price = report[9:12]
print(price, type(price))
cost = amount * int(price)
print(cost)