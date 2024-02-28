import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset

data = pd.read_csv('jml_prdks.csv')


st.title("Data Produksi Daging Ayam di Jawa Barat")
st.write("Dasbord ini menampilkan data produksi daging ayam di jawa barat dari tahun 2013 hingga 2022.")


# Filter by year
year = st.slider("Pilih tahun", 2013, 2022, (2013, 2022))
data_filtered = data[(data['tahun'] >= year[0]) & (data['tahun'] <= year[1])]


# Insight: Total production for selected year
total_production = data_filtered['jumlah_produksi'].sum()
st.write(f"Total produksi daging ayam pedaging di Jawa Barat pada tahun {year[0]} - {year[1]} adalah {total_production} ton.")


# Insight: Average production per kabupaten/kota
avg_production = total_production / len(data_filtered['nama_kabupaten_kota'].unique())
st.write(f"Rata-rata produksi daging ayam pedaging per kabupaten/kota di Jawa Barat pada tahun {year[0]} - {year[1]} adalah {avg_production} ton.")


# Line chart of production by year

st.header("Produksi Daging Ayam Pedaging di Jawa Barat per Tahun")
fig, ax = plt.subplots()
sns.lineplot(x='tahun', y='jumlah_produksi', data=data_filtered, ax=ax)
st.pyplot(fig)


# Insight: Top 5 kabupaten/kota with highest production
top_5 = data_filtered.nlargest(5, 'jumlah_produksi')
st.header("Top 5 Kabupaten/Kota dengan Produksi Daging Ayam Terbanyak")
fig, ax = plt.subplots()
sns.barplot(x='nama_kabupaten_kota', y='jumlah_produksi', data=top_5, ax=ax)
st.pyplot(fig)


# Insight: Lowest 5 kabupaten/kota with production
lowest_5 = data_filtered.nsmallest(5, 'jumlah_produksi')
st.header("5 Kabupaten/Kota dengan Produksi Daging Ayam Terendah")
fig, ax = plt.subplots()
sns.barplot(x='nama_kabupaten_kota', y='jumlah_produksi', data=lowest_5, ax=ax)
st.pyplot(fig)

# Summary

st.header("Summary")
st.write("Dari hasil pengolahan data, dapat disimpulkan bahwa:")
st.write("- Total produksi daging ayam pedaging di Jawa Barat pada tahun yang dipilih adalah " + str(total_production) + " ton.")
st.write("- Rata-rata produksi daging ayam pedaging per kabupaten/kota di Jawa Barat pada tahun yang dipilih adalah " + str(avg_production) + " ton.")
st.write("- Kabupaten/kota dengan produksi daging ayam pedaging terbanyak adalah " + str(top_5['nama_kabupaten_kota'].tolist()) + ".")
st.write("- Kabupaten/kota dengan produksi daging ayam pedaging terendah adalah " + str(lowest_5['nama_kabupaten_kota'].tolist()) + ".")