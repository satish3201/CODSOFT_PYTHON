contacts = []

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("\nEnter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("❌ Contact not found.")

def update_contact():
    name = input("\nEnter name of contact to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave blank to keep current value.")
            new_phone = input("New phone number: ") or contact["phone"]
            new_email = input("New email: ") or contact["email"]
            new_address = input("New address: ") or contact["address"]

            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address
            print("✅ Contact updated successfully.")
            return
    print("❌ Contact not found.")

def delete_contact():
    name = input("\nEnter name of contact to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully.")
            return
    print("❌ Contact not found.")

def main():
    print("📞 Welcome to Contact Book")
    while True:
        print("\n--- Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()
