for item in range (1,5):
    nim = input('Masukkan NIM:')
    nama = input('Masukkan nama:')
    alamat = input('Masukkan alamat:')
    asalSekolah = input('Masukkan asal sekolah:')
    kodeProdi = input('Masukkan kode prodi (TI/SI/DKV/Teknik Industri):')
    ipkAwal = int(input('masukkan nilai IPK awal:'))
    x,y,z =map(int,input('Masukkan nilai UTS,UAS,TM(dipisah dengan spasi):').split())
    nilaiNilai = [x]+[y]+[z]
    ips = (nilaiNilai[0]*30/100)+(nilaiNilai[2]*30/100)+(nilaiNilai[1]*40/100)
    ipk = (ips+ipkAwal)/2
    if kodeProdi == 'TI' or 'SI':
        if ipk > 75 and ipk < 85:
                print('NIM',nim);print('Nama',nama);print('Alamat:',alamat);print('Asal sekolah',asalSekolah)
                print('beasiswa 20%')
        if ipk > 85 and ipk < 100:
                print('NIM',nim);print('Nama',nama);print('Alamat:',alamat);print('Asal sekolah',asalSekolah)
                print('beasiswa 30%')
    elif kodeProdi == 'DKV' or 'Teknik Industri':
        if ipk > 75 and ipk < 85:
                print('NIM',nim);print('Nama',nama);print('Alamat:',alamat);print('Asal sekolah',asalSekolah)
                print('beasiswa 20%')
        if ipk > 85 and ipk < 100:
                print('NIM',nim);print('Nama',nama);print('Alamat:',alamat);print('Asal sekolah',asalSekolah)
                print('beasiswa 30%')