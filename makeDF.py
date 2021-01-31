import os
import pandas as pd



def make_df_from_excel(filename, sheetName, nrows):
  
    
    df_header = pd.read_excel(filename, sheet_name=sheetName, nrows=1)
    print(f"Excel file: {filename} (worksheet: {sheetName})")

    chunks = []
    i_chunk = 0
   
    skiprows = 1
    

    while True:
        df_chunk = pd.read_excel(
            filename, sheet_name=sheetName,
            nrows=nrows, skiprows=skiprows, header=None)
        skiprows += nrows
       
        if not df_chunk.shape[0]:
            break
        else:
            print(f"  - chunk {i_chunk} ({df_chunk.shape[0]} rows)")
            chunks.append(df_chunk)
        i_chunk += 1

    df_chunks = pd.concat(chunks)
    
    columns = {i: col for i, col in enumerate(df_header.columns.tolist())}
    df_chunks.rename(columns=columns, inplace=True)
    df = pd.concat([df_header, df_chunks])
    print("ready")
    return df

