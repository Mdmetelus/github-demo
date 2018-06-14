#vowelCount.py
#A simple Program That Tells You How Many Vowels You Have In Our Name
#
#Max Metelus

def main():
    print("A simple Program That Tells You How Many Vowels You Have In Our Name")

    vowelCount = 0
    
    x = (input("Please enter your Name or A Statment you Like the vowls counted from. "))
    lowerX = x.lower()
    #Inventory each possible vowel, and add it to the total.
    vowelCount += lowerX.count('a')
    vowelCount += lowerX.count('e')
    vowelCount += lowerX.count('i')
    vowelCount += lowerX.count('o')
    vowelCount += lowerX.count('u')
     #Print the added vowel total
    print("You Name, or Statment has " + str(vowelCount) +" Vowels" )
    
main()
