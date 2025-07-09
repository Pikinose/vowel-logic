def vow(text):
    vowels = 'aeiouAEIOU'
    num = 0
    for char in text:
        if char in vowels:
            num += 1
    return num

print(vow("Hello Lava")) 
    