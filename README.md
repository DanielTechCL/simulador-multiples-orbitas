# simulador-multiples-orbitas
# Simulador de Múltiples Órbitas

Este proyecto es un programa en Python que permite simular y visualizar múltiples órbitas circulares de forma interactiva. El usuario puede definir el radio de cada órbita y la cantidad de órbitas a simular, obteniendo un gráfico comparativo con diferentes colores y etiquetas.

## Descripción
El programa calcula las coordenadas X e Y de cada órbita utilizando funciones trigonométricas. Además, clasifica cada órbita según su altura sobre el nivel del mar:
- Órbita baja: ≤ 2000 km
- Órbita media: 2001 km – 35786 km
- Órbita alta: ≥ 35787 km
- Fuera de órbita: ≥ 1,500,001 km  

El gráfico resultante muestra todas las órbitas en el mismo plano, con colores distintos y leyenda para identificar cada una.

## Cómo funciona
1. El usuario ingresa la cantidad de órbitas que quiere simular.
2. Para cada órbita, ingresa el radio en kilómetros.
3. El programa calcula las coordenadas de la órbita y determina su tipo.
4. Se grafica cada órbita con un color diferente y se muestra la leyenda.

## Características
- Simulación de múltiples órbitas en un mismo gráfico.
- Clasificación automática de cada órbita según altura.
- Visualización clara y proporcional de todas las órbitas.
- Interactividad mediante entrada por consola.
- Código simple y fácil de entender, ideal para principiantes.

## Tecnologías
- Python 3
- NumPy
- Matplotlib

## Objetivo del proyecto
Este proyecto tiene fines educativos y está pensado para aprender Python, matemáticas básicas y visualización científica. Permite comprender cómo se representan gráficamente órbitas circulares y cómo se comparan diferentes radios de manera visual.



# Multi-Orbit Simulator

This project is a Python program that allows users to simulate and visualize multiple circular orbits interactively. Users can define the radius of each orbit and the number of orbits to simulate, generating a comparative plot with different colors and labels.

## Description
The program calculates the X and Y coordinates of each orbit using trigonometric functions. It also classifies each orbit based on its altitude above sea level:
- Low orbit: ≤ 2000 km
- Medium orbit: 2001 km – 35786 km
- High orbit: ≥ 35787 km
- Out of orbit: ≥ 1,500,001 km

The resulting plot shows all orbits on the same plane with different colors and a legend for easy identification.

## How it works
1. The user inputs the number of orbits to simulate.
2. For each orbit, the user enters the radius in kilometers.
3. The program calculates the coordinates and determines the orbit type.
4. Each orbit is plotted with a different color and labeled in the legend.

## Features
- Simulation of multiple orbits in a single plot.
- Automatic classification of each orbit by altitude.
- Clear and proportional visualization of all orbits.
- Interactive via console input.
- Simple and beginner-friendly code.

## Technologies
- Python 3
- NumPy
- Matplotlib

## Project Goal
This project is for educational purposes and designed to help beginners learn Python, basic mathematics, and scientific visualization. It allows understanding how circular orbits are graphically represented and how different radii can be compared visually.
