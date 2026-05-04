
#hello i'm shayan and this is my first case study for learn python 
#input your variable 

first_name = "kia"
last_name = "rad"
full_name = f"{first_name} {last_name}"

#output your message with a clean string code 

print(f"Hello, {full_name.title()} \n\t{first_name.title()} would you like to learn some Python today?") 
print(f"\t lowercase {full_name.lower()} \t uppercase {full_name.upper()}")
print('Steve Jobs once said, "Everybody should learn to program a computer, because it teaches you how to think"')
famous_person ="     Cristiano Ronaldo      "
message = " Practice makes Perfect   "
print(f" {famous_person.strip()} \n\tonce said {message.lstrip()}")

#file name removesuffix training

filename = "message to friend.txt"
print(filename.removesuffix(".txt"))