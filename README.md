Nama: Gresius Krisna Samuel
NIM: 058

Studi Kasus 3: Pengelompokan Nilai Ujian Mahasiswa (Genap)


Penjelasan Singkat Kode Program saya

1. Inisialisasi Data
-batas_nilai = (65, 100): Menggunakan Tuple untuk menyimpan batas standar nilai lulus (65) dan nilai maksimal (100) karena datanya bersifat tetap.

-nilai_masuk = [], lulus = [], remedi = []: Menggunakan List kosong untuk menampung semua nilai yang diinput dan hasil pengelompokannya karena datanya bersifat dinamis atau bisa diubah ubah.

2. Input Nilai dan Perulangan
-Perulangan While True digunakan agar pengguna dapat memasukkan nilai berulang kali tanpa batasan jumlah input.

-Variabel input_nilai menerima input teks, lalu diubah menjadi huruf kecil dengan .lower() supaya kalaupun inputan seperti 'SeLEsAi' bakal tetap terbaca.

-Kondisi if input_nilai == 'selesai': mengecek kalo dosen mengetik 'selesai', maka perulangan langsung berhenti dengan break.

-Fungsi int(input_nilai) mengubah input teks menjadi angka bulat.

-Metode .append(nilai) digunakan untuk memasukkan angka yang baru diinput ke dalam List nilai_masuk.


3. Validasi Kelulusan
-Kondisi if nilai >= batas_nilai[0]: mengecek apakah nilai lebih besar atau sama dengan indeks ke 0 dari tuple batas_nilai (yaitu angka 65).
Jika memenuhi syarat (>= 65), nilai dimasukkan ke List lulus. Jika kurang (< 65), nilai dimasukkan ke List remedi.

4. Fitur Hapus Nilai
-Variabel tanya_hapus menanyakan apakah dosen ingin menghapus nilai yang salah diinput.

-Jika dijawab 'ya', variabel hapus_nilai meminta angka spesifik yang mau dihapus.

-Kondisi if hapus_nilai in nilai_masuk: memastikan apakah angka tersebut ada di dalam list sebelum dihapus.

-Metode .remove(hapus_nilai) digunakan untuk menghapus angka tersebut dari List nilai_masuk, serta menghapusnya juga dari List lulus atau List remedi tempat angka itu tersimpan.

5. Menampilkan Hasil Akhir
Di bagian akhir, program menampilkan seluruh isi dari List nilai_masuk, List lulus, dan List remedi.


Hasil Output Program
<img width="466" height="384" alt="Copied_Item_1788871832682" src="https://github.com/user-attachments/assets/a8bbeb62-eefe-43f9-9fca-401bd9f76580" />
