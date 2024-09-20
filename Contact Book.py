import os
import json

FILENAME = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file if it exists."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save the current list of contacts to the JSON file."""
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file)

def display_contacts(contacts):
    """Display all contacts in the list."""
    if not contacts:
        print("No contacts available.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contacts(contacts, query):
    """Search for contacts by name or phone number."""
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return results

def add_contact(contacts):
    """Add a new contact to the list."""
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    new_contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully.")

def update_contact(contacts):
    """Update an existing contact's details."""
    display_contacts(contacts)
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_phone = input(f"Enter the new phone number (current: {contact['phone']}): ")
            new_email = input(f"Enter the new email address (current: {contact['email']}): ")
            new_address = input(f"Enter the new address (current: {contact['address']}): ")
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print(f"Contact '{name}' updated successfully.")
            return
    print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Delete a contact from the list."""
    display_contacts(contacts)
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print(f"Contact '{name}' not found.")

def main():
    """Run the Contact Management System."""
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Display Contacts")
        print("2. Search Contacts")
        print("3. Add Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            query = input("Enter the name or phone number to search: ")
            search_results = search_contacts(contacts, query)
            if search_results:
                print(f"Search results for '{query}':")
                display_contacts(search_results)
            else:
                print(f"No contacts found matching '{query}'.")
        elif choice == '3':
            add_contact(contacts)
            save_contacts(contacts)  # Save after adding a new contact
        elif choice == '4':
            update_contact(contacts)
            save_contacts(contacts)  # Save after updating a contact
        elif choice == '5':
            delete_contact(contacts)
            save_contacts(contacts)  # Save after deleting a contact
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()