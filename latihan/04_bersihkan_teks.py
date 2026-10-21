
# Membersihkan Teks

teks = "   Saya sedang belajar Python.   "

print("Sebelum dibersihkan:", repr(teks))

teks_bersih = teks.strip()

print("Sesudah dibersihkan:", repr(teks_bersih))
print("Panjang teks sebelum dibersihkan:", len(teks))
print("Panjang teks sesudah dibersihkan:", len(teks_bersih))