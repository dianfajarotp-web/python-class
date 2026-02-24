class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False


    def return_book (self):
        self.is_borrowed = False


class Member:
    def __init__(self, nama, id_member):
        self.nama = nama
        self.id_member = id_member
        self.borrowed_books = []

class Staff:
    def __init__(self, nama, id_staff):
        self.nama = nama
        self.id_staff = id_staff

class BorrowTransaction:
    def __init__(self, book ,member, staff, borrow_date):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False

    def borrow_book(self):
        if not self.book.is_borrowed:
            self.book.is_borrowed = True
            self.member.borrowed_books.append(self)
            print(f"{self.member.nama} meminjam buku {self.book.title} oleh {self.staff.nama}")
        else:
            print("Maaf, buku", self.book.title, "sedang dipinjam.")
    
    def return_book(self):
        if not self.returned:
            self.book.return_book()
            self.returned = True
            print(f"{self.member.nama} mengembalikan buku {self.book.title} oleh {self.staff.nama}")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
member1 = Member("Alice", "M001")
staff1 = Staff("Bob", "S001")
transaction1 = BorrowTransaction(book1, member1, staff1, "2024-06-01")
transaction1.borrow_book()
transaction1.return_book()
