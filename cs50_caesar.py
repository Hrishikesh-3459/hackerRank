def caesar(k, plaintext):
    ciphertext = ""
    calc = 0
    for i in plaintext:
        if(i.isalpha()):
            if(i.islower()):
                calc = (ord(i) + k) % 123
                if(calc > 97 and calc < 122):
                    ciphertext += chr(calc)
                else:
                    x = calc % 26
                    ciphertext += chr(x + 97)
            if(i.isupper()):
                calc = (ord(i) + k) % 91
                if(calc > 65 and calc < 90):
                    ciphertext += chr(calc)
                else:
                    x = calc % 26
                    ciphertext += chr(x + 65)

        else:
            ciphertext += i
    print(ciphertext)
   
key = int(input("Key: "))
plaintext = input("Plaintext: ")
caesar(key, plaintext)

