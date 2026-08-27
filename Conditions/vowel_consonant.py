character = input("Enter a character: ")
has_vowel = character.lower() in ['a', 'e', 'i', 'o', 'u'] or character.upper() in ['A', 'E', 'I', 'O', 'U']
if has_vowel:
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonant.")