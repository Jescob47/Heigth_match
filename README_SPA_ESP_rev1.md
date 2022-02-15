### Mach Eight Sample Project

Gracias por tomarse el tiempo para realizar este proyecto de ejemplo. Somos una 
empresa con bases técnicas fuertes que valora enormemente a nuestros ingenieros.
Buscamos ingenieros inteligentes con excelente experiencia y/o mucho potencial.


## Proyecto

El proyecto consiste en crear una funcion que busca los jugadores de la NBA
basado en la entrada del usuario. Los datos originalmente vienen de
[aquí](https://www.openintro.org/data/index.php?data=nba_heights). Para facilidad
de implementación, hemos servido los datos en formato json [aquí](https://mach-eight.uc.r.appspot.com/).

La tarea es crear una aplicación que solicite al usuario que ingrese una entrada
numérica. La aplicación descarga los datos del sitio web arriba mencionado
(https://mach-eight.uc.r.appspot.com) e imprime todas las parejas de jugadores
cuyas alturas en pulgadas (in), al ser sumadas, corresponden al número de entrada.
Si no se encuentran coincidencias, la aplicación imprime "No se encontraron coincidencias"

Ejemplo de salida de la siguiente manera:
```
> app 139

- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks
```

El algoritmo para encontrar los pares debe ser más rápido que O(n^2). Debe
funcionar correctamente en todos los casos de borde. Esta _no_ es una prueba a
libro cerrado. Lo invitamos a contactarnos con cualquier duda que tenga.


## Evaluación

Todos los candidatos que presenten un algoritmo que es eficiente y correcto
pasarán al siguiente paso del proceso de selección. Definimos "eficiente" como
más rápido que O(n^2). Definimos "correcto" como imprimir la respuesta correcta
para todas las entradas posibles. Todas las tareas que no impriman la respuesta
correcta por la entrada del ejemplo mencionado arriba no serán tenidas en cuenta.

Si siente que nos quiere impresionar yendo más allá, nos impresionan las
buenas pruebas unitarias y el código limpio. No es prioridad el conocimiento de un
sistema específico como react o django. Puede crear una aplicación compleja de
una sola pagina con bonitos gráficos si quiere, pero esto no va a mejorar la
probabilidad de pasar ya que no es lo prioritario. Hemos recibido tareas que han pasado nuestros filtros que
contienen poco menos de 30 líneas de código.

## Envío

La forma preferida de envío es mediante la publicación de un repositorio
público en github con su código y un archivo README que explique cómo ejecutar
el código. También podemos aceptar un archivo zip enviado por correo electrónico
con el mismo contenido. 
