KKM = 75


def tentukan_status(nilai):
    if nilai >= KKM:
        return "Tuntas"
    else:
        return "Belum Tuntas"


def hitung_statistik(data_mahasiswa):
    jumlah_mahasiswa = len(data_mahasiswa)

    total_nilai = sum(
        mahasiswa["nilai"] for mahasiswa in data_mahasiswa
    )

    rata_rata = total_nilai / jumlah_mahasiswa

    nilai_terendah = min(
        mahasiswa["nilai"] for mahasiswa in data_mahasiswa
    )

    nilai_tertinggi = max(
        mahasiswa["nilai"] for mahasiswa in data_mahasiswa
    )

    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for mahasiswa in data_mahasiswa:
        status = tentukan_status(mahasiswa["nilai"])

        mahasiswa["status"] = status

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    statistik = {
        "jumlah_mahasiswa": jumlah_mahasiswa,
        "rata_rata": rata_rata,
        "nilai_terendah": nilai_terendah,
        "nilai_tertinggi": nilai_tertinggi,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas
    }

    return statistik