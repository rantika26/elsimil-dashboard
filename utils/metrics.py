import pandas as pd


def hitung_kpi(df, bulan):

    df = df.copy()

    # Pastikan kolom numerik
    df[bulan] = pd.to_numeric(df[bulan], errors="coerce").fillna(0)
    df["TOTAL"] = pd.to_numeric(df["TOTAL"], errors="coerce").fillna(0)
    df["JUMLAH TPK"] = pd.to_numeric(df["JUMLAH TPK"], errors="coerce").fillna(0)

    # ===========================
    # 1. Jumlah TPK melakukan pendampingan
    # ===========================

    jumlah_tpk_pendampingan = int(df[bulan].sum())

    # ===========================
    # 2. Jumlah keseluruhan TPK
    # ===========================

    jumlah_tpk = (
        df
        .drop_duplicates(["KABUPATEN","KECAMATAN","DESA/KEL"])
        ["JUMLAH TPK"]
        .sum()
    )

    # ===========================
    # 3. Persentase Partisipasi
    # ===========================

    if jumlah_tpk == 0:
        persentase = 0
    else:
        persentase = round(
            (jumlah_tpk_pendampingan / jumlah_tpk) * 100,
            2
        )

    # ===========================
    # 4. Jumlah Entry Jan-Jun
    # ===========================

    jumlah_entry = int(df["TOTAL"].sum())

    return (
        jumlah_tpk_pendampingan,
        jumlah_tpk,
        persentase,
        jumlah_entry
    )