from flask import Flask
import platform
import psutil
import os 

print(psutil.cpu_percent())

print(psutil.cpu_percent(percpu=True)) # ultilização por nucleo 

print(psutil.virtual_memory()) ## pegar cois ada Memoria , está em unidade de media : byts

print(psutil.virtual_memory().used / 1024 ** 2) 

print(os.getpid()) ## id do processo 

print(platform.platform()) ## qual SO está sendo ultizado 
