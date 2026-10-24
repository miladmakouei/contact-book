
contact_names = []
contact_phones = []


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name == "" or phone == "":
        print("Name and phone number cannot be empty.")
        return

    if phone in contact_phones:
        print("This phone number already exists.")
        return

    contact_names.append(name)
    contact_phones.append(phone)

    print("Contact added successfully.")


def show_contacts():
    if len(contact_names) == 0:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for index in range(len(contact_names)):
        print(
            f"{index + 1}. {contact_names[index]} "
            f"- {contact_phones[index]}"
        )


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    for index in range(len(contact_names)):
        if search_name in contact_names[index].lower():
            print(
                f"{contact_names[index]} - "
                f"{contact_phones[index]}"
            )
            found = True

    if not found:
        print("No matching contact found.")


def delete_contact():
    if len(contact_names) == 0:
        print("No contacts to delete.")
        return

    show_contacts()
    contact_number = input("Enter contact number to delete: ")

    if not contact_number.isdigit():
        print("Please enter a valid number.")
        return

    index = int(contact_number) - 1

    if index >= 0 and index < len(contact_names):
        deleted_name = contact_names.pop(index)
        contact_phones.pop(index)
        print(f"{deleted_name} was deleted.")
    else:
        print("Invalid contact number.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
