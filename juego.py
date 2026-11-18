import json
import random
from pathlib import Path
from pregunta import Pregunta

class Juego:

    def __init__(self):
        self.preguntas = []
        self.indice_actual = 0
        self.puntuacion = 0
        self.aciertos = 0
        self.errores = 0
        self.categoria = ""
        self.respondida = False

    def cargar_preguntas(self, categoria):

        ruta = Path(__file__).parent / "preguntas.json"

        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        preguntas_categoria = datos[categoria]

        seleccionadas = random.sample(
            preguntas_categoria,
            min(10, len(preguntas_categoria))
        )

        self.preguntas = [
            Pregunta(
                pregunta["enunciado"],
                pregunta["opciones"],
                pregunta["correcta"]
            )
            for pregunta in seleccionadas
        ]

        self.categoria = categoria
        self.indice_actual = 0
        self.puntuacion = 0
        self.aciertos = 0
        self.errores = 0
        self.respondida = False

    def obtener_pregunta(self):

        if not self.juego_terminado():
            return self.preguntas[self.indice_actual]

        return None

    def responder(self, respuesta):

        if self.juego_terminado() or self.respondida:
            return None

        pregunta = self.obtener_pregunta()

        es_correcta = pregunta.verificar_respuesta(respuesta)

        if es_correcta:
            self.puntuacion += 10
            self.aciertos += 1
        else:
            self.errores += 1

        self.respondida = True

        return es_correcta

    def siguiente_pregunta(self):

        if not self.juego_terminado() and self.respondida:
            self.indice_actual += 1
            self.respondida = False

    def juego_terminado(self):

        return self.indice_actual >= len(self.preguntas)

    def obtener_progreso(self):

        if not self.preguntas:
            return 0

        return self.indice_actual / len(self.preguntas)

    def obtener_resultados(self):

        return {
            "categoria": self.categoria,
            "puntuacion": self.puntuacion,
            "aciertos": self.aciertos,
            "errores": self.errores,
            "total": len(self.preguntas)
        }
