def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0
    while True:
        a = str(input('Masukkan asal mobil(ketik "done" untuk keluar: ')).lower()

        if a == 'solo':
           jumlahSol += 1
        elif a == 'jogja':
            jumlahJog += 1
        elif a == 'surabaya':
            jumlahSur += 1
        elif a == 'magelang':
            jumlahMag += 1
        elif a == 'done':
            print(f'Jumlah Mobil Solo\t: {jumlahSol}')
            print(f'Jumlah mobil Surabaya\t: {jumlahSur}')
            print(f'Jumlah mobil Jogja\t: {jumlahJog}')
            print(f'Jumlah mobil Magelang\t: {jumlahMag}')
            break
        else:
            print('Input salah')


            
hitung_mobil()   




