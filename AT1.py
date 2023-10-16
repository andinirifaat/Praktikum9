angka=[]
for i in range (5):
    angka_baru=int(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(angka_baru)
print (f"Hasil rata-rata adalah {sum(angka)/5}")