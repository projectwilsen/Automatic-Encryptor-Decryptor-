# Dibuat oleh:
#Kelompok 9
# Netri Alia Rahmi             162112133029
# Geraldus Wilsen              162112133043
# Christeigen Theodore Suhalim 162112133055

def encryptor():
    # Membuka File Plain Text dalam bentuk txt
    fileplaintext = input("Nama File Plain Text:")
    fileplaintext = fileplaintext + ".txt"
    with open(fileplaintext) as f:
        kata = f.read()
        print("Plain Text: ",kata)
        symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "-", "_", ":", ";", "?", "/", '"', "'","<", ">"]
        for i in kata:
            for y in symbol:
                if i == y:
                    kata = kata.replace(y, "")
        x = kata.split()
        kata = kata.replace(" ", '')
        kata = kata.lower()

    print("")
    print("=== Viginere Encryptor ===")

    # Meminta Kode
    kode = input("Kode: ")
    kode = kode.replace(" ", '')
    kode = kode.lower()
    list_kode = []
    for i in kode:
        list_kode.append(i)

    # Pengulangan Kode sesuai dengan panjang Cypher Text
    panjangkode = len(kode)
    while len(kode) < len(kata):
        for i in range (len(kata)-len(kode)):
           kode += list_kode[i%panjangkode]

    # Mengubah setiap elemen plain text dan kode menjadi angka
    katajadiangka = []
    kodejadiangka = []
    alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())

    for i in kata:
        a = alphabet.get(i)
        katajadiangka.append(a)

    for y in kode:
        b = alphabet.get(y)
        kodejadiangka.append(b)

    # Proses Perhitungan Kode
    total = []
    for i in range(len(katajadiangka)):
        tot = (katajadiangka[i] + kodejadiangka[i])%26
        total.append(tot)

    hasil = []
    for i in total:
            position = val_list.index(i)
            hasil.append(key_list[position])

    #Pemecahan kata berdasarkan spasi
    z = 0
    hasilkata = []
    for i in x:
        b = 0
        hasilakhir = ''
        for y in i:
            a = hasil[b]
            b += 1
            hasilakhir += a

        del hasil[0:len(x[z])]
        z += 1
        hasilkata.append(hasilakhir)

    def listtostring(hasilkata):
        a =" "
        return (a.join(hasilkata))

    print("Cipher Text: ", listtostring(hasilkata))

    # Memulai Polybius Encryptor
    print("")
    print("=== Polybius Encryptor ===")
    kata = listtostring(hasilkata)
    symbol = ["!","@","#","$","%","^","&","*","(",")",",",".","-","_",":",";","?","/",'"',"'","<",">"]
    for i in kata:
        for y in symbol:
            if i == y:
                kata = kata.replace(y,"")
    x = kata.split()
    kata = kata.replace(" ", '')
    kata = kata.upper()

    # Meminta Kode
    kode = input("Kode: ")
    kode = kode.upper()

    # Dictionary Polybius Table awal
    dict_cipher = {"11":"A","12":"B","13":"C","14":"D","15":"E","16":"F","21":"G","22":"H","23":"I","24":"J","25":"K","26":"L","31":"M","32":"N","33":"O","34":"P","35":"Q","36":"R","41":"S","42":"T","43":"U","44":"V","45":"W","46":"X","51":"Y","52":"Z","53":"0","54":"1","55":"2","56":"3","61":"4","62":"5","63":"6","64":"7","65":"8","66":"9"}
    key_list = list(dict_cipher.keys())
    val_list = list(dict_cipher.values())

    # Memecah kode menjadi menjadi sebuah list
    listkode = []
    for i in kode:
        listkode.append(i)

    # Mengupdate setiap value dalam list value
    for i in listkode:
        for a in val_list:
            if i == a:
                val_list.remove(a)
            else:
                continue

    valuelist = listkode + val_list

    #elemen duplikasi / double yang ada dalam list
    val_list_clear = list(dict.fromkeys(valuelist))
    if " " in val_list_clear:
        val_list_clear.remove(" ")

    #Membuat dictionary dengan cara mengambil key dari key_list dan value dari val_list_clear
    cipherdict = dict(zip(key_list,val_list_clear))
    key1_list = list(cipherdict.keys())
    val1_list = list(cipherdict.values())

    hasil =[]
    for i in kata:
        position = val1_list.index(i)
        hasil.append(key1_list[position])

    # Pemecahan kata berdasarkan spasi
    z = 0
    hasilkata = []
    for i in x:
        b = 0
        hasilakhir = ''
        for y in i:
            a = hasil[b]
            b += 1
            hasilakhir += a

        del hasil[0:len(x[z])]
        z += 1
        hasilkata.append(hasilakhir)

    def listtostring(hasilkata):
        a ="  "
        return (a.join(hasilkata))

    print("Cipher Text: ", listtostring(hasilkata))

    def maketxt():
        f = open("ciphertext.txt","a+")
        f.truncate(0)
        for i in listtostring(hasilkata):
            f.write(i)

        f.close()
    maketxt()

encryptor()