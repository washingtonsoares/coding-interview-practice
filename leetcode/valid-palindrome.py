# using a more python-like approach
def isPalindrome1(s: str):
    alpha_num_str = ""

    for c in s:
        if c.isalnum():
         alpha_num_str += c.lower()
    
    return alpha_num_str == alpha_num_str[::-1]

def isPalindrome2(s: str):
    alpha_num_str = ""

    for c in s:
        if c.isalnum():
         alpha_num_str += c.lower()
    
    alpha_num_str_len = len(alpha_num_str)  
    
    for index, n in enumerate(range(alpha_num_str_len // 2)):
       if alpha_num_str[index] != alpha_num_str[alpha_num_str_len - index - 1]:
          return False
    
    return True

# using a "two pointers" like approach
def isPalindrome(s: str):
    L = 0
    R = len(s) - 1 

    while L < R:
        if not s[L].isalnum():
            L += 1
            continue
        if not s[R].isalnum():
            R -= 1
            continue
        if s[L].lower() != s[R].lower():
           return False

        L += 1
        R -= 1
    return True

       
print(isPalindrome("A man, a plan, a canal: Panama"))

