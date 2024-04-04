#Student Name: Luis Gabriel Stedile Portella
#Program Title: 
#Description: 
"""
Design and develop a program that presents the user with a “Mad Libs” type game, where a random choice of
words is read from one file, then interjected into a story read from another file.
"""
import csv

def main():

    #Declaration of variables and initial lists
    choice = ""
    letters = ["","a","b","c","d","e"]
    numbers = ["","1","2","3","4","5"]
    user_choices = [""]
    print("The Itsy Bitsy Aardvark\n")

    #Assembiling the choices of the user

    #Manipulation of the choices file
    with open("P2 - Aardvark/the_choices_file.csv","r") as file_csv_reader:
        file_choices = csv.reader(file_csv_reader)
    
        #Printing options and descriptions of the options to the user/loops over each row
        for row in file_choices:

            #Description of the option itself
            print(f"Please choose {row[0]}:")

            #loops over each element of row (loops over all options)
            for letter in range(1,len(letters)):

                #Printing the actual options
                print(f"{letters[letter]})  {row[letter]}")
                
            #Making sure a valid option is inputed
            while not (choice in letters or choice in numbers) or choice == "":
                choice = str.lower(input("Enter choice (a-e): "))
            
            #Is acconting for index 0 of the choices file (index 0 = description)
                
            #Getting the user's choice if the user response was a letter
            if not choice.isdigit():
                user_choices.append(row[letters.index(choice)])

            #Getting the user's choice if the user response was a number
            else:
                choice = int(choice)
                user_choices.append(row[choice])

            choice = ""
            print()

    #Opening and geting the text file
    with open("P2 - Aardvark/the_story_file.txt","r") as text_story:
        story_read = text_story.read()

    #Loops for each letter in the text, if the letter is the value sinalized to be replaced. The program is going to replace it for the option choose by the user
    print("Your Completed Story:\n")
    for i in story_read:
        if i.isdigit():
            i = int(i)

            #Prints the option
            print(str.upper(user_choices[i]),end="")
        elif i == "_":

            #Remove underscores from the text
            print("",end="")
        else:

            #Just print other letters normally
            print(i,end="")

    print("\n")

if __name__ == "__main__":
    main()