"""
program menghitung luas segitiga
luas_segitiga = alas*tinggi
"""
print('\nmenghitung luas segitiga tanpa fungsi')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nmembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas,tinggi) :
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga
alas = 10
tinggi = 6
print(f'dengan fungsi,  segitiga dengan alas={alas} dan tinggi={tinggi} = {hitung_luas_segitiga(alas,tinggi)}')
print(f'segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10,9)}')