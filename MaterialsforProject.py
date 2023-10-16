def caesar_letter(letter,task="encryption"): # We pass 2 arguments: letter, that needs to be encrypted/decrypted and task. By default it is Encyption
    #Since we are only implementing Caesar Cipher, we can use 2 strings. 
    # One for storing normal alphabet and the other for Caesar Cipher. (Each letter moved by 4 places) 
    normal_AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    caesar_AZ = "XYZABCDEFGHIJKLMNOPQRSTUVW"

    if task == "encryption":
        if (letter>='A' and letter<='Z') or (letter >= 'a' and letter <='z'): #We only Encrypt letters and not symbols nor spaces...
            if letter.isupper():
                #Since we store letters in uppercase (in our variables) 
                #if letter is already in uppercase we just search
                #for letter in caesar_AZ on same index as it was in normal_AZ.
                return caesar_AZ[normal_AZ.find(letter)] 
            else: #Not uppercase
                #Since we store letters in uppercase (in our variables) 
                #if letter is NOT already in uppercase we just transform
                #it in uppercase (temporarily) then search
                #for letter in caesar_AZ on same index as it was in normal_AZ 
                #and finally returning encrypted letter in lowercase.
                return (caesar_AZ[normal_AZ.find(letter.upper())]).lower()
        else: # If letter is actually a symbol. We DO NOT change it
            return letter
    elif task.lower() == "decryption": #For Decryption
        if (letter>='A' and letter<='Z') or (letter >= 'a' and letter <='z'): #We only Encrypt letters and not symbols nor spaces...
            if letter.isupper():
                #Since we store letters in uppercase (in our variables) 
                #if letter is already in uppercase we just search
                #for letter in normal_AZ on same index as it was in caesar_AZ.
                return normal_AZ[caesar_AZ.find(letter)]
            else: #Not uppercase
                #Since we store letters in uppercase (in our variables) 
                #if letter is NOT already in uppercase we just transform
                #it in uppercase (temporarily) then search
                #for letter in normal_AZ on same index as it was in caesar_AZ 
                #and finally returning encrypted letter in lowercase.
                return (normal_AZ[caesar_AZ.find(letter.upper())]).lower()
        else:# If letter is actually a symbol. We DO NOT change it
            return letter
        

#letter fo exryption or decryption
#key
#curr_index to match index of letter in the word to the index of letter in key, for easier encryption and decryption
#task by default is encryption
def vigenere_letter(letter, key, curr_index, task = "encryption"): 
    if task.lower() == "encryption":
        if (letter>='A' and letter<='Z') or (letter >= 'a' and letter <='z'):
            if letter.isupper():
                return chr(ord('A')+(ord(letter)+ord(key[curr_index].upper()))%26) #we need to move from 'A' letter (word[i]+key[i])%26 times
            elif letter.islower():
                return chr(ord('A')+(ord(letter.upper())+ord(key[curr_index].upper()))%26).lower() #we need to move from 'A' letter (word[i]+key[i])%26 times, but return lowercase
                
        else: # If letter is actually a symbol. We DO NOT change it
            return letter
    elif task.lower() == "decryption" : #For Decryption
        if (letter>='A' and letter<='Z') or (letter >= 'a' and letter <='z'):
            if letter.isupper():
                return chr(ord('A') + ((ord(letter) - ord((key[curr_index]).upper()))%26)) #we need to move from 'A' letter (word[i]-key[i])%26 times
            elif letter.islower():
                return chr(ord('A') + ((ord(letter.upper()) - ord((key[curr_index]).upper())))%26).lower() #we need to move from 'A' letter (word[i]-key[i])%26 times, but return lowercase
        else: # If letter is actually a symbol. We DO NOT change it
            return letter

def check_symbol(symbol): #checks symbol is letter or not
    if (symbol>='A' and symbol<='Z') or (symbol >= 'a' and symbol <='z'):
        return "Letter"
    else:
        return "Extra Symbol"
    
def greeting():
    print("")
    print("...........................................................................................................")
    print("|>---HH----------HH------EEEEEEEEEEEEE------LL-------------------LL------------------------OOOOOOO--------|")
    print("|>---HH----------HH------EE-----------------LL-------------------LL----------------------OO-------OO------|")
    print("|>---HH----------HH------EE-----------------LL-------------------LL--------------------OO-----------OO----|")
    print("|>---HH----------HH------EE-----------------LL-------------------LL-------------------OO-------------OO---|")
    print("|>---HHHHHHHHHHHHHH------EEEEEEEEEEEEE------LL-------------------LL-------------------OO-------------OO---|")
    print("|>---HH----------HH------EE-----------------LL-------------------LL-------------------OO-------------OO---|")
    print("|>---HH----------HH------EE-----------------LL-------------------LL--------------------OO-----------OO----|")
    print("|>---HH----------HH------EE-----------------LL-------------------LL---------------------OO---------OO-----|")
    print("|>---HH----------HH------EEEEEEEEEEEEE------LLLLLLLLLLLLLLL------LLLLLLLLLLLLLLL----------OOOOOOOOO-------|")
    print("...........................................................................................................")
    print("")

def goodbye():
    print("")
    print("...........................................................")
    print("|>----BBBBBBBB---------YY--------YY------EEEEEEEEEEEEE----|")
    print("|>----BB----BBBB--------YY------YY-------EE---------------|")
    print("|>----BB------BBB--------YY----YY--------EE---------------|")
    print("|>----BB-------BB---------YY--YY---------EE---------------|")
    print("|>----BBBBBBBBBB-----------YYYY----------EEEEEEEEEEEEE----|")
    print("|>----BB------_BB-----------YY-----------EE---------------|")
    print("|>----BB------BBB-----------YY-----------EE---------------|")
    print("|>----BB----BBBB------------YY-----------EE---------------|")
    print("|>----BBBBBBBB--------------YY-----------EEEEEEEEEEEEE----|")
    print("...........................................................")
    print("")
