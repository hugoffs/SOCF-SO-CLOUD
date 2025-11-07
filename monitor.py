from flask import Flask
import platform
import psutil
import os 

print(psutil.cpu_percent())

print(psutil.cpu_percent(percpu=True))  # utilização por núcleo

print(psutil.virtual_memory())  # pegar informações da memória, está em unidade de medida: bytes

print(psutil.virtual_memory().used / 1024 ** 2)  # memória usada em MB

print(os.getpid())  # id do processo

print(platform.platform())  # qual SO está sendo utilizado