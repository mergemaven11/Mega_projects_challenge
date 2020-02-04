'''
Movie Store - Manage video rentals and controls when videos are checked out,
            due to return, overdue fees and for added complexity
            create a summary of those accounts which are overdue for contact.
'''
import timeit
# Set up Account
class Account:
    def __init__(self, name, email, phoneNum):
        self.name = name
        self.email = email
        self.phoneNum = phoneNum

    def movieStore(self):
        titles = {
            "Titanic": 12,
            "Jaws 3": 4,
            "Harry Potter": 16,
            "Star Wars": 3,
            "IT: Chapter two": 5,
            "Swamp thing": 0
        }
        for key, value in titles.items():
            if value > 0 in titles.values():
                print("Title: " + key + " \n# On hand: " + str(value))
            else:
                print(key + " is not in stock at the moment\n") 

        rental = input("Check out(CO) or Return(RTN)? ")

        if rental == "CO":
            coTitle = input("which title would you like? ")
            if coTitle in titles:
                init_num = titles[coTitle]
                init_num -= 1
                titles[coTitle] = init_num
                print("You have checked out " + coTitle)
                print("Total Titles Left: " + str(titles[coTitle]))    
        elif rental == "RTN":
            rtnTitle = input("What title will you be returning? ")
            if rtnTitle in titles:
                init_num = titles[rtnTitle]
                init_num += 1
                titles[rtnTitle] = init_num
            print("You have returned " + rtnTitle)
            print("Total Titles on hand: " + str(titles[rtnTitle]))
        
        
        

a1 = Account("Sam", "Email@noemail.com", 5555555555)
a1.movieStore()


