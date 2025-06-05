import pandas as pd
import os
def save_to_excel(record, path):
    df_new = pd.DataFrame([record])

    #dodawanie nowego rekordu do istnięjącego pliku
    if os.path.exists(path):
        df = pd.read_excel(path) #jeśli istnieje to czyta
        df = pd.concat( #konkatenacja dodaje do istnięjącego pliku
            [df, df_new],
            ignore_index=False
        )
    else: #jeśli nie istnieje
        df = df_new

    df.to_excel(path, index=False)