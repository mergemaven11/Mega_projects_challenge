'''

Count Vowels – 
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.

'''
# Define Vowels
vowels = ["a", "e", "i", "o", "u"]
# Keep Track of each vowel and place in dict
v_count = {}


def count_vowels(string):
    lower = string.lower()
    for vowel in vowels:
        count = lower.count(vowel)
        v_count[vowel] = count
    print(v_count)
    
            
    # return v_count

if __name__ == "__main__":
    count_vowels("Tomato")
