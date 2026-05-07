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

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())

for language in favorite_languages.values():
    print(language.title())

