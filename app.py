from flask import Flask, render_template
import platform
import psutil
import os 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/metricas")
def metricas():
    dados = {
        "integrantes": "Angelo Andrioli Netho, Hugo Fagundes Faria Santos",
        "pid": os.getpid(),
        "cpus": psutil.cpu_percent(percpu=True),
        "memoria_usada_mb": round(psutil.virtual_memory().used / 1024 ** 2, 2),
        "sistema_operacional": platform.platform()
    }
    return dados

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    print("Nome dos integrates: Angelo Andrioli Netho, Hugo Fagundes Faria Santos")
    print(f"PID: {os.getpid()}")
    print(f"CPUS: {psutil.cpu_percent(percpu=True)}") 
    print(f"Memória Usada: {psutil.virtual_memory().used /1024 ** 2}" )
    print(f"Sistema Operacional: {platform.platform()}")
