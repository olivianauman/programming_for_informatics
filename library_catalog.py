# Olivia Nauman
#Homework Assignment 6

def readFile(filename):
    #open the file for reading
    readIn = open(filename, 'r')
    #ContentsofFile will read the file lines and put them into a list 
    ContentsofFile = readIn.read().splitlines()
    #close the file
    readIn.close()
    #return the list of file lines
    return ContentsofFile


def check_in_book(catalog_dictionary, book_title, author_name):
    #decision is initially nothing but a blank string, but we will utilize it later
    decision = ''
    # first we make sure that the book is one the library owns
    if (book_title, author_name) in catalog_dictionary:
        # we check it in by adding 1 to the count of this particular book (if it is one of the library's books)
        catalog_dictionary[(book_title, author_name)] += 1
        #return that you returned it and how many copies remain AFTER checking it in
        decision = "Returned, Remaining copies: " + str(catalog_dictionary[(book_title, author_name)])
    else:
        #if the book is not owned by the library, let the user know that you reject the book
        decision = "Not in catalog - Rejected"
    #return whether you can return it or not and the updated library catalog
    return decision, catalog_dictionary


def check_out_book(catalog_dictionary, book_title, author_name):
    #decision begins as an empty string which will be updated later
    decision = ''
    #if the book is a title the library carries
    if (book_title, author_name) in catalog_dictionary:
        #number of copies shows how many copies of a title the library has
        numberOfCopies = catalog_dictionary[(book_title, author_name)]
        #if there are more than 0 copies of the book, check it out by subracting 1 from the available amount
        if numberOfCopies > 0:
            numberOfCopies -= 1
            #decision tells the user that the book is available, being checked out for them, and adds a string of how many copies remain
            decision = "Book Available - Checked Out, Remaining copies: " + str(numberOfCopies)
            catalog_dictionary[(book_title, author_name)] = numberOfCopies
        else:
            #if there are no copies available, tell the user that they are unable to check out the book because there are zero copies available
            decision = "Book Unavailable - Rejected, Remaining copies: 0"
    else:
        #if the library does not carry the book, tell the user that their request is denied
        decision = "Not in catalog: Rejected."
    #return whether it can be checked out or not, why, and the updated library catalog
    return decision, catalog_dictionary


def book_transactions(file_contents, catalog_dictionary):
    # for each line in the given file, wordlist shows that line, split on the commas, in the list.
    for line in file_contents:
        wordlist = line.split(',')
        #the third element in the list tells the user whether the book is checked in or checked out
        #if the value reads 'out', call the check_out_book function 
        if 'Out' in wordlist[2]:
            decision, catalog_dictionary = check_out_book(catalog_dictionary, wordlist[0], wordlist[1])
        else:
            #if the value does not read 'out' then it reads 'in' which means you must call the check_in_book function
            decision, catalog_dictionary = check_in_book(catalog_dictionary, wordlist[0], wordlist[1])
        #print what you have done with the book and why
        print(decision)
    #return a copy of the updated dictionary
    return catalog_dictionary


def create_catalog(file_contents):
    # further down, we will be adding info to this dictionary so for now it is blank
    catalog_dictionary = {}
    # seperate the lines of the file into dictionary format
    for line in file_contents:
        wordlist = line.split(',')
        # the first and second elements of the list are the key for the third which is the value
        catalog_dictionary[(wordlist[0], wordlist[1])] = int(wordlist[2])
    #return the dictionary
    return catalog_dictionary
