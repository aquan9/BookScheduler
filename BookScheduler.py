#Program to organize the books I read so that I know
#things in a timely fashion.
import datetime
import math
print(datetime.date.today())

print("Welcome to the book reading calculator")

titles = []
pages = []
time = 0
morebooks = True
while morebooks == True:
    titles.append(input("What is the name of the book?"))
    pages.append(int(input("How many pages are in this book?")))
    checkifdone = input("Another book?")
    print("Printing Check if done --> " + checkifdone)
    if(checkifdone.upper() == "NO" or checkifdone.upper() == "N"):
                           morebooks = False

    
                           
                           


time = int(input("In how many days do you want to read these?"))

print("Below is your calculated schedule")

for i in titles:
    print("\n\n\n")
    print(i)
    checknumber = titles.index(i)
    pagesPerDay = pages[checknumber] / time
    print(pagesPerDay)
    for b in range(0,time):
        print(datetime.date.today() + datetime.timedelta(days=b))
        print("Page " + str(math.ceil(((b+1)*pagesPerDay))))

        
        
    

