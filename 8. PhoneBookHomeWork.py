class PhoneBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, phone):
         self.contacts.append(Contact(name, phone))
    def output_contacts(self):
        for item in self.contacts:
            print(item)
    def delete_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name==name:
                self.contacts.remove(contact)
                print(f"Контакт з ім'ям {name}, було видалено")
    def delete_contact_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone==phone:
                self.contacts.remove(contact)
                print(f"Контакт з номером {phone}, було видалено")
    def search_contact_by_name(self,name):
        for contact in self.contacts:
            if contact.name==name:
                print(f"{contact.name}: {contact.phone}")
    def search_contact_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                print(f"{contact.name}: {contact.phone}")
class Contact:
    def __init__(self, name, phone):
        self.name=name
        self.phone=phone
    def __str__(self):
        return f"{self.name}: {self.phone}"
res=1
phonebook = PhoneBook()
while res!=0:
    print("------------Телефонна книга------------")
    try:
        res=int(input("1. Вивести всі контакти\n"
                "2. Створити новий контакт\n"
                "3. Видалити контакт за ім'ям\n"
                "4. Видалити контакт за номером\n"
                "5. Знайти контакти за ім'ям\n"
                "6. Знайти контакти за номером\n"
                "0. Вихід\n"
                "Ваша відповідь :: "))
    except ValueError:
        print("Введіть число!")
    if(res==1):
        print("Ваші контакти")
        phonebook.output_contacts()
    elif(res==2):
        name=input("Введіть ім'я :: ")
        phone=input("Введіть номер телефону :: ")
        phonebook.add_contact(name, phone)
    elif(res==3):
        name=input("Введіть ім'я контакту, який потрібно видалити :: ")
        phonebook.delete_contact_by_name(name)
    elif (res == 4):
        phone = input("Введіть номер контакту, який потрібно видалити :: ")
        phonebook.delete_contact_by_phone(phone)
    elif (res == 5):
        name = input("Введіть ім'я контакту, який потрібно знайти :: ")
        phonebook.search_contact_by_name(name)
    elif (res == 6):
        phone = input("Введіть номер контакту, який потрібно знайти :: ")
        phonebook.search_contact_by_phone(phone)
    elif(res==0):
        print("До зустрічі!")

