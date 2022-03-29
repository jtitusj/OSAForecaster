import pandas as pd


# upload csv file
def upload_file(type="csv"):
    data_file = st.file_uploader("Upload csv file", type=["csv"])
    if data_file is not None:
        excel_file = pd.ExcelFile(data_file)
        df_mt = pd.read_excel(excel_file, sheet_name="MT OSA")
        df_rmt = pd.read_excel(excel_file, sheet_name="RMT OSA")

        return df_mt, df_rmt