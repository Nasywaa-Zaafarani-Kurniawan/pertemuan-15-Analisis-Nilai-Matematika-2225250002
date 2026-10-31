# Pengujian Program Pengolahan dan Analisis Nilai Matematika

## A. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca, memvalidasi, mengolah, dan menampilkan data nilai mahasiswa dengan benar.

## B. Hasil Pengujian

| No. | Skenario Pengujian | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1 | Data normal | 15 data mahasiswa dengan nilai valid | Program menampilkan laporan dengan benar | Program berhasil menampilkan laporan | PASS |
| 2 | Nilai minimum | 0 | Data diterima, status Belum Tuntas | Nilai diterima dan status Belum Tuntas | PASS |
| 3 | Nilai tepat pada KKM | 75 | Data diterima, status Tuntas | Nilai diterima dan status Tuntas | PASS |
| 4 | Nilai maksimum | 100 | Data diterima, status Tuntas | Nilai diterima dan status Tuntas | PASS |
| 5 | Nilai berupa teks | abc | Program menampilkan pesan kesalahan | Input ditolak | PASS |
| 6 | Nilai berupa desimal | 75.5 | Program menampilkan pesan kesalahan | Program menampilkan pesan bahwa masukan harus berupa bilangan bulat | PASS |
| 7 | Nilai di bawah rentang | -5 | Program menampilkan pesan kesalahan | Input ditolak dan diminta memasukkan nilai antara 0–100 | PASS |
| 8 | Nilai di atas rentang | 110 | Program menampilkan pesan kesalahan | Input ditolak | PASS |
| 9 | Data kosong | Salah satu kolom tidak diisi | Program menampilkan pesan kesalahan | Program menampilkan pesan bahwa terdapat nilai kosong | PASS |
| 10 | Jumlah kolom tidak sesuai | Salah satu baris hanya memiliki 3 kolom | Program menampilkan pesan kesalahan | Program menampilkan pesan kesalahan | PASS |
| 11 | File tanpa data mahasiswa | File hanya berisi header | Program menampilkan pesan kesalahan | Program menampilkan pesan kesalahan | PASS |

## C. Kriteria Pengujian

- **PASS:** Hasil aktual sesuai dengan hasil yang diharapkan.
- **FAIL:** Hasil aktual tidak sesuai dengan hasil yang diharapkan.

## D. Kesimpulan Pengujian

Berdasarkan hasil pengujian, seluruh skenario berhasil dijalankan sesuai dengan hasil yang diharapkan. Program dapat menerima data nilai yang valid, menentukan status ketuntasan berdasarkan KKM 75, serta menolak data yang tidak sesuai dengan ketentuan.

Dengan demikian, seluruh 11 test case memperoleh status PASS.

## E. Hasil Statistik Data Normal

| Komponen | Hasil |
|---|---:|
| Jumlah mahasiswa | 15 |
| Rata-rata nilai | 80.00 |
| Nilai terendah | 60 |
| Nilai tertinggi | 100 |
| Jumlah mahasiswa tuntas | 10 |
| Jumlah mahasiswa belum tuntas | 5 |
