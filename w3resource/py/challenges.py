import re

# Challenge 1.
# Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z, and 0-9)

def is_char_allowed(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    found = charRe.search(string)
    res = not bool(found)
    return res


# Challenge 2.
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b'-s.

def text_match(text):
    pattern = re.compile(r'ab*')
    res = pattern.search(text).group()
    return res


# Challenge 3.
# Write a Python program that matches a string that has an 'a' followed by one or more 'b'-s.

def text_match2(text):
    pattern = re.compile(r'ab+?')
    res = pattern.search(text).group()
    return res


# Challenge 4.
# Write a Python program that matches a string that has an 'a' followed by zero or one 'b'-s.

def text_match3(text):
    pattern = re.compile(r'ab?')
    res = pattern.search(text).group()
    return res


# Challenge 5.
# Write a Python program that matches a string that has an 'a' followed by three 'b'-s.

def text_match4(text):
    pattern = re.compile(r'ab{3}?')
    res = pattern.search(text).group()
    return res


# Challenge 6.
# Write a Python program that matches a string that has an 'a' followed by two to three 'b'-s.

def text_match5(text):
    pattern = re.compile(r'ab{2,3}?')
    res = pattern.search(text).group()
    return res


# Challenge 7.
# Write a Python program to find sequences of lowercase letters joined with an underscore.

def text_match6(text):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    res = pattern.search(text).group()
    return res


# Challenge 8.
# Write a Python program to find sequences of one upper case letter
# followed by the lower case letters.

def text_match7(text):
    pattern = re.compile(r'[A-Z]?[a-z]+')
    res = pattern.search(text).group()
    return res


# Challenge 9.
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

def text_match8(text):
    pattern = re.compile(r'a.*b$')
    res = pattern.search(text).group()
    return res


# Challenge 10.
# Write a Python program that matches a word at the beginning of a string.

def text_match9(text):
    pattern = re.compile(r'^\w+')
    res = pattern.search(text).group()
    return res


# Challenge 11.
# Write a Python program that matches a word at the end of a string, with optional punctuation.

def text_match10(text):
    pattern = re.compile(r'\w+$')
    res = pattern.search(text).group()
    return res


# Challenge 12.
# Write a Python program that matches a word containing 'z'.

def text_match11(text):
    pattern = re.compile(r'\w*z\w*')
    res = pattern.search(text).group()
    return res

# Challenge 13.
# Write a Python program that matches a word containing 'z', not start or end of the world.

def text_match12(text):
    pattern = re.compile(r'\Bz\B')
    res = pattern.search(text)
    return res


# Challenge 14.
# Write a Python program that contains only upper and lowercase letters, numbers, and underscores.

def text_match13(text):
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    res = pattern.search(text)
    return res


# Challenge 15.
# Write a Python program where a string will start with a specific number.

def text_match14(text, number):
    number_str = str(number)
    is_number = bool(re.search(r'0-9', number_str))
    if is_number:
        return ''
    else:
        pattern = re.compile(r'^{0}'.format(number_str))
        res = pattern.search(text).group()
        return res


