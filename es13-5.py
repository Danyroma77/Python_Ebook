import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

##Titolo Pagina
st.title("Esercizio 13.5")

#Tasto di caricamento del file
uploaded_file = st.file_uploader("Carica un file CSV", type="csv")

if uploaded_file is not None:
    #Caricamento del file e visualizzazione dei dati
    df = pd.read_csv(uploaded_file)

    #Sottotitolo
    st.subheader("Dati caricati")
    st.write(df.head())

    #Riepilogo dati
    st.subheader("Riepilogo dati")
    st.write(df.describe())

    #Dati Filtrati
    st.subheader("Dati filtrati")
    columns = df.columns.to_list()
    selected_columns = st.selectbox("Seleziona una colonna per filtrare: ", columns)

    unique_values = df[selected_columns].unique()   
    select_value = st.selectbox("Seleziona un valore per filtrare: ", unique_values)

    #Mostriamo i dati filtrati
    filtered_df = df[df[selected_columns] == select_value]
    st.write(filtered_df)

    #Grafico
    st.subheader("Grafico")
    x_column = st.selectbox("Seleziona una colonna per l'asse x: ", columns)
    y_column = st.selectbox("Seleziona una colonna per l'asse y: ", columns)

    if st.button("Visualizza grafico"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Nessun file caricato")
    