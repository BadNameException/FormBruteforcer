def CaesarEncoder(message, shift):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    message = message.lower()

    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)

            index = (index + shift)%(len(alphabet))

            if index < 0:
                index = index + len(alphabet)

            result = result + alphabet[index]

        else:
            result = result + letter

    return result + " "


DictionaryFile = open("Wordlists/unEncodedWordlist.txt")
Dictionary = []
for word in DictionaryFile:
    listFromFile = word.split(",")
    for splitWord in listFromFile:
        Dictionary.append(splitWord)
Encryptedwordlist = []

for word in Dictionary:
    Encryptedwordlist.append(CaesarEncoder(word, 11))

file = open("Wordlists/EncodedWordlist.txt", "w+")
for caesarWord in Encryptedwordlist:
    file.write(caesarWord)
file.close()
