# Hi I'm shayan and I want to practice today about nesting and hybrid using list and dictionary
# 1. Create three dictionaries
# 2. Assign dictionaries in list
# 3. Create a for-loop on my list to print each person's information
# 4. Create variable and use dictionaries keys
# 5. Print variable


person_1 = {'first_name': 'shayan', 'last_name': 'hasanzade', 'city': 'tehran', 'age': 23}
person_2 = {'first_name': 'sara', 'last_name': 'rad', 'city': 'babol', 'age': 21}
person_3 = {'first_name': 'hamta', 'last_name': 'rahmani', 'city': 'amol', 'age': 21}
people = [person_1, person_2, person_3]
for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    info = f"From {person['city']} , {person['age']} years old"
    print(name.title())
    print(info)
    print("----------")