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
Al iniciar el script únicamente debe introducir un número de teléfono. En el formato que se pide (ejemplo para España: +34966666666 si fuera un fijo o +34666666666 si es móvil).

AGRADECIMIENTOS
---------------
Este script ha sido posible realizarlo gracias a los post publicados en el blog de esta maravillosa herramienta que permite una infinidad de servicios. Recomiendo a los interesados visitar https://www.twilio.com/blog/tag/python donde podrá encontrar desarrollos muy interesantes relacionados con whatsapp, envio de mensajes de texto o multimedia, gestión de llamadas, machine learning con imagenes, etc.

