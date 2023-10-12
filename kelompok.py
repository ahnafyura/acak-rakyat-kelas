import random

# Membuat daftar angka dari 1 hingga 36
angka = list(range(1, 37))

# Mengacak urutan angka
for i in range(5):
    random.shuffle(angka)

# --!! Jumlah anggota kelompok !!--
jumlahMurid = int(input("Berapa jumlah anggota pada setiap kelompok?\nJawab: "))

# Membagi urutan angka menjadi kelompok-kelompok 4 angka
kelompok_angka = [angka[i: i + jumlahMurid] for i in range(0, len(angka), jumlahMurid)]


# Dictionary
NamaAbsen = {1: "Adam", 2: "Adel", 3: "Ahnaf", 4: "Aljesa", 5: "Nindy", 6: "Ariya",
             7: "Asha", 8: "Zahrah", 9: "Azmi", 10: "Bintang", 11: "Dhanu", 12: "Dhini",
             13: "Dimas", 14: "Egalita", 15: "estu", 16: "Fara", 17: "Fariecha", 18: "Ganes",
             19: "Gilang", 20: "Vano", 21: "Ryan", 22: "Jilan", 23: "Lailatul", 24: "Rani",
             25: "Daryl", 26: "Ungu", 27: "Fishal", 28: "Dhaffa",
             29: "Pravda", 30: "Rasya", 31: "Nabila", 32: "Tantra",
             33: "Aliya", 34: "Tiara", 35: "Diva", 36: "Tiyan"}


# Menampilkan kelompok-kelompok angka yang teracak
for kelompok in kelompok_angka:
    print(kelompok)

# Jarak output
print('')
print('[[[]--------- List Kelompok ---------[]]]')
# Mengganti absen ke nama
for i in range(len(kelompok_angka)):
    for j in range(len(kelompok_angka[i])):
        NoAbsen = kelompok_angka[i][j]
        kelompok_angka[i][j] = NamaAbsen.get(NoAbsen)

# Menampilkan nama anggota kelompok
nomer = 1
for kelompok in kelompok_angka:
    # noinspection PyTypeChecker
    unlist = ", ".join(kelompok)
    teks = f"Kelompok-{nomer}: \n{unlist}"
    print(teks + "\n")
    nomer += 1
