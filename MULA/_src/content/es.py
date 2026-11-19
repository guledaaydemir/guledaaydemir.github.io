# Spanish copy for the MULA website. Facts must match ../FACTS.md. Same structure as en.py, plus "species".
# {email} is replaced with the support address, {{link:ID}} with a page URL in the same language.
# The app's interface is English: quoted in-app labels stay in English, with a short Spanish translation.

T = {
    "lang_name": "Español",
    "skip": "Saltar al contenido",
    "menu": "Menú",
    "language": "Idioma",
    "close": "Cerrar",
    "home_label": "Inicio de MULA",
    "theme": "Ambiente de papel",
    "theme_light": "Papel claro",
    "theme_dark": "Bosque oscuro",
    "nav": {"home": "Inicio", "about": "Por qué MULA", "guides": "Guías", "faq": "Preguntas", "support": "Ayuda",
            "privacy": "Privacidad", "terms": "Términos"},
    "get": "Descargar",
    "badge": {"top": "Descargar en el", "big": "App Store", "aria": "Descarga MULA: Plant Care en el App Store"},
    "llms_title": "MULA en texto plano para asistentes de IA",
    "free": "Gratis",
    "premium": "Premium",
    "months": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
               "noviembre", "diciembre"],
    "store_name": "MULA: Plant Care",
    "seasons": ["Primavera", "Verano", "Otoño", "Invierno"],
    "season_months": ["mar – may", "jun – ago", "sep – nov", "dic – feb"],
    "light": {"low": "Poca luz", "bright": "Luminosa, indirecta", "direct": "Sol directo"},
    "place": {"inside": "Interior", "balcony": "Balcón", "outside": "Exterior"},
    "intro": {"skip": "Saltar intro", "tagline": "Cuida · Crece · Florece"},

    "foot": {
        "tagline": "Una app tranquila para cuidar plantas y flores en el iPhone. Una revisión de la tierra, nunca una "
                   "orden.",
        "app": "MULA", "learn": "Guías", "help": "Ayuda", "more": "Más apps de la desarrolladora",
        "demo": "Prueba la revisión de la tierra", "all_guides": "Todas las guías",
        "privacy": "Política de privacidad", "terms": "Términos de uso",
        "made": "Hecho despacio y con cariño por",
        "apple": "Apple, iPhone, Apple Watch y Siri son marcas comerciales de Apple Inc.",
        "apps": [("Solo.Shots", "Timelapses de tu planta", "https://apps.apple.com/app/id6762450478"),
                 ("Solora", "Un planificador de vida amable", "https://apps.apple.com/app/id6778808618")],
    },
    "cta_box": {"h": "Deja que MULA pregunte por ti",
                "p": "Gratis en el App Store para iPhone y iPad, con Apple Watch y widgets. Sin anuncios, sin cuenta."},

    "article": {"by": "Por", "updated": "Actualizado", "read": "{n} min de lectura", "answer": "Respuesta corta",
                "takeaways": "Puntos clave", "toc": "En esta página", "faq": "Preguntas", "sources": "Fuentes",
                "related": "Sigue leyendo", "tip": "Consejo de MULA", "all": "Todas las guías",
                "art_label": "Retrato de papel"},
    "cats": {"app": "Usar MULA", "care": "Riego y cuidados", "seasons": "Estaciones y clima", "light": "Luz"},

    # ------------------------------------------------------------------ home
    "home": {
        "title": "App para cuidar plantas y recordatorio de riego | MULA",
        "description": "App para cuidar plantas en iPhone: MULA pregunta cómo está la tierra antes de regar, sigue "
                       "las estaciones y no hace ruido. Sin anuncios y sin cuenta.",
        "og_alt": "MULA, app para cuidar plantas en iPhone: pantalla Today (Hoy) con una costilla de Adán y tareas de "
                  "riego tranquilas",
        "eyebrow": "Cuidado de plantas y flores para iPhone",
        "h1": "Cuida tus plantas, con calma.",
        "lead": "MULA nunca te ordena regar. Pregunta cómo está la tierra, acompaña a cada planta a lo largo de las "
                "estaciones y solo habla cuando una planta de verdad te necesita.",
        "cta_demo": "Prueba la revisión de la tierra",
        "badges": ["Sin anuncios, nunca", "Sin cuenta", "Tu jardín se queda en tu iPhone", "Apple Watch y widgets"],
        "phone_alt": "La pantalla de arranque de MULA armándose pieza a pieza y, después, la pantalla Today (Hoy)",
        "replay": "Ver de nuevo el arranque",
        "ribbon_label": "Plantas que MULA conoce, estación por estación",

        "faces_kicker": "Una cara para cada planta",
        "faces_h2": "Tu jardín, en fotografías y retratos de papel",
        "faces_lead": "Cada planta guarda su nombre, su imagen y su ritmo en un lugar tranquilo. Gira una tarjeta para "
                      "ver el retrato de papel recortado que MULA le asigna.",
        "faces_hint": "Toca una tarjeta para girarla",
        "faces": [("Momo", "monstera", "Monstera deliciosa"), ("Tsubaki", "camellia", "Camellia japonica"),
                  ("Nori", "ficus", "Ficus elastica"), ("Ajisai", "hydrangea", "Hydrangea macrophylla"),
                  ("Ran", "orchid", "Phalaenopsis"), ("Mame", "pilea", "Pilea peperomioides")],

        "soil_kicker": "La revisión de la tierra",
        "soil_h2": "Una revisión de la tierra, nunca una orden",
        "soil_lead": "La mayoría de las plantas de interior se pierden por exceso de agua, no por falta. Por eso, "
                     "cuando se cumple el intervalo de una planta, MULA no dice “riega ya”. Pregunta cómo está la "
                     "tierra, y tu respuesta decide.",
        "soil_eyebrow": "Riego · Momo",
        "soil_q": "¿Cómo está la tierra de Momo al tacto?",
        "soil_opts": [("dry", "Seca", "Hora de beber"), ("moist", "Un poco húmeda", "Revisar de nuevo en 2 días"),
                      ("wet", "Mojada", "Saltar esta vez"), ("unsure", "No lo sé", "Muéstrame cómo comprobarlo")],
        "soil_res": {
            "dry": "Riego registrado. La próxima revisión de la tierra de Momo será en {n} días, el ritmo de otoño "
                   "para una costilla de Adán.",
            "moist": "No se registra nada. MULA volverá a preguntar en 2 días.",
            "wet": "No se registra nada. Esta vez se salta; la próxima revisión llegará tras un intervalo completo de "
                   "{n} días.",
            "unsure": "Hunde un dedo 3 cm en la tierra. Si sale limpio y seco, es hora de regar. Si se le pega tierra, "
                      "espera.",
        },
        "soil_btn": {"dry": "Regué a Momo", "moist": "Revisar de nuevo en 2 días", "wet": "Saltar esta vez",
                     "unsure": "Elige cómo está la tierra"},
        "soil_points": [
            "Solo “Dry” (Seca) registra un riego, así el historial muestra lo que de verdad pasó.",
            "Responde desde la notificación, un widget, tu Apple Watch o Siri, sin abrir la app.",
            "Una revisión que espera demasiado pasa a “Emergency Care” (Cuidado urgente) a los 7 días. Tú eliges el "
            "número.",
        ],
        "soil_layers": {"dry": "seca", "moist": "húmeda", "wet": "mojada"},

        "seasons_kicker": "Planes de cuidado por estación",
        "seasons_h2": "Cada planta tiene su ritmo",
        "seasons_lead": "En los meses fríos, las plantas beben menos y descansan. MULA da a cada planta un plan para "
                        "las cuatro estaciones y ajusta los recordatorios cuando cambia la estación.",
        "seasons_pick": "Elige una planta",
        "seasons_water": "Riego",
        "seasons_water_v": "Revisar la tierra cada {n} días",
        "seasons_feed": "Abono",
        "seasons_feed_v": "Cada {n} días",
        "seasons_rest": "En reposo esta estación",
        "seasons_temp": "Temperatura",
        "seasons_temp_v": "Feliz entre {a} y {b} °C",
        "seasons_note": "Los planes son puntos de partida amables, no reglas. Verlos es gratis; cambiar los números es "
                        "Premium. El interruptor “Southern hemisphere” (Hemisferio sur) invierte las estaciones.",

        "features_kicker": "Dentro de MULA",
        "features_h2": "Todo lo que tu jardín necesita, nada que no",
        "features": [
            ("drop", "Recordatorios suaves", "Solo cuando una planta te necesita. Nunca de noche, nunca más de una vez "
                                             "al día para la misma planta, con sonidos tranquilos como una kalimba o "
                                             "un cuenco tibetano.", "free"),
            ("leaf", "Hoy, en orden", "Primero las revisiones atrasadas, luego lo que viene. “Emergency Care” solo da "
                                      "un paso al frente cuando una revisión lleva mucho retraso.", "free"),
            ("season", "Planes para las cuatro estaciones", "Intervalos de riego y abono para primavera, verano, "
                                                            "otoño e invierno. El abono se pausa mientras la planta "
                                                            "descansa.", "free"),
            ("frost", "Alertas de helada y calor", "El pronóstico de Apple Weather, comparado con el rango de confort "
                                                   "de cada planta del balcón. Un aviso la tarde antes de una noche "
                                                   "fría.", "premium"),
            ("sun", "Medidor de luz", "Sostén tu iPhone donde vivirá una planta. La cámara trasera estima la luz en "
                                      "lux y te muestra a qué plantas les gustaría ese rincón.", "premium"),
            ("camera", "“Not sure what it is?” (¿No sabes qué es?)",
             "Toma una foto y MULA le echa un vistazo en tu iPhone. Nombra tipos de planta como orquídea, rosa o "
             "helecho, y nunca adivina a la ligera.", "free"),
            ("book", "Diario y pósteres", "Primera flor, hoja nueva, un buen domingo. Las fotos se acompañan de un "
                                          "sereno retrato de papel, y cada planta puede convertirse en un póster.",
             "free"),
            ("suitcase", "Modo vacaciones", "Pausa los recordatorios, mantenlos o comparte una hoja de cuidados con "
                                            "quien te ayude. Nada se marca como hecho por ti.", "premium"),
            ("widget", "Widgets", "Ve la próxima planta en tu pantalla de inicio y en la pantalla bloqueada. Responde "
                                  "“Dry”, “Moist” o “Wet” (Seca, Húmeda, Mojada) directamente en los widgets más "
                                  "grandes.", "free"),
            ("watch", "Apple Watch", "Las plantas que te necesitan, en tu muñeca, con una complicación para la esfera "
                                     "del reloj.", "free"),
            ("wave", "Siri y Atajos", "“I watered Momo in MULA.” “What needs care in MULA?” En inglés y sin "
                                      "configurar nada.", "free"),
            ("moon", "Dos ambientes de papel", "“Light Paper” y “Dark Forest” (Papel claro y Bosque oscuro), textura "
                                               "de papel, movimiento sereno y una suave música de jardín con cantos "
                                               "de pájaros.", "free"),
        ],
        "tier_note": "Las funciones gratuitas llevan la etiqueta Gratis. Premium añade el resto.",

        "screens_kicker": "Pantallas reales",
        "screens_h2": "Hecha para sentirse como papel y mañanas tranquilas",
        "screens_lead": "Cada imagen de esta página es una pantalla real de la app, con un jardín de ejemplo.",
        "screens": [("today", "Today (Hoy): primero lo que te necesita"), ("soil", "La revisión de la tierra"),
                    ("garden", "My Garden (Mi jardín)"), ("plant", "La página de una planta"),
                    ("poster", "Póster: foto y retrato de papel"), ("seasons", "El año de una planta"),
                    ("weather", "Cuidados en orden, con un aviso de helada"),
                    ("whatplant", "“Looks like: Orchid” (Parece una orquídea)"), ("lightmeter", "El medidor de luz"),
                    ("vacation", "Modo vacaciones"), ("reminders", "Suave, y solo cuando hace falta"),
                    ("dark", "Dark Forest (Bosque oscuro)")],

        "light_kicker": "Luz",
        "light_h2": "¿Hay suficiente luz en este rincón?",
        "light_lead": "Mueve el sol para ver cómo se describe la luz y cuáles de las 20 plantas de MULA estarían "
                      "felices ahí.",
        "light_label": "Luz en este rincón",
        "light_value": "Unos {lux} lux",
        "light_fits": "Plantas a las que les gustaría este lugar",
        "light_note": "En la app, el medidor de luz (Premium) usa la cámara trasera de tu iPhone para estimar la luz. "
                      "No se toma ni se guarda ninguna foto, y es una estimación, no un instrumento de laboratorio.",

        "every_kicker": "Dondequiera que estés",
        "every_h2": "Responde sin abrir la app",
        "every_lead": "La misma revisión de la tierra vive en tus notificaciones, tus widgets, tu Apple Watch y Siri. "
                      "Responde donde estés; MULA guarda un único historial honesto.",
        "every_items": [
            ("Notificaciones", "“Dry · I watered it” (Seca · La regué), “A little moist” (Un poco húmeda) o “Wet” "
                               "(Mojada), directamente en el recordatorio. Los recordatorios de abono ofrecen “Fed "
                               "today” (Abonada hoy) o “Later” (Más tarde)."),
            ("Widgets", "Los widgets pequeño y de pantalla bloqueada muestran la próxima planta, gratis. Los widgets "
                        "mediano y grande añaden botones de respuesta con Premium."),
            ("Apple Watch", "Una lista de las plantas que te necesitan y una complicación para la esfera del reloj. "
                            "Responder desde la muñeca es Premium."),
            ("Siri", "Habla con MULA en inglés, sin configurar nada."),
        ],
        "siri_phrases": ["I watered Momo in MULA", "What needs care in MULA", "Soil check for Momo in MULA",
                         "I fed Momo in MULA"],
        "widgets_alt": "Widgets de MULA: la próxima planta, una pregunta sobre la tierra con los botones Dry, Moist y "
                       "Wet, y la lista de hoy",
        "watch_alt": "MULA en el Apple Watch: Momo, Mame y Nori necesitan cuidados",

        "why_kicker": "El nombre",
        "why_h2": "MULA significa raíz",
        "why_p": [
            "MULA viene de Mūlādhāra, el chakra raíz en sánscrito: mūla significa raíz y ādhāra, soporte. Es el "
            "primero de los siete, el que nos mantiene con los pies en la tierra, seguros y estables.",
            "Una planta muestra sus hojas, pero vive a través de sus raíces. Por eso MULA nunca ordena un riego. Te "
            "pide que primero toques la tierra y deja que la respuesta decida.",
        ],
        "why_link": "Por qué creamos MULA",

        "plans_kicker": "Gratis y Premium",
        "plans_h2": "Gratis para empezar. Premium cuando tu jardín crezca.",
        "plans_free_h": "Gratis",
        "plans_free": ["Hasta 10 plantas y 5 fotos de cada una",
                       "Recordatorios de revisión de la tierra con botones de respuesta",
                       "Planes de las cuatro estaciones para consultar",
                       "Revisión de temperatura por estación para plantas de balcón",
                       "Identificación por foto en tu iPhone",
                       "Widgets pequeño y de pantalla bloqueada, lista en Apple Watch, Siri",
                       "Light Paper y Dark Forest, sonidos tranquilos, música de jardín"],
        "plans_premium_h": "MULA Premium",
        "plans_premium": ["Plantas y retratos ilimitados", "Cambia cada plan de temporada",
                          "El diario de fotos completo y los pósteres", "Modo vacaciones y hojas de cuidados",
                          "Medidor de luz para cada rincón", "Alertas de helada y calor de Apple Weather",
                          "Responde desde los widgets mediano y grande y desde el Apple Watch"],
        "plans_note": "Anual con 1 semana de prueba gratis, o De por vida: pagas una vez y es tuyo para siempre. Los "
                      "precios se muestran en el App Store en tu moneda. Sin anuncios en ninguna versión.",

        "privacy_kicker": "Privacidad",
        "privacy_h2": "Tu jardín se queda contigo",
        "privacy_points": [("Sin cuenta", "Abre la app y empieza. No hay nada en lo que registrarse."),
                           ("Sin anuncios ni rastreo", "Sin publicidad, sin venta de datos. Solo estadísticas de "
                                                       "uso anónimas, nunca los nombres ni las fotos de tus plantas."),
                           ("En tu iPhone", "Plantas, fotos e historial viven en tu dispositivo, con copia en tu "
                                            "propio iCloud."),
                           ("Discretamente en el dispositivo", "La identificación por foto y el medidor de luz "
                                                               "funcionan en tu iPhone.")],
        "privacy_link": "Lee la política de privacidad",

        "guides_kicker": "Guías",
        "guides_h2": "Respuestas amables a preguntas reales sobre plantas",
        "guides_link": "Todas las guías",

        "faq_h2": "Preguntas y respuestas",
        "faq": [
            ("¿Qué es MULA?", "MULA es una app tranquila para cuidar plantas y flores en el iPhone y el iPad, con app para Apple "
                              "Watch, widgets y Siri. Te recuerda revisar la tierra en lugar de decirte que riegues un "
                              "día fijo, sigue las estaciones de cada planta y guarda un diario de fotos. Sin "
                              "anuncios, sin cuenta."),
            ("¿MULA es gratis?", "Sí. Descargar MULA es gratis y la versión gratuita guarda hasta 10 plantas con todos "
                                 "los recordatorios, revisiones de la tierra y planes por estación. MULA Premium (Anual "
                                 "con 1 semana de prueba gratis, o De por vida) añade plantas ilimitadas, edición de "
                                 "planes, modo vacaciones, el medidor de luz, alertas de helada y calor, y más."),
            ("¿Cómo sabe MULA cuándo regar?", "No adivina. Cada planta tiene un intervalo de revisión de la tierra "
                                              "para la estación actual. Cuando se cumple, MULA pregunta cómo está la "
                                              "tierra: “Dry” (Seca) registra un riego, “A little moist” (Un poco "
                                              "húmeda) vuelve a preguntar en 2 días y “Wet” (Mojada) salta esa vez."),
            ("¿Puede MULA identificar mi planta?", "Puede sugerir el tipo de planta a partir de una foto, en tu "
                                                   "iPhone: orquídea, rosa, tulipán, cactus, helecho y unos 20 tipos "
                                                   "en total. No identifica especies exactas ni diagnostica "
                                                   "enfermedades, y te lo dice cuando no está segura."),
            ("¿MULA necesita una cuenta o internet?", "No hace falta cuenta. MULA funciona sin conexión. Cuando hay "
                                                      "conexión, hace la copia y sincroniza tu jardín a través de tu "
                                                      "propio iCloud, envía estadísticas de uso anónimas y, si las "
                                                      "activas, pide a Apple Weather las alertas de helada y calor."),
            ("¿En qué dispositivos funciona MULA?", "En iPhone con iOS 17 o posterior, en iPad con iPadOS 17 o "
                                                    "posterior, en Mac con chip de Apple (como app de iPad) y en "
                                                    "Apple Watch con watchOS 10 o posterior. Con la sincronización "
                                                    "con iCloud, todos muestran el mismo jardín."),
            ("¿La app está en turco o en español?", "Por ahora, la interfaz de la app está en inglés. Este sitio web "
                                                    "está en inglés, turco y español."),
        ],
        "faq_more": "Más preguntas",

        "final_h2": "Haz sitio para un poco más de verde.",
        "final_p": "MULA guarda el nombre, la cara y el ritmo de cada planta en un lugar tranquilo.",

        "ld_features": ["Recordatorios de riego con revisión de la tierra (Seca / Un poco húmeda / Mojada)",
                        "Planes de cuidado para las cuatro estaciones",
                        "Recordatorios de abono que se pausan en la estación de reposo",
                        "Alertas de helada y calor de Apple Weather para plantas de balcón",
                        "Medidor de luz con la cámara del iPhone (estimación en lux)",
                        "Identificación de plantas por foto en el dispositivo (tipos de planta)",
                        "Diario de fotos y pósteres de plantas", "Modo vacaciones con hoja de cuidados",
                        "Widgets para la pantalla de inicio y la pantalla bloqueada",
                        "App para Apple Watch y complicaciones", "Siri y Atajos",
                        "Temas de papel claro y oscuro", "Sin anuncios, sin cuenta"],
        "ld_keywords": "app para cuidar plantas, recordatorio de riego, app de plantas de interior, app para regar "
                       "plantas iPhone, revisión de la tierra, cuidado de plantas por estación, medidor de luz para "
                       "plantas, alerta de heladas, diario de plantas",
    },

    # ------------------------------------------------------------------ about
    "about": {
        "title": "App para cuidar plantas: por qué creamos MULA",
        "description": "La historia de MULA, la app para cuidar plantas que pregunta cómo está la tierra en lugar de "
                       "ordenar un riego. El nombre, las ideas y su desarrolladora.",
        "kicker": "Por qué MULA",
        "h1": "Una planta muestra sus hojas, pero vive a través de sus raíces.",
        "lead": "MULA nació de un deseo sencillo: una app de plantas que se sienta como papel y mañanas tranquilas, y "
                "que nunca te haga regar una planta que no tiene sed.",
        "sections": [
            ("El problema de “riega cada domingo”",
             "<p>La mayoría de las apps de plantas funcionan como un despertador: riega esta planta cada siete días. "
             "Pero la sed de una planta cambia con la luz, la maceta, la estación y la habitación. En invierno, la "
             "misma costilla de Adán puede necesitar la mitad. Un calendario fijo es justo lo que hace que muchas "
             "plantas de interior acaben con exceso de riego, raíces empapadas y hojas amarillas.</p><p>Muchas de "
             "esas apps además hacen ruido: anuncios entre pantallas, rachas, cuentas, insignias. Cuidar de algo vivo "
             "debería sentirse más tranquilo que eso.</p>"),
            ("Preguntar, no ordenar",
             "<p>Por eso MULA pregunta. Cuando se cumple el intervalo de una planta, pregunta <em>¿cómo está la "
             "tierra?</em> “Dry” (Seca) significa que es hora de beber y el riego queda registrado. “A little moist” "
             "(Un poco húmeda) significa que MULA volverá a preguntar en dos días. “Wet” (Mojada) significa que esta "
             "vez se salta. Decide tu dedo en la tierra, no un calendario.</p><p>Lee más en "
             "<a href=\"{{link:when-to-water}}\">cada cuánto regar las plantas de interior</a>.</p>"),
            ("Seguir las estaciones",
             "<p>Cada planta en MULA tiene un plan para primavera, verano, otoño e invierno: cada cuánto revisar la "
             "tierra, cuándo abonar y cuándo dejarla descansar. Cuando cambia la estación, los recordatorios cambian "
             "con ella. Las plantas de balcón reciben una revisión de temperatura por estación y, con Premium, un "
             "aviso la tarde antes de una noche de helada.</p>"),
            ("El nombre: Mūlādhāra",
             "<p>MULA viene de <strong>Mūlādhāra</strong>, el chakra raíz en sánscrito. <em>Mūla</em> significa raíz "
             "y <em>ādhāra</em>, soporte. Es el primero de los siete, el que se asocia con sentirse con los pies en la "
             "tierra, a salvo y estable.</p><p>Cuidar de algo vivo también nos devuelve a la tierra. Esa es toda la "
             "idea de MULA: nada de ruido, solo el siguiente pequeño gesto que necesita tu jardín.</p>"),
            ("Papel, no plástico",
             "<p>MULA está dibujada como papel recortado: la textura cálida del washi, un sol, unas colinas, un cuenco "
             "de tierra con raíces. Dos ambientes de papel, “Light Paper” y “Dark Forest” (Papel claro y Bosque "
             "oscuro). Una tipografía con serifa que se lee como un libro. Sonidos suaves, como una kalimba o un "
             "cuenco tibetano, en lugar de alarmas, y una música de jardín tranquila con cantos de pájaros mientras la "
             "app está abierta. Cada planta recibe un retrato de papel recortado que acompaña a sus fotografías.</p>"),
            ("Privada por diseño",
             "<p>No hay cuenta de MULA ni servidor de MULA. Tus plantas, fotos e historial se quedan en tu iPhone. No "
             "hay anuncios ni rastreo; MULA solo envía estadísticas de uso anónimas, nunca los nombres, las notas ni "
             "las fotos de tus plantas. La identificación por foto y el medidor de luz "
             "funcionan en el dispositivo. Lee la <a href=\"{{link:privacy}}\">política de privacidad</a>.</p>"),
            ("Quién hace MULA",
             "<p>MULA está hecha por <strong>Gül Eda Aydemir</strong>, desarrolladora independiente de iOS que también "
             "crea Solo.Shots y Solora. Cada pantalla, cada sonido y cada palabra de la app están hechos con cuidado, "
             "sin prisa. Si tienes una idea o algo no va bien, escribe a <a href=\"mailto:{email}\">{email}</a> o "
             "saluda en Instagram en <a href=\"https://www.instagram.com/solo.stasera/\" "
             "rel=\"noopener\">@solo.stasera</a>.</p>"),
        ],
        "principles_h": "Cinco promesas tranquilas",
        "principles": [("Preguntar, no ordenar", "Una revisión de la tierra antes de cada riego."),
                       ("Seguir las estaciones", "Planes que descansan cuando la planta descansa."),
                       ("Solo cuando hace falta", "Nunca de noche, nunca dos veces al día por la misma planta."),
                       ("Nada que venderte", "Sin anuncios, sin cuenta, sin rastreo."),
                       ("Hecha como el papel", "Tranquila de mirar, tranquila de usar.")],
    },

    # ------------------------------------------------------------------ guides index
    "guides_page": {
        "title": "Guías para cuidar plantas: riego, luz y estaciones | MULA",
        "description": "Guías para cuidar plantas, tranquilas y prácticas: cada cuánto regar, señales de exceso de "
                       "riego, luz, estaciones, heladas y calor, vacaciones y la app MULA.",
        "kicker": "Guías",
        "h1": "Guías amables para preguntas reales sobre plantas",
        "lead": "Primero las respuestas cortas, luego los detalles. Escritas para quienes aman las plantas pero no "
                "quieren un título en botánica, y contrastadas con fuentes de horticultura de confianza.",
        "all": "Todas",
    },

    # ------------------------------------------------------------------ faq
    "faq_page": {
        "title": "App para cuidar plantas MULA: preguntas frecuentes",
        "description": "Respuestas sobre la app para cuidar plantas MULA: revisión de la tierra, estaciones, gratis o "
                       "Premium, widgets, Apple Watch, privacidad, idiomas y dispositivos.",
        "kicker": "Preguntas frecuentes",
        "h1": "Preguntas sobre MULA",
        "lead": "¿No encuentras tu respuesta? Escribe a {email}.",
        "groups": [
            ("Usar MULA", [
                ("¿Cómo añado una planta?", "Toca + en “Garden” (Jardín) o en “Today” (Hoy). Ponle un nombre, elige "
                                            "una especie (o quédate con el plan de cuidado general), indica dónde vive "
                                            "(“Indoor”, “Balcony” u “Outdoor”: interior, balcón o exterior) y cuánta "
                                            "luz recibe. MULA te sugiere un plan inicial suave que puedes cambiar "
                                            "después."),
                ("¿Por qué MULA pregunta por la tierra en lugar de decirme que riegue?",
                 "Porque la tierra sabe más que un calendario. Un riego solo se registra cuando dices que la tierra "
                 "estaba seca; “A little moist” (Un poco húmeda) vuelve a preguntar en 2 días y “Wet” (Mojada) salta "
                 "esa vez. Así se evita el problema más común de las plantas de interior: demasiada agua."),
                ("¿Qué es “Emergency Care” (Cuidado urgente)?", "Cuando una revisión de la tierra lleva esperando más "
                                                                "que tu límite (7 días por defecto; cámbialo en "
                                                                "“Settings → Emergency care after”, es decir, Ajustes → "
                                                                "Cuidado urgente después de), la planta sube a lo alto "
                                                                "de “Today” con un aviso extra."),
                ("¿Qué plantas conoce MULA?", "20 plantas con planes por estación: costilla de Adán, camelia, árbol "
                                              "del caucho, hortensia, orquídea mariposa, planta china del dinero, "
                                              "lengua de suegra, espatifilo, poto, lavanda, aloe vera, rosa, tulipán, "
                                              "cactus, helecho de Boston, hiedra, begonia, flor de Pascua, romero y "
                                              "palmera areca. Cualquier otra planta puede usar un plan de cuidado "
                                              "general que tú ajustas."),
                ("¿Puede MULA identificar una planta a partir de una foto?", "Sugiere el tipo de planta (unos 20 "
                                                                             "tipos, como orquídea, rosa, tulipán, "
                                                                             "cactus, helecho o palmera) con el "
                                                                             "reconocimiento de imágenes de Apple en "
                                                                             "tu iPhone. No da la especie exacta y "
                                                                             "nunca diagnostica plagas ni "
                                                                             "enfermedades."),
                ("¿MULA sigue las estaciones en el hemisferio sur?", "Sí. Activa “Settings → Southern hemisphere” "
                                                                     "(Ajustes → Hemisferio sur) y las estaciones se "
                                                                     "invierten."),
                ("¿Qué pasa mientras estoy de vacaciones?", "Con Premium, “Vacation mode” (Modo vacaciones) te permite "
                                                            "pausar los recordatorios, mantenerlos o compartir una "
                                                            "hoja de cuidados con quien te ayude. Nada se marca como "
                                                            "hecho por ti; cuando vuelves, MULA te ayuda a ver cómo "
                                                            "está cada planta."),
            ]),
            ("Recordatorios, widgets y dispositivos", [
                ("¿Cuándo llegan los recordatorios?", "A la hora que elijas en “Settings → Reminders & quiet hours” "
                                                      "(Ajustes → Recordatorios y horas de silencio), las 9:00 por "
                                                      "defecto; nunca durante las horas de silencio (de 22:00 a 08:00 "
                                                      "por defecto) y nunca más de una vez al día para la misma "
                                                      "planta."),
                ("¿Puedo responder sin abrir la app?", "Sí. Los recordatorios de revisión de la tierra tienen los "
                                                       "botones “Dry · I watered it” (Seca · La regué), “A little "
                                                       "moist” y “Wet”; los de abono tienen “Fed today” (Abonada hoy) "
                                                       "y “Later” (Más tarde). Con Premium también puedes responder "
                                                       "desde los widgets mediano y grande y desde el Apple Watch."),
                ("¿Qué widgets hay?", "Pequeño (la próxima planta) y de pantalla bloqueada (circular, rectangular y "
                                      "en línea), ambos gratis, además de los widgets mediano y grande, cuyos botones "
                                      "de respuesta son Premium."),
                ("¿MULA funciona con Siri?", "Sí, sin configurar nada: “I watered Momo in MULA”, “What needs care in "
                                             "MULA”, “Soil check for Momo in MULA”, “I fed Momo in MULA”. Las frases "
                                             "son en inglés."),
                ("¿Hay versión para iPad, Mac o Android?", "Para iPad y Mac, sí; para Android, por ahora no. La misma "
                                                           "app funciona en iPhone (iOS 17 o posterior), iPad "
                                                           "(iPadOS 17 o posterior) y Mac con chip de Apple, donde "
                                                           "muestra una columna tranquila del ancho de un teléfono. "
                                                           "Con “Sync with iCloud” (Sincronizar con iCloud) activado, "
                                                           "todos los dispositivos muestran el mismo jardín; Premium "
                                                           "llega con “Restore purchases” (Restaurar compras). El "
                                                           "medidor de luz necesita una cámara trasera, así que no "
                                                           "está disponible en Mac."),
                ("¿La app está disponible en otros idiomas?", "Por ahora, la interfaz de la app está en inglés. Este "
                                                              "sitio web está disponible en inglés, turco y "
                                                              "español."),
            ]),
            ("Gratis y Premium", [
                ("¿Qué es gratis?", "Hasta 10 plantas con 5 fotos cada una, todos los recordatorios de revisión de la "
                                    "tierra y de abono, ver los planes por estación, la revisión de temperatura por "
                                    "estación, la identificación por foto, los widgets pequeño y de pantalla "
                                    "bloqueada, la lista en el Apple Watch, Siri, ambos temas y los sonidos."),
                ("¿Qué añade Premium?", "Plantas y retratos ilimitados, edición de los planes por estación, el diario "
                                        "de fotos completo y los pósteres, el modo vacaciones y las hojas de cuidados, "
                                        "el medidor de luz, las alertas de helada y calor, y botones de respuesta en "
                                        "los widgets mediano/grande y en el Apple Watch."),
                ("¿Cuánto cuesta Premium?", "Premium es Anual (con 1 semana de prueba gratis) o De por vida (una sola "
                                            "compra). Los precios dependen de tu país y se muestran en el App Store "
                                            "antes de comprar."),
                ("¿Cómo cancelo o restauro?", "Cancela el plan Anual cuando quieras en Ajustes de tu iPhone → tu "
                                              "nombre → Suscripciones, al menos 24 horas antes de que se renueve. Para "
                                              "restaurar una compra, abre en MULA “Settings → MULA Premium → Restore "
                                              "purchases” (Ajustes → MULA Premium → Restaurar compras)."),
                ("¿Hay anuncios?", "No. Ni en la versión gratuita, ni en Premium, nunca."),
            ]),
            ("Privacidad y datos", [
                ("¿Dónde se guarda mi jardín?", "En tu iPhone (o iPad o Mac), compartido con los widgets y la app para Apple Watch "
                                                "de MULA, y con copia y sincronización a través de tu propio iCloud, "
                                                "que solo tú puedes ver. No hay cuenta de MULA ni servidor de MULA."),
                ("¿MULA recopila analíticas?", "Solo estadísticas de uso anónimas, a través de Google Analytics for "
                                               "Firebase: qué pantallas se abren, qué cuidados se registran y cuántas "
                                               "plantas tiene un jardín. Nunca nombres de plantas, notas, pies de "
                                               "foto ni fotos, y sin identificador de publicidad ni rastreo. Puedes "
                                               "desactivarlo en “Settings → Your garden → Share anonymous usage” "
                                               "(Ajustes → Tu jardín → Compartir uso anónimo)."),
                ("¿Por qué MULA pide mi ubicación?", "Solo si activas las alertas de helada y calor (Premium). Tu "
                                                     "ubicación aproximada se redondea a 1 km aproximadamente, se "
                                                     "guarda en tu iPhone y solo ese punto redondeado se envía a "
                                                     "Apple Weather para obtener el pronóstico."),
                ("¿Se guardan fotos del medidor de luz?", "No. El medidor de luz lee la exposición de la cámara para "
                                                          "estimar los lux; no se toma ni se guarda ninguna foto."),
                ("¿Cómo paso mi jardín a un iPhone nuevo?", "Inicia sesión con la misma cuenta de Apple e instala "
                                                            "MULA. Si tu jardín tiene copia en iCloud (“Settings → "
                                                            "iCloud backup”, activada por defecto), MULA te propone "
                                                            "recuperarlo antes de la introducción, con su historial, "
                                                            "sus fotos y tus ajustes. Premium vuelve con “Restore "
                                                            "purchases” (Restaurar compras)."),
                ("¿Puedo usar MULA en más de un dispositivo o compartir mi jardín?", "Sí. Con “Sync with "
                                                            "iCloud” (Sincronizar con iCloud) activado (“Settings → "
                                                            "Sync & sharing”, Ajustes → Sincronización y uso "
                                                            "compartido), todos los dispositivos con tu cuenta de "
                                                            "Apple muestran el mismo jardín. Con Premium también "
                                                            "puedes invitar a tu pareja o a quien comparte piso "
                                                            "contigo; cuando uno riega, el recordatorio del otro "
                                                            "desaparece sin ruido."),
            ]),
        ],
    },

    # ------------------------------------------------------------------ support
    "support": {
        "title": "Recordatorio de riego MULA: ayuda con avisos y Premium",
        "description": "Ayuda con el recordatorio de riego MULA: avisos que no llegan, widgets, Apple Watch, alertas "
                       "de helada, medidor de luz, restaurar Premium y cambiar de iPhone.",
        "kicker": "Ayuda",
        "h1": "¿Cómo podemos ayudarte?",
        "lead": "Escribe cuando quieras a {email}. Incluye el modelo de tu iPhone y la versión de iOS. La mayoría de "
                "las preguntas reciben respuesta en dos días hábiles.",
        "write": "Escribir a soporte",
        "write_subject": "Soporte de MULA",
        "faq_link": "Lee las preguntas frecuentes",
        "h_fix": "Soluciones rápidas",
        "fixes": [
            ("Los recordatorios no llegan", "<ul><li>Comprueba en Ajustes del iPhone → Notificaciones → MULA que las "
                                            "notificaciones estén permitidas.</li><li>En MULA, abre “Settings → "
                                            "Reminders & quiet hours” (Ajustes → Recordatorios y horas de silencio) y "
                                            "revisa los interruptores y la hora del recordatorio.</li><li>Los "
                                            "recordatorios nunca llegan durante las horas de silencio, y solo una vez "
                                            "al día por planta.</li><li>Los modos de concentración pueden retener las "
                                            "notificaciones; permite MULA en tus ajustes de Concentración.</li><li>Abre "
                                            "MULA una vez después de cambiar de zona horaria para que los "
                                            "recordatorios se vuelvan a programar.</li></ul>"),
            ("Los botones del widget no responden", "<p>Los botones de respuesta de los widgets mediano y grande "
                                                    "forman parte de MULA Premium. Un botón solo registra una "
                                                    "respuesta mientras esa tarea siga pendiente; si ya respondiste "
                                                    "en otro sitio, no hace nada. Quita el widget y vuelve a añadirlo "
                                                    "si parece desactualizado.</p>"),
            ("El Apple Watch no muestra nada", "<p>Abre MULA una vez en tu iPhone para que pueda enviar la lista más "
                                               "reciente al reloj. Si el iPhone no está cerca, las respuestas desde el "
                                               "reloj esperan y se aplican cuando lo esté. Responder desde el reloj es "
                                               "Premium.</p>"),
            ("Alertas de helada y calor", "<p>Necesitan MULA Premium, el permiso de ubicación aproximada y conexión a "
                                          "internet para Apple Weather. Las alertas son solo para plantas configuradas "
                                          "como “Balcony” (Balcón) u “Outdoor” (Exterior). Puedes ver la hora de la "
                                          "última actualización en “Settings → Reminders & quiet hours”.</p>"),
            ("El medidor de luz da lecturas raras", "<p>Sostén el iPhone donde vivirá la planta, con la cámara trasera "
                                                    "mirando hacia la ventana, y espera un momento a que se "
                                                    "estabilice. La lectura es una estimación; los umbrales (unos 800 "
                                                    "y 10 000 lux) son guías aproximadas, no ciencia exacta.</p>"),
            ("Restaurar Premium", "<p>Abre “Settings → MULA Premium → Restore purchases” (Ajustes → MULA Premium → "
                                  "Restaurar compras) con la sesión iniciada en el mismo Apple ID con el que compraste. "
                                  "Los reembolsos los gestiona Apple en <a href=\"https://reportaproblem"
                                  ".apple.com\" rel=\"noopener\">reportaproblem.apple.com</a>.</p>"),
            ("iPhone nuevo", "<p>Inicia sesión en iCloud con la misma cuenta de Apple e instala MULA. Si tu jardín "
                             "tiene copia (“Settings → iCloud backup”, Ajustes → Copia en iCloud), MULA te propone "
                             "restaurarlo antes de la introducción. También puedes hacerlo más tarde desde esa "
                             "misma pantalla. Premium vuelve con “Settings → MULA Premium → Restore purchases” "
                             "(Restaurar compras).</p>"),
            ("Borrarlo todo", "<p>Al eliminar la app MULA se borran del iPhone tus plantas, fotos e historial. Tu "
                              "copia en iCloud y tu jardín sincronizado se quedan en tu propio iCloud, así que "
                              "pueden volver; para quitarlos, borra los datos de MULA en Ajustes del iPhone → tu "
                              "nombre → almacenamiento de iCloud. Yo no guardo nada tuyo que haya que borrar.</p>"),
        ],
        "h_contact": "Contacto",
        "contact": "<p>Correo: <a href=\"mailto:{email}\">{email}</a><br>Instagram: <a href=\"https://www.instagram.com"
                   "/solo.stasera/\" rel=\"noopener\">@solo.stasera</a><br>Desarrolladora: Gül Eda Aydemir</p>",
    },

    # ------------------------------------------------------------------ privacy
    "privacy": {
        "title": "Política de privacidad de MULA: sin anuncios ni cuenta",
        "description": "Política de privacidad de MULA: sin anuncios, cuenta ni rastreo. Plantas, fotos e historial "
                       "viven en tu iPhone; solo se envían estadísticas de uso anónimas a Google Analytics for "
                       "Firebase.",
        "kicker": "Privacidad",
        "h1": "Política de privacidad",
        "lead": "En resumen: MULA guarda tu jardín en tu iPhone. No hay cuenta, ni servidor, ni anuncios, ni "
                "rastreo. MULA envía estadísticas de uso anónimas (Google Analytics for Firebase), nunca los "
                "nombres, las notas ni las fotos de tus plantas, y puedes desactivarlas en los ajustes. Las alertas "
                "de helada y calor envían una ubicación redondeada a Apple Weather, solo si las activas.",
        "effective": "Vigente desde",
        "badges": ["Sin anuncios", "Sin cuenta", "Sin rastreo", "Solo estadísticas anónimas", "Jardín en tu iPhone"],
        "sections": [
            ("1. Quiénes somos", "<p>MULA: Plant Care (“MULA”, “la app”) está hecha por Gül Eda Aydemir, desarrolladora "
                                 "independiente (“yo”). Esta política cubre la app MULA para iPhone, iPad, Mac y Apple Watch, sus "
                                 "widgets y este sitio web. Preguntas: <a href=\"mailto:{email}\">{email}</a>.</p>"),
            ("2. Qué guarda la app y dónde", "<p>Tus plantas (nombres, especies, dónde viven, luz), los planes de "
                                             "cuidado, el historial de cuidados, las fotos y notas del diario, y tus "
                                             "ajustes. Se guardan <strong>en tu iPhone</strong>, en un contenedor "
                                             "compartido con los widgets y la app para Apple Watch de MULA. MULA no "
                                             "tiene cuentas ni servidor propio, y yo no puedo ver ninguno de estos "
                                             "datos.</p><ul><li><strong>Copia en iCloud</strong> (activada por "
                                             "defecto): MULA guarda una copia de tu jardín, fotos incluidas, en su "
                                             "espacio privado de tu propio iCloud, para que pueda volver en un "
                                             "iPhone nuevo o después de borrar MULA. Solo tú puedes verla. Se "
                                             "desactiva en “Settings → iCloud backup” (Ajustes → Copia en iCloud)."
                                             "</li><li><strong>Sincronización con iCloud</strong> (activada por "
                                             "defecto): los dispositivos con tu cuenta de Apple muestran el mismo "
                                             "jardín, a través de CloudKit de Apple en tu base de datos privada de "
                                             "iCloud. Se desactiva en “Settings → Sync & sharing” (Ajustes → "
                                             "Sincronización y uso compartido).</li><li><strong>Jardín "
                                             "compartido</strong> (solo si invitas a alguien o aceptas una "
                                             "invitación): quienes están en él ven las mismas plantas, el mismo "
                                             "historial y las mismas fotos, y los nombres de los demás tal como los "
                                             "muestra iCloud. Quien se va conserva una copia de las plantas.</li>"
                                             "</ul><p>La copia y la sincronización necesitan que hayas iniciado "
                                             "sesión en iCloud. iCloud es un servicio de Apple y funciona según su "
                                             "<a href=\"https://www.apple.com/legal/privacy/\" rel=\"noopener\">política de privacidad</a>. Tu jardín también se incluye en las propias "
                                             "copias de seguridad de tu iPhone si las usas.</p>"),
            ("3. Estadísticas de uso anónimas", "<p>Para entender cómo se usa MULA y mejorarla, la app "
                                               "envía estadísticas de uso anónimas a <strong>Google Analytics for "
                                               "Firebase</strong>, un servicio de Google:</p><ul><li>qué pantallas "
                                               "se abren y qué cuidados se registran o se posponen (por ejemplo, "
                                               "“regada” o “aún húmeda”) y desde dónde (la app, un recordatorio, un "
                                               "widget, el Apple Watch o Siri);</li><li>categorías y cifras, nunca tus "
                                               "palabras: la especie de una planta según el catálogo de MULA, dónde "
                                               "vive y su luz, cuántas plantas, fotos y registros de cuidado tiene un "
                                               "jardín, qué ajustes están activados o desactivados y qué funciones "
                                               "se usan;</li><li>pasos relacionados con MULA Premium: cuándo se "
                                               "muestra la oferta, qué plan se elige y si hubo una compra, una prueba "
                                               "gratuita, una cancelación o un reembolso (nunca tu nombre ni tus "
                                               "datos de pago);</li><li>información técnica básica que Firebase "
                                               "recopila automáticamente: modelo de dispositivo, versión de iOS y de "
                                               "la app, idioma, un identificador aleatorio de la instalación y una "
                                               "región aproximada derivada de la dirección IP.</li></ul><p>MULA "
                                               "nunca envía los nombres de tus plantas, tus notas, los pies de foto, "
                                               "el nombre de quien te ayuda, tus fotos ni nada que escribas. Estas "
                                               "estadísticas no se vinculan a tu nombre, tu correo ni tu cuenta de "
                                               "Apple. MULA no usa el identificador de publicidad (IDFA), desactiva "
                                               "la personalización de anuncios y no te rastrea en apps ni webs de "
                                               "otras empresas. Google trata estos datos en mi nombre según sus <a "
                                               "href=\"https://firebase.google.com/support/privacy\" "
                                               "rel=\"noopener\">condiciones de privacidad de Firebase</a> y solo "
                                               "los conserva durante un tiempo limitado. Nada se vende ni se "
                                               "comparte con intermediarios de datos.</p><p><strong>Para "
                                               "desactivarlo</strong>, abre “Settings → Your garden” (Ajustes → Tu "
                                               "jardín) y desactiva “Share anonymous usage” (Compartir uso anónimo). "
                                               "MULA deja de enviar estadísticas y borra los datos de analítica de "
                                               "tu iPhone. MULA no tiene cuentas, así que nunca te pide tu nombre, "
                                               "correo ni teléfono, y no tiene herramientas de publicidad ni de "
                                               "informes de fallos.</p>"),
            ("4. Permisos", "<ul><li><strong>Notificaciones</strong>: para enviarte los recordatorios que elijas. iOS "
                            "los programa de forma local.</li><li><strong>Cámara</strong>: para tomar fotos de plantas "
                            "y, en el medidor de luz, para leer la exposición de la cámara. Las lecturas de luz nunca "
                            "se guardan y no se toma ninguna foto para ellas.</li><li><strong>Fotos</strong>: a través "
                            "del selector de fotos del sistema, MULA solo recibe las fotos que tú eliges.</li><li>"
                            "<strong>Ubicación aproximada (mientras se usa la app)</strong>: solo si activas las "
                            "alertas de helada y calor.</li></ul><p>Puedes cambiar cada permiso en los Ajustes de "
                            "iOS.</p>"),
            ("5. Alertas de helada y calor (Apple Weather)", "<p>Si activas las alertas meteorológicas (MULA "
                                                             "Premium), MULA te pide una vez tu ubicación aproximada, "
                                                             "la redondea a 1 km aproximadamente y la guarda en tu "
                                                             "iPhone. Solo ese punto redondeado se envía al servicio "
                                                             "WeatherKit de Apple para obtener el pronóstico. Apple "
                                                             "trata esta solicitud conforme a su <a href=\"https://www."
                                                             "apple.com/legal/privacy/\" rel=\"noopener\">política de "
                                                             "privacidad</a>. Si desactivas las alertas, no se hace "
                                                             "ninguna solicitud.</p>"),
            ("6. Funciones en el dispositivo", "<p>La identificación por foto usa el reconocimiento de imágenes de "
                                               "Apple en tu iPhone; la foto nunca sale del dispositivo. El medidor de "
                                               "luz también funciona en el dispositivo.</p>"),
            ("7. Compras", "<p>MULA Premium se vende a través del App Store de Apple. Apple procesa el pago; yo nunca "
                           "veo tus datos de pago. La app verifica tu compra con Apple (StoreKit) para desbloquear "
                           "Premium.</p>"),
            ("8. Enlaces a otras apps", "<p>“Settings → Grow further” (Ajustes → Seguir creciendo) puede abrir las "
                                        "páginas del App Store de mis otras apps (como Solo.Shots y Solora). No se les "
                                        "transmite nada sobre tu jardín.</p>"),
            ("9. Niños", "<p>MULA es una app para público general. No pide información personal a nadie, tampoco a "
                         "los niños. Las estadísticas de uso anónimas de la sección 3 son iguales para todos y no "
                         "se usan para identificar a nadie.</p>"),
            ("10. Conservación y eliminación de datos", "<p>Tus datos se conservan hasta que los eliminas. Una planta "
                                                        "eliminada espera 30 días en “Settings → Recently deleted” "
                                                        "(Eliminadas recientemente) y luego se borra. Al eliminar la "
                                                        "app, se borra todo lo que MULA guardó en el iPhone; tu copia "
                                                        "en iCloud y tu jardín sincronizado se quedan en tu iCloud "
                                                        "hasta que borres los datos de MULA en Ajustes de iOS → tu "
                                                        "nombre → almacenamiento de iCloud. Tu jardín nunca me llega. "
                                                        "Para borrar las estadísticas de uso anónimas de tu "
                                                        "instalación, desactiva “Share anonymous usage” y "
                                                        "escríbeme. Si me escribes un correo, "
                                                        "conservo la conversación solo para ayudarte y la elimino si "
                                                        "me lo pides.</p>"),
            ("11. Este sitio web", "<p>Este sitio web no usa cookies, analítica ni anuncios, y no carga fuentes ni "
                                   "scripts de terceros. Está alojado en GitHub Pages, que puede registrar datos "
                                   "técnicos como direcciones IP por motivos de seguridad. El sitio recuerda algunas "
                                   "pequeñas elecciones en el almacenamiento de tu propio navegador (el ambiente de "
                                   "papel, los elementos marcados de las listas, un aviso de idioma cerrado y si ya "
                                   "viste la intro); nunca salen de tu navegador.</p>"),
            ("12. Tus derechos", "<p>Tienes los derechos que te reconocen las leyes que se te aplican, como el "
                                 "Reglamento General de Protección de Datos (RGPD) o la KVKK de Turquía. MULA no "
                                 "recopila tu nombre ni tus datos de contacto y sus estadísticas de uso son anónimas, "
                                 "así que normalmente no hay nada a lo que acceder ni que corregir, "
                                 "pero siempre puedes escribirme.</p>"),
            ("13. Cambios", "<p>Si esta política cambia, la nueva versión aparecerá en esta página con una nueva fecha "
                            "de entrada en vigor.</p>"),
        ],
    },

    # ------------------------------------------------------------------ terms
    "terms": {
        "title": "Términos de uso de MULA, app para cuidar plantas",
        "description": "Términos de uso de MULA: Plant Care, con las suscripciones Premium, la semana de prueba "
                       "gratis, la compra De por vida y la información de cuidado de la app.",
        "kicker": "Términos",
        "h1": "Términos de uso",
        "lead": "Términos sencillos para una app tranquila. MULA se licencia bajo el EULA estándar de Apple junto con "
                "estos términos.",
        "effective": "Vigente desde",
        "sections": [
            ("1. El acuerdo", "<p>MULA se te concede bajo licencia conforme al <a href=\"https://www.apple.com/legal/"
                              "internet-services/itunes/dev/stdeula/\" rel=\"noopener\">Contrato de licencia de "
                              "usuario final de aplicaciones con licencia</a> de Apple (el EULA estándar) junto con "
                              "estos términos. Al usar MULA, aceptas ambos.</p>"),
            ("2. Qué es MULA", "<p>MULA es una herramienta de recordatorios y diario para el cuidado de plantas. Los "
                               "planes de cuidado, los intervalos y los rangos de temperatura son puntos de partida "
                               "generales que puedes cambiar. No constituyen asesoramiento profesional de "
                               "horticultura, y MULA no puede diagnosticar plagas, enfermedades ni el estado de salud "
                               "de las plantas. La identificación por foto y las lecturas de luz son "
                               "estimaciones.</p>"),
            ("3. MULA Premium", "<ul><li>Premium se ofrece como una suscripción <strong>Anual</strong> de renovación "
                                "automática con <strong>1 semana de prueba gratis</strong> para usuarios elegibles, o "
                                "como una compra única <strong>De por vida</strong>. Los precios se muestran en el App "
                                "Store antes de comprar.</li><li>El pago se carga a tu Apple ID al confirmar la compra "
                                "(en el plan Anual, cuando termina la prueba gratis).</li><li>La suscripción se renueva "
                                "automáticamente salvo que se cancele al menos 24 horas antes del final del periodo "
                                "en curso; la renovación se cobra dentro de las 24 horas anteriores al final del "
                                "periodo.</li><li>Gestiona o cancela la suscripción en Ajustes de tu iPhone → tu "
                                "nombre → Suscripciones.</li><li>Cualquier parte no utilizada de una prueba gratis se "
                                "pierde al comprar una suscripción.</li><li>Los reembolsos los gestiona Apple según sus "
                                "políticas.</li></ul>"),
            ("4. Datos meteorológicos", "<p>Las alertas de helada y calor usan datos de pronóstico de Apple Weather. "
                                        "Los pronósticos pueden fallar; usa tu propio criterio con las plantas en "
                                        "riesgo. La marca de Apple Weather y las fuentes de datos se muestran en la "
                                        "app.</p>"),
            ("5. Tu contenido", "<p>Tus plantas, fotos y notas son tuyas. Se quedan en tu dispositivo y, si usas la "
                                "copia o la sincronización con iCloud, en tu propio iCloud; yo no tengo ninguna "
                                "copia. Una copia puede fallar, por ejemplo si iCloud está lleno o desactivado, así "
                                "que haz también tus propias copias de seguridad.</p>"),
            ("6. Disponibilidad", "<p>Trabajo para que MULA funcione bien, pero no puedo prometer que esté siempre "
                                  "libre de errores. Las funciones pueden cambiar con el tiempo.</p>"),
            ("7. Responsabilidad", "<p>En la medida en que lo permita la ley, MULA se ofrece “tal cual”, y no soy "
                                   "responsable de la pérdida de plantas, de datos ni de otros daños indirectos "
                                   "derivados de su uso.</p>"),
            ("8. Contacto", "<p>Preguntas sobre estos términos: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ],
    },

    # ------------------------------------------------------------------ species (site only; not in en.py)
    "species": {
        "monstera": {"common": "Costilla de Adán", "tips": [
            "Llegan hojas nuevas. Abona una vez al mes y mantén la tierra ligeramente húmeda.",
            "Luz brillante e indirecta y una revisión semanal de la tierra hacen que las hojas sigan abriéndose.",
            "Riega con menos frecuencia y deja de abonar hasta marzo. Mantenla por encima de 15 °C.",
            "En reposo. Deja que se seque la capa superior de la tierra y aléjala de los cristales fríos.",
        ]},
        "camellia": {"common": "Camelia", "tips": [
            "Tras la floración, abona con un fertilizante para plantas ácidas y poda ligeramente.",
            "Mantén la tierra húmeda de forma uniforme y protégela del sol del mediodía.",
            "Mantén la tierra húmeda de forma uniforme y no cambies la maceta de sitio.",
            "En flor. Protege los capullos y las flores de las heladas.",
        ]},
        "ficus": {"common": "Árbol del caucho", "tips": [
            "Una nueva vaina roja anuncia una hoja nueva. Abona una vez al mes.",
            "Limpia las hojas y revisa la tierra cada semana.",
            "Riega con menos frecuencia. Ahora no le gusta que lo muevan.",
            "Aléjalo de las corrientes de aire y deja que la tierra se seque hasta la mitad.",
        ]},
        "hydrangea": {"common": "Hortensia", "tips": [
            "Los brotes se hinchan. Empieza a abonar y nunca dejes que la maceta se seque.",
            "Con el calor bebe mucho. Revisa la tierra cada dos días.",
            "Las flores se apagan. Deja de abonar y riega menos.",
            "En reposo y resistente. Deja las flores viejas en la planta para protegerla.",
        ]},
        "orchid": {"common": "Orquídea mariposa", "tips": [
            "Riega cuando las raíces se vuelvan plateadas. Un abono suave cada dos semanas.",
            "Mantenla lejos del sol directo y pulveriza las raíces en los días de calor.",
            "Las noches más frescas favorecen una nueva vara floral.",
            "Riega con moderación por la mañana y aléjala de los alféizares fríos.",
        ]},
        "pilea": {"common": "Planta china del dinero", "tips": [
            "Gira la maceta cada semana para que crezca pareja.",
            "Revisa la tierra a menudo; las hojas caídas piden agua.",
            "Riega menos y deja de abonar.",
            "Deja que se seque el tercio superior de la tierra entre riegos.",
        ]},
        "sansevieria": {"common": "Lengua de suegra"},
        "spathiphyllum": {"common": "Espatifilo"},
        "pothos": {"common": "Poto"},
        "lavender": {"common": "Lavanda"},
        "aloe": {"common": "Aloe vera"},
        "rose": {"common": "Rosa"},
        "tulip": {"common": "Tulipán"},
        "cactus": {"common": "Cactus"},
        "fern": {"common": "Helecho de Boston"},
        "ivy": {"common": "Hiedra"},
        "begonia": {"common": "Begonia"},
        "poinsettia": {"common": "Flor de Pascua"},
        "rosemary": {"common": "Romero"},
        "palm": {"common": "Palmera areca"},
    },
}
