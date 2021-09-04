# DEK23_PHONE
Herramienta OSINT para obtener información de un teléfono usando TWILIO

INTRODUCCION
------------
DEK23_PHONE es un script desarrollado en Python3 y usado en Kali Linux. Mediante la herramienta TWILIO y usando su API podemos obtener información de un número de teléfono. La información que podemos obtener con este script es:
- Verificar si el número existe.
- El formato correcto del teléfono.
- La compañía a la que pertenece el teléfono.
- Los códigos de referencia del operador y del país.
- Si la línea es móvil, fija o voip.
- Si el número se utiliza para enviar spam.
- Si el número es un robot automático de llamadas.

CONFIGURACION
-------------
Para ejecutar el script debe tener instalado Python3 y la librería Twilio en python que se instala de la siguiente manera:

              pip install twilio
              
Una vez instalado el programa se ejecuta como cualquier otro script de Python3:

              python3 DEK23_PHONE.py
              
Pero antes debe ir a la web de TWILIO https://twilio.com y registrarse. El registro es gratuito y te dan un saldo en dólares gratuito para que utilices en todos sus servicios. Ahora ya puedes crear la API en la página principal. Con esta API que se compone del código SID y el token ya lo puedes copiar y pegar dentro del script DEK23_PHONE.py para poder usar la herramienta.

Es posible usar variables de entorno con la API si se desea, para ello consultar en la web de TWILIO.

Para que funcione la opción de spam y robot necesita acceder a su cuenta de TWILIO y en el apartado developer-->add-ons, instalar el plugin NOMOROBO.

FUNCIONAMIENTO
--------------
Al iniciar el script únicamente debe introducir un número de teléfono. En el formato que se pide (ejemplo para España: +3496XXXXXXX si fuera un fijo o +346XXXXXXXX si es móvil).

He aquí un ejemplo del teléfono +15108675309: 
Fuente: https://www.twilio.com/blog/2016/02/how-to-verify-phone-numbers-in-python-with-the-twilio-lookup-api.html


                  ********************
                       DEK23 PHONE
                  ********************

                Suigueme en Twitter: @rickdeckard23
                Mi web: deckcard23.com

Introduce tu número de teléfono (ejemplo. +34666445533): +15108675309
Datos generales: {'mobile_country_code': '311', 'mobile_network_code': '880', 'name': 'Sprint Spectrum, L.P.', 'type': 'mobile', 'error_code': None}
Sprint Spectrum, L.P.
Chequeo del telefono: (510) 867-5309
El teléfono es válido:True
La línea es del tipo:  mobile
(landline=fija   mobile=móvil   VOIP=Voz por datos)
Datos sobre spam: {'status': 'successful', 'message': None, 'code': None, 'results': {'nomorobo_spamscore': {'status': 'successful', 'request_sid': 'XRd9470d9d5c08666645922307e74be6df', 'message': None, 'code': None, 'result': {'status': 'success', 'message': 'success', 'score': 0, 'neighbor_score': 0}}}}
Datos sobre linea robot:False


AGRADECIMIENTOS
---------------
Este script ha sido posible realizarlo gracias a los post publicados en el blog de esta maravillosa herramienta que permite una infinidad de servicios. Recomiendo a los interesados visitar https://www.twilio.com/blog/tag/python donde podrá encontrar desarrollos muy interesantes relacionados con whatsapp, envio de mensajes de texto o multimedia, gestión de llamadas, machine learning con imagenes, etc.

