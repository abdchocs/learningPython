jam1 = int(input('Masukkan Jam :'))
menit1 = int(input('Masukkan menit :'))
detik1 = int(input('Masukkan detik :'))

jam2 = int(input('Masukkan Jam :'))
menit2 = int(input('Masukkan menit :'))
detik2 = int(input('Masukkan detik :'))

#konversi masing-masing jam ke total detik
total_detik1 = (jam1*3600) + (menit1*60) + detik1
total_detik2 = (jam2*3600) + (menit2*60) + detik2

totalDetik1 = int(total_detik1)
totalDetik2 = int(total_detik2)
#hitung selisih total detik
selisih_detik = totalDetik2 - totalDetik1

#konversi selisih_detik ke dalam jam-menit-detik

jam3 = selisih_detik / 3600
sisa = selisih_detik % 3600
menit3 = sisa / 60
detik3 = sisa % 60

sisa = int(sisa)
selisih_detik = int(selisih_detik)
jam3 = int(jam3)
menit3 = int(menit3)
detik3 = int(detik3)




print(jam3, "Jam", menit3, "Menit", detik3, "Detik")


