#!/usr/bin/env python
# coding: utf-8

# In[84]:


nama = input("Nama: ");
lamaHari = int(input("Lama(hari): "));
jenisKamar = input("Jenis Kamar: ");
kartuMember = input("Kartu Member: ");
kamarDeluxe = 300000;
kamarSuperior = 500000;
kamarSuperiorGrandDeluxe = 1000000;

if kartuMember == "Ya":
    if jenisKamar == "Deluxe":
        totalBiaya = kamarDeluxe * lamaHari;
        diskon = 0.1;
        totalBayar = int(totalBiaya - (totalBiaya * diskon));
        print("Bpk / Ibu: " , nama);
        print("Anda memilih kamar jenis ", jenisKamar, "untuk tinggal selama ", lamaHari, " hari");
        print("Harga kamar per malam adalah ", kamarDeluxe);
        print("Total biaya Rp: ", totalBiaya);
        print("Selamat Anda medapat diskon sebesar 10 %");
        print("Total bayar Rp.", totalBayar);
        print("Terima kasih telah bermalam di Luxury Hotel");
    elif jenisKamar == "Superior":
        totalBiaya = kamarSuperior * lamaHari;
        diskon = 0.1;
        totalBayar = int(totalBiaya - (totalBiaya * diskon));
        print("Bpk / Ibu: " , nama);
        print("Anda memilih kamar jenis ", jenisKamar, "untuk tinggal selama ", lamaHari, " hari");
        print("Harga kamar per malam adalah ", kamarSuperior);
        print("Total biaya Rp: ", totalBiaya);
        print("Selamat Anda medapat diskon sebesar 10 %");
        print("Total bayar Rp.", totalBayar);
        print("Terima kasih telah bermalam di Luxury Hotel");
    else :
        totalBiaya = kamarSuperiorGrandDeluxe * lamaHari;
        diskon = 0.1;
        totalBayar = int(totalBiaya - (totalBiaya * diskon));
        print("Bpk / Ibu: " , nama);
        print("Anda memilih kamar jenis ", jenisKamar, "untuk tinggal selama ", lamaHari, " hari");
        print("Harga kamar per malam adalah ", kamarSuperiorGrandDeluxe);
        print("Total biaya Rp: ", totalBiaya);
        print("Selamat Anda medapat diskon sebesar 10 %");
        print("Total bayar Rp.", totalBayar);
        print("Terima kasih telah bermalam di Luxury Hotel");

else:
    if jenisKamar == "Deluxe":
        totalBiaya = kamarDeluxe * lamaHari;
        print("Bpk / Ibu: " , nama);
        print("Anda memilih kamar jenis ", jenisKamar, "untuk tinggal selama ", lamaHari, " hari");
        print("Harga kamar per malam adalah ", kamarDeluxe);
        print("Total biaya Rp: ", totalBiaya);
        print("Terima kasih telah bermalam di Luxury Hotel");
    elif jenisKamar == "Superior":
        totalBiaya = kamarSuperior * lamaHari;
        print("Bpk / Ibu: " , nama);
        print("Anda memilih kamar jenis ", jenisKamar, "untuk tinggal selama ", lamaHari, " hari");
        print("Harga kamar per malam adalah ", kamarSuperior);
        print("Total biaya Rp: ", totalBiaya);
        print("Terima kasih telah bermalam di Luxury Hotel");
    else:
        totalBiaya = kamarSuperiorGrandDeluxe * lamaHari;
        print("Bpk / Ibu: " , nama);
        print("Anda memilih kamar jenis ", jenisKamar, "untuk tinggal selama ", lamaHari, " hari");
        print("Harga kamar per malam adalah ", kamarSuperiorGrandDeluxe);
        print("Total biaya Rp: ", totalBiaya);
        print("Selamat Anda medapat diskon sebesar 10 %");
        print("Total bayar Rp.", totalBayar);
        print("Terima kasih telah bermalam di Luxury Hotel");
        


# In[ ]:





# In[ ]:




