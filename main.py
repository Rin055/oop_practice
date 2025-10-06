#Library
class Book:
    def __init__(self, title, author, year):
        self.title = title  
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if self.dont_repeat_same_book(book):
            print("This book already exists in the library.")
        else:
            self.books.append(book)
            print(f"Added: {book.title} by {book.author} ({book.year})")
    
    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                print(f"Removed: {title}")
                return
        print(f"Book '{title}' not found.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in library:")
            for book in self.books:
                print(f"- {book.title} by {book.author} ({book.year})")

    def dont_repeat_same_book(self, book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                return True
        return False


#Bank
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance    


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")



library = Library()

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)  # Duplicate book for testing

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

library.remove_book("1984")
library.list_books()

account = BankAccount("John Doe", 500)
account.deposit(200)
account.withdraw(100)
print("Current balance:", account.get_balance())

savings_account = SavingsAccount("Jane Doe", 1000, 0.05)
savings_account.apply_interest()
print("Savings account balance:", savings_account.get_balance())
