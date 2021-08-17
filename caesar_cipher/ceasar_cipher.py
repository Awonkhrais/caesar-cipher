import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()


def encrypt(plain, key):

    encrypt_text = ''
    
    for char in plain:

        if char.islower():
            encrypt_text += chr((ord(char) + key-97) % 26 + 97)

        elif char.isupper():
            encrypt_text += chr((ord(char) + key-65) % 26 + 65)

        else:
            encrypt_text += char
            
    return encrypt_text

def decrypt(encoded, key):
    original_text = encrypt(encoded, -key)
    return original_text

def count_words(text):

    candidate_words = text.split()

    word_count = 0 

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
     
            # print('not english word or name', word)

    return word_count

def crack(encrypted):
    for i in range(len(encrypted.split())):
        candidate_dec = decrypt(encrypted, i)
        word_count = count_words(candidate_dec)
        percentage = int(word_count / len(candidate_dec.split()) * 100)
        if percentage > 50:
            decrypt_word = candidate_dec
    # print (decrypt_word)
    return decrypt_word




if __name__ == "__main__":
    text = "Hello I am Awon Khrais "
    encrpt = encrypt(text, 3)
    print(encrpt)
    # print(decrypt(encrpt, 5))
    crack(encrpt)
