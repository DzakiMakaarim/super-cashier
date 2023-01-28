# *Self-Service Cashier*
Sistem *self-service cashier* dengan menggunakan bahasa pemrograman Python dengan versi 3.11.

## Latar Belakang
- Seorang pengusaha melakukan perbaikan bisnis karena dengan kondisi saat ini proses transaksi masih berjalan dengan tidak efisien.
- Proses transaksi tidak berjalan dengan efisien karena pelanggan harus antri untuk melakukan pembelian barang dan penghitungan masih dilakukan secara manual.
- Diperlukan pembuatan sebuah sistem kasir yang dapat digunakan oleh pelanggan untuk melakukan transaksi secara cepat dan dapat dilakukan secara mandiri.

## Tujuan Pengerjaan Project
1. Membuat sistem *cashier* yang dapat melakukan tugas:
    - Membuat fungsi `menambahkan barang` belanjaan dengan atribut seperti nama barang, jumlah barang, dan harga barang.
    - Membuat fungsi `update nama` barang.
    - Membuat fungsi `update jumlah` barang.
    - Membuat fungsi `update harga` barang.
    - Membuat fungsi `hapus barang berdasarkan nama`.
    - Membuat fungsi `menghapus semua barang`.
    - Membuat fungsi `menampilkan semua barang`.
    - Membuat fungsi `menghitung diskon dan total harga` sesuai dengan ketentuan yang telah ditentukan.
    - Membuat `menu` untuk memudahkan pengguna dalam menggunakan *cashier*.

## Alur kode
![Untitled Diagram](https://user-images.githubusercontent.com/43342204/215276768-1909a038-8db2-4203-85fe-3ed656bb5c9f.png)

## Attribute dan Method
Penjelasan mengenai attribute dan fungsi yang berada di file `Transaction` dan `validation`

#### Attribute
- `items`. Digunakan untuk inisiasi data pada sebuah class dengan berbentuk *dictionary*.
- Syarat diskon yang ditentukan sebagai berikut:
	1. Jika di atas Rp 200.000 diskon sebesar 5%
	2. Jika di atas Rp 300.000 diskon sebesar 8%
	3. Jika di atas Rp 500.000 diskon sebesar 10%

#### Method

- `add_item`. Menambahkan barang ke dalam keranjang belanja dengan atribut name, quantity, dan item_price lalu divalidasi agar datanya dapat sesuai.
- `delete_item`. Menghapus barang berdasarkan nama lalu divalidasi jika barang tersedia.
- `reset_item`. Menghapus semua barang dalam barang keranja.
- `update_item_name`. Merubah nama barang yang diinginkan dan melakukan update dengan nama baru dengan validasi jika barang yang diinginkan sudah berada didalam keranjang belanja.
- `update_item_qty`. Merubah jumlah barang sesuai dengan barang yang ingin diubah dengan validasi jika barang tersedia didalam keranjang.
- `update_item_price`. Merubah harga per item barang sesuai dengan barang yang ingin diubah dengan validasi jika barang tersedia didalam keranjang.
- `total_price`. Menghitung semua harga barang dan melakukan penghitungan diskon jika total harga barang sesuai dengan syarat dan ketentuan yang berlaku. Lalu menampilkan harga sebelum, jumlah diskon dan sesudah diskon.
- `check_order`. Menampilkan semua barang yang ada didalam keranjang belanja.
- `random_trnsct_id`. Melakukan pembuatan id unik transaksi.
- `main_menu`. Menampilkan fungsi menu agar user mudah menggunakan kasir.
- `validate_add`. Validasi input sebelum item ditambahkan. Dengan validasi format nama harus alphabet, jumlah dan harga harus angka dengan nilai tidak boleh negatif
- `validate_update_name`. Validasi input sebelum item diubah. Dengan validasi dengan validasi format nama harus alphabet.
- `validate_update_qty`. Validasi input sebelum item diubah. Dengan validasi dengan validasi harus angka dengan nilai tidak boleh negatif.
- `validate_update_price`. Validasi input sebelum item diubah. Dengan validasi dengan validasi harus angka dengan nilai tidak boleh negatif.

## Cara Menggunakan Program
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Lakukan instalasi library tabulate dengan `pip install tabulate`.
3. Buka terminal dan pastikan path terminal sudah sesuai dengan program.
4. Jalankan module dengan command `python main.py`.

## Demonstrasi Program
### Menu kasir
saat pertama kali program dijalankan akan menampilkan dengan id transaksi yang berbeda setiap kali program dijalankan ulang.
![image](https://user-images.githubusercontent.com/43342204/215276790-48c7883b-70c1-47af-9f9a-7d44d9cb71ba.png)

### Menambahkan Barang
Pelanggan ingin menambah barang dengan detail nama, jumlah dan harga dapat menggunakan menu `add new item`.
![image](https://user-images.githubusercontent.com/43342204/215276771-b13cf691-ad7f-4ac8-9a33-c6347871cdfe.png)

### Mengubah nama barang
Pelanggan ingin mengubah nama barang maka dapat menggunakan menu 3 menu yaitu `update item name / quantity / price`.
![image](https://user-images.githubusercontent.com/43342204/215276791-4d9fe6c6-89f6-48f1-96cc-f74d3ce6670d.png)

### Menghapus barang berdasarkan nama
Pelanggan ingin menghapus salah satu barang maka dapat menggunakan menu `delete item`.
![image](https://user-images.githubusercontent.com/43342204/215276778-ed9aa80c-7152-4c56-baae-b76147bf5449.png)

### Menghapus semua barang
Pelanggan ingin hapus semua barang yang telah ditambahkan maka dapat menggunakan `reset transaction`.
![image](https://user-images.githubusercontent.com/43342204/215276785-2f570552-4afe-473a-a281-e417f3d0f2bb.png)

### Menampilkan harga akhir
Pelanggan ingin mengetahui total semua barang yang telah ditambahkan beserta dengan diskonnya maka dapat menggunakan menu `check total price`.
![image](https://user-images.githubusercontent.com/43342204/215276787-b5ad9724-45ab-4ce0-846b-f1a5ee66303a.png)

### Keluar dari program
Pelanggan ingin keluar dari program maka dapat menggunakan `exit`.
![image](https://user-images.githubusercontent.com/43342204/215276789-4754fb23-f8f9-4f5a-84aa-b971d1bea390.png)

## Kesimpulan
- Super cashier adalah sebuah program sederhana untuk melakukan transaksi yang berguna untuk membantu pelanggan dalam melakukan membeli barang secara self-service untuk lebih efisien dan efektif.
- Terdapat fitur-fitur seperti menambahkan nama barang beserta harga dan jumlahnya, mengubah data barang seperti nama, jumlah dan harga. Lalu menghapus barang, dan menjumlahkan harga barang beserta diskonnya.

## Future Work
- Melakukan koneksi ke database agar data belanja dapat tersimpan walaupun programnya berhenti.
- Membuat tampilan sistem kasir agar pengguna lebih nyaman dalam menggunakannya.
- Membuat sistem yang lebih baik dibandingkan sekarang.

    
