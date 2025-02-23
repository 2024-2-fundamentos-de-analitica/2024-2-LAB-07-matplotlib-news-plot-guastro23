"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Lee el archivo 'files/input/news.csv', genera el gráfico de líneas que
    muestra cómo evolucionan los porcentajes de personas que
    adquieren noticias desde distintas fuentes (Television, Newspaper,
    Radio, Internet) en el tiempo, y lo guarda en
    'files/plots/news.png'.
    """
    # 1. Leer el archivo CSV (asegurarse de que la primera columna sea el índice).
    df = pd.read_csv('files/input/news.csv', index_col=0)
    
    # 2. Crear la figura.
    plt.figure(figsize=(8, 6))
    
    # Diccionario de colores (3 grises para Television, Newspaper y Radio, y azul para Internet).
    colors = {
        'Television': 'dimgray',
        'Newspaper': 'gray',
        'Radio': 'lightgray',
        'Internet': 'tab:blue'
    }
    
    # Diccionario para el "zorder" (qué trazas van encima).
    zorders = {
        'Television': 1,
        'Newspaper': 1,
        'Radio': 1,
        'Internet': 2  # Internet va encima
    }
    
    # Diccionario para el grosor de cada línea.
    line_widths = {
        'Television': 1.5,
        'Newspaper': 1.5,
        'Radio': 1.5,
        'Internet': 3.5  # más gruesa para resaltar
    }
    
    # 3. Graficar cada columna.
    for col in df.columns:
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            linewidth=line_widths[col],
            zorder=zorders[col]
        )
    
    # 4. Título (opcional para contexto).
    plt.title('People Get News', fontsize=16)
    
    # 5. Remover spines superior, derecha e izquierda.
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    
    # 6. Ocultar el eje Y (para que no se vean valores ni ticks).
    plt.gca().yaxis.set_visible(False)
    
    # 7. Agregar puntos y texto (fuente + valor %) al inicio y fin de cada traza.
    for col in df.columns:
        # Año inicial (primer índice) y su valor
        first_year = df.index[0]
        first_value = df[col].iloc[0]
        
        # Año final (último índice) y su valor
        last_year = df.index[-1]
        last_value = df[col].iloc[-1]
        
        # Punto y texto inicial
        plt.scatter(first_year, first_value, color=colors[col], zorder=zorders[col])
        plt.text(
            first_year - 0.2,  # desplazar un poco a la izquierda
            first_value,
            f'{col} {first_value}%',
            ha='right',
            va='center',
            color=colors[col]
        )
        
        # Punto y texto final (solo valor)
        plt.scatter(last_year, last_value, color=colors[col], zorder=zorders[col])
        plt.text(
            last_year + 0.2,
            last_value,
            f'{last_value}%',
            ha='left',
            va='center',
            color=colors[col]
        )
    
    # 8. Ajustar los ticks del eje X para que muestre todos los años del índice.
    plt.xticks(df.index, df.index, ha='center')
    
    # 9. Ajustar márgenes
    plt.tight_layout()
    
    # Asegurarnos de que la carpeta 'files/plots' exista
    os.makedirs('files/plots', exist_ok=True)
    
    # Guardar la figura en 'files/plots/news.png'
    plt.savefig('files/plots/news.png')
    plt.close()


