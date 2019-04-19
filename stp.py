# FizzBuzz
# def fizz_buzz():
#     for i in range(1, 101):
#       if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#       elif i % 3 ==0:
#         print('Fizz')
#       elif i % 5 ==0:
#         print('Buzz')
#       else:
#         print(i)
#
# fizz_buzz()

# Sequential Search
# def ss(num_list, n):
#     found = False
#     for i in num_list:
#         if i == n:
#             found = True
#             break
#     return found

# Palindrome
# def palindrome(word):
#     word = word.lower()
#     return word[::-1] == word
#
# print(palindrome('Mom'))

# Anagram
def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram('iceman', 'cinema'))
print(anagram('wumbo', 'mumbo'))
