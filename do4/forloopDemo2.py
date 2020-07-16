scores = [100, 95, 81, 72, 66, 53]
#print(scores[0])
#print(scores[1])
#print(scores[2])
#print(scores[3])
#print(scores[4])
print(len(scores)) # 數組的元素
#per scores
for i in range (0,len(scores)):
    print(scores[i])

#求總分?
sum = 0
for i in range (0, len(scores)):
    sum += scores[i]
print("totalsum: %d" % sum)

avg = sum/len(scores)
print("average: %.1f" %avg)