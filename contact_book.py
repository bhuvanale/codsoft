# List to store contacts
contacts = []

# Functions for Contact Book operations

def add_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print(f"Contact for {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact(search_term):
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
        return
    for contact in found_contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(search_term, name=None, phone=None, email=None, address=None):
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            print(f"Contact for {search_term} updated.")
            return
    print("Contact not found.")

def delete_contact(search_term):
    global contacts
    contacts = [contact for contact in contacts if search_term not in contact['name'] and search_term not in contact['phone']]
    print(f"Contact for {search_term} deleted.")

# Command-line interface

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            update_contact(search_term, name or None, phone or None, email or None, address or None)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            delete_contact(search_term)
        elif choice == '6':
            print("Exiting Contact Book.\nsee you again")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
