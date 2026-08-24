import pandas as pd


def hitung_kpi(df, bulan):
    """
    Menghitung KPI Dashboard
    """

    # ===============================
    # Jumlah Keseluruhan TPK
    # ===============================
    total_tpk = pd.to_numeric(
    df["JUMLAH TPK"],
    errors="coerce"
).fillna(0).sum()

    # ===============================
    # Jumlah Entry SELALU Januari–Juni
    # ===============================
    jumlah_entry = 0

    for b in ["JAN","FEB","MAR","APR","MEI","JUN"]:
        jumlah_entry += pd.to_numeric(
        df[b],
        errors="coerce"
    ).fillna(0).sum()

    # ===============================
    # TPK Aktif mengikuti filter bulan
    # ===============================
    tpk_aktif = pd.to_numeric(
    df[f"{bulan} TPK"],
    errors="coerce"
).fillna(0).sum()

    # ===============================
    # Persentase Partisipasi
    # ===============================
    if total_tpk == 0:
        partisipasi = 0
    else:
        partisipasi = round((tpk_aktif / total_tpk) * 100, 2)

    return (
        int(tpk_aktif),
        int(total_tpk),
        partisipasi,
        int(jumlah_entry)
    )