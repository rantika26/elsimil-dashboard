import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

SERVICE_ACCOUNT = "service_account.json"

SPREADSHEET_ID = "1Zcy1pB5r1mPYzIqdy8OYHQb9YJmbIvPOokxPCL_KkZM"


def baca_google_sheet(nama_sheet):

    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT,
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    sh = client.open_by_key(
        SPREADSHEET_ID
    )

    ws = sh.worksheet(
        nama_sheet
    )

    data = ws.get_all_records()

    df = pd.DataFrame(data)

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.upper()
    )

    return df