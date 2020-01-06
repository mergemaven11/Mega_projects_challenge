# Counts the number of individual words in a string.
#** For added complexity read these strings in from a text file and generate a summary.

def count_words():
     # read, open loop through words in file
    with open('count_words.txt', "r") as f:
        for line in f: 
            for word in line.split():
                totalWords = sum(1 for word in line.split()) 
                return totalWords






