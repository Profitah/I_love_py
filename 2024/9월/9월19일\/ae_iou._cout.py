user_text = input()
user_text_list = list(user_text)
user_text_list = [char.lower() for char in user_text_list]
aeiou = ['a', 'e', 'i', 'o', 'u']

count = 0
for char in user_text_list:
    if char in aeiou:  
        count += 1

print(count)