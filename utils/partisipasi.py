def hitung_partisipasi(total_entry, jumlah_tpk):

    if jumlah_tpk == 0:
        return 0

    return round(
        total_entry / (jumlah_tpk * 3) * 100,
        2
    )