
# Penggunaan Split dan Join

kalimat = "Saya belajar bahasa pemrograman Python"

# Memisahkan kalimat menjadi beberapa kata
daftar_kata = kalimat.split()

print("Kalimat awal:", kalimat)
print("Hasil split:", daftar_kata)

# Menggabungkan kembali kata-kata
kalimat_baru = "-".join(daftar_kata)

print("Hasil join:", kalimat_baru)

# Menggabungkan menggunakan spasi
kalimat_spasi = " ".join(daftar_kata)

print("Hasil join dengan spasi:", kalimat_spasi)