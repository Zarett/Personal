my_file=input('File: ') # Menyerahkan input nama file

f=open(my_file,'r') # Membuka file
semuakartu=f.read().split() # Mendefinisikan isi file dengan split agar terpisah antar spasi
list(semuakartu) # Jadikan list agar mudah diindex dengan urutan

# Print masing-masing kartu dalam file
for i in semuakartu:
    print(i, end=' ')
print('')


# Ini merupakan urutan seharusnya tepok nyamuk sesuai soal yang diberikan
urutan=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'AS']
# Ada kemungkinan tidak ketemu yang sama meski sudah sangat panjang indexnya, jadi agar tidak error (sempat error saat dicoba tanpa memperpanjang range) sehingga dipanjangkan.
giliran=urutan*100


# mulailagi sebagai counter untuk melakukan pemotongan, jadi awal dari setelah 'Tepok: '
# counter untuk counter di semuakartu
# zero sebagai counter giliran, dibedakan karena giliran akan kembali lagi ke 2 saat tertepok
mulailagi=0
counter=0
zero=0


# Melakukan loop untuk tepok


while counter<len(semuakartu): # Loop akan selesai bila semua kartu dalam file sudah terperiksa
    if semuakartu[counter]==giliran[zero]: # Memutuskan apakah antara giliran yang seharusnya dengan kartu yang keluar equal
        lst=semuakartu[mulailagi:counter] # Membuat list baru dari mulai sampai tepok
        print('Tepok: ', end=' ') # Print Tepok biasa, dengan end=' ' agar tidak new line
        for kartu in lst: # Loop baru untuk melakukan print setiap kartu di dalam list
            print(kartu, end=' ') # Print biasa tanpa new line
        print('['+str(semuakartu[counter])+']') # Print kartu yang ditepok
        mulailagi=counter+1 # Ditaruh penambahan dengan counter agar dimulai dari setelah counter, tidak repetitif dari index 0 lagi
        zero=-1 #Agar Index kembali ke 0 lagi karena nanti akan di incarnate
    elif semuakartu[counter]=='JOKER': # Ini bila Joker yang keluar, sisanya sama
        lst=semuakartu[mulailagi:counter] 
        print('Tepok: ', end=' ')
        for kartu in lst:
            print(kartu, end=' ')
        print('[JOKER]')
        mulailagi=counter+1
        zero=-1
    counter+=1 #incarnate counter dan zero
    zero+=1

print('Permainan selesai.') #Print permainan selesai

f.close() # Tutup file
