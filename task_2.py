#parsing of the entered command
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


#adding new contact
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#changing contact
def change_contact(args, contacts):
    name, phone = args

    if name in contacts.keys():
        changed_contact = {name : phone}
        contacts.update(changed_contact)
        return "Contact updated."
    else:
        return "The entered name was not found"

#phone number output
def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return f"{contacts[name]}"
    else:
        return "The entered name was not found"
#output all data   
def show_all(contacts):
    if contacts == {}:
        return contacts
    else:
        for key, value in sorted(contacts.items()):
            return f"{key}: {value}"

def main():

    contacts = {}

    print("Welcome to the assistant bot!")
    print("----------------------------------")
    print("Please, enter a command:")
    print("  - 'hello' to start the chat")
    print("  - 'close'/'exit' to end the chat")
    print("----------------------------------")
    print("                                  ")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
            print("----------------------------------")
            print("Please, enter a command:")
            print("  - 'add [username] [phone]' to adde Contact")
            print("  - 'change [username] [new phone number]' to update Contact")
            print("  - 'phone [username]' to get the phone number")
            print("  - 'all' to output all the data")
            print("----------------------------------")
            print("                                  ")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))        

        elif command == "phone":
            print(show_phone(args, contacts))       

        elif command == "all":
            print(show_all(contacts))              

        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()