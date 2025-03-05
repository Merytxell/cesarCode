import sys

def cesar_code(text, key):
    messageCrypted = ""

    for c in text:
        if 'a' <= c <= 'z':
            newLetter = chr(((ord(c) - ord('a') + key) % 26) + ord('a'))
            messageCrypted += newLetter
        else:
            messageCrypted += c

    return messageCrypted

# Vérifier si des arguments sont passés en ligne de commande
if len(sys.argv) > 2:
    message = sys.argv[1]
    key = int(sys.argv[2])
else:
    message = input("Entrez le message à chiffrer : ")
    key = int(input("Entrez la clé : "))

cryptedText = cesar_code(message, key)
print("Texte chiffré :", cryptedText)
