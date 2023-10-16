from MaterialsforProject import caesar_letter
from MaterialsforProject import greeting
from MaterialsforProject import goodbye

class GetUserText: 
    #Custom Class to modify user input as we please, Encrypting/Decrypting
    def __init__(self, user_input):
        self.text = user_input
       
    def caesar_text_encrypt(self):
        result=""
        for i in range(0,len(self.text)):
            result += caesar_letter(self.text[i]) # From caesar_letter Function we get Encrypted letter. For more information check function itself. 
        self.text = result

    def caesar_text_decrypt(self):
        result = ""
        for i in range(0,len(self.text)):
            result += caesar_letter(self.text[i],task = "decryption") # From caesar_letter Function we get Decrypted letter. For more information check function itself. 
        self.text = result
       
    def getText(self): #Method for returning modified(or not) user input
        return self.text
    

def handle_user_input(): #Handle wrong/bad texts
    text = ""
    while True:
        try:
            text = GetUserText(input("Please Enter Text: "))
            # if text is just empty or only spaces
            if text.getText() == '' or text.getText().count(' ') == len(text.getText()):
                raise ValueError()
            break
        except ValueError:
            print("")
            print("Please type valid text")
    return text

def handle_user_response(): #Handle wrong/bad responses from user
    user_response = -1
    while True:
        try:
            print("What would you like: Encryption, Decryption, New Text ? (Type corresponding number)") 
            print("Encryption --> 1")
            print("Decryption --> 2")
            print("New Text --> 3")
            print("For Exit --> -1")
            user_response = int(input("Your Response: "))
            if user_response != 1 and user_response != 2 and user_response != 3 and user_response != -1:
                raise ValueError()
            print("")
            break;
        except ValueError:
            print("")
            print("Please just use 1, 2 or 3 as a response")
    return user_response

def main():
    greeting()
    user_response = 3
    text = ""
    times_encrypted = 0

    while True:
        if user_response == 3:
            text = handle_user_input()
            user_response = 0

        user_response = handle_user_response() # 1,2 or 3

        #If user wants to exit program
        if user_response == -1:
            goodbye()
            print("It was fun, Bye Bye :)")
            print("Kind Regards,")
            print("George M.")
            return 0
        
        #If user chose 3 it means he/she wants new text 
        if user_response == 3:
            user_response = 3
            times_encrypted = 0
            continue

        #If user chose 1 it means he/she wants to encrypt text 
        if user_response == 1:
            times_encrypted += 1 #to count how many times did we encrypted same text
            if times_encrypted + 1 == 27: #If user Encrypted his/her text so many times that now it is same as original
                times_encrypted = 0
                print("You encrypted too many times, now it is again original text ;)")
            text.caesar_text_encrypt() #Encrypting Text
            print(f"Your Encrypted Text: {text.getText()}")
            print("")

        #If user chose 2 it means he/she wants to decrypte current text
        if user_response == 2:
            if times_encrypted - 1 < 0 : #If user wants to decrypt not yet encrypted text
                print("This is already an original text")
                continue
            times_encrypted -= 1 #Counter for how many times we decrypted current text
            text.caesar_text_decrypt() #Decrypting Text
            print(f"Your Decrypted Text: {text.getText()}")
            print("")

main()
