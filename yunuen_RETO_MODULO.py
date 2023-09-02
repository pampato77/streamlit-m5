#Librerias a ocupar en el proyecto
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

BUFF_SIZE = 500
@st.cache_data(persist=True)
def load_data(nrows, searchInput, searchNivelEd):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    if (searchInput):
        data = data[data['Employee_ID'].str.upper().str.contains(searchInput.upper())]
    if searchNivelEd:
        searchNivelEd = int(searchNivelEd)  
        data = data[data["Education_Level"] == searchNivelEd]
    return data

def main():
    df = load_data(BUFF_SIZE, "", "")

    st.title('Reto_Módulo_5_Yunuen Alcocer')
    st.header('Deserción Laboral')
    st.write('...')  # Descripción del proyecto

    sidebar = st.sidebar
    sidebar.title("Filtros")

    showData = sidebar.checkbox("¿Visualizar datos?")
    if showData:
        st.dataframe(df, use_container_width=True)
        sidebar.markdown("---")

    searchInput = sidebar.text_input("Introduce elemento a buscar")
    searchButton = sidebar.button("Buscar")
    if searchButton:
        filtered_df = load_data(BUFF_SIZE, searchInput, "")
        st.dataframe(filtered_df, use_container_width=True)
        sidebar.markdown("---")

    # Resto de los filtros...
    # Filtro SelectBox
    NivelEd_Selected = sidebar.selectbox("Seleccionar un Nivel", df["Education_Level"].unique(), index=0)
    searchNivelEdButton = sidebar.button("Buscar Nivel", key="search_nivel")
    if searchNivelEdButton:
        filtered_df = load_data(BUFF_SIZE, "", NivelEd_Selected)
        st.dataframe(filtered_df, use_container_width=True)   # actualiza el DF filtrado

    City_Selected = sidebar.selectbox("Seleccionar una Ciudad", df["Hometown"].unique(), index=0)
    searchCityButton = sidebar.button("Buscar Ciudad", key="search_city")
    if searchCityButton:
        filtered_df = load_data(BUFF_SIZE, "", City_Selected)
        st.dataframe(filtered_df, use_container_width=True)   # actualiza el DF filtrado

    Unit_Selected = sidebar.selectbox("Seleccionar una Unidad", df["Unit"].unique(), index=0)
    searchUnitButton = sidebar.button("Buscar Unidad", key="search_unit")
    if searchUnitButton:
        filtered_df = load_data(BUFF_SIZE, "", Unit_Selected)
        st.dataframe(filtered_df, use_container_width=True)   # actualiza el DF filtrado


    # Histograma
    st.write("Rango de edades")
    fig, ax = plt.subplots()
    plt.hist(df['Age'], alpha=0.5, color='#6495ED')
    plt.title('Rango de edades')
    plt.xlabel('Rango')
    plt.ylabel('Conteo')
    ax.grid(True)  # Add grid lines to the histogram
    st.pyplot(fig)  # Use st.pyplot(fig) to display the matplotlib figure
    
    # Gráfica de frecuencia
    st.write("Unidades funcionales")
    sns.set_style('white')  # Remove grid from count plot
    ax = sns.countplot(data=df, x='Unit', order=df['Unit'].value_counts().index, linewidth=3)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=70)
    st.pyplot(ax.figure)
    
    # Resto de las visualizaciones...

if __name__ == "__main__":
    main()