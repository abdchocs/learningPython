print("MENGHITUNG LAMA DAN BIAYA PERCAKAPAN DI WARTEL(WARUNG TELEKOMUNIKASI)","\n")
print("======Jam memulai percakapan======","\n")
hh1 = int(input('Masukkan jam : ',))
mm1 = int(input('Masukkan menit : '))
ss1 = int(input('Masukkan detik : '))
print("\n")
print("======Jam mengakhiri percakapan======","\n")
hh2 = int(input('Masukkan jam : '))
mm2 = int(input('Masukkan menit : '))
ss2 = int(input('Masukkan detik : '))

lamaPulsa = 5
biayaPerPulsa = 150

#konversi ke detik
totalDetik1 = (hh1*3600) + (mm1*60) + ss1
totalDetik2 = (hh2*3600) + (mm2*60) + ss2

#hitung lama percakapan
durasi = totalDetik2 - totalDetik1

#hitung jumalah pulsa dan biaya untuk seluruh pulsa
pulsa = durasi / lamaPulsa
biaya = pulsa * biayaPerPulsa

#konversi durasi kedalam jam-menit-detik
hh = durasi / 3600
sisa = durasi % 3600
mm = sisa / 60
ss = sisa % 60

hh = int(hh)
mm = int(mm)
ss = int(ss)
sisa = int(sisa)
biaya = int(biaya)

print("\n")
print("Lama Percakapan : ",hh, "Jam", mm, "Menit", ss, "Detik")
print("Biaya yang dikenakan : Rp.",biaya)




