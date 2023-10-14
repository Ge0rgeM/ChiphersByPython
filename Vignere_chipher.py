from MaterialsforProject import vignere_letter

class GetUserText():
    def __init__(self, user_input):
        self.user_text = user_input

    def vignere_encrypt(self, key):
        result = ""
        for i in range(0,len(self.user_text)):
            result += vignere_letter(self.user_text[i], key, curr_index = i)
        self.user_text = result
    
    def vignere_decrypt(self, key):
        result = ""
        for i in range(0,len(self.user_text)):
            result += vignere_letter(self.user_text[i], key, curr_index = i, task = "decryption")
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

    def getKey(self):
        return self.user_key


user_text = GetUserText(input("Word: "))
user_key = GetUserKey(input("Key: "))
user_key.modify_user_key(userText = user_text.getUserText())
print(f"userKey: {user_key.getKey()}")

user_text.vignere_encrypt(key = user_key.getKey())
print(f"Encr: {user_text.getUserText()}")

user_text.vignere_decrypt(key = user_key.getKey())
print(f"Decr: {user_text.getUserText()}")
