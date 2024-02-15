# Masterpiece!!!

# Making the the word be a 2d_list
def plain_text_to_2d_list(word):
    column_2d_list = []
    column_list = []

    counter = 0

    for index, char in enumerate(word):
        if index == counter:
            column_list = []
            column_list.append(char)
            column_2d_list.append(column_list)
            counter += 4 # This determines how many values inside a list of a column_2d_list(This can also change the encrypt word)
        else:
            column_list.append(char)

    # For creating an equal amount of values inside a list
    while len(column_2d_list[0]) != len(column_2d_list[len(column_2d_list) - 1]):
        column_2d_list[len(column_2d_list) - 1].append(" ") # Creates white space to get the equal amount of values

    return word, column_2d_list


#Taking the first index of the first list, then second list, then third list... once loops through every list, then it goes back and get the second index this time
def apply_cipher_depth_1(column_2d_list):
    cipher_list = []

    for x in range(len(column_2d_list[0])):
        column_list = []
        for scramble_list in column_2d_list:
            column_list.append(scramble_list[x])
        cipher_list.append(column_list)
    # print(cipher_list)
    return cipher_list

#Changing the values inside into a different character
# So inputs with only 1 letter can also be encrypted
#Note: I do not have a value to change for special characters (#, $, !, etc)
def apply_cipher_depth_2(cipher_2d_list:list):
    cipher_key_list = [
        ['a', 'n'],
        ['b', 'z'],
        ['c', 't'],
        ['d', 'y'],
        ['h', 'x'],
        ['m', 'w'],
        ['e', 'v'],
        ['f', 'u'],
        ['g', 's'],
        ['i', 'r'],
        ['j', 'q'],
        ['k', 'p'],
        ['l', 'o'],
        ['A', 'Q'],
        ['B', 'O'],
        ['C', 'Z'],
        ['D', 'N'],
        ['H', 'S'],
        ['M', 'X'],
        ['E', 'W'],
        ['F', 'Y'],
        ['G', 'V'],
        ['I', 'R'],
        ['J', 'P'],
        ['K', 'U'],
        ['L', 'T'],
        [' ', '%'],
        ]
    
    # print(cipher_2d_list)
    for index, cipher_list in enumerate(cipher_2d_list):
        for cipher_letter_index, letter in enumerate(cipher_list):
            for key_list in cipher_key_list:
                if letter in key_list: #.lower()
                    # print(f"{letter:<2} {index_2:<2} {key_list.index(letter.lower())}", end=' ')
                    if key_list.index(letter) == 0: #.lower()
                        cipher_2d_list[index][cipher_letter_index] = key_list[1]
                        
                    else:
                        cipher_2d_list[index][cipher_letter_index] = key_list[0]
    return cipher_2d_list


# Reversing the values inside of each list ["H", "O", "R"] -> ["R", "O", "H"]
def apply_cipher_depth_3(cipher_list_v1):
    cipher_list_v2 = []

    for x in cipher_list_v1:
        index_counter = len(x) - 1
        column_list = []
        for char in range(len(x)): # Loops through the first list by the amount of the values inside the first list and then the second and them so forth
            column_list.append(x[index_counter])
            index_counter -= 1
        cipher_list_v2.append(column_list)
    
    return cipher_list_v2, len(column_list)


# Getting the cipher text
def get_cipher_text(cipher_list_v2):
    cipher_text = ''
    for x in cipher_list_v2:
        for char in x:
            cipher_text += char

    return cipher_text




# The functions below are the deciphering parts


# This puts the cipher_text in a 2d list as the same length as the cipher_list from before
def apply_decipher_depth_1(cipher_text, length_column):
    decipher_2d_list = []
    column_list = []
    for letter in cipher_text:
        column_list.append(letter)
        if len(column_list) == length_column:
            decipher_2d_list.append(column_list)
            column_list = []
    return decipher_2d_list


def get_decipher_text(decipher_2d_list):
    decipher_text = ''
    for x in decipher_2d_list:
        for char in x:
            decipher_text += char

    return decipher_text


# The texts that will be displayed
def display(word, cipher, decipher):
    print(f"Word: {word}")
    print(f"Cipher: {cipher}")
    print(f"Decipher: {decipher}")

    
def main():

    word = input("Give me a word: ")
    print()

    # Ciphering
    word, column_2d_list =  plain_text_to_2d_list(word)
    cipher_list = apply_cipher_depth_1(column_2d_list)
    cipher_2d_list = apply_cipher_depth_2(cipher_list)
    cipher_2d_list, length_column = apply_cipher_depth_3(cipher_2d_list) 
    cipher_text = get_cipher_text(cipher_2d_list) # Get the cipher text


    # Deciphering (Used almost all the same functions to decrypt)
    decipher_2d_list = apply_decipher_depth_1(cipher_text, length_column)
    
    decipher_2d_list, x = apply_cipher_depth_3(decipher_2d_list) 
    decipher_2d_list = apply_cipher_depth_2(decipher_2d_list)
    decipher_2d_list = apply_cipher_depth_1(decipher_2d_list)
    decipher_text = get_decipher_text(decipher_2d_list) # Get the decipher text

    
    display(word , cipher_text, decipher_text)


if __name__ == '__main__':
    main()
