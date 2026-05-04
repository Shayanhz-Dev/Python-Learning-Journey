#Hello , my name is shayan and i started learn python last night , this is my cases list training
#I dont use loop in list becouse i just want use list and practice
#I make contains variables becuase if i just print message is ugly and not readable
my_name = "shayan prime"
friend_name = ["reza baktash", "fayaz farzadian", "mostafa bostan", "hosein omran"]
print(friend_name)


#first message is for reza 

greeting_first = f"Hello brother \n  '{friend_name[0].title()}'"
message_first = f"i hope to see you in the best position and top level Goodbye {friend_name[0].title()}"
end_first = f"\t\n I love you my brother \n\t from '{my_name.upper()}'"
print(greeting_first, message_first, end_first)

#secound message is for fayaz

greeting_second  = f"Hello my friend \n ' {friend_name[1].title()}'"
message_second = f"I hope to see you in luxury and healthful lifestyle Goodbye {friend_name[1].title()}"
end_second  = f"\t\n I love you my friend \n\t from '{my_name.upper()}'"
print(greeting_second , message_second, end_second )

#third message is for mostafa

greeting_third = f"Hello my space marine  \n  '{friend_name[2].title()}'"
message_third = f"ahhh mostafa you are my space marine with your amazing drink bro, i want to see your happy face always \n Goodbye {friend_name[2].title()}"
end_third = f"\t\n I love you my friend \t from '{my_name.upper()}'"
print(greeting_third, message_third, end_third)

#fourth message is for hosein

greeting_fourth = f"Hello my oldfriend \n  '{friend_name[3].title()}'"
message_fourth = f"we have a lot mommories with each other , we have diffrent way but i want a good and peaceful life for you \n Goodbye {friend_name[3].title()}"
end_fourth = f"\t\n I love you my oldfriend \t from '{my_name.upper()}'"

#now i create my own list and my dreams
#i dont create variable for each list item becouse i want just type a text
own_list = ["Bmw m5 cs" , "Mac book pro m4 max" , "iphone 17 promax"]
print(f"\n I would like to own a {own_list[0].upper()}")
print(f"I realy need one '{own_list[1].title()}' becouse i'm a programmer")
print(f"I would like to own a {own_list[2].lower()} becouse i always want best")