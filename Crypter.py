from hashlib import sha256
entree = input("entrez le nom du fichier a chiffrer/déchiffrer: ")
sortie = input("entrez le nom du fichier final: ")
key = input("entrez la clé: ")
keys = sha256(key.encode('utf-8')).digest()
with open(entree,'rd') as f_entree:
    with open(sortie,'wb') as f_sortie:
        i = 0
        with f_entree.peek() :
            c = ord(f_entree.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_sortie.write(b)
            i = i + 1