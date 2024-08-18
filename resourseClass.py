from resourses import Book
from resourses import Magazine
from resourses import Lecture_CD
from resourses import Educational_DVD

def printBook(book):
    print(f"ISBN Number: {book.isbnNum}, Title: {book.title}, Format: {book.format}, Subject: {book.subject}, Rental Price per day: {book.rental}, Available Copies: {book.copies}")

def printMagazine(magazine):
    print(f"Magazine Number: {magazine.magazineNum}, Title: {magazine.title}, Format: {magazine.color}, Subject: {magazine.subject}, Rental Price per day: {magazine.rental}, Available Copies: {magazine.copies}")

def printDVD(Dvd):
    print(f"Educational DVD Number: {Dvd.DVDNum}, Title: {Dvd.title}, Subject: {Dvd.subject}, Rental Price per day: {Dvd.rental}, Available Copies: {Dvd.copies}")

def printCD(Cd):
    print(f"Lecture CD Number: {Cd.CDNum}, Title: {Cd.title}, Subject: {Cd.subject}, Rental Price per day: {Cd.rental}, Available Copies: {Cd.copies}")

class BookClass:
    def __init__(self):
        self.ListofBooks=[]
        self.initial()

    def initial(self):
        booka=Book(isbnNum="ISBN1234",title="The Solar System", format="Harcover", subject="Science", rental=15.00, copies=5)
        bookb=Book(isbnNum="ISBN9876",title="Eloquent JavaScript", format="Paperback", subject="Computer Science", rental=100.00, copies=8)
        bookc=Book(isbnNum="ISBN1290",title="Second World War", format="Hardcover", subject="History", rental=12.50, copies=1)
        self.ListofBooks.append(booka)
        self.ListofBooks.append(bookb)
        self.ListofBooks.append(bookc)

    def add_res(self):
        isbn_sample=input("Enter ISBN Number:")
        title_sample=input("Enter the Title:")
        format_sample=input("Enter the Format:")
        subject_sample=input("Enter the Subject:")
        rental_sample=float(input("Rental per day:"))
        copies_sample=int(input("Copies available:"))
        book0= Book(isbnNum=isbn_sample, title=title_sample, format=format_sample, subject=subject_sample,rental=rental_sample,copies=copies_sample)
        self.ListofBooks.append(book0)
        print("Book added")

    def remove_res(self):
        isbn_sample=input("Enter ISBN Number:")
        match_data=list(x for x in self.ListofBooks if x.isbnNum==isbn_sample)
        for x in match_data:
            self.ListofBooks.remove(x)
            print("Book Removed")

    def view_available(self):
        match_data=list(x for x in self.ListofBooks if x.copies>0)
        for x in match_data:
            printBook(book=x)

    def view_unavailable(self):
        match_data=list(x for x in self.ListofBooks if x.copies ==0)
        for x in match_data:
            printBook(book=x)

    def lend_res(self):
        isbn_sample=input("Enter ISBN Number:")
        copies1=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofBooks if x.isbnNum ==isbn_sample)
        for x in match_data:
            x.copies-=copies1
            print("Book Lent")

    def receive_res(self):
        isbn_sample=input("Enter ISBN Number:")
        copies=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofBooks if x.isbnNum == isbn_sample)
        for x in match_data:
            x.copies+=copies
            print("Books received")

    def filter_subject(self):
        subject_sample=input("Enter Subject:")
        match_data=list(x for x in self.ListofBooks if x.subject==subject_sample)
        for x in match_data:
            printBook(book=x)

class MagazineClass:
    def __init__(self):
        self.ListofMagazine=[]
        self.initial()

    def initial(self):
        magazine_a=Magazine(magazineNum="01",title="History of Cricket",color="color", subject="Sports", rental=5.00, copies=7)
        magazine_b=Magazine(magazineNum="02",title="Evolution of the Computer", color="black&white", subject="Technology", rental=3.00, copies=21)
        self.ListofMagazine.append(magazine_a)
        self.ListofMagazine.append(magazine_b)
       

    def add_res(self):
        magazine_sample=input("Enter Magazine Number:")
        title_sample=input("Enter the Title:")
        color_sample=input("Enter the Color type:")
        subject_sample=input("Enter the Subject:")
        rental_sample=float(input("Rental per day:"))
        copies_sample=int(input("Copies available:"))
        magazine_sample= Magazine(magazineNum=magazine_sample, title=title_sample, color=color_sample, subject=subject_sample,rental=rental_sample,copies=copies_sample)
        self.ListofMagazine.append(magazine_sample)
        print("Magazine added")

    def remove_res(self):
        magazine_sample=input("Enter Magazine Number:")
        match_data=list(x for x in self.ListofMagazine if x.magazineNum==magazine_sample)
        for x in match_data:
            self.ListofMagazine.remove(x)
            print("Magazine Removed")

    def view_available(self):
        match_data=list(x for x in self.ListofMagazine if x.copies>0)
        for x in match_data:
            printMagazine(magazine=x)

    def view_unavailable(self):
        match_data=list(x for x in self.ListofMagazine if x.copies==0)
        for x in match_data:
            printMagazine(magazine=x)

    def lend_res(self):
        magazine_sample=input("Enter Magazine Number:")
        copies1=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofMagazine if x.magazineNum ==magazine_sample)
        for x in match_data:
            x.copies-=copies1
            print("Magazine Lent")

    def receive_res(self):
        magazine_sample=input("Enter Magazine Number:")
        copies=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofMagazine if x.magazineNum == magazine_sample)
        for x in match_data:
            x.copies+=copies
            print("Magazine received")

    def filter_subject(self):
        subject_sample=input("Enter Subject:")
        match_data=list(x for x in self.ListofMagazine if x.subject==subject_sample)
        for x in match_data:
            printMagazine(magazine=x)

        

class Educational_DVD_Class:
    def __init__(self):
        self.ListofEdDVD=[]
        self.initial()

    def initial(self):
        EdDVD_a=Educational_DVD(DVDNum="10",title="Birth of the Solar System", subject="Astronomy", rental=2.50, copies=10)
        EdDVD_b=Educational_DVD(DVDNum="11",title="Pythagoras Theorem", subject="Maths", rental=1.00, copies=50)
        self.ListofEdDVD.append(EdDVD_a)
        self.ListofEdDVD.append(EdDVD_b)
       

    def add_res(self):
        EdDvd_sample=input("Enter Educational DVD Number:")
        title_sample=input("Enter the Title:")
        subject_sample=input("Enter the Subject:")
        rental_sample=float(input("Rental per day:"))
        copies_sample=int(input("Copies available:"))
        EdDvd_sample= Educational_DVD(DVDNum=EdDvd_sample, title=title_sample, subject=subject_sample,rental=rental_sample,copies=copies_sample)
        self.ListofEdDVD.append(EdDvd_sample)
        print("Educational DVD added")

    def remove_res(self):
        EdDvd_sample=input("Enter Educational DVD Number:")
        match_data=list(x for x in self.ListofEdDVD if x.DVDNum==EdDvd_sample)
        for x in match_data:
            self.ListofEdDVD.remove(x)
            print("Educational DVD Removed")

    def view_available(self):
        match_data=list(x for x in self.ListofEdDVD if x.copies>0)
        for x in match_data:
            printDVD(Dvd=x)

    def view_unavailable(self):
        match_data=list(x for x in self.ListofEdDVD if x.copies==0)
        for x in match_data:
            printDVD(Dvd=x)

    def lend_res(self):
        EdDvd_sample=input("Enter Educational DVD Number:")
        copies1=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofEdDVD if x.DVDNum ==EdDvd_sample)
        for x in match_data:
            x.copies-=copies1
            print("Educational DVD Lent")

    def receive_res(self):
        EdDvd_sample=input("Enter Educational DVD Number:")
        copies=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofEdDVD if x.DVDNum == EdDvd_sample)
        for x in match_data:
            x.copies+=copies
            print("Educational DVD received")

    def filter_subject(self):
        subject_sample=input("Enter Subject:")
        match_data=list(x for x in self.ListofEdDVD if x.subject==subject_sample)
        for x in match_data:
            printDVD(Dvd=x)


class LectureCD_Class:
    def __init__(self):
        self.ListofLecCD=[]
        self.initial()

    def initial(self):
        LecCD_a=Lecture_CD(CDNum="21",title="Basics of Western Music", subject="Music", rental=1.50, copies=11)
        LecCD_b=Lecture_CD(CDNum="22",title="Japanese Language", subject="Foreign Languages", rental=2.00, copies=3)
        self.ListofLecCD.append(LecCD_a)
        self.ListofLecCD.append(LecCD_b)
       

    def add_res(self):
        LecCD_sample=input("Enter Lecture CD Number:")
        title_sample=input("Enter the Title:")
        subject_sample=input("Enter the Subject:")
        rental_sampe=float(input("Rental per day:"))
        copies_sample=int(input("Copies available:"))
        LecCD_sample= Lecture_CD(CDNum=LecCD_sample, title=title_sample, subject=subject_sample,rental=rental_sampe,copies=copies_sample)
        self.ListofLecCD.append(LecCD_sample)
        print("Lecture CD added")

    def remove_res(self):
        LecCD_sample=input("Enter Lecture CD Number:")
        match_data=list(x for x in self.ListofLecCD if x.CDNum==LecCD_sample)
        for x in match_data:
            self.ListofLecCD.remove(x)
            print("Lecture CD Removed")

    def view_available(self):
        match_data=list(x for x in self.ListofLecCD if x.copies>0)
        for x in match_data:
            printCD(Cd=x)

    def view_unavailable(self):
        match_data=list(x for x in self.ListofLecCD if x.copies==0)
        for x in match_data:
            printCD(Cd=x)

    def lend_res(self):
        LecCD_sample=input("Enter Lecture CD Number:")
        copies1=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofLecCD if x.CDNum ==LecCD_sample)
        for x in match_data:
            x.copies-=copies1
            print("Lecture CD Lent")

    def receive_res(self):
        LecCD_sample=input("Enter Lecture CD Number:")
        copies=int(input("Number of copies:"))
        match_data=list(x for x in self.ListofLecCD if x.CDNum == LecCD_sample)
        for x in match_data:
            x.copies+=copies
            print("Lecture CD received")

    def filter_subject(self):
        subject_sample=input("Enter Subject:")
        match_data=list(x for x in self.ListofLecCD if x.subject==subject_sample)
        for x in match_data:
            printCD(Cd=x)