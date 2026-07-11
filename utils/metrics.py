import pandas as pd

bulan = ["JAN", "FEB", "MAR", "APR", "MEI", "JUN"]

def hitung_kpi(df):

    # Pastikan semua kolom bulan bertipe numerik
    for b in bulan:
        df[b] = pd.to_numeric(df[b], errors="coerce").fillna(0)

    total_entry = df[bulan].sum().sum()

    total_desa = df["DESA/KEL"].nunique()

    total_kecamatan = df["KECAMATAN"].nunique()

    rata = round(total_entry / total_desa, 2) if total_desa > 0 else 0

    return total_entry, total_desa, total_kecamatan, rata