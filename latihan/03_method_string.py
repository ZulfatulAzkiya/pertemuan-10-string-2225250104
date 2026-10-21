
# Penggunaan Method String

teks = "  Belajar Python itu Menyenangkan  "

print("Teks asli:", repr(teks))
print("Upper:", teks.upper())
print("Lower:", teks.lower())
print("Title:", teks.title())
print("Capitalize:", teks.capitalize())
print("Tanpa spasi di awal dan akhir:", teks.strip())
print("Mengganti kata:", teks.replace("Python", "Pemrograman"))
print("Apakah diawali Belajar?", teks.strip().startswith("Belajar"))
print("Apakah diakhiri Menyenangkan?", teks.strip().endswith("Menyenangkan"))