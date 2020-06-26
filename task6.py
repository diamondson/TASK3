text1 = list(input("Введите текст: "))


text2 = text1[:]
text1.reverse()
if text2 == text1:
    print("Да, это полиндром!")

else: 
    print("Это не полиндром..")