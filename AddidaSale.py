import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("C:\\Users\\USER\\OneDrive\\Desktop\\Python\\Etc\\AddidasSale\\Adidas US Sales Datasets.xlsx",sheet_name="Data")

print(data.head(5))

print(data.isnull().sum())

print(data.dtypes)

print(data.describe())

data['Invoice Date']=pd.to_datetime(data['Invoice Date'],errors='coerce')
data['Year']=data['Invoice Date'].dt.year
data['Month']=data['Invoice Date'].dt.month


plt.figure(figsize=(10,5))
sns.heatmap(data.corr(numeric_only=True),annot=True)
plt.xticks(rotation=45)
plt.show()

with pd.ExcelWriter("C:\\Users\\USER\\OneDrive\\Desktop\\Python\\Etc\\AddidasSale\\Adidas US Sales Datasets.xlsx",engine='openpyxl',mode='a') as writer:
      data.to_excel(writer, sheet_name="Cleaned_Data", index=False)



# pd.ExcelWriter(...)	 A context manager (like open()) to write to an Excel file using pandas.
# engine='openpyxl'	Specifies that openpyxl will be used to handle .xlsx files. Required for .xlsx format.
# mode='a'	'a' means append mode — don't overwrite the existing file, just add a new sheet to it.
# data.to_excel(...)	Writes the data DataFrame to the Excel file.
# sheet_name="Cleaned_Data"	The new sheet name where your cleaned data is saved.
# index=False	Prevents pandas from writing the DataFrame's index as a separate column in Excel.