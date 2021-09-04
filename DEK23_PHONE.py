import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Set environment variables for your Account Sid and Auth Token!
# These can be found at twilio.com/console
# Your Account SID from twilio.com/console
account_sid = "" # COLOCA ENTRE LAS COMILLAS TU ACCOUNT SID DE TWILIO
# Your Auth Token from twilio.com/console
auth_token  = "" # COLOCA ENTRE LAS COMILLAS TU AUTH TOKEN DE TWILIO

client = Client(account_sid, auth_token)

# RECUERDA QUE PARA QUE FUNCIONA SPAM Y ROBOT DETECTOR DEBES INSTALAR EL PLUGIN NOMOROBO EN TWILIO ACCEDIENDO A TU CUENTA.


def presentation():
	os.system('clear')
	print("""                  ********************
		       DEK23 PHONE
		  ********************
		
		Suigueme en Twitter: @rickdeckard23
		Mi web: deckcard23.com""", end="\n\n")

def is_valid_number(number):

    try:
        response = client.lookups.phone_numbers(number).fetch(type="carrier")
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e



def datos_generales():
	phone_number = client.lookups \
        	             .phone_numbers(telefono) \
        	             .fetch(type=['carrier'])

	print(phone_number.carrier) # All of the carrier info.
	print(phone_number.carrier['name']) # Just the carrier name.

def chequear_telefono(telefono):
	number = client.lookups.phone_numbers(telefono).fetch()
	print(number.national_format)


def line_type(phone_number):
	"""
	Args:
	phone_number (string): phone number in e.164 format
	Returns:
	string: line type associated with the phone number
	possible values are mobile, landline, or voip
	"""
	phone_number_type = client \
		.lookups \
		.phone_numbers(phone_number) \
		.fetch(type='carrier') \
		.carrier \
		.get('type')
	return phone_number_type

def robot_spam(phone_number):
	phone_number = client.lookups \
		.phone_numbers(phone_number) \
		.fetch(add_ons='nomorobo_spamscore')

	print(phone_number.add_ons)

def is_robocaller(phone_number):
   """
   Args:
       phone_number (string): phone number in e.164 format

   Returns:
       boolean: 'True' if robocaller
   """
   spam_score = client \
       .lookups \
       .phone_numbers(phone_number) \
       .fetch(add_ons='nomorobo_spamscore') \
       .add_ons['results']['nomorobo_spamscore']['result']['score']

   return spam_score == 1


presentation()

telefono = input('Introduce tu número de teléfono (ejemplo. +34666445533): ')


print("Datos generales: ", end="")
datos_generales()
print("Chequeo del telefono: ", end="")
chequear_telefono(telefono)
print("El teléfono es válido:", end="")
print(is_valid_number(telefono))
phone_number = telefono
print("La línea es del tipo: ", line_type(phone_number))
print("(landline=fija   mobile=móvil   VOIP=Voz por datos)")
print("Datos sobre spam: ", end="")
robot_spam(phone_number)
print("Datos sobre linea robot:", end="")
print(is_robocaller(telefono))
