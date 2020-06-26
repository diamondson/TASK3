number = int(input("Введите ваш возраст: "))

if number%2 == 0:
     number = list(range(0,number+2,2)) # +2 в аргументе чтобы ваш возраст был
                                        # включителен 
     print(number) # до сюдого код работает
elif number%2 ==1:
     number = list(range(1, number+2, 2))
     print(number)


# if number%2 == 0:
#     n = 0
#     while n <= number:
#         print(n)
#         n+=2
# elif number%2 ==1:
#     n = 1
#     while n <= number:
#         print(n)
#         n+=2



