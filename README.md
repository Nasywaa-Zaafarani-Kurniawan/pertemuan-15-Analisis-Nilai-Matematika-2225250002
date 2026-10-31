# pertemuan-15-Analisis-Nilai-Matematika-2225250002

## 1. Deskripsi Proyek

Program Pengolahan dan Analisis Data Hasil Belajar Matematika Mahasiswa merupakan program berbasis Python yang digunakan untuk membaca, memvalidasi, mengolah, dan menganalisis data nilai mahasiswa.

Program ini menentukan status ketuntasan mahasiswa berdasarkan Kriteria Ketuntasan Minimal (KKM) sebesar 75. Hasil pengolahan ditampilkan melalui terminal dan disimpan dalam file teks (`.txt`).

## 2. Tujuan Program

- Mengolah data nilai mahasiswa secara terstruktur.
- Memvalidasi data agar sesuai dengan ketentuan.
- Menghitung statistik nilai mahasiswa.
- Menentukan status ketuntasan berdasarkan KKM.
- Menghasilkan laporan pengolahan nilai dalam format TXT.

## 3. Fitur Program

1. Membaca data mahasiswa dari file TXT.
2. Memvalidasi NIM, nama, kelas, dan nilai agar tidak kosong.
3. Memastikan nilai berupa bilangan bulat dalam rentang 0–100.
4. Menentukan status ketuntasan mahasiswa:
   - Tuntas: nilai >= 75.
   - Belum Tuntas: nilai < 75.
5. Menghitung jumlah mahasiswa, rata-rata, nilai tertinggi, dan nilai terendah.
6. Menghitung jumlah mahasiswa yang tuntas dan belum tuntas.
7. Menampilkan laporan hasil pengolahan melalui terminal.
8. Menyimpan laporan ke dalam file TXT.

## 4. Struktur Folder

```text
Analisis_Nilai_Matematika/
│
├── README.md
├── proposal.md
├── main.py
│
├── data/
│   └── data_nilai.txt
│
├── src/
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    ├── .gitkeep
    └── laporan_nilai.txt
```

## 5. Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Editor kode: Visual Studio Code
- Format data masukan: TXT
- Format laporan keluaran: TXT

## 6. Format Data Masukan

Data mahasiswa disimpan dalam file `data/data_nilai.txt`.

Setiap data dipisahkan menggunakan tanda `|` dengan susunan kolom:

```text
NIM|Nama|Kelas|Nilai
```

Contoh:

```text
NIM|Nama|Kelas|Nilai
250101001|Aditya Pratama|A|85
250101002|Bella Anggraini|A|72
```

Ketentuan data:
- NIM, nama, kelas, dan nilai wajib diisi.
- Nilai harus berupa bilangan bulat.
- Nilai harus berada pada rentang 0–100.

## 7. Cara Menjalankan Program

1. Buka folder proyek menggunakan Visual Studio Code.
2. Pastikan Python sudah terpasang.
3. Buka terminal pada folder utama proyek.
4. Jalankan perintah berikut:

```bash
python main.py
```

5. Program akan membaca data dari `data/data_nilai.txt`.
6. Jika data valid, program akan menampilkan laporan pada terminal.
7. Laporan juga disimpan secara otomatis ke folder `output` dengan nama `laporan_nilai.txt`.

## 8. Penanganan Kesalahan

Program menangani beberapa kondisi data tidak valid, antara lain:

- File data tidak ditemukan.
- Jumlah kolom tidak sesuai.
- Terdapat data kosong.
- Nilai bukan bilangan bulat.
- Nilai berada di luar rentang 0–100.
- File tidak memiliki data mahasiswa.

Jika terjadi kesalahan, program menampilkan pesan kesalahan dan meminta pengguna memperbaiki file data sebelum melanjutkan proses.

## 9. Pengujian Program

Pengujian dilakukan menggunakan beberapa skenario, yaitu:

- Data normal.
- Nilai minimum (0).
- Nilai tepat pada KKM (75).
- Nilai maksimum (100).
- Nilai berupa teks.
- Nilai desimal.
- Nilai di bawah 0.
- Nilai di atas 100.
- Data kosong.
- Jumlah kolom tidak sesuai.
- File tanpa data mahasiswa.

Dokumentasi hasil pengujian dapat dilihat pada file `tests/test_case.md`.
