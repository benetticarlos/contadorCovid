import pandas as pd
import numpy as np
import datetime
import os
import tkinter as tk
import matplotlib.pyplot as plt

# -------   ------  ------  RUTAS  ------  ------  ------  ----- 
path = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(path+"/BaseFiltradaModificada.csv", encoding="utf8")

# -------   ------  ------  VENTANA  ------  ------  ------  ----- 
miVentana = tk.Tk()
miVentana.title("HERRAMIENTA CONSULTAS COVID-19 CABA")
miVentana.geometry("1200x900")
miVentana.configure(bg="AntiqueWhite2")

fechasPosibles = df["fecha_referencia_tipo_caso"].unique()
edad = df["edad"].unique()

# -------   ------  ------  TITULO APLICACIÓN  ------  ------  ------  -----   
labelTitulo = tk.Label(miVentana, text="Bienvenido/a a la Herramienta de Consultas COVID-19 CABA", font=("arial", "18"), bg="AntiqueWhite2")
labelTitulo.pack()

# -------   ------  ------  BOTONES FECHAS  ------  ------  ------  -----   

varFechaDesde = tk.StringVar(miVentana)
varFechaDesde.set(fechasPosibles[0])

labelDesde = tk.Label(miVentana, text="Fecha desde:", font=("arial", "18"), bg="AntiqueWhite2")
menuDesde = tk.OptionMenu(miVentana,varFechaDesde,*fechasPosibles)

varFechaHasta = tk.StringVar(miVentana)
varFechaHasta.set(fechasPosibles[0])

labelHasta = tk.Label(miVentana, text="Fecha hasta:", font=("arial", "18"), bg="AntiqueWhite2")
menuHasta = tk.OptionMenu(miVentana,varFechaHasta,*fechasPosibles)

labelDesde.pack(pady=10)
menuDesde.pack(pady=6)
labelHasta.pack(pady=10)
menuHasta.pack(pady=6)

# -------   ------  ------  FUNCION QUE TOMA LOS DATOS  ------- ------- ------  ------

def registrar():

    # CAPTA LOS VALORES DE LOS BOTONES
    FechaDesdeElegida = varFechaDesde.get()
    FechaHastaElegida = varFechaHasta.get()
    RangoEdadElegida = varEdad.get()


    # CREA UN RANGO ENTRE LAS FECHAS ELEGIDAS
    fechas_elegidas = df[(FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida)]
    #print(fechas_elegidas["RangoEdad"])
    
    # # Mujeres confirmados
    mujeresConfirmadas = df[(df["sexo"] == "F") & (df["clasificacion_resumen"] == "Confirmado") & (FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida) & (RangoEdadElegida == df["RangoEdad"])]
    print("las mujeres confirmadas son :" + str(mujeresConfirmadas["indice"].count()))
    labelMujeresConfirmadas["text"] = "Mujeres confirmadas: " + str(mujeresConfirmadas["indice"].count())

    # # Hombres confirmados
    hombresConfirmados = df[(df["sexo"] == "M") & (df["clasificacion_resumen"] == "Confirmado") & (FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida) & (RangoEdadElegida == df["RangoEdad"])]
    print("los hombres confirmados son :" + str(hombresConfirmados["indice"].count()))
    labelHombresConfirmados["text"] = "Hombres confirmados: " + str(hombresConfirmados["indice"].count())

    # # Total Mujeres Analizadas
    mujeresAnalizadas = df[(df["sexo"] == "F") & (FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida) & (RangoEdadElegida == df["RangoEdad"])]
    print("Total mujeres analizadas: " + str(mujeresAnalizadas["indice"].count()))
    labelMujeresAnalizadas["text"] = "Mujeres analizadas: " + str(mujeresAnalizadas["indice"].count())

    # # Total Hombres Analizadas
    hombresAnalizados = df[(df["sexo"] == "M") & (FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida) & (RangoEdadElegida == df["RangoEdad"])]
    print("Total hombres analizados: " + str(hombresAnalizados["indice"].count()))
    labelHombresAnalizados["text"] = "Hombres analizados: " + str(hombresAnalizados["indice"].count())


# -------   ------  ------  BOTON EDADES  ------  ------  ------  -----   

# CUT a la tabla edad en 4 segmentos
cortesEspeciales = [df["edad"].min(),20,40,60,df["edad"].max()]
misRotulos = ["< A 20 AÑOS","20-40 AÑOS","40-60 AÑOS","> A 60 AÑOS"]
df["RangoEdad"]= pd.cut(df["edad"], bins=cortesEspeciales, labels=misRotulos)

dfAgrupado = df.groupby(["RangoEdad"]).agg({"edad":"count"})
#print(dfAgrupado)

varEdad = tk.StringVar(miVentana)
varEdad.set("< A 20 AÑOS")

labelEdad = tk.Label(miVentana, text="Grupos etarios:", font=("arial", "18"), bg="AntiqueWhite2")
labelEdad.pack(pady=10)
menuEdad = tk.OptionMenu(miVentana,varEdad,*misRotulos)
menuEdad.pack(pady=6)

# -------   ------  ------  BOTON MOSTRAR REPORTES  ------  ------  ------  ----- 
botonReportes = tk.Button(miVentana, text="Mostrar reportes", command=registrar, bg = "gray90", fg = "tomato")
botonReportes.pack(pady=10)


# -------   ------  ------  LABELS REPORTES  ------  ------  ------  -----
labelMujeresConfirmadas = tk.Label(miVentana, bg="AntiqueWhite2", font=("Helvetica", "14"), fg="black")
labelMujeresConfirmadas.pack()
labelHombresConfirmados = tk.Label(miVentana, bg="AntiqueWhite2", font=("Helvetica", "14"), fg="black")
labelHombresConfirmados.pack()
labelMujeresAnalizadas = tk.Label(miVentana, bg="AntiqueWhite2", font=("Helvetica", "14"), fg="black")
labelMujeresAnalizadas.pack()
labelHombresAnalizados = tk.Label(miVentana, bg="AntiqueWhite2", font=("Helvetica", "14"), fg="black")
labelHombresAnalizados.pack()


# -------   ------- ------- -------     GRAFICOS   ------    -------    -------    -------

# Funcion para grafico de torta -> cantidad de casos por cada percentil de edad
def generarTorta():
    plt.close('all')

    FechaDesdeElegida = varFechaDesde.get()
    FechaHastaElegida = varFechaHasta.get()

    fechas_elegidas = df[(FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida)]
    edadesEntreFechas = fechas_elegidas["RangoEdad"].value_counts()
    print(dfAgrupado)
    print(edadesEntreFechas)
    print(type(edadesEntreFechas))
    edadesEntreFechas.plot.pie(autopct='%.2f')

    plt.show()

botonTorta = tk.Button(miVentana, text="Mostrar grafico torta", command=generarTorta, bg = "gray90", fg = "tomato")
botonTorta.pack(pady=15)

# Funcion para grafico 2D -> cantidad de casos confirmados y descartados en funcion del tiempo
def generarGraficoTemp():
    plt.close('all')
    FechaDesdeElegida = varFechaDesde.get()
    FechaHastaElegida = varFechaHasta.get()
    fechas_elegidas = df[(FechaDesdeElegida <= df["fecha_referencia_tipo_caso"]) & (df["fecha_referencia_tipo_caso"] <= FechaHastaElegida)]
    dfPivoteado = df.pivot_table(index=fechas_elegidas["fecha_referencia_tipo_caso"], columns=["clasificacion_resumen"], values=["indice"],  aggfunc="count")
    print(dfPivoteado)
    dfPivoteado.plot.line()
    plt.show()

botonGraficoTemp = tk.Button(miVentana, text="Mostrar grafico temporal", command=generarGraficoTemp, bg = "gray90", fg = "tomato")
botonGraficoTemp.pack(pady=10)
label2 = tk.Label(miVentana, text="---")

miVentana.mainloop()
print("¡FIN!")

