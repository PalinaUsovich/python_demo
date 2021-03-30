
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
'''
this is another way to comment smth
'''
"""
this is also  comments
"""

print(translate(input("Enter a phrase: ")))







