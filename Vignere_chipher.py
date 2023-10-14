from MaterialsforProject import vignere_letter

class GetUserText():
    def __init__(self, user_input):
        self.user_text = user_input

    def vignere_encrypt(self, key):
        result = ""
        extra_symbols = 0
        for i in range(0,len(self.user_text)):
            if check_symbol(self.user_text[i]) == "Extra Symbol":
                extra_symbols += 1
            result += vignere_letter(self.user_text[i], key, curr_index = i-extra_symbols)
        self.user_text = result
    
    def vignere_decrypt(self, key):
        result = ""
        extra_symbols = 0
        for i in range(0,len(self.user_text)):
            if check_symbol(self.user_text[i]) == "Extra Symbol":
                extra_symbols += 1
            # else:
            #     i-=1 
            result += vignere_letter(self.user_text[i], key, curr_index = i-extra_symbols, task = "decryption")
        self.user_text = result
    
    def getUserText(self):
        return self.user_text
        
        
class GetUserKey:
    def __init__(self, user_input):
        self.user_key = user_input

    def modify_user_key(self,userText):
        if len(self.user_key) <= len(userText):
            index = 0
            original_user_key = self.user_key
            while len(self.user_key) != len(userText):
                if index == len(original_user_key):
                    index = 0

                self.user_key += self.user_key[index]
                index += 1

    def is_key_valid(self):
        for i in self.user_key:
            if check_symbol(i) == "Extra Symbol":
                return False
        return len(self.user_key) #If key is empty returns False, 0 == False
    
    def getKey(self):
        return self.user_key

def handle_user_text():
    user_text = ""
    while True:
        try:
            user_text = GetUserText(input("Please Enter Text: "))
            # if text is just empty or only spaces
            if user_text.getUserText() == '' or user_text.getUserText().count(' ') == len(user_text.getUserText()):
                raise ValueError()
            break
        except ValueError:
            print("")
            print("Please type valid text")
    return user_text
    
def handle_user_key():
    user_key = ""
    while True:
        try:
            user_key = GetUserKey(input("Please Enter Key: "))
            if not user_key.is_key_valid():
                raise ValueError()
            break
        except ValueError:
            print("")
            print("Please type valid Key (a-z,A-Z)")
    return user_key

def handle_user_response():
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
    user_response = 3
    times_encrypted = 0
    while True:
        if user_response == 3:
            user_text = handle_user_text()
            user_key = handle_user_key()
            user_key.modify_user_key(user_text.getUserText())
        user_response = handle_user_response()
        
        if user_response == -1:
            print("It was fun, Bye Bye :)")
            print("Kind Regards,")
            print("George M.")
            return 0
        
        if user_response == 3:
            times_encrypted = 0
            continue
    
        if user_response == 1:
            times_encrypted += 1
            if times_encrypted + 1 == 27: #If user Encrypted his/her text so many times that now it is same as original
                times_encrypted = 0
                print("You encrypted too many times, now it is again original text ;)")
            user_text.vignere_encrypt(user_key.getKey())
            print(f"Your Encrypted Text: {user_text.getUserText()}")
            print("")
        
        if user_response == 2:
            if times_encrypted - 1 < 0 : #If youser wants to decrypt not yet encrypted text
                print("This is already an original text")
                continue
            times_encrypted -= 1 
            user_text.vignere_decrypt(user_key.getKey()) 
            print(f"Your Decrypted Text: {user_text.getUserText()}")
            print("")
    
main()
