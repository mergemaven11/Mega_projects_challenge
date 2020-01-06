# Enter a string and the program will reverse it and print it out.

def rev():
    # Get user input and store in variable 
    string = input('Please Enter a word: ')
    # method merges all of the characters resulting from the reversed iteration into a new string
    rev_string = ''.join(reversed(string))  
    # Print the string
    print(rev_string)
