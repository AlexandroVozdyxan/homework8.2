import string

def is_palindrome(text) -> bool :

    clear_text = "".join(char.lower() for char in text if char.isalnum())

    if clear_text == clear_text[::-1]:
        return bool(1)
    else:
        return bool(0)
print(is_palindrome("Qwrq"))
# print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("0P"))
# print(is_palindrome("a."))
# print(is_palindrome("aurora"))
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")


