batas_nilai = (65, 100) 
nilai_masuk = []
lulus = []
remedi = []

print(" Program Pengelompokan Nilai Ujian Mahasiswa ")

while True:
    input_nilai = input("Masukkan nilai (ketik selesai untuk berhenti) : ").lower()
    
    if input_nilai == 'selesai':
        break
        
    nilai = int(input_nilai)
    
    nilai_masuk.append(nilai)
    
    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)

print("\nDaftar nilai sementara : ", nilai_masuk)

tanya_hapus = input("Ingin menghapus nilai yang salah input? (ya/tidak) : ").lower()

if tanya_hapus == 'ya':
    hapus_nilai = int(input("Masukkan angka nilai yang ingin dihapus : "))
    
    if hapus_nilai in nilai_masuk:
        nilai_masuk.remove(hapus_nilai)
        
        if hapus_nilai in lulus:
            lulus.remove(hapus_nilai)
        elif hapus_nilai in remedi:
            remedi.remove(hapus_nilai)
            
        print("Nilai berhasil dihapus")
    else:
        print("Nilai tidak ada")

print("\n Hasil Akhir ")
print("Seluruh nilai yang masuk : ", nilai_masuk)
print("Nilai yang lulus : ", lulus)
print("Nilai yang remedi : ", remedi)
