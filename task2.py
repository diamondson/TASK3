apples = input("Введите количество яблок: ")
boys = input("Введите количество парней: ")

apples2 =str(int(apples)//int(boys))
basket = int(apples)%int(boys)

print(f"У каждого парня по {str(int(apples)//int(boys))} яблок") # new type of format 
print("В корзине осталось {} яблок".format(str(basket)))