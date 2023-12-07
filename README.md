#  Analysis_burgerking

En este proyecto se va a llevar a cabo un estudio estratégico sobre las ventas de Burger King. Se desempeña un proceso completo de los datos comenzando desde la creación de las fuentes, su preparación para realizar el almacenamiento de los datos, la creación de una base de datos estructurada con MySQLWorbench y finalizando con la explotación de los datos creando una visualización en PowerBI.

## Indice
1.[Contexto](#Contexto)\
2.[Fuentes de datos](#Fuentes_de_datos)\
3.[Almacenamiento de los datos](#Almacenamiento_de_los_datos)\
4.[Explotacion: visualizacion en PowerBI](#Explotación:visualización_en_PowerBI)

## 1. Contexto <a name="Contexto"/>
Burguer King, una cadena internacional perteneciente a la empresa Restaurant Brands
International, se centra en el sector de la restauración de comida rápida especializada en las
hamburguesas. A nivel nacional, en España, la marca ofrece una variada selección de productos
para satisfacer los gustos de sus clientes. Algunos de ellos son los siguientes:
- Hamburguesas: Carne 100% vacuno, sin conservantes ni aditivos, provenientes de la
Península Ibérica. Algunas de las hamburguesas más populares en España son: el Whopper, el
Steakhouse y el Big King.
- Menús: Ofrecen diferentes menús como, por ejemplo, el menú Originals, el menú
Parrilla, el menú Pollo o el menú Angus.
- Complementos y salsas: No toda su carta se centra en las hamburguesas, también tienen otros
productos, algunos de ellos son: patatas (fritas y supreme), aros de cebolla, Nuggets, etc.
- Postres: nos podemos encontrar con helados (ej: Sundae, King Fusion, Cono), tartas y
brownies, frutas, yogures…
- Bebidas y cafés
- Ensaladas
- Opciones vegetarianas y sin gluten
Por otra parte, esta cadena cuenta con alrededor de 900 restaurantes distribuidos en toda
España, brindando múltiples formas de servicio. Ofrecen servicio en el establecimiento para aquellos
que desean disfrutar de la experiencia en el local. La opción para llevar está disponible, incluyendo el
servicio de King auto para aquellos que prefieren llevar la comida en el coche. Además, la empresa se
adapta a la era moderna con un servicio a domicilio eficiente, gracias a su colaboración con riders.
Este enfoque integral destaca el compromiso de Burger King con la calidad, la variedad y la
adaptabilidad a las preferencias y necesidades de sus clientes.

## 2. Fuentes de datos <a name="Fuentes_de_datos"/>
En este proyecto, se ha decidido crear las fuentes de datos desde 0. Para poder llevarlo a cabo se ha tenido que realizar un estudio previo de la empresa estudiando sus ingresos anuales, la variación de los precios a lo largo de los años, el precio de sus productos, etc.

#### 2.1 Recopilación de precios y productos 
Lo primero que se realizó fue realizar una recopilación de los precios y productos de forma manual en un establecimiento en Madrid. Esto se llevo a cabo de forma manual ya que comprobamos que la variación de precios y productos disponibles en Uber Eats, Glovo e inclusive, su propia página web, divergía mucho en cuanto a lo ofrecido en los establecimientos. 

#### 2.2 Parámetros de dispersión para contextualizar los datos 
Para poder llevar a cabo una contextualización de los datos lo primeró que se hizo fue calcular una estacionalidad, tanto anual, como mensual.
Este proyecto se ha enfocado en realizar un estudio a corto plazo, con lo cual vamos a escoger unicamente los últimos 5 años (de 2018 a 2022). La estacionalidad anual la extraímos de este [link](https://www.statista.com/statistics/266462/burger-king-revenue/) pudiendo adquirir los ingresos anuales mundiales de Burger King en billones de Dólares Estado Unidenses(USD). 
Por otra parte, para estacionalizar los datos mensualmente, otorgamos unos indices de venta mayores a los meses con mayores ingresos como enero o diciembre y unos indices menores a los meses que tienen menos ventas, por ejemplo los correspondientes a los meses de verano (junio, julio y agosto).
Otro punto importante a tener en cuenta son los precios, ya que como bien sabemos, estos últimos años en nuestro país a habido una notable inflación. Así que, para poder adaptar los precios extraídos en 2023 a los años de los que realizamos el estudio, hemos utilizado el Indice Big Mac de la Eurozona extraído de The Economist (el csv utilizado se puede encontrar aquí). 

##### 2.3 Realización de dataframes
Para realizar una base de datos enfocandonos en el departamento de ventas de Burger King. Se ha decidido realizar 5 dataframes:
- canal_venta: contiene los canales de venta por los que se puede comprar su productos y sus respectivos ids.
- tickets: este dataframe tiene los tickets de venta que se han realizado en estos últimos 5 años con sus fechas de emisión.
- categoría_producto: se enumeran las diferentes categorías de los productos que están a la venta en los estableciemientos con sus respectivos ids.
- productos: en esta tabla se pueden ver los diferentes productos que venden en los establecimientos y las categorías a las que pertenecen. 
- ventas: se pueden encontrar los precios (estacionalizados) y las unidades vendidas para cada ticket y producto.

## 3. Almacenamiento de los datos <a name="Almacenamiento_de_los_datos"/>
Una vez preparados ya los dataframes añado las tablas a MySQL. Para poder relacionarlas todas se ha decidido crear las siguientes llaves:
- Canal_venta: en esta tabla la primary key es id_canal.
- Tickets: tenemos como primary key id_ticket y como foreign key id_canal para poder relacionar esta tabla con canal_ventas.
- Categoria_producto: la primary key que se ha creado es id_categoria_producto.
- Producto: se ha establecido como primary key id_producto y como foreign key id_categoria_producto.
- Ventas: en esta tabla unicamente nos encontramos con dos foreign keys las cuales son id_ticket y id_producto.
En cuanto a las relaciones, han sido one to many todas,aunque se podría considerar que ventas actúa como tabla intermedia (pero hemos incorporado columnas adicionales). 
Se puede ver el ERD en la imagen siguiente:![](https://github.com/Lidiavf1912/analysis_burgerking/blob/main/imagenes/esquema_erd.png)

## 4. Explotación:visualización en PowerBI <a name="Explotación:visualización_en_PowerBI"/>

