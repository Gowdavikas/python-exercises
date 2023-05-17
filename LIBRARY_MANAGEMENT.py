class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks


    def displayAvaliableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
        
    def lendBook(self, requestedbook):
        if requestedbook in self.availableBooks:
            print("You have now borrowed the book!")
            self.availableBooks.remove(requestedbook)
        else:
            print("Sorry, the book is not avaliable right now")
    
    def addBook(self, returnedbook):

        self.availableBooks.append(returnedbook)
        print("You have returned the book. Thank You!")
        pass

class Customer:

    def requestBook(self):
        print("Enter the name of the book you would like to borrow : ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which your returning")
        self.book = input()
        return self.book

library = Library(['Think and Grow rich', 'Try untill win', 'Because of You', 'Flower and God'])
customer = Customer()
while True:
    print("Enter 1 to display the avaliable books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userchoice = int(input())
    if userchoice == 1:
        library.displayAvaliableBooks()
    elif userchoice == 2:
        requestedbook = customer.requestBook()
        library.lendBook(requestedbook)
    elif userchoice == 3:
        returnedbook = customer.returnBook()
        library.addBook(returnedbook)
    elif userchoice == 4:
        print("Thank you!, Please visit again")
        break
