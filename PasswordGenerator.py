
import string,random

# Define minimum password length as a tip for user 
min_Password_Length = 8

# characters percentages % in a password ----- Total = 100
numbersWT   = 40
uLettersWT  = 20
lLettersWT  = 20
symbolsWT   = 20

# Available characters to be used 
numbers     =list(string.digits)
upperCase   =list(string.ascii_uppercase)
lowerCase   =list(string.ascii_lowercase)
symbols     =list(string.punctuation)

############################### DON'T CHANGE VALUES BELOW THIS LINE #######################

# Define a class to combine data about each part of password 
class charDetails:
    percentage=0
    charList=[]
    
    # constructor 
    def __init__(self,percentage,charList):
        self.percentage=percentage
        self.charList=charList

    # generate a list of characters from a type 
    def pickedChars(self,length:int) ->list:
        count=round(length*self.percentage/100)
        random.shuffle(self.charList)
        pickedList=[]
        for i in range(count):
            pickedList.append(random.choice(self.charList))
        return pickedList
            

def password(length:int) ->str:
        # Generate parts of Password 
        n=charDetails(numbersWT,numbers).pickedChars(length)
        u=charDetails(uLettersWT,upperCase).pickedChars(length)
        l=charDetails(lLettersWT,lowerCase).pickedChars(length)
        s=charDetails(symbolsWT,symbols).pickedChars(length)

        finalList = n+u+l+s
        random.shuffle(finalList)
        
        # Make sure the generated password list has the required length 
        if len(finalList)>length:
            finalList=finalList[0:length]
        elif len(finalList)<length:
            for i in range(length-len(finalList)):
                finalList.append(random.choice(numbers+upperCase+lowerCase+symbols))

        #Create A String From The Created Final List 
        generatedPassword="".join(finalList)

        return generatedPassword

def main():
    print("Welcome to Password Generator v1.0")
    print("#--------------------------------#")
    print("... Press (C) to exit the program or follow instructions below ")
    print(2*"\n")


    while True:
        try:
            # Ask user for password length 
            passwordLength = input(f"-> How many characters in password (minimum {min_Password_Length})?\n").strip()

            # Exit program when user press special character
            if passwordLength.capitalize()=="C":
                break
            # Convert input to int type 
            passwordLength=int(passwordLength)

            # Proceed 
            if passwordLength>=min_Password_Length:
                # Generate
                print(password(passwordLength))

                # give user options to (regenerate password with same length) (create new with new length) ( exit ) 
                while True:
                    operation=input("press (R) to re-generate || (N) to create new length password || (C) to exit > ").strip().capitalize()
                    if operation =="C":
                        break
                    elif operation =="R":
                        print(password(passwordLength)) 
                    elif operation=="N":
                        raise                       
                break
            else:
                raise KeyError

        except KeyError:
            print(f"WRONG INPUT ; only a number above {min_Password_Length} is allowed !")
        except:
            continue
           
main()