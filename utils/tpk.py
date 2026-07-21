import pandas as pd

FILE_TPK = "data/Detail TPK BABEL.xlsx"


def load_tpk():

    df = pd.read_excel(
        FILE_TPK,
        sheet_name="detailByTpk",
        header=None
    )

    return df

def rekap_total_tpk(df):

    hasil = (
        df.groupby("NAMA KELURAHAN")["KODE TPK"]
        .nunique()
        .reset_index()
        .rename(columns={
            "NAMA KELURAHAN":"DESA/KEL",
            "KODE TPK":"TOTAL_TPK"
        })
    )

    return hasil

import re
import pandas as pd

def hitung_tpk_aktif(df):

    # Cari otomatis semua kolom yang mengandung "id tpk"
    kolom_id = [
        c for c in df.columns
        if "id tpk" in c.lower()
    ]

    hasil = {}

    for _, row in df.iterrows():

        desa = str(row["DESA/KEL"]).strip()

        if desa not in hasil:
            hasil[desa] = set()

        for kolom in kolom_id:

            nilai = row[kolom]

            if pd.isna(nilai):
                continue

            isi = str(nilai)

            # Ambil semua angka minimal 10 digit
            ids = re.findall(r"\d{10,}", isi)

            for id_tpk in ids:
                hasil[desa].add(id_tpk)

    data = []

    for desa, ids in hasil.items():

        data.append({
            "DESA/KEL": desa,
            "AKTIF": len(ids)
        })

    return pd.DataFrame(data)

def gabung_tpk(df_master, df_entry):

    total = rekap_total_tpk(df_master)

    aktif = hitung_tpk_aktif(df_entry)

    hasil = total.merge(
        aktif,
        on="DESA/KEL",
        how="left"
    )

    hasil["AKTIF"] = (
        hasil["AKTIF"]
        .fillna(0)
        .astype(int)
    )

    hasil["TIDAK_AKTIF"] = (
        hasil["TOTAL_TPK"] - hasil["AKTIF"]
    )

    hasil["TIDAK_AKTIF"] = hasil["TIDAK_AKTIF"].clip(lower=0)

    hasil["PERSEN"] = (
        hasil["AKTIF"] /
        hasil["TOTAL_TPK"] * 100
    ).fillna(0).round(1)

    return hasil
def kpi_tpk(df):

    total = int(df["TOTAL_TPK"].sum())

    aktif = int(df["AKTIF"].sum())

    tidak = int(df["TIDAK_AKTIF"].sum())

    persen = round(aktif/total*100,1) if total else 0

    return total, aktif, tidak, persen