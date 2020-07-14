def getBMI(h, w):
    bmi = w / ((h/100)**2)
    return bmi


bmi = getBMI(170, 60)
print("%.2f" % bmi)

bmi = getBMI(160, 60)
print("%.1f" % bmi)

bmi = getBMI(180, 60)
print("%.3f" % bmi)