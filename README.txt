LIBRERÍA DE MATRICES Y VECTORES COMPLEJOS

En la librería encontrará las herramientas para llevar a cabo operaciones con vectores y matrices complejas, como las siguientes:
Adición de vectores complejos.
Inverso (aditivo) de un vector complejo.
Multiplicación de un escalar por un vector complejo.
Adición de matrices complejas.
Inversa (aditiva) de una matriz compleja.
Multiplicación de un escalar por una matriz compleja.
Transpuesta de una matriz/vector
Conjugada de una matriz/vector
Adjunta (daga) de una matriz/vector
Producto de dos matrices (de tamaños compatibles)
Función para calcular la "acción" de una matriz sobre un vector.
Producto interno de dos vectores
Norma de un vector
Distancia entre dos vectores
Revisar si una matriz es unitaria
Revisar si una matriz es Hermitiana
Producto tensor de dos matrices/vectores


Para obtener una copia del proyecto es necesario dirigirse al link del repositorio (https://github.com/leoncico/LibreriaMatricesVectoresComplejos.git) y descargar todos los archivos publicados.

Pre-requisitos.
Es necesario descargar el entorno de desarrollo PyCharm o el lenguaje de programación Python.
Así mismo obtener una copia de la librería publicada en el repositorio.
Si aún no cuenta con alguno de los anteriores, siga los siguientes pasos:

Descargar e Instalar PyCharm.
1. Dirijase al siguiente link: https://www.jetbrains.com/es-es/pycharm/
2. Haga clic en el botón “Descargar”, es azul y está ubicado en la esquina superior derecha de la web.
3. A continuación elija su sistema operativo; ya sea Windows, macOS o Linux.
4. Haga clic en Descargar, bajo el titular “Community”.
5. Luego se iniciará la descarga y deberá esperar.
6. Una vez completada la descarga, abra el instalador, presione “siguiente” en los pasos posteriores y acepte los términos y condiciones de la aplicación.

Descargar e Instalar Python.
1. Diríjase al siguiente link: https://www.python.org/downloads/
2. Haga clic en el botón “Download Python”, si es necesario elija la versión para macOS o Linux.
3. Luego se iniciará la descarga y deberá esperar.
4. Una vez completada la descarga, abra el instalador, presione “siguiente” en los pasos posteriores y acepte los términos y condiciones de la aplicación.

Instalación.	
Obtener una copia del Proyecto.
1. Dijirase al link del repositorio: https://github.com/leoncico/LibreriaMatricesVectoresComplejos.git
2. Pulse el botón “Code” de color verde.
3. Seleccione la opción “Download ZIP”
4. Descomprima el .ZIP y ejecute el archivo .py

Ejecutando las pruebas.
Si desea realizar pruebas en la librería abra el archivo “TestLib2.py”, allí podrá probar cada una de las operaciones con los números que desee de la siguiente manera:

Luego del texto “self.assertEqual” se indica la operación a realizar, en los dos siguientes pares de vectores indique los complejos que desee operar (primer valor para real, segundo valor para imaginario), luego de la coma deberá ingresar el resultado que debería obtener), por ejemplo:

    def test_sumacplx(self):
        self.assertEqual(lc.sumacplx((3,-1),(1 , 4)), (4,3))
Donde (3,-1), (1,4) son los complejos que se desean sumar, (4,3) es el resultado a comprobar.

También podrá utilizar el archivo “Libreria2.py” para realizar las operaciones cuando lo necesite.
 
Construido con
PyCharm Community Edition

Autores
David Leonardo Piñeros – Programador.
Luis Daniel Benavides – Tutor y Revisor.

Licencia
Este proyecto está bajo la licencia GNU General Public License - mire el archivo LICENSE.txt para mas detalles.