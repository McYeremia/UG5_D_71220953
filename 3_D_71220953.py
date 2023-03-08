import math
while True:
    jar_awal = input('Masukkan jarak awal (meter): ')
    if jar_awal == 'stop':
        print('Program Dihentikan')
        break
    elif jar_awal == 'berhenti':
        print('Program Dibentikan')
        break

    sudut1 = int(input('Masukkan sudut elevasi pada menit ke-5 (derajat): '))
    sudut2 = int(input('Masukkan sudut elevasi pada menit ke-6 (derajat): '))

    tinggi_awal = float(jar_awal) * math.tan(math.radians(sudut1))
    tinggi_akhir = float(jar_awal) * ((math.tan(math.radians(sudut2))) - (math.tan(math.radians(sudut1))))
    selisih = tinggi_akhir * (math.tan(math.radians(sudut2)))

    for i in range(1):
        hasil1 = print(f'Ketinggian drone pada menit ke-5 adalah {round(tinggi_awal, 2 )} meter')
        hasil2 = print(f'Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah {round(selisih, 2)} meter')

