number = int(input("Число: "))
# While
counter = 0
sum_kub = 0

while counter <= number:
    sum_kub += counter**3
    counter +=1
print(sum_kub)


sum_kub = 0

for i in range(0, number+1):
    sum_kub += i**3
print(sum_kub)
