def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1

        # Pindahkan elemen dari l[0..i-1] yang lebih besar dari key
        # ke satu posisi di depan dari posisi saat ini
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        
        # Masukkan key ke posisi yang sesuai
        l[j + 1] = key

# Input jumlah elemen
m = int(input().strip())

# Input elemen-elemen yang akan diurutkan
ar = [int(i) for i in input().strip().split()]

# Panggil fungsi insertion_sort untuk mengurutkan elemen
insertion_sort(ar)

# Cetak elemen-elemen yang sudah diurutkan
print(" ".join(map(str, ar)))
