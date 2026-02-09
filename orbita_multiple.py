import numpy as np  
import matplotlib.pyplot as plt  

num_orbitas = int(input('Cuántas órbitas quieres simular: '))
colores = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']

for i in range(num_orbitas):
    radio = float(input(f'Radio para órbita {i+1} (km): '))
    angulos = np.linspace(0, 2*np.pi, 1000)

    if radio <= 2000:
        print(f'Órbita {i+1}: Baja sobre el mar')
    elif radio >= 1500001:
        print(f'Órbita {i+1}: Fuera de Órbita')
    elif radio >= 35787:
        print(f'Órbita {i+1}: Alta sobre el mar')
    elif radio >= 2001:
        print(f'Órbita {i+1}: Media sobre el mar')

    x = radio * np.cos(angulos)  
    y = radio * np.sin(angulos)  

    plt.plot(x, y, color=colores[i % len(colores)], label=f'Órbita {i+1}: {radio} km')  
    plt.title('Comparación de múltiples órbitas')  
    plt.xlabel('X (km)',
            fontsize=11)  
    plt.ylabel('Y (km)',
            fontsize=11)  
    plt.axis('equal')  
plt.show()