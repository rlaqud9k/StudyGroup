def is_palindrome(word):
    i = int(len(word)/2)
    e = len(word)
    result = True
    for i in range(i):
       if(word[i] == word[e -1]):
           e-=1
           result = True
       else:
           result = False

    return result


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))