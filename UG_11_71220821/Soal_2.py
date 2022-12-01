print ("Pemeriksa Kelipatan 9")
kelipatan=int(input("Masukkan Kelipatan 9 yang ingin diperiksa:"))
def kelipatan_sembilan():
    hasil=kelipatan%9
    return hasil
if kelipatan_sembilan()==0:
    print ("Benar")
else :
    print ("Salah")
    
