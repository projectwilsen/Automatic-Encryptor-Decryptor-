def decryptor():

    # Membuka File Cipher Text dalam bentuk txt
    fileciphertext = input("Nama File Cipher Text:")
    fileciphertext = fileciphertext + ".txt"
    with open(fileciphertext) as f:
        encpt = f.read()
        print("Cipher Text: ", encpt)
        symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "-", "_", ":", ";", "?", "/", '"', "'",
                  "<", ">"]
        for i in encpt:
            for y in symbol:
                if i == y:
                    encpt = encpt.replace(y, "")
        encptsplit = encpt.split()
        copy = encptsplit.copy()
        encpt = encpt.replace(" ", '')
        encpt = encpt.lower()

    print("")
    print("=== Polybius Decryptor ===")

    #Meminta kode
    password=input("Kode: ")
    a=encpt.replace(" ","")
    b=password.replace(" ","")
    dict_cipher = {"11":"a","12":"b","13":"c","14":"d","15":"e","16":"f","21":"g","22":"h","23":"i","24":"j","25":"k","26":"l","31":"m","32":"n","33":"o","34":"p","35":"q","36":"r","41":"s","42":"t","43":"u","44":"v","45":"w","46":"x","51":"y","52":"z","53":"0","54":"1","55":"2","56":"3","61":"4","62":"5","63":"6","64":"7","65":"8","66":"9"}
    key_list = list(dict_cipher.keys())
    val_list = list(dict_cipher.values())

    x=[]
    for i in b:
        if i not in x:
            x.append(i)
        else:
            continue

    y=[]
    for i in val_list:
        if i not in x:
            y.append(i)
    kode=x+y
    split_strings=[]

    for index in range(0, len(a), 2):
        split_strings.append(a[index : index + 2])
    plain = []

    for i in range(len(split_strings)):
      row = int(split_strings[i][0])
      col = int(split_strings[i][1])
      letter = kode[(row-1)*6 + col-1]
      plain.append(letter)

    i = 0
    listenc = []
    akhir = []
    hasilakhir = []
    z = 0

    while i < len(copy):
        for y in encptsplit[z]:
            listenc.append(y)
            a = int(len(listenc) / 2)
        for j in range(a):
            akhir.append(plain[j])

        def listtostring(akhir):
            a = " "
            return (a.join(akhir))

        hasilakhir.append(listtostring(akhir).replace(" ", ""))
        del encptsplit[0]
        del plain[0:len(akhir)]
        del listenc[0:len(listenc)]
        del akhir[0:len(akhir)]
        i += 1

    if len(encptsplit) == 1:
        for y in encptsplit[0]:
            listenc.append(y)
            a = int(len(listenc) / 2)
        for j in range(a - 1):
            akhir.append(plain[j])

        def listtostring(akhir):
            a = " "
            return (a.join(akhir))

        hasilakhir.append(listtostring(akhir).replace(" ", ""))

    def listtostring(hasilakhir):
        a = " "
        return (a.join(hasilakhir))

    print("Plain Text: ", listtostring(hasilakhir))

    print("")
    print("=== Vigenere Decryptor ===")

    cipher = listtostring(hasilakhir)
    symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "-", "_", ":", ";", "?", "/", '"', "'", "<",
              ">"]
    for i in cipher:
        for y in symbol:
            if i == y:
                cipher = cipher.replace(y, "")
    x = cipher.split()
    cipher = cipher.replace(" ", '')
    cipher = cipher.lower()

    # Meminta Kode
    kode = input("Kode: ")
    kode = kode.replace(" ", '')
    kode = kode.lower()
    list_kode = []
    for i in kode:
        list_kode.append(i)

    # Pengulangan Kode sesuai dengan panjang Cypher Text
    panjangkode = len(kode)
    while len(kode) < len(cipher):
        for i in range(len(cipher) - len(kode)):
            kode += list_kode[i % panjangkode]

    # Mengubah setiap elemen cypher text dan kode menjadi angka
    cipherjadiangka = []
    kodejadiangka = []
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
                "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
                "z": 25}
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())

    for i in cipher:
        a = alphabet.get(i)
        cipherjadiangka.append(a)

    for y in kode:
        b = alphabet.get(y)
        kodejadiangka.append(b)

    # Proses Perhitungan Kode
    total = []
    for i in range(len(cipherjadiangka)):
        tot = (cipherjadiangka[i] - kodejadiangka[i]) % 26
        total.append(tot)

    hasil = []
    for i in total:
        position = val_list.index(i)
        hasil.append(key_list[position])

    # Pemecahan kata berdasarkan spasi
    z = 0
    plaintext = []
    for i in x:
        b = 0
        hasilakhir = ''
        for y in i:
            a = hasil[b]
            b += 1
            hasilakhir += a

        del hasil[0:len(x[z])]
        z += 1
        plaintext.append(hasilakhir)


    def listtostring(plaintext):
        a = " "
        return (a.join(plaintext))

    print("Plain Text: ", listtostring(plaintext))

    def maketxt():
        f = open("plaintext.txt","a+")
        f.truncate(0)
        for i in listtostring(plaintext):
            f.write(i)

        f.close()
    maketxt()

decryptor()
