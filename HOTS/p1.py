# reverse
# s = "abcdef"
# def reverse_str(s):
#     return s[::-1]
# print(reverse_str(s))
# print(s)

# palindrome
# s = "madam"
# def isPal(s):
#     return s==s[::-1]
# print(isPal(s))

# fibonacci
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a+b 
# print(fib(10))

# fibonacci
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)
# print(fact(4))

# arr = [1,10, 2, 6,2,2,19]
# print(max(arr))

# def remove_dup(arr):
#     return list(set(arr))
# print(remove_dup(arr))

s = "abcdefiou"
def count_fun(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
        return count 

print(count_fun(s))