letters = "аоиеёэыуюя"
text = input('Введите текст: ')

glasn = [gls for gls in text if gls in letters]
print(glasn)
print(len(glasn))
