
import random


class Pregunta:

    def __init__(self, enunciado, opciones, correcta):

        self.enunciado = enunciado

        self.opciones = opciones.copy()

        self.__correcta = correcta

        self.mezclar_opciones()

    @property
    def correcta(self):

        return self.__correcta

    def verificar_respuesta(self, respuesta):

        return respuesta == self.__correcta

    def mezclar_opciones(self):

        # Guardar las opciones con su índice original
        opciones_numeradas = list(
            enumerate(self.opciones)
        )

        # Mezclar las opciones
        random.shuffle(opciones_numeradas)

        # Obtener el nuevo orden
        self.opciones = [
            texto
            for indice, texto in opciones_numeradas
        ]

        # Actualizar el índice de la respuesta correcta
        self.__correcta = next(
            nuevo_indice
            for nuevo_indice, (indice_original, texto)
            in enumerate(opciones_numeradas)
            if indice_original == self.__correcta
        )
