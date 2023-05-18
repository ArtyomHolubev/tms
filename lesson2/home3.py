strin = input("Вводи: ")

str1 = strin[1::2]
str2 = strin[::2]

#print(str1, str2)

print("Введена строка: ", "\"", strin, "\"", sep="", end='\n\n\n')

print(str1, str2, sep='     ', end='\n!!!')

