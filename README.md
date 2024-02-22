# Cara Kerja Sistem Prediksi Produk

Aplikasi ini memungkinkan pengguna untuk memasukkan data interaksi pelanggan dan menerima prediksi produk berdasarkan data tersebut. Berikut adalah langkah-langkah proses kerja sistem:

1. **Pemuatan Data:**
   - Aplikasi memuat tiga jenis data dari file CSV:
     - Interaksi pelanggan (`customer_interactions.csv`)
     - Detail produk (`product_details.csv`)
     - Riwayat pembelian (`purchase_history.csv`)
   - Data pelanggan dan produk dihubungkan menggunakan kolom `customer_id` dan `product_id`.

2. **Pemrosesan Data:**
   - Data interaksi pelanggan digabungkan dengan riwayat pembelian untuk membentuk satu dataset (`merged_data`).
   - Fitur-fitur yang relevan dipilih dari dataset (`page_views` dan `time_spent` sebagai fitur-fitur masukan `X`, dan `product_id` sebagai target `y`).

3. **Pembagian Data:**
   - Dataset dibagi menjadi data latih dan data uji menggunakan fungsi `train_test_split`.

4. **Pelatihan Model:**
   - Model klasifikasi `RandomForestClassifier` dilatih menggunakan data latih untuk memprediksi produk berdasarkan fitur-fitur masukan.
   - Model yang telah dilatih disimpan ke dalam file `model.pkl` untuk digunakan nanti.

5. **Aplikasi Flask:**
   - Aplikasi menggunakan framework Flask untuk membuat REST API.
   - API memiliki dua endpoint:
     - `/`: Menampilkan halaman beranda aplikasi.
     - `/predict`: Menerima permintaan POST dengan data pengguna dan memberikan prediksi produk.

6. **Prediksi Produk:**
   - Saat menerima permintaan POST di endpoint `/predict`, aplikasi melakukan hal berikut:
     - Memeriksa apakah data pelanggan yang diberikan valid.
     - Menerima data masukan berupa `customer_id`, `page_views`, dan `time_spent`.
     - Menggunakan model yang telah dilatih untuk memprediksi produk berdasarkan data masukan.
     - Mengembalikan informasi produk yang diprediksi dalam format JSON.

7. **Antarmuka Pengguna:**
   - Pengguna dapat berinteraksi dengan aplikasi melalui antarmuka pengguna sederhana yang dapat diakses melalui browser.
   - Antarmuka pengguna memungkinkan pengguna untuk memasukkan `customer_id`, `page_views`, dan `time_spent` untuk melakukan prediksi produk.

8. **Deploy Aplikasi:**
   - Aplikasi dapat didistribusikan dan dijalankan di platform Streamlit Sharing atau dijalankan secara lokal.

