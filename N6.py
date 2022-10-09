def reverse(s): 
    return s[::-1] 
def is_palindrome(s): 
    rev = reverse(s) 
    if (s == rev): 
        return True
    else:
        return False
s = input()
print(is_palindrome(s))
