# message= "c'est donc ça c’est bien sur l’incroyable bazar dont j’ai vague mémoire à mon sommeil troublé"
# cle=24


def cesar_code(text, key):

    messageCrypted=""

    for c in text:
        if 'a' <= c <='z':
            newLetter = chr(((ord(c) - ord('a')+ key)%26)+ord('a'))
            messageCrypted += newLetter

    else:
       messageCrypted += c
       return messageCrypted

message = input("Entrez le message à chiffrer :")
key = int(input("Entrez la clé : "))

cryptedText = cesar_code(message,key)
print(cryptedText)
