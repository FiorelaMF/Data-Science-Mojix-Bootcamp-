import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt


# ----------- DATA ANALYSIS ----------------
df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

df_counted = df_counted.drop_duplicates("RFID")
df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})

my_cols_selected = ["Retail_Product_Color",
"Retail_Product_Level1",
"Retail_Product_Level1Name",
"Retail_Product_Level2Name",
"Retail_Product_Level3Name",
"Retail_Product_Level4Name",
"Retail_Product_Name",
"Retail_Product_SKU",
"Retail_Product_Size",
"Retail_Product_Style",
"Retail_SOHQTY"]
df_A = df_expected[my_cols_selected]
df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)

df_discrepancy['Retail_CCQTY'] = df_discrepancy['Retail_CCQTY'].fillna(0)
df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)

df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)
df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]

df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)

df_result = df_discrepancy.groupby("Retail_Product_Level1Name").sum()

df_discrepancy.describe()



# --------------- WEB APP DEV --------------------
st.title('Discrepancy Data - Analysis')
#st.write('Simple but effective tips for every python lovers')

# Table
st.dataframe(df_result)

# Cake Chart SOH
st.write('Retail_SOHQTY')
st.bar_chart(df_result['Retail_SOHQTY'])

# Bar Chart CC
st.write('Retail_CCQTY')
st.line_chart(df_result['Retail_CCQTY'])
#fig1, ax1 = plt.subplots()
#ax1.pie(df_result['Retail_CCQTY'], autopct='%1.1f%%', startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#st.pyplot(fig1)

# Graf Diff - unders
st.write('Stadistic metrics')
st.dataframe(df_discrepancy.describe())



