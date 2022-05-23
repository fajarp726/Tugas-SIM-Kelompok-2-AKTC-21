import streamlit as st
import pandas as pd

Data_Produk = {
    101:"BERAS PUTIH",
    102:"GULA PASIR",
    103:"GULA JAWA",
    104:"MIE INSTANT",
    105:"TELUR AYAM",
    106:"MINYAK GORENG",
    107:"SUSU BUBUK",
    108:"SUSU KENTAL",
    109:"SUSU UHT",
    110:"TEPUNG TERIGU",
    111:"TEPUNG MAIZENA",
    112:"TEPUNG TAPIOKA",
    113:"TEPUNG BERAS",
    114:"TEPUNG KETAN",
    115:"KOPI HITAM",
    116:"KECAP MANIS",
    117:"KECAP ASIN",
    118:"SAUS TOMAT",
    119:"SAUS PEDAS",
    120:"SAUS TIRAM",
}
Data_Harga = {
    101: 15000,
    102: 12000,
    103: 28000,
    104: 48000,
    105: 20000,
    106: 21000,
    107: 35000,
    108: 15000,
    109: 10000,
    110: 18000,
    111: 17000,
    112: 15000,
    113: 12000,
    114: 19000,
    115: 10000,
    116: 13000,
    117: 13000,
    118: 11500,
    119: 11000,
    120: 11000,
}

if "Button_clicked" not in st.session_state:
    st.session_state . Button_clicked = False

def callback ():
    st.session_state . Button_clicked = True

st.title('TOKO SEDERHANA')
st.write('OLEH KELOMPOK 2 AKUNTANSI C 2021')
Barang = pd.DataFrame(
   {
       'NAMA PRODUK': Data_Produk,
       'HARGA PRODUK': Data_Harga
   })

st.table(Barang)

Produk = st.selectbox(
    'PILIH ID PRODUK',
    (Data_Produk))
Keterangan = st.write('*PRODUK DENGAN ID', Produk, 'ADALAH', Data_Produk[Produk],)
Nama = st.text_input('NAMA PEMBELI')
Alamat = st.text_input('ALAMAT PEMBELI')
No_HP = st.text_input('NOMOR HP')
Ekspedisi = st.text_input('EKSPEDISI PENGIRIMAN')

Metode = st.radio(
    "METODE PEMBAYARAN",
    ('TRANSFER BANK', 'DANA', 'OVO', 'LINKAJA'))
st.write('*HARGA', Data_Produk[Produk], 'ADALAH RP.', Data_Harga[Produk])
Input_Harga = st.number_input('MASUKKAN NOMINAL PEMBAYARAN', min_value=0)

Hasil = st.button('Bayar', on_click=callback) or st.session_state. Button_clicked

if Hasil:
    if Nama == '' or Alamat == '' or No_HP == '' or Ekspedisi == '' or Input_Harga == '':
        st.warning('ISIAN TIDAK BOLEH KOSONG')
    else:
        st.write('NAMA PEMBELI          : ', Nama)
        st.write('ALAMAT PEMBELI        : ', Alamat)
        st.write('NOMOR HP              : ', No_HP)
        st.write('EKSPEDISI             : ', Ekspedisi)
        st.write('BARANG YANG DIBELI    : ', Data_Produk[Produk])
        st.write('METODE PEMBAYARAN     : ', Metode)
        st.write('UANG YANG DIBAYARKAN  : RP.', Input_Harga)

        st.write('APAKAH ANDA YAKIN INGIN MELAKUKAN PEMBAYARAN?')
        Konfirmasi = st.button('YES')
        Pembatalan = st.button('NO')
        if Konfirmasi:
            if Input_Harga < Data_Harga[Produk]:
                st.info('UANG YANG ANDA MASUKKAN KURANG')
            else:
                st.info('PROSES TRANSAKSI BERHASIL')

        if Pembatalan:
            st.error('PROSES TRANSAKSI BATAL')