


data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    
    nama = input("Nama: ")
    
    try:
        nilai_tugas = float(input("Nilai Tugas (0-100): "))
        nilai_uts = float(input("Nilai UTS (0-100): "))
        nilai_uas = float(input("Nilai UAS (0-100): "))
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        continue

    if not (0 <= nilai_tugas <= 100 and 0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100):
        print("Nilai harus berada dalam rentang 0-100. Silakan coba lagi.")
        continue

    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

    data_mahasiswa.append({
        "nama": nama,
        "nilai_tugas": nilai_tugas,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_akhir": nilai_akhir
    })

    lanjut = input("Apakah ingin menambahkan data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

print("\nDaftar Data Mahasiswa:")
print("=" * 50)
print(f"{'No.':<4} {'Nama':<15} {'Tugas':<7} {'UTS':<7} {'UAS':<7} {'Akhir':<7}")
print("=" * 50)

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i:<4} {mahasiswa['nama']:<15} {mahasiswa['nilai_tugas']:<7.2f} "
          f"{mahasiswa['nilai_uts']:<7.2f} {mahasiswa['nilai_uas']:<7.2f} {mahasiswa['nilai_akhir']:<7.2f}")

print("=" * 50)
