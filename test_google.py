from utils.google_sheet import baca_google_sheet


df_catin = baca_google_sheet("CATIN_BABEL")
df_baduta = baca_google_sheet("BADUTA_BABEL")
df_bumil = baca_google_sheet("BUMIL_BABEL")


print("=== CATIN ===")
print(df_catin.head())
print(df_catin.columns)


print("\n=== BADUTA ===")
print(df_baduta.head())
print(df_baduta.columns)


print("\n=== BUMIL ===")
print(df_bumil.head())
print(df_bumil.columns)