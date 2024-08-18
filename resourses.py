class Book:
    def __init__(self, isbnNum, title, format, subject, rental, copies):
        self.isbnNum = isbnNum
        self.title = title
        self.format = format
        self.subject = subject
        self.rental = rental
        self.copies = copies


class Magazine:
    def __init__(self, magazineNum, title, color, subject, rental, copies):
        self.magazineNum = magazineNum
        self.title = title
        self.color = color
        self.subject = subject
        self.rental = rental
        self.copies = copies
    
class Educational_DVD:
    def __init__(self, DVDNum, title, subject, rental, copies):
        self.DVDNum = DVDNum
        self.title = title
        self.subject = subject
        self.rental = rental
        self.copies = copies


class Lecture_CD:
    def __init__(self, CDNum, title, subject, rental, copies):
        self.CDNum = CDNum
        self.title = title
        self.subject = subject
        self.rental = rental
        self.copies = copies