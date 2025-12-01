import os
import json

CONTACTS_FILE = "contacts.json"

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            contacts = json.load(f)
            return contacts
    except:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contact = {
    "name": name,
    "phone": phone,
    "email": email
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n" + "=" * 40)
    print("ALL CONTACTS")
    print("=" * 40)

for index, contact in enumerate(contacts, start=1):
    print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")
print("-" * 40)

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
            break

    if not found:
        print("Contact not found.")
    
    

def delete_contact(contacts):
    if not contacts:
        print("No contacts to delete.")
        return

    print("\n" + "=" * 40)
    print("       DELETE A CONTACT")
    print("=" * 40)

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")
    print("-" * 40)

    choice = input("Enter the number of the contact to delete: ").strip()

    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

    index = int(choice)

    if 1 <= index <= len(contacts):
        deleted = contacts.pop(index - 1)
        save_contacts(contacts)
        print(f"Deleted contact: {deleted['name']}")
    else:
        print("Invalid contact number.")
    
    
def edit_contact(contacts):
if not contacts:
print("No contacts to edit.")
return

print("\n" + "=" * 40)
print("        EDIT A CONTACT")
print("=" * 40)

for index, contact in enumerate(contacts, start=1):
    print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")
print("-" * 40)

choice = input("Enter the number of the contact to edit: ").strip()

if not choice.isdigit():
    print("Invalid input. Please enter a number.")
    return

index = int(choice)

if not (1 <= index <= len(contacts)):
    print("Invalid contact number.")
    return

contact = contacts[index - 1]

print("\nWhat do you want to edit?")
print("1. Name")
print("2. Phone")
print("3. Email")
print("4. Name, Phone, and Email")

field_choice = input("Enter your choice (1-4): ").strip()

if field_choice == "1":
    new_name = input("Enter new name: ").strip()
    if new_name:
        contact["name"] = new_name
elif field_choice == "2":
    new_phone = input("Enter new phone: ").strip()
    if new_phone:
        contact["phone"] = new_phone
elif field_choice == "3":
    new_email = input("Enter new email: ").strip()
    if new_email:
        contact["email"] = new_email
elif field_choice == "4":
    new_name = input("Enter new name: ").strip()
    new_phone = input("Enter new phone: ").strip()
    new_email = input("Enter new email: ").strip()
    if new_name:
        contact["name"] = new_name
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email
else:
    print("Invalid choice.")
    return

save_contacts(contacts)
print("Contact updated successfully.")
print("Starting Contact Book...")

contacts = load_contacts()

while True:
clear_screen()
print("\n" + "=" * 40)
print(" CONTACT BOOK MENU")
print("=" * 40)
print("1. Add contact")
print("2. View contacts")
print("3. Search contact")
print("4. Edit contact")
print("5. Delete contact")
print("6. Exit")
print("-" * 40)

choice = input("Enter your choice (1-6): ").strip()

if choice == "1":
    add_contact(contacts)
elif choice == "2":
    view_contacts(contacts)
elif choice == "3":
    search_contact(contacts)
elif choice == "4":
    edit_contact(contacts)
elif choice == "5":
    delete_contact(contacts)
elif choice == "6":
    print("Goodbye!")
    break
else:
    print("Invalid choice. Please enter a number between 1 and 6.")