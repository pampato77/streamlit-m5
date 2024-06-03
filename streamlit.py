import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#--- IMPORTAR DATOS DE EMPLEADOS ---#
bdem=pd.read_csv("employeed.csv")

#--- Configuración de pagina ---#
st.set_page_config(page_title="Analisis de desempeño de los colaboradores",
                   page_icon=":busts_in_silhouette:")

st.title("Analisis de desempeño de los colaboradores")
st.markdown("Se presentara el analisis del desempeño que han tenido los colaboradores de la empresa Clue")

#--- AGREGAR LOGO ---#
st.sidebar.image("sunlogo.jpeg")
st.sidebar.markdown("##")
#--- DESPLEGAR FILTROS DE CONTROL ---#
gender = st.sidebar.multiselect("Seleccionar el genero",
                                options=bdem['gender'].unique(),
                                default=bdem['gender'].unique())
st.sidebar.markdown("##")
performance_score= st.sidebar.multiselect("Seleccionar el Rango del Resultado del Desempeño",
                                          options=bdem['performance_score'].unique(),
                                          default=bdem['performance_score'].unique())
st.sidebar.markdown("##")
marital_status= st.sidebar.multiselect("Seleccionar el Estado Civil",
                                       options=bdem['marital_status'].unique(),
                                       default=bdem['marital_status'].unique())

df_selection=bdem.query("gender == @gender & performance_score == @performance_score & marital_status == @marital_status")
#--- GRAFICAS ---#

#Grafica para visualizar la distribución de los puntajes de desempeño 
name=df_selection['name_employee']
performance=df_selection['performance_score']

fig_distribution_perf=px.bar(df_selection,
                             x=name,
                             y=performance,
                             title="Distribución de Rango de desempeño",
                             labels=dict(name_employee="Nombre del empleado", 
performance_score="Puntaje de desempeño"),
                             color_discrete_sequence=["#7EACCB"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)

#Grafica del promedio de horas trabajadas por el genero del empleado
avg_hours_gender=(
    df_selection.groupby(by=['gender']).sum()
[['average_work_hours']].sort_values(by="average_work_hours"))

fig_hours_gender=px.bar(avg_hours_gender,
                        x=avg_hours_gender.index,
                        y="average_work_hours", 
                        orientation="v",
                        title="Promedio de horas trabajadas por genero",
                        labels=dict(average_work_hours="Total Worked Hours", gender="Gender"),
                        color_discrete_sequence=["#F2D44B"],
                        template="plotly_white")

fig_hours_gender.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_hours_gender)

#Gráfica de la edad del empleado con respecto su salario.
age=df_selection['age']
position=df_selection['position']
salary=df_selection['salary']
fig_age=px.scatter(df_selection,
                   x=age,
                   y=salary,
                   color=position,
                   title="Salario del empleado por edad",
                   labels=dict(age="Age", salary="Salary", position="Position"),
                   template="plotly_white")
fig_age.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_age)

#Grafica para mostrar el promedio de horas trabajadas por el puntaje de desempeño. 
avg_hours=df_selection['average_work_hours']
perf_score=df_selection['performance_score']
dept=df_selection['department']
salary=df_selection['salary']

fig_perf_work=px.scatter(df_selection,
                         x=perf_score,
                         y=avg_hours,
                         size=salary,
                         color=dept,
                         title="Horas trabajadas vs Puntaje de desempeño",
                         labels=dict(average_work_hours="Average Hours", 
performance_score="Performance Score",
                                     department="Department", salary="Salary"),
                         template="plotly_white")
fig_perf_work.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_perf_work)


#--- CONCLUSION ---#
st.markdown("**Analisis del desempeño de los empleados**")
st.markdown("""Con las gráficas anteriores se concluye que, se tiene siete empleados 
               con el puntaje de desempeño más alto, las horas promedio trabajadas por 
               genero es mayor en el genero femenino y aproximadamente son 775 horas 
               promedio, los salarios por edad realmente se encuentran distribuidos, 
               la diferencia recae en los tipos de posiciones de los empleados, 
               hay una concentración en el puntaje de desempeño 3 con dos rangos de 
               promedio de horas laborales, asi mismo, el departamento con mas 
               frecuencia de horas laborales es el de IT/IS. """)



