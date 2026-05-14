# Hi I'm shayan and today I want to practice function
# 1. Create first function for print every list messages (use for-loops)
# 2. Create second function for print every messages and move first list items to second list
# 3. Create first list with values and second list empty
# 4. Positional Call functions
# 5. Print lists 
def show_messages(messages):
    """Display list Messages"""
    print("\n--- Show my messages---")
    for msg in messages:
        print(msg.upper())

def send_messages(unsend_messages, completed_messages):
    """Send messages and append to new list"""
    print(f"\n--- Message sending started.....")
    while unsend_messages:
        move = unsend_messages.pop()
        completed_messages.append(move)
        print(f"-'{move.upper()}' sending.....")
        
messages_list = [
    "just do it",
    "be a warrior, not a worrier",
    "Heart of iron",
]

sent_messages = []

show_messages(messages_list)
send_messages(messages_list[:], sent_messages)

print(messages_list)
print(sent_messages)
