import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

@st.cache
def load_data (nrows):
  doc=codecs.open('Employees (1).csv','rU','latin1')
  data=pd.read_csv(doc,nrows=nrows)
  return data
  
data=load_data(500)

st.title("RETO MODULO 5 - APLICACION WEB DE CIENCIA DE DATOS")
st.header("Alexa Gabriela Nava Rodríguez")

if st.sidebar.checkbox ('Mostrar datos'):
  st.write (data)

st.markdown("___")


@st.cache
def load_data_byId (employee_id):
  employees_data = pd.read_csv(employees_link)
  filter_byId= employees_data[employees_data['Employee_ID'].str.contains(employee_id)]
  return filter_byId

id_empleado= st.sidebar.text_input("Id Empleado: ")
btnFilterbyId=st.sidebar.button('Filtrar por id de empleado',key="1")

if(btnFilterbyId):
  filterId=load_data_byId(id_empleado)
  count_row=filterId.shape[0]
  st.write(f"Total items: {count_row}")
  st.dataframe(filterId)


@st.cache
def load_data_byHometown (hometown):
  employees_data = pd.read_csv(employees_link)
  filter_byHometown= employees_data[employees_data['Hometown'].str.contains(hometown)]
  return filter_byHometown

select_Hometown = st.sidebar.text_input("Ciudad: ")
btnFilterbyHometown=st.sidebar.button('Filtrar por Ciudad',key="2")

if(btnFilterbyHometown):
  filterHometown=load_data_byHometown(select_Hometown)
  count_row=filterHometown.shape[0]
  st.write(f"Total items: {count_row}")
  st.dataframe(filterHometown)


@st.cache
def load_data_byUnit (unit):
  employees_data = pd.read_csv(employees_link)
  filter_byUnit= employees_data[employees_data['Unit'].str.contains(unit)]
  return filter_byUnit

select_Unit =  st.sidebar.text_input("Area: ")
btnFilterbyUnit=st.sidebar.button('Filtrar por Ciudad',key="3")

if(btnFilterbyUnit):
  filterUnit=load_data_byUnit(select_Unit)
  count_row=filterUnit.shape[0]
  st.write(f"Total items: {count_row}")
  st.dataframe(filterUnit)



@st.cache
def load_data_byEducation (education):
  employees_data = pd.read_csv(employees_link)
  filter_byEducationLevel= employees_data[employees_data['Education_Level']==education]
  return filter_byEducationLevel

select_Education_Level = st.sidebar.selectbox("Datos por nivel educativo: ", data['Education_Level'].unique())
st.header("Datos por nivel educativo")
st.write("Seleccionar Nivel Educativo:", select_Education_Level)
data_level=data.query(f"""Education_Level==@select_Education_Level""")
count_row=data_level.shape[0]
st.write(f"Total empleados: {count_row}")
st.write(data_level)
st.markdown("___")

@st.cache
def load_data_byCiudad (hometown):
  employees_data = pd.read_csv(employees_link)
  filter_byCiudad= employees_data[employees_data['Hometown']==hometown]
  return filter_byCiudad

select_Ciudad = st.sidebar.selectbox("Seleccionar ciudad: ", data['Hometown'].unique())
st.header("Datos por Ciudad")
st.write("Seleccionar Ciudad:", select_Ciudad)
data_city=data.query(f"""Hometown==@select_Ciudad""")
count_row=data_city.shape[0]
st.write(f"Total empleados: {count_row}")
st.write(data_city)
st.markdown("___")

@st.cache
def load_data_byArea (area):
  employees_data = pd.read_csv(employees_link)
  filter_byArea= employees_data[employees_data['Unit']==area]
  return filter_byArea

select_Area = st.sidebar.selectbox("Seleccionar Area: ", data['Unit'].unique())
st.header("Datos por Área")
st.write("Seleccionar Area:", select_Area)
data_unit=data.query(f"""Unit==@select_Area""")
count_row=data_unit.shape[0]
st.write(f"Total empleados: {count_row}")
st.write(data_unit)

st.markdown("___")
if st.sidebar.checkbox ('Empleados por edad'): 
  st.header("Histograma empleados agrupados por edad")
  df_age=plt.hist(data["Age"])
  st.bar_chart(df_age)

if st.sidebar.checkbox ('Empleados por Ciudad'): 
  st.header("Frecuencias de empleados por Ciudad por área")
  df_age=plt.hist(data["Hometown"])
  st.bar_chart(df_age)

if st.sidebar.checkbox ('Ciudades con mayor indice de desercion'): 
  st.header("Ciudades con mayor indice de desercion")
  df_rate=data[["Hometown","Attrition_rate"]].groupby("Hometown").mean()
  st.bar_chart(df_rate)

if st.sidebar.checkbox ('Edad y tasa de desercion'): 
  st.header("Edad y tase de desercion")
  df_rate1=data[["Age","Attrition_rate"]]
  st.bar_chart(df_rate1)


if st.sidebar.checkbox ('Tasa de Desercion y tiempo de servicio'): 
  st.header("Tasa de Desercion y tiempo de servicio")
  fig3, ax3 = plt.subplots()
  ax3.scatter(data.Time_of_service, data.Attrition_rate)
  ax3.set_xlabel("Time_of_service")
  ax3.set_ylabel("Attrition_rate")
  st.header("Grafica de Dispersión")
  st.pyplot(fig3)
