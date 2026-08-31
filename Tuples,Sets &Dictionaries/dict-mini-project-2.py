contacts = {
    "Rahul": "9876543210",
    "Aman": "9123456780",
    "Priya": "9988776655"
}

while True:

    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "4":
        print("\n--- CONTACTS ---")

        for name in contacts:
            print(name, "→", contacts[name])

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice!")