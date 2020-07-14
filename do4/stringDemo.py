word = "she sell sea shell on the sea shore"
print(word.count('s'))
print(word.count('she'))
print(word.count(' '))

password = 'abc' .join('xyz123')
print(password.isalpha()) #including only english
print(password.isalnum()) #including number or alpha
print(password.isdigit()) #including only number
print(password)


str ='hello python'
print(str[4])
print(str[-4])
print(str[1:4])
print(str[:4])

path = 'C:\nba\tiket.txt'
print(path)
path = r'C:\nba\tiket.txt'
print(path)
path = 'C:\\nba\\tiket.txt'
print(path)