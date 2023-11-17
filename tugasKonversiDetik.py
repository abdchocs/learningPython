total_detik = int(input('Masukkan total detik : '))

hh = total_detik / 3600
sisa = total_detik % 3600
mm = sisa / 60
ss = sisa % 60

jam = int(hh)
menit = int(mm)
detik = int(ss)

print(jam,"Jam", menit,"Menit", detik, "Detik")
