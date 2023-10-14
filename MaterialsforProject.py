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
    else : #For Decryption
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
        

def vignere_letter(letter, key, curr_index, task = "encryption"):
    if task == "encryption":
        if (letter>='A' and letter<='Z') or (letter >= 'a' and letter <='z'):
            if letter.isupper():
                return chr(65 + ((ord(letter)-65 + ord((key[curr_index]).upper())-65) % 26))
            elif letter.islower():
                return chr(97 + ((ord(letter)-97 + ord((key[curr_index]).lower())-97) % 26))
                
        else: # If letter is actually a symbol. We DO NOT change it
            return letter
    else : #For Decryption
        if (letter>='A' and letter<='Z') or (letter >= 'a' and letter <='z'):
            if letter.isupper():
                return chr(65 + (abs((ord(letter) - ord((key[curr_index]).upper())))%26))
            elif letter.islower():
                return chr(97 + (abs((ord(letter) - ord((key[curr_index]).lower())))%26))
        else: # If letter is actually a symbol. We DO NOT change it
            return letter