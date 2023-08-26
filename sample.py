# python -m uvicorn sample:app --reload --host 0.0.0.0
from typing import Union

from fastapi import FastAPI
from gpiozero import LED

app = FastAPI()
led = LED(14)


@app.get("/")
def read_root():
    return {"Hello": "World 2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/toggle")
def read_toggle():
    led.toggle()
    return {"status": led.value}

@app.get("/on")
def read_toggle():
    led.on()
    return {"status": led.value}

# Virtual button
@app.get("/off")
def read_toggle():
    led.off()
    return {"status": led.value}


# Status del boton del real

# Para accionar el boton remoto, crear un boton virtual y que ejecute el mismo flujo/funcion
# Del boton fisico
# Ustedes presiones el boton, yo presione el boton virtual. Ambos deben ejecutar:
# print("Hola mundo")

