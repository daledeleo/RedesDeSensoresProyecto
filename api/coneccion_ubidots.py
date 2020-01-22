from ubidots import *
import smtplib, ssl
import requests

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "banios.redes@gmail.com"  # Enter your address
receiver_email = "banios.redes@gmail.com"  # Enter receiver address
password = "redesdesensores2020"
message = """\
Subject: Agotamiento de papel higienico en el Banio de FIEC

Por favor realizar el cambio lo mas rapido posible."""

api = ApiClient(token="BBFF-dl4iMp3rt8ZGYV8kuJOx1qgDaiXC1C", base_url="http://things.ubidots.com/api/v1.6/",
                apikey="BBFF-4dc3e95dfb69c92faf9c517d5dfeb09d27d")

variable_distancia = api.get_variable("5e25fe124763e73f1946c34a")  # distancia
variable_magnetismo = api.get_variable("5e25fe134763e73f1946c34b")  # magnetismo
variable_obstaculo = api.get_variable("5e25fe144763e73bd046f96e")  # obstaculo
valores_finales = dict()


def llenar_arreglo_variables(dic):
    dic = {"distancia": variable_distancia.get_values(1)[0]["value"],
           "magnetismo": variable_magnetismo.get_values(1)[0]["value"],
           "obstaculo": variable_obstaculo.get_values(1)[0]["value"]}
    return dic


# print(llenar_arreglo_variables(valores_finales))

valor_dis = (llenar_arreglo_variables(valores_finales))["distancia"]

if (valor_dis >= 9.5 and valor_dis <= 11):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

"""
#valores_t=requests.get("")
valores_p=requests.get("https://trabajo-autonomo-3.firebaseio.com/Registros.json")
dicciona=valores_p.json()
print(dicciona['-Lz8a5xoQleoVOERV2qg'])
#print(valores_t.json()[0]["latitude"])
"""