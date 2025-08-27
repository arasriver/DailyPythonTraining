class PhoneBook:
    def __init__(self):
        self.contact = {}

    def add_contact(self):
        name = input("Enter a name: ").strip()
        phone = input("Enter a phone number: ").strip()
        email = input("Enter an email: ").strip()
        self.contact[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added successfully!")

    def update_contact(self):
        update = input("Enter a name you want to update: ").strip()
        if update in self.contact:
            updated_phone = input("Enter a phone number: ").strip()
            if updated_phone != "":
                self.contact[update]["phone"] = updated_phone

            updated_email = input("Enter an email: ").strip()
            if updated_email != "":
                self.contact[update]["email"] = updated_email

            print(f"Contact {update} updated successfully!")
        else:
            print(f"{update} not found")

    def delete_contact(self):
        delete = input("Enter a name you want to delete: ").strip()
        if delete in self.contact:
            self.contact.pop(delete)
            print(f"Contact {delete} deleted successfully!")
        else:
            print(f"{delete} not found")

    def show_contact(self):
        if self.contact:
            print(self.contact)
        else:
            print("Phone book is empty!!")

    def start_phonebook(self):
        while True:
            print("\nWelcome to Phone Book")
            print(" 1. Add a contact \n 2. Update a contact \n 3. Delete a contact \n 4. Show contacts \n 5. Exit")
            choice = input("\nEnter a number: ").strip()
            if choice not in ["1", "2", "3", "4", "5"]:
                print("Enter a valid choice!")
                continue
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.update_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                self.show_contact()
            elif choice == "5":
                print("Exit")
                break


if __name__ == "__main__":
    phonebook = PhoneBook()
    phonebook.start_phonebook()
