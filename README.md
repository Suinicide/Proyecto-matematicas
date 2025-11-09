🔐 Análisis de Red y Cifrado RSA en Nodos Centrales

Este proyecto analiza una red real de comunicaciones (Email-Eu-core) y simula el uso de criptografía RSA entre los nodos más importantes del grafo. Combina conceptos de análisis de redes complejas (Network Science) y seguridad informática (criptoanálisis práctico).

El objetivo es comprender cómo se comporta una red real de correos electrónicos, identificar los nodos más centrales y aplicar técnicas de cifrado para medir el rendimiento de RSA en un entorno simulado.

📘 Descripción del Proyecto
Análisis de red: Se descarga el dataset real de comunicaciones entre empleados (Email-Eu-core.txt.gz) desde el repositorio de Stanford SNAP. Se construye un grafo no dirigido donde los nodos representan personas y las aristas representan correos intercambiados. Se estudia la distribución de grados y se identifican los 5 nodos más centrales (con mayor número de conexiones).

Criptografía RSA: A los 5 nodos más centrales se les generan claves RSA de 2048 bits. Se simula el envío de mensajes cifrados entre ellos usando padding OAEP con SHA-256. Se miden los tiempos de cifrado, descifrado y el tamaño del mensaje cifrado.

Visualización y resultados: Se generan gráficas de la red, histograma de grados y barras comparativas de tiempos. Los resultados se exportan a un archivo CSV llamado resultados_rsa.csv.

⚙️ Tecnologías Utilizadas

Python 3.x

Librerías principales:

networkx → construcción y análisis del grafo.

matplotlib → visualización.

pandas → manejo de resultados.

cryptography → generación y uso de claves RSA.

urllib → descarga del dataset.

📂 Estructura del Proyecto

El repositorio está organizado de la siguiente forma:

📁 proyecto-red-rsa/
├── main.py                 # Código principal con todo el flujo del proyecto
├── resultados_rsa.csv      # Resultados exportados (tiempos, tamaños, etc.)
├── README.md               # Descripción del proyecto
└── email-Eu-core.txt.gz    # Dataset descargado automáticamente

🚀 Ejecución

Clonar el repositorio:

git clone https://github.com/tuusuario/proyecto-red-rsa.git
cd proyecto-red-rsa


Instalar las dependencias:

pip install networkx matplotlib pandas cryptography


Ejecutar el proyecto:

python main.py


Resultados generados:

Gráficas del grafo y distribución de grados.

Gráficas de tiempos de cifrado y descifrado.

Archivo resultados_rsa.csv con las métricas obtenidas.


