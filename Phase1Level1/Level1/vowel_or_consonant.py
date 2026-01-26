#Take a character and check if it’s a vowel or consonant.

char = input("Enter a character: ")

vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

if char in vowel:
    print("Vowel")
else:
    print("Consonant")