from resourseClass import BookClass
from resourseClass import MagazineClass
from resourseClass import Educational_DVD_Class
from resourseClass import LectureCD_Class

Books = BookClass()
Magazines = MagazineClass()
Educationals = Educational_DVD_Class()
Lectures = LectureCD_Class()

def menu():
    print("Select your resourse")
    print("1 - Books")
    print("2 - Magazines")
    print("3 - Educational DVDs")
    print("4 - Lecture CDs")
    print("0 - Quit")
    menu_input=1
    while menu_input > 0:
        menu_input=int(input("Enter your resourse number:-"))
        if menu_input == 0:
            print("Thankyou for using library system")

        elif menu_input ==1:
            menu_book()
            break

        elif menu_input ==2:
            menu_magazine()
            break

        elif menu_input ==3:
            menu_dvd()
            break

        elif menu_input ==4:
            menu_cd()
            break

        else:
            print("Invalid input")
            menu()

def menu_book():
        menu_input =1
        while menu_input > 0:
            print("1 - Add Book")
            print("2 - Remove Book")
            print("3 - Lend Book")
            print("4 - View unavailable Books")
            print("5 - View available Books")
            print("6 - Receive Book")
            print("7 - Filter Subject")
            print("0 - Change Resourse")
            menu_input=int(input("Enter your option:"))
            if menu_input ==1:
                Books.add_res()
                

            elif menu_input ==2:
                Books.remove_res()
                

            elif menu_input ==3:
                Books.lend_res()
                

            elif menu_input ==4:
                Books.view_unavailable()
                

            elif menu_input ==5:
                Books.view_available()
                

            elif menu_input ==6:
                Books.receive_res()
                
            elif menu_input ==7:
                Books.filter_subject()

            elif menu_input ==0:
                menu()

            else:
                print("Invalid Input!TRY AGAIN")
                menu_book()
def menu_magazine():
        menu_input =1
        while menu_input > 0:
            print("1 - Add Magazine")
            print("2 - Remove Magazine")
            print("3 - Lend Magazine")
            print("4 - View unavailable Magazines")
            print("5 - View available Magazines")
            print("6 - Receive Magazine")
            print("7 - Filter Subject")
            print("0 - Change Resourse")
            menu_input=int(input("Enter your option:"))
            if menu_input ==1:
                Magazines.add_res()
                

            elif menu_input ==2:
                Magazines.remove_res()
                

            elif menu_input ==3:
                Magazines.lend_res()
                

            elif menu_input ==4:
                Magazines.view_unavailable()
                

            elif menu_input ==5:
                Magazines.view_available()
                

            elif menu_input ==6:
                Magazines.receive_res()
                
            elif menu_input ==7:
                Magazines.filter_subject()

            elif menu_input ==0:
                menu()

            else:
                print("Invalid Input!TRY AGAIN")
                menu_magazine()
def menu_dvd():
        menu_input =1
        while menu_input > 0:
            print("1 - Add Educational DVD")
            print("2 - Remove Educational DVD")
            print("3 - Lend Educational DVD")
            print("4 - View unavailable Educational DVD")
            print("5 - View available Educational DVD")
            print("6 - Receive Educational DVD")
            print("7 - Filter Subject")
            print("0 - Change Resourse")
            menu_input=int(input("Enter your option:"))
            if menu_input ==1:
                Educationals.add_res()
                

            elif menu_input ==2:
                Educationals.remove_res()
                

            elif menu_input ==3:
                Educationals.lend_res()
                

            elif menu_input ==4:
                Educationals.view_unavailable()
                

            elif menu_input ==5:
                Educationals.view_available()
                

            elif menu_input ==6:
                Educationals.receive_res()
                
            elif menu_input ==7:
                Educationals.filter_subject()

            elif menu_input ==0:
                menu()

            else:
                print("Invalid Input!TRY AGAIN")
                menu_dvd()
def menu_cd():
        menu_input =1
        while menu_input > 0:
            print("1 - Add Lecture CD")
            print("2 - Remove Lecture CD")
            print("3 - Lend Lecture CD")
            print("4 - View unavailable Lecture CD")
            print("5 - View available Lecture CD")
            print("6 - Receive Lecture CD")
            print("7 - Filter Subject")
            print("0 - Change Resourse")
            menu_input=int(input("Enter your option:"))
            if menu_input ==1:
                Lectures.add_res()
                

            elif menu_input ==2:
                Lectures.remove_res()
                

            elif menu_input ==3:
                Lectures.lend_res()
                

            elif menu_input ==4:
                Lectures.view_unavailable()
                

            elif menu_input ==5:
                Lectures.view_available()
                

            elif menu_input ==6:
                Lectures.receive_res()
                
            elif menu_input ==7:
                Lectures.filter_subject()

            elif menu_input ==0:
                menu()

            else:
                print("Invalid Input!TRY AGAIN")
                menu_magazine()

print("\n\n\n\n\n\n\n\n-----------------------------------------------------------------------------")
print("Hello and Welcome to the university Library System ")
print("\nOur system provides you with the ability to search for resources based on their attributes\n\nHave a nice day!!")
print("\n*******************************************************************************************")
menu()
