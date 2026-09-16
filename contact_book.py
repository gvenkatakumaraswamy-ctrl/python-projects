contacts = {
    "chakri": {
        "phone": "7075328005",
        "email": "gchakri@gmail.com"
    },
    "Uday": {
        "phone": "7799572164",
        "email": "guday@gmail.com"
    },
    "Rama": {
        "phone": "8688699523",
        "email": "grama@gmail.com"
    },
    "khechar": {
        "phone": "7337219832",
        "email": "skhechar@gmail.com"
    }
}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Sort Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            contact_name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            contacts[contact_name] = {
                "phone": phone,
                "email": email
            }

            more = input("Do you want to add another contact? yes/no: ").lower()
            if more == "no":
                break

    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact does not exist")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            contacts[name]["phone"] = input("Enter new contact number: ")
            contacts[name]["email"] = input("Enter new email: ")
            print("Contact updated successfully")
        else:
            print("Contact does not exist")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact does not exist")

    elif choice == "5":
        print("\n===== SORTED CONTACTS =====")

        for name in sorted(contacts):
            print("\nName:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid choice")