# 펠린드롬은 앞에서 읽을 때와 뒤에서 읽을 때 같은 단어를 말한다.
# ex) level, sos, rotator
# 맨 앞글자와 맨 뒷글자의 알파벳만 같은 단어는 펠린드롬이라고 볼 수 없는 것이다.
# ex) radar, deed, reader

user_input_word = input().strip()
change_to_list = list(user_input_word)

length = len(change_to_list)

palindrome_bool = 1  
for i in range(length // 2): 
    if change_to_list[i] != change_to_list[length - 1 - i]: 
        palindrome_bool = 0 
        break

print(palindrome_bool)