
nums = [1,2,3,4]
result = []

for i, el in enumerate(nums):
    if i == 0:
        result.append(el)
    else:
        s = el + result[i-1]
        result.append(s)

print(result)



# n = int(input())
# result = []

# for _ in range(n):
#     word = input()
#     if len(word) <= 10:
#         result.append(word)
#     else:
#         pervyi = word[0]
#         poslednyi = word[-1]
#         sud_dlina = len(word) - 2
#         abbr = pervyi + str(sud_dlina) + poslednyi
#         result.append(abbr)

# for slovo in result:
#     print(slovo)



# n = int(input())

# if n < 2 :

#   print('Yes!')

# else:

#   list = list(map(int,input().split()))

#   print(min(list),max(list))

def capitalize(apple):
    first_letter_small = apple[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + apple[1:]
 
source = input().split()
res = []
for apple in source:
    res.append(capitalize(apple))
print(' '.join(res))