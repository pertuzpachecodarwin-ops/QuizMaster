
import json
from pathlib import Path


class Record:

    def __init__(self):

        self.ruta = Path(__file__).parent / "records.json"

        self.records = {
            "Tecnología": 0,
            "Cultura general": 0,
            "Deportes": 0,
            "Ciencia": 0
        }

        self.cargar_records()

    def cargar_records(self):

        if self.ruta.exists():

            try:

                with open(
                    self.ruta,
                    "r",
                    encoding="utf-8"
                ) as archivo:

                    self.records.update(json.load(archivo))

            except (json.JSONDecodeError, OSError):
                pass

    def guardar_records(self):

        with open(
            self.ruta,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                self.records,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def obtener_record(self, categoria):

        return self.records.get(categoria, 0)

    def actualizar_record(self, categoria, puntuacion):

        record_actual = self.obtener_record(categoria)

        if puntuacion > record_actual:

            self.records[categoria] = puntuacion

            self.guardar_records()

            return True

        return False
