
import flet as ft
from juego import Juego
from record import Record

class InterfazJuego:

    def __init__(self, page: ft.Page):

        self.page = page
        self.juego = Juego()
        self.record = Record()

        # Configuración de la ventana
        self.page.title = "QuizMaster"
        self.page.bgcolor = "#0F172A"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.page.window.width = 800
        self.page.window.height = 750
        self.page.window.min_width = 650
        self.page.window.min_height = 650

        self.page.padding = 30
        self.page.scroll = ft.ScrollMode.AUTO

        self.page.horizontal_alignment = (
            ft.CrossAxisAlignment.CENTER
        )

        self.page.vertical_alignment = (
            ft.MainAxisAlignment.CENTER
        )

        # Mostrar pantalla principal
        self.mostrar_inicio()
    
    def crear_tarjeta(self, categoria, icono, color):

        mejor_puntuacion = self.record.obtener_record(
            categoria
        )

        return ft.Container(
            content=ft.Column(
                controls=[

                    ft.Icon(
                        icono,
                        size=50,
                        color=color
                    ),

                    ft.Text(
                        categoria,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#FFFFFF"
                    ),

                    ft.Text(
                        "10 preguntas",
                        size=14,
                        color="#94A3B8"
                    ),

                    ft.Divider(
                        color="#334155",
                        height=10
                    ),

                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.EMOJI_EVENTS,
                                size=20,
                                color="#FACC15"
                            ),

                            ft.Text(
                                f"Récord: {mejor_puntuacion}/100",
                                size=15,
                                color="#FACC15",
                                weight=ft.FontWeight.BOLD
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],

                alignment=ft.MainAxisAlignment.CENTER,

                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                ),

                spacing=8
            ),

            width=280,
            height=210,
            bgcolor="#1E293B",
            border_radius=20,
            padding=20,
            ink=True,

            on_click=lambda e: self.iniciar_juego(categoria)
        )
    
    def mostrar_inicio(self):

        self.page.controls.clear()

        titulo = ft.Text(
            "QuizMaster",
            size=48,
            weight=ft.FontWeight.BOLD,
            color="#FFFFFF"
        )

        subtitulo = ft.Text(
            "¡Demuestra cuánto sabes!",
            size=20,
            color="#94A3B8"
        )

        tecnologia = self.crear_tarjeta(
            "Tecnología",
            ft.Icons.COMPUTER,
            "#3B82F6"
        )

        cultura = self.crear_tarjeta(
            "Cultura general",
            ft.Icons.PUBLIC,
            "#22C55E"
        )

        deportes = self.crear_tarjeta(
            "Deportes",
            ft.Icons.SPORTS_SOCCER,
            "#EAB308"
        )

        ciencia = self.crear_tarjeta(
            "Ciencia",
            ft.Icons.SCIENCE,
            "#A855F7"
        )

        fila_superior = ft.Row(
            controls=[
                tecnologia,
                cultura
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

        fila_inferior = ft.Row(
            controls=[
                deportes,
                ciencia
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

        self.page.add(

            ft.Icon(
                ft.Icons.PSYCHOLOGY,
                size=85,
                color="#A78BFA"
            ),

            titulo,
            subtitulo,

            ft.Container(height=15),

            ft.Text(
                "Selecciona una categoría",
                size=22,
                weight=ft.FontWeight.BOLD
            ),

            fila_superior,
            fila_inferior,

            ft.Container(height=15),

            ft.Divider(color="#334155"),

            ft.Text(
                "QuizMaster v1.0 | Python + Flet + POO",
                size=13,
                color="#64748B"
            )
        )

        self.page.update()

    def iniciar_juego(self, categoria):

        self.juego.cargar_preguntas(categoria)

        self.mostrar_pregunta()

    
    def mostrar_pregunta(self):

        self.page.controls.clear()

        pregunta = self.juego.obtener_pregunta()

        numero = self.juego.indice_actual + 1
        total = len(self.juego.preguntas)

        # Puntuación
        self.texto_puntuacion = ft.Text(
            f"{self.juego.puntuacion} puntos",
            size=18,
            weight=ft.FontWeight.BOLD,
            color="#FACC15"
        )

        # Barra de progreso
        self.barra_progreso = ft.ProgressBar(
            value=self.juego.obtener_progreso(),
            width=600,
            color="#8B5CF6",
            bgcolor="#334155"
        )

        # Encabezado
        encabezado = ft.Row(
            controls=[
                ft.Text(
                    f"Pregunta {numero} de {total}",
                    size=18,
                    color="#94A3B8"
                ),

                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.STAR,
                            color="#FACC15"
                        ),
                        self.texto_puntuacion
                    ]
                )
            ],
            width=600,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        # Panel de la pregunta
        panel_pregunta = ft.Container(
            content=ft.Text(
                pregunta.enunciado,
                size=25,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            width=600,
            padding=25,
            bgcolor="#1E293B",
            border_radius=20
        )

        # Crear las cuatro opciones
        self.botones_respuesta = []

        letras = ["A", "B", "C", "D"]

        for i, opcion in enumerate(pregunta.opciones):

            boton = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                letras[i],
                                size=20,
                                weight=ft.FontWeight.BOLD
                            ),
                            width=40,
                            height=40,
                            bgcolor="#334155",
                            border_radius=10,
                            alignment=ft.Alignment(0, 0)
                        ),

                        ft.Text(
                            opcion,
                            size=17,
                            expand=True
                        )
                    ],
                    spacing=15
                ),
                width=600,
                padding=15,
                bgcolor="#1E293B",
                border_radius=12,
                ink=True,

                on_click=lambda e, indice=i:
                    self.procesar_respuesta(indice)
            )

            self.botones_respuesta.append(boton)

        # Mensaje de respuesta
        self.mensaje_respuesta = ft.Text(
            "",
            size=19,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        # Botón siguiente
        self.boton_siguiente = ft.Button(
            content=(
                "Ver resultados"
                if numero == total
                else "Siguiente pregunta"
            ),
            icon=ft.Icons.ARROW_FORWARD,
            bgcolor="#7C3AED",
            color="#FFFFFF",
            width=300,
            height=50,
            disabled=True,
            on_click=self.avanzar_pregunta
        )

        # Mostrar todos los elementos
        self.page.add(

            ft.Icon(
                ft.Icons.QUIZ,
                size=55,
                color="#A78BFA"
            ),

            ft.Text(
                self.juego.categoria,
                size=32,
                weight=ft.FontWeight.BOLD
            ),

            encabezado,

            self.barra_progreso,

            panel_pregunta,

            *self.botones_respuesta,

            self.mensaje_respuesta,

            self.boton_siguiente,

            ft.TextButton(
                content="Volver al inicio",
                icon=ft.Icons.HOME,
                on_click=lambda e: self.mostrar_inicio()
            )
        )

        self.page.update()

    
    def procesar_respuesta(self, indice):

        # Evitar respuestas repetidas
        if self.juego.respondida:
            return

        pregunta = self.juego.obtener_pregunta()

        resultado = self.juego.responder(indice)

        # Cambiar colores de las opciones
        for i, boton in enumerate(self.botones_respuesta):

            if i == pregunta.correcta:
                boton.bgcolor = "#166534"

            elif i == indice:
                boton.bgcolor = "#991B1B"

            else:
                boton.bgcolor = "#1E293B"

            # Desactivar los clics
            boton.on_click = None

        # Mostrar resultado de la respuesta
        if resultado:

            self.mensaje_respuesta.value = (
                "¡Respuesta correcta! +10 puntos"
            )

            self.mensaje_respuesta.color = "#4ADE80"

        else:

            self.mensaje_respuesta.value = (
                "¡Respuesta incorrecta!"
            )

            self.mensaje_respuesta.color = "#F87171"

        # Actualizar puntuación
        self.texto_puntuacion.value = (
            f"{self.juego.puntuacion} puntos"
        )

        # Actualizar progreso
        self.barra_progreso.value = (
            (self.juego.indice_actual + 1)
            / len(self.juego.preguntas)
        )

        # Habilitar botón siguiente
        self.boton_siguiente.disabled = False

        self.page.update()

    
    def avanzar_pregunta(self, e):

        self.juego.siguiente_pregunta()

        if self.juego.juego_terminado():

            self.mostrar_resultados()

        else:

            self.mostrar_pregunta()

    
    def mostrar_resultados(self):

        self.page.controls.clear()

        resultados = self.juego.obtener_resultados()

        puntuacion = resultados["puntuacion"]
        aciertos = resultados["aciertos"]
        errores = resultados["errores"]
        total = resultados["total"]
        categoria = resultados["categoria"]
        nuevo_record = self.record.actualizar_record(
            categoria,
            puntuacion
        )

        mejor_puntuacion = self.record.obtener_record(categoria)

        porcentaje = (aciertos / total) * 100 if total else 0

        # Mensaje según el rendimiento
        if porcentaje == 100:
            mensaje = "¡Perfecto! Eres un maestro."
            color = "#FACC15"

        elif porcentaje >= 80:
            mensaje = "¡Excelente trabajo!"
            color = "#4ADE80"

        elif porcentaje >= 60:
            mensaje = "¡Muy buen desempeño!"
            color = "#60A5FA"

        elif porcentaje >= 40:
            mensaje = "¡Vas por buen camino!"
            color = "#FB923C"

        else:
            mensaje = "¡Sigue practicando!"
            color = "#A78BFA"

        # Panel de puntuación
        panel_puntuacion = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "PUNTUACIÓN FINAL",
                        size=16,
                        color="#94A3B8"
                    ),

                    ft.Text(
                        f"{puntuacion} / {total * 10}",
                        size=60,
                        weight=ft.FontWeight.BOLD,
                        color="#A78BFA"
                    ),

                    ft.Text(
                        f"{porcentaje:.0f}% de aciertos",
                        size=20,
                        color="#CBD5E1"
                    ),

                    ft.ProgressBar(
                        value=porcentaje / 100,
                        width=450,
                        color="#8B5CF6",
                        bgcolor="#334155"
                    )
                ],
                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                ),
                spacing=15
            ),
            width=600,
            padding=25,
            bgcolor="#1E293B",
            border_radius=20
        )

        # Tarjeta de respuestas correctas
        tarjeta_correctas = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.CHECK_CIRCLE,
                        size=40,
                        color="#4ADE80"
                    ),

                    ft.Text(
                        str(aciertos),
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="#4ADE80"
                    ),

                    ft.Text(
                        "Correctas",
                        size=18
                    )
                ],
                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                )
            ),
            width=290,
            padding=20,
            bgcolor="#1E293B",
            border_radius=20
        )

        # Tarjeta de respuestas incorrectas
        tarjeta_incorrectas = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.CANCEL,
                        size=40,
                        color="#F87171"
                    ),

                    ft.Text(
                        str(errores),
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="#F87171"
                    ),

                    ft.Text(
                        "Incorrectas",
                        size=18
                    )
                ],
                horizontal_alignment=(
                    ft.CrossAxisAlignment.CENTER
                )
            ),
            width=290,
            padding=20,
            bgcolor="#1E293B",
            border_radius=20
        )

        # Fila de estadísticas
        estadisticas = ft.Row(
            controls=[
                tarjeta_correctas,
                tarjeta_incorrectas
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

        # Botón para repetir la categoría
        boton_repetir = ft.Button(
            content="Volver a jugar",
            icon=ft.Icons.REFRESH,
            bgcolor="#7C3AED",
            color="#FFFFFF",
            width=300,
            height=50,
            on_click=lambda e: self.iniciar_juego(categoria)
        )

        # Botón para regresar al menú
        boton_inicio = ft.OutlinedButton(
            content="Menú principal",
            icon=ft.Icons.HOME,
            width=300,
            height=50,
            on_click=lambda e: self.mostrar_inicio()
        )

        # Mostrar pantalla completa
        self.page.add(

            ft.Icon(
                ft.Icons.EMOJI_EVENTS,
                size=100,
                color="#FACC15"
            ),

            ft.Text(
                "¡Juego terminado!",
                size=36,
                weight=ft.FontWeight.BOLD
            ),

            ft.Text(
                f"Categoría: {categoria}",
                size=18,
                color="#A78BFA"
            ),

            ft.Text(
                mensaje,
                size=22,
                weight=ft.FontWeight.BOLD,
                color=color
            ),

            panel_puntuacion,
            ft.Text(
                "Nuevo Record PERSONAL!"
                if nuevo_record
                else f"record personal: {mejor_puntuacion}/100",

                size=22 if nuevo_record else 16,
                color="#FACC15",
                weight=ft.FontWeight.BOLD
            ),

            estadisticas,

            ft.Container(height=10),

            boton_repetir,

            boton_inicio,

            ft.Divider(color="#334155"),

            ft.Text(
                "QuizMaster v1.0 | Python + Flet + POO",
                size=13,
                color="#64748B"
            )
        )

        self.page.update()

    
    


