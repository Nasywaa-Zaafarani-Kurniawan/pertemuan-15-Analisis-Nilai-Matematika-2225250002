def baca_data(nama_file):
    data_mahasiswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            baris_data = file.readlines()

        for nomor_baris, baris in enumerate(baris_data[1:], start=2):
            baris = baris.strip()

            bagian = baris.split("|")

            if len(bagian) != 4:
                raise ValueError(
                    f"Baris {nomor_baris}: jumlah kolom tidak sesuai."
                )

            nim, nama, kelas, nilai = bagian

            if not nim or not nama or not kelas or not nilai:
                raise ValueError(
                    f"Baris {nomor_baris}: terdapat data yang kosong."
                )

            try:
                nilai = int(nilai)
            except ValueError:
                raise ValueError(
                    f"Baris {nomor_baris}: nilai harus berupa bilangan bulat."
                )

            if nilai < 0 or nilai > 100:
                raise ValueError(
                    f"Baris {nomor_baris}: nilai harus berada pada rentang 0-100."
                )

            mahasiswa = {
                "nim": nim,
                "nama": nama,
                "kelas": kelas,
                "nilai": nilai
            }

            data_mahasiswa.append(mahasiswa)

        if not data_mahasiswa:
            raise ValueError("File tidak memiliki data mahasiswa.")

        return data_mahasiswa

    except FileNotFoundError:
        raise FileNotFoundError(
            f"File Data_Nilai.txt tidak ditemukan."
        )
