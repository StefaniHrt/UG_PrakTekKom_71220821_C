print ("=========================")
print ("Operasi Matematika")
print ("1. Jumlah [+]")
print ("2. Kurang [-]")
print ("3. Kali [*]")
print ("4. Bagi [/]")
print ("=========================")
operasi=int(input("Pilih operasi (1/2/3/4):"))
print ("=========================")
pertama=int(input("Masukkan bilangan pertama:"))
kedua=int(input("Masukkan bilangan kedua:"))
if operasi==1 :
    def penjumlahan(pertama,kedua):
        jumlah=pertama+kedua
        return jumlah
    print("Hasil operasi dari", pertama, "+", kedua, "=", penjumlahan(pertama,kedua))
elif operasi==2 :
    def pengurangan(pertama,kedua):
        kurang=pertama-kedua
        return kurang
    print("Hasil operasi dari", pertama, "-", kedua, "=", pengurangan(pertama,kedua))
elif operasi==3 :
    def perkalian(pertama,kedua):
        kali=pertama*kedua
        return kali
    print("Hasil operasi dari", pertama, "*", kedua, "=", perkalian(pertama,kedua))
elif operasi==4 :
    def pembagian(pertama,kedua):
        bagi=pertama/kedua
        return bagi
    print("Hasil operasi dari", pertama, "/", kedua, "=", pembagian(pertama,kedua))
