#Olivia Nauman
#Assignment 6

# HW6 stub file 
def create_catalog(file_contents):
    #further down, we will be adding info to this dictionary so for now it is blank
    catalog_dictionary = {}
    #read in file contents
    readIn = open(file_contents, 'r')
    #seperate the lines of the file into dictionary format
    for line in file_contents:
        wordlist = line.splitlines(',')
        #the first and second elements of the list are the key for the third which is the value
        
    readIn.close()
        
    return wordlist

def check_out_book(catalog_dictionary, book_title, author_name):
    #first we will check to see if the book is in the catalog dictionary 
    #if so, we check to see how many copies are available
        #if there are copies available, then check out one copy and update the tuple list and returns the string "Book Available - Checked Out, Remaining copies : (number of remaining copies)"
    
    #if not, let the user know that the library does not have the book with the string "Book Unavailable - Rejected, Remaining copies: 0"
    
def check_in_book(catalog_dictionary, book_title, author_name):
    #First this function checks if a book exists in the catalog
    #If so, check one copy in, and return the string "Returned, Remaining copies: (number of copies after chekc-in)"
    #If not, the string returned is "Not in catalog - Rejected"
    
def book_transactions(file_contents, catalog_dictionary):
     #based on whether a book needs to be checked in or out it calls the appropritate function and then 
    