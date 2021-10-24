# Hackbbva

## Equipo: Religión del cuyo

# Descripción de la iniciativa 

Esta iniciativa surge de la necesidad actual de llevar un control de gastos y facturación a fin de permitir a las personas comprobar sus ingresos y egresos para declarar impuestos y así recibir los reembolsos correspondientes. 

El objetivo es facilitar este proceso que muchas veces puede ser tedioso mediante la recaudación y almacenamiento de facturas y tickets para mantener una organización adecuada al momento de la declaración de impuestos. 

Por medio de la aplicación Ayudante Financiero, el usuario podrá escanear sus facturas y tickets, por medio de la cámara del celular, y estos se almacenarán de forma automática a la red de la aplicación y opcionalmente a la memoria interna del móvil.
La aplicación detectará el gasto generado y así mismo comprobación de ingresos y egresos, llevará un control del límite de consumo, y una media de consumo diario.

Como aditamento suplementario a la función principal de la aplicación, podrá generar una alta a la opción de análisis de viatico financiero de gasto total. Mostrará un monto máximo como el viático dado al usuario y éste se deducirá de las facturaciones generadas y a sí mismo generará un monto de deuda con la finalidad de tener un mejor manejo de sus finanzas.


# Objetivos 

Generar de manera autodidacta formación sobre el manejo sustentable y real de las finanzas de manera fácil y rápida.

Hoy en día el usuario tiene una exigencia mayor a las aplicaciones y funciones que instala en sus dispositivos inteligentes, del mismo modo esto implica y limita el compartir la información personal. Siendo así el usuario prefiere resolver las problemáticas y procesos tediosos de manera rápida y sencilla. Y al instalar y utilizar la aplicación tendrá acceso a realizar difíciles procesos de manera automática.
Facilitaremos la forma en la que se mueven las facturas y ayudará en los movimientos financieros. 
El ser humano por naturaleza es flojo. Si solo tiene que dar 1 click para hacer todo o buscarán así mismo las empresas y los individuos por facilitarse el trabajo harían uso como herramienta necesaria y casi obligatoria.
#### Cuantitativos
- Posicionar al Ayudante Financiero dentro de las primeras herramientas para el control financiero.
- Llegar a los 11.6 millones de usuarios (aprox.) móviles que tiene actualmente BBVA en su app.
- Que los 3,093,591 que realizan sus declaraciones anualmente utilicen la app como una herramienta extra para mejorar sus finanzas.  
####  Cualitativos 

- Que los usuarios encuentren dentro del Ayudante Financiero una herramienta amistosa, práctica y útil para realizar estimaciones de ingresos y egresos. 
- Que el usuario se sienta seguro de confiar en el banco y en sus herramientas para realizar operaciones financieras. 
- Mejorar la educación financiera de los mexicanos. 






# DESCRIPCIÓN TECNOLÓGICA

#### Descripción General
El usuario entra a la aplicación  por medio de apex y cuando hace una petición se conecta a aws usando s3, lambda y Api gateway.


#### Principales Tecnologías
En la nube:
- Apex
- Aws (S3, Lambda, Api Gateway)

#### Lenguajes:
- Js
- Python
- Html
- Css
- Sql

# Diagrama
![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/aws.png?raw=true)



# Prototipo 

link git
link api
link url
link video

# Definición de la audiencia
Usuarios de BBVA ,ciudadanos registrados en el padrón de contribuyentes y que poseen un RFC 
Personas en México que pagan impuestos (2021)

![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/Padr%C3%B3n%20por%20rfc.jpg?raw=true)
![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/padr%C3%B3n-por-tipo-de-contribuyente.png?raw=true)





Declaraciones de impuestos en México (2021)
![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/declaraciones-anuales-por-tipo-de-contribuyente.png?raw=true)
![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/declaracion%20por%20tipo%20de%20contribuyente.jpg?raw=true)









#### Mercado Meta
En los meses de enero, febrero y marzo del 2021 en México existen 78,883,432 ciudadanos registrados en el padrón de contribuyentes de los cuáles solo 3,093,591 realizan declaración de impuestos, dejándonos un resto de 75,789,841 ciudadanos que no realizan declaración.
Nuestro mercado meta son esos 3,093,591 que presentan su declaración con la posibilidad de aumentar esta cantidad en los meses consecutivos. 


# Estrategia de comunicación: Canales y puntos de contacto

Nuestra estrategia de comunicación se basa principalmente en el uso de la app. Desarrollando una campaña, tanto para los usuarios existentes de las nuevas funciones, como de los nuevos para que les resulte atrayente descargar y registrarse en la app. 

##### Canales 
- Internet
- Redes Sociales
- Aviso al inicio de la app 
- Impreso en Sucursal bancaria


# Indicadores de éxito
Para tener conocimiento si la aplicación tuvo éxito y saber si los usuarios una vez que la han obtenido la siguen necesitando es necesario llevar a cabo ciertas métricas.
##### Analitica digital de negocio
- Número de descargas de la aplicación
- Número de usuarios que abren e interactúan con la aplicación.
- Duración media de sesión (duración total de las sesiones dividido entre el número de sesiones)
- Intervalos entre sesiones
- Tiempo que el usuario pasa en la aplicación
- Uso de la aplicación (conocimiento de la navegación del usuario dentro de la app)
- Retención (porcentaje de usuarios que siguen utilizando la app después de cierto tiempo)


# Benchmark - Prácticas en el mundo 
|Aplicaciones por País   |Puntos Fuertes   | Puntos débiles  |
| ------------ | ------------ | ------------ |
|![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/declaraciones-anuales-por-tipo-de-contribuyente.png?raw=true)India   | - Acceso rápido a facturas y pagos recientes  | No muestra detalladamente los reportes   |
|   | Funciones comerciales  |No tiene categoría de productos   |
|   | Interfaz simple  |No registra otros ingresos sin factura   |
|   |Gestión de inventario   |No maneja códigos de barra.   |
|   | Tablas de informes  |   |
|  ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/Captura%20de%20pantalla%202021-10-22%20a%20las%2011.04.36.png?raw=true)Australia |  Interfaz simple |  Su función se limita a generar facturas. |
|   |Realiza facturas en segundos   |   |
|   |Ofrece múltiples formas de recibir pagos   |   |
|![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/Captura%20de%20pantalla%202021-10-22%20a%20las%2011.05.16.png?raw=true)España   | Crea facturas  |Difícil para ingresar   |
|   | Realiza presupuestos  |No hay una organización para las facturas   |
|   | Gestiona gastos, clientes y proveedores.  |No hay una organización para las facturas  |
|||Interfaz compleja|
|  ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/Captura%20de%20pantalla%202021-10-22%20a%20las%2011.05.58.png?raw=true)Canada |  Convierte presupuestos en facturas |  Solo enfocada para pequeñas empresas y generación de sus facturas|
| ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/Logo%20alegra.png?raw=true)México  | Crea, envía y administra tus facturas   |Interfaz compleja
|   | Controla y administra tus gastos y lo que debes |No te permite hacer correcciones |
|   | Controla y concilia tus cuentas bancarias  |No muestra el IVA ni los reportes del mismo. |
|| Incluye tienda en línea||
| ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/konfio.png?raw=true)México  | Emite, recibe, valida, consulta y envía tus comprobantes fiscales   |Interfaz de aplicación deficiente y compleja.
|   | Asesoría en facturación |
|   | Genera estadísticas y reportes. |
| ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/logo%20facturama.png?raw=true)México  | Genera comprobantes fiscales   |No te permite descargar facturas al celular
|   | Genera comprobante electrónico de pagos |
|   | Consulta facturas emitidas |
|   | Interfaz intuitiva |
| ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/logo%20factura%20app.png?raw=true)México  | Genera facturas de forma fácil   |Se limita a la generación de facturas
|   | Diversas opciones de diseño de factura |
| ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/logo%20invoice%20home.png?raw=true)México  | interfaz intuitiva  |No tiene versión para celular
|   | Facturas válidas ante el SAT |
|   | Precios bajos para su uso |
|   | Calcula impuestos |
| ![](https://github.com/DaliaVazquez/Hackbbva/blob/main/imagenes/logo%20invoice%20home.png?raw=true)España  | Creación de presupuestos  |No es gratuita y requiere un precio alto para usarla
|   | Gestión de cobros |
|   | Generación de facturas y gastos |



