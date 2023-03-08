input_kata = str(input('Masukkan kalimat: '))
input_cari = str(input('Masukkan kata yang dicari: '))
input_ganti = str(input('Kata yang diganti: '))
kata_sama = []
pisah = input_kata.split()

def ganti_kata():
    for i in pisah:
        if i in input_cari:
            kata_sama.append(i)

    for i in range(len(pisah)):
        if pisah[i] == input_cari:
            pisah[i] = input_ganti
    
    hasil = " ".join(pisah)
    print(hasil)

ganti_kata()