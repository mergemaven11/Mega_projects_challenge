"""
    Randomly select a word from a file, have the user guess characters in the word. 
    For each character they guess that is not in the word, have it draw another part of a man hanging in a noose.
    If the picture is completed before they guess all the characters, they lose. 
    - Incomplete

"""
import random
from bisect import bisect_left

# Read and Randomly select word from file
f = open('Hangman_words.txt', 'r')
word_list = f.readlines()
Secret_word = random.choice(word_list).lower()

f.close()

#=================== MR HANGMAN ========================

welcome = print("""\
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | |_ \ / _ |  _ ` _ \ /  _` |  |_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 



                """)


HHEAD =  r"""
                |----------------
                |                |     
                                 0

                                      
                  """

HBODY = r"""
                      |----------------
                                      |
                                      0
                                      |
            """
LArm = r"""
                      |----------------
                                      |
                                      0
                                     /|
                  """

RArm = r""""
                      |----------------
                                      |
                                      0
                                     /|\
                  """


LLeg = r"""
                      |----------------
                                      |
                                      0
                                     /|\
                                     / 
                  """
RLeg = r"""
                      |------------------  
                      |                |
                      |                0
                      |               /|\
                      |               / \
                      |
                      |
                      |
                 |=========HANGMAN=============|

                  """

winner = r"""
                 _    _ _                       
| |  | (_)                      
| |  | |_ _ __  _ __   ___ _ __ 
| |/\| | | '_ \| '_ \ / _ \ '__|
\  /\  / | | | | | | |  __/ |   
 \/  \/|_|_| |_|_| |_|\___|_|   
                                """


executioner = [HHEAD, HBODY, LArm, RArm, LLeg, RLeg]

print(executioner[5])

#============================================================================


# Ask user to guess a letter
def Hangman():
    letters = list(Secret_word.rstrip().replace(' ', ''))
    count = 5
    correct_guesses = 0
    word_complete = len(letters)
    
# Check if letter exist in random word if not req another letter ; 8 tries
    
    try:
        while count > 0:      
            guess = input('Please guess a lowercase letter: ' )
            i = guess
            if i in letters:
                print("Pass")
                correct_guesses += 1
                if correct_guesses == word_complete:
                    print(winner + " \nYou've Guessed the SECRET WORD: " + Secret_word)
                
            else:                    # loop through each ascii art item in executioner list and print on each loop if true
                    print(" Word Not Found: " + str(count) + " Tries left")
                    count-=1
        if count == 0:
            print('GAME OVER LOST!' + RLeg + "SECRET WORD WAS: " + Secret_word)
        
            
    except ValueError:
        print("Letters only!")
       
            

                

# if letter exist print "Letter in word"


if __name__ == '__main__':
    Hangman()
