def buat_laporan(data_mahasiswa, statistik):
    laporan = []

    laporan.append("=" * 65)
    laporan.append("       LAPORAN PENGOLAHAN NILAI MATEMATIKA MAHASISWA")
    laporan.append("=" * 65)

    laporan.append(f"Jumlah mahasiswa : {statistik['jumlah_mahasiswa']}")
    laporan.append(f"Rata-rata nilai  : {statistik['rata_rata']:.2f}")
    laporan.append(f"Nilai tertinggi  : {statistik['nilai_tertinggi']}")
    laporan.append(f"Nilai terendah   : {statistik['nilai_terendah']}")
    laporan.append(f"KKM              : 75")

    laporan.append("-" * 65)
    laporan.append("DAFTAR NILAI MAHASISWA")
    laporan.append("-" * 65)

    laporan.append(
        f"{'NIM':<12} {'NAMA':<20} {'KELAS':<8} {'NILAI':<8} {'STATUS'}"
    )

    laporan.append("-" * 65)

    for mahasiswa in data_mahasiswa:
        laporan.append(
            f"{mahasiswa['nim']:<12} "
            f"{mahasiswa['nama']:<20} "
            f"{mahasiswa['kelas']:<8} "
            f"{mahasiswa['nilai']:<8} "
            f"{mahasiswa['status']}"
        )

    laporan.append("-" * 65)
    laporan.append(f"Jumlah Tuntas        : {statistik['jumlah_tuntas']}")
    laporan.append(
        f"Jumlah Belum Tuntas  : {statistik['jumlah_belum_tuntas']}"
    )
    laporan.append("=" * 65)
    
    return "\n".join(laporan)
def tampilkan_laporan(data_mahasiswa, statistik):
    laporan = buat_laporan(data_mahasiswa, statistik)
    print(laporan)
def simpan_laporan(data_mahasiswa, statistik, nama_file):
    laporan = buat_laporan(data_mahasiswa, statistik)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(laporan)

    print(f"\nLaporan berhasil disimpan ke {nama_file}")
