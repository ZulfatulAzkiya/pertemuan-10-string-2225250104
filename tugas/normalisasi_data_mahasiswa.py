
# Normalisasi Data Mahasiswa Menggunakan String

nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan kelas: ")

# Membersihkan spasi di awal dan akhir
nama = nama.strip()
nim = nim.strip()
kelas = kelas.strip()

# Menyeragamkan format data
nama = nama.title()
nim = nim.replace(" ", "")
kelas = kelas.upper()

print("\n=== DATA MAHASISWA ===")
print("Nama:", nama)
print("NIM:", nim)
print("Kelas:", kelas)