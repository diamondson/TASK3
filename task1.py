text = input("Введите текст через пробел: ")
text = text.split()

text.sort(key=len) # сортирует по длине 
print(text)