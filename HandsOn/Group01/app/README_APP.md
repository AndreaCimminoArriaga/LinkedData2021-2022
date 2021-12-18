# FUNCIONAMIENTO DEL PROGRAMA APP.PY

Una vez ejecutado el script de python, te saldrá un mensaje en el que te pregunta "What are you looking for?". A este mensaje se puede contestar con "pos" o con "street". Si contestas con "pos" entonces el sistema te pedirá que introduzcas una coordenadas, primero te pregunta por la longitud y después te preguntará por la latitud. A continuación, el sistema te preguntará si quieres introducir un radio, mediante la frase "Do you want a radius?". Se puede contestar con "Y" o "y" si quieres introducir un radio o con "N" o "n" si no deseas introducir un radio.

Por otra parte, si contestas a la primera pregunta con "street", el sistema te dirá que le introduzcas la calle deseada.

Teniendo en cuenta lo anterior, se nos presentan tres posibilidades, que se corresponden con las tres queries que conforman nuestra aplicación.

Si eliges contestar a la primera pregunta con "pos" y no quieres introducir un radio, entonces el sistema te devolverá todas las estaciones ordenadas por la distancia a su posición, introducida anteriormente, además de sus correspondientes direcciones y número de bicicletas en cada estación --> función find.

Por el contrario, si eliges contestar "pos", pero le quieres introducir un radio, el sistema te devolverá todas aquellas estaciones que se encuentran dentro de el radio introducido partiendo de las coordenadas. Las estaciones estarán ordenadas, en este caso, por el número de bicis. Además, también te devuelve las direcciones de las distintas estaciones, junto con sus distancias a las coordenadas --> función findRadius.

Por último, si eliges contestar a la primera pregunta con "street", el sistema te devolverá todas aquellas estaciones que se encuentran en la calle introducida, junto con la dirección exacta y el número de bicis de cada estación. Si la calle no existe o no contiene estaciones el sistema devolverá "The street is not valid" --> función findStreet.
