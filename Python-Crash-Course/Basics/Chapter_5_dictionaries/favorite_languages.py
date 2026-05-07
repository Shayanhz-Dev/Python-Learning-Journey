favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"sarah's favorite language is {language}.")

# code updated:
# 1. for-loop for dictionary
# 2. return key-value with items() method

for name, language in sorted(favorite_languages.items()):
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in sorted(favorite_languages.keys()):
    print(name.title())

for language in sorted(favorite_languages.values()):
    print(language.title())

# updated code...
# I create a list
# Using if statement for checking dictionary and list 

friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()):
    print(f"HI, {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
