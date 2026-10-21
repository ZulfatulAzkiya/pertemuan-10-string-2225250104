
# Pencarian Kata dalam String

kalimat = "Saya belajar matematika dan pemrograman Python"

kata_dicari = input("Masukkan kata yang ingin dicari: ")

if kata_dicari.lower() in kalimat.lower():
    print(f"Kata '{kata_dicari}' ditemukan dalam kalimat.")
else:
    print(f"Kata '{kata_dicari}' tidak ditemukan dalam kalimat.")

print("Kalimat:", kalimat)
print("Jumlah karakter:", len(kalimat))