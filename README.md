# Pratikum 4 - program sederhana untuk data mahasiswa

Nama:Afnan Dika Ramadhan

Nim:312410518

Mata Kuliah:Bahasa pemrograman

# Deklarasi List Data Mahasiswa
```
data_mahasiswa = []
```
Sebuah List kosong `data_mahasiswa` dideklarasikan untuk menyimpan data mahasiswa yang dimasukkan

# Loop Input Data Mahasiswa
```
while True:
    print("\nMasukkan data mahasiswa:")
    ...
    lanjut = input("Apakah ingin menambahkan data lagi? (y/t): ").lower()
    if lanjut == 't':
        break
```
Program ini menggunakan `while True` untuk membuat loop yang akan terus meminta input hingga pengguna memilih untuk berhenti.

Dalam setiap iterasi loop, program meminta input dari pengguna untuk memasukkan data mahasiswa (nama, nilai tugas, UTS, dan UAS).

Setelah data dimasukkan, program menanyakan apakah pengguna ingin menambahkan data lagi. Jika pengguna menjawab "t" (tidak), maka loop akan berhenti.

# Input Nama dan Nilai Mahasiswa
```
nama = input("Nama: ")
try:
    nilai_tugas = float(input("Nilai Tugas (0-100): "))
    nilai_uts = float(input("Nilai UTS (0-100): "))
    nilai_uas = float(input("Nilai UAS (0-100): "))
except ValueError:
    print("Input harus berupa angka. Silakan coba lagi.")
    continue

```
Nama mahasiswa diminta menggunakan `input()`.

Nilai untuk tugas, UTS, dan UAS diminta dalam bentuk angka (diubah ke tipe `float`).

Jika pengguna memasukkan nilai yang bukan angka (misalnya string atau karakter),
maka akan muncul pesan error dan program akan meminta input lagi.

# Validasi Nilai
```
if not (0 <= nilai_tugas <= 100 and 0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100):
    print("Nilai harus berada dalam rentang 0-100. Silakan coba lagi.")
    continue

```
Program memeriksa apakah nilai tugas, UTS, dan UAS berada dalam rentang 0 hingga 100. Jika ada nilai yang tidak valid, program akan memberi pesan peringatan dan melanjutkan untuk meminta input ulang.

# Perhitungan Nilai Akhir
```
nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

```
Program menghitung nilai akhir mahasiswa dengan bobot sebagai berikut:

Nilai tugas: 30% (0.3)

Nilai UTS: 35% (0.35)

Nilai UAS: 35% (0.35)

Nilai akhir dihitung dengan formula ini dan disimpan dalam variabel `nilai_akhir`.

# Menyimpan Data Mahasiswa
```
data_mahasiswa.append({
    "nama": nama,
    "nilai_tugas": nilai_tugas,
    "nilai_uts": nilai_uts,
    "nilai_uas": nilai_uas,
    "nilai_akhir": nilai_akhir
})

```
Setelah nilai dihitung, data mahasiswa (nama, nilai tugas, UTS, UAS, dan nilai akhir) disimpan dalam bentuk dictionary.

Dictionary tersebut kemudian ditambahkan ke dalam list `data_mahasiswa`menggunakan method `append()`.

# Menampilkan Daftar Data Mahasiswa
```
print("\nDaftar Data Mahasiswa:")
print("=" * 50)
print(f"{'No.':<4} {'Nama':<15} {'Tugas':<7} {'UTS':<7} {'UAS':<7} {'Akhir':<7}")
print("=" * 50)

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i:<4} {mahasiswa['nama']:<15} {mahasiswa['nilai_tugas']:<7.2f} "
          f"{mahasiswa['nilai_uts']:<7.2f} {mahasiswa['nilai_uas']:<7.2f} {mahasiswa['nilai_akhir']:<7.2f}")
print("=" * 50)

```
Setelah semua data mahasiswa dimasukkan, program akan menampilkan daftar semua mahasiswa yang sudah diinputkan dalam bentuk tabel.

Setiap kolom tabel diatur lebar dan formatnya, menggunakan f-string untuk mencetak dengan presisi dua angka desimal untuk nilai tugas, UTS, UAS, dan nilai akhir.

`enumerate(data_mahasiswa, start=1)` digunakan untuk menampilkan nomor urut mahasiswa (dimulai dari 1).

Program menampilkan tabel dengan kolom sebagai berikut:

No. (nomor urut mahasiswa)

Nama

Nilai Tugas

Nilai UTS

Nilai UAS

Nilai Akhir

# Tampilan Hasil

Akhirnya, setelah semua data ditampilkan, program menutup tampilan dengan garis pemisah (`"=" * 50`) untuk memberikan kesan format yang rapi.

Penjelasan Flow:

Pengguna diminta untuk memasukkan data mahasiswa (nama dan nilai).

Data yang valid disimpan dalam list `data_mahasiswa`.

Setelah semua data dimasukkan, program menampilkan daftar lengkap mahasiswa beserta nilai-nilainya dalam format tabel yang rapi.

# Contoh Tampilan:
Jika Anda memasukkan data untuk dua mahasiswa, contoh tampilan akhir program bisa terlihat seperti ini:
```
Daftar Data Mahasiswa:
==================================================
No.  Nama                   Tugas   UTS     UAS     Akhir  
==================================================
1   Brando Windah           90.00   87.00   80.00   85.45  
2   Anomali                 70.00   80.00   90.00   80.50
3   Afnan Dika Ramadhan     81.00   90.00   100.00   75.50  
==================================================
```
Fitur Tambahan yang Bisa Ditingkatkan:

Menghitung grade: Anda bisa menambahkan kode untuk menghitung grade (A, B, C, D, E) berdasarkan nilai akhir.

Mengurutkan data: Program bisa diperbaiki untuk menampilkan data yang terurut berdasarkan nilai akhir atau nama mahasiswa.

# FLOWCHART 
![Foto](https://github.com/nanafnan09/labpy4/blob/e434697ca70f8cdc1604f3dc5e3380c9f063a062/FLOWCHART%20PRATIKUM4.png)
