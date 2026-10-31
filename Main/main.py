import os

from data_io import baca_data
from analisis import hitung_statistik
from utilitas import tampilkan_laporan, simpan_laporan

def main():
    folder_proyek = os.path.dirname(os.path.abspath(__file__))

    file_data = os.path.join(folder_proyek, "Data_Nilai.txt")
    file_output = os.path.join(folder_proyek, "laporan_nilai.txt")

    print("Lokasi folder:", folder_proyek)
    print("File data ditemukan:", os.path.exists(file_data))

    while True:
        try:
            data_mahasiswa = baca_data(file_data)
            break

        except (ValueError, FileNotFoundError) as error:
            print("\nTerjadi kesalahan pada data:")
            print(error)

            input("Perbaiki Data_Nilai.txt, lalu tekan Enter...")

    statistik = hitung_statistik(data_mahasiswa)

    print("\n")
    tampilkan_laporan(data_mahasiswa, statistik)

    simpan_laporan(data_mahasiswa, statistik, file_output)


if __name__ == "__main__":
    main()
