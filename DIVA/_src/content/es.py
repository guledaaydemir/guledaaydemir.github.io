# DIVA website copy — Spanish (neutral Spanish for Spain and Latin America, "tú").
#
# Voice: Gül Eda, the reader's sassy Y2K BFF who built the app. Warm, funny, glam, honest.
# Rules every language keeps (same as en.py):
#   * Never promise outcomes. Affirmations are a ritual for mindset and mood, not magic, therapy,
#     medical, financial or sleep treatment.
#   * The voices are AI-generated (not real people, not imitating anyone).
#   * The app itself speaks English and Turkish, NOT Spanish. A Spanish speaker gets the English
#     app, so CD titles, ritual names and in-app buttons stay in English (with a Spanish gloss);
#     iPhone system menus are given in Spanish. iPhone only, iOS 17 or later.
#   * No account, no ads, no tracking; everything stays on the iPhone.
#   * Placeholders the builder replaces — keep them exactly, never translate them:
#       {{home}} {{guides}} {{faq}} {{support}} {{privacy}} {{guide:<id>}} {{appstore}}
#       [[img:<photo-slug>|<alt text>]]   [[cd:<cd_id>]]   [[cta]]
#     ([[img]] alt text after the "|" IS translated.)

LANG = "es"
OG_LOCALE = "es_ES"
NAME = "Español"

PATHS = {
    "home": "/DIVA/es/",
    "guides": "/DIVA/es/guias/",
    "faq": "/DIVA/es/preguntas-frecuentes/",
    "support": "/DIVA/es/soporte/",
    "privacy": "/DIVA/es/privacidad/",
}

UI = {
    "skip": "Saltar al contenido",
    "nav_guides": "Diarios de Diva",
    "nav_faq": "Preguntas",
    "nav_support": "Soporte",
    "nav_privacy": "Privacidad",
    "nav_cta": "Consigue DIVA",
    "menu": "Menú",
    "close": "Cerrar",
    "lang_label": "Idioma",
    "appstore_small": "Descárgalo en el",
    "appstore_big": "App Store",
    "appstore_aria": "Descarga DIVA en el App Store",
    "qr_caption": "¿No estás en tu iPhone? Escanéame con él, amiga.",
    "byline": "Gül Eda",
    "byline_role": "tu mejor amiga y la chica que creó DIVA",
    "published": "Publicado",
    "updated": "Actualizado",
    "min_read": "{n} min de lectura",
    "quick_answer": "La respuesta rápida, amiga",
    "toc": "En esta guía",
    "faq_in_guide": "Preguntas rápidas",
    "related": "Sigue leyendo, preciosa",
    "cds_in_guide": "Dale play a estos",
    "back_guides": "Todas las guías",
    "home_crumb": "DIVA",
    "cta_title": "¿Lista para tu era de protagonista?",
    "cta_body": "DIVA es gratis en iPhone (la app está en inglés y turco; las voces, en inglés). Elige un CD, dale play y escucha tu vida soñada.",
    "free": "GRATIS",
    "pro": "PRO",
    "lang_hint": "Psst, esta página también está en español.",
    "lang_hint_go": "Llévame ahí",
    "lang_hint_close": "No, gracias",
    "footer_tagline": "CDs de afirmaciones para protagonistas. Hecho con amor (y un poquito de leopardo) por Gül Eda.",
    "footer_disclaimer": "DIVA es para la reflexión personal y la relajación. No es consejo médico, psicológico ni financiero y no promete resultados. La narración es voz generada por IA.",
    "footer_app": "La app",
    "footer_help": "Ayuda",
    "footer_terms": "Condiciones de uso (EULA de Apple)",
    "footer_contact": "Soporte por email",
    "footer_rights": "© 2026 Gül Eda Aydemir. DIVA es una app independiente.",
    "guides_title": "Diarios de Diva: guías de afirmaciones y manifestación",
    "guides_desc": "Guías honestas y con chispa de Gül Eda, creadora de DIVA: cómo manifestar con afirmaciones, rituales de mañana y noche, dinero, vision board y más.",
    "guides_h1": "Diarios de Diva",
    "guides_script": "querido diario,",
    "guides_lead": "Todo lo que sé sobre afirmaciones, manifestación y rituales de protagonista, escrito como si le mandara mensajes a mi mejor amiga. Porque eso hago. Hola.",
    "faq_title": "Preguntas frecuentes sobre DIVA, app de afirmaciones",
    "faq_desc": "¿DIVA es gratis? ¿Las voces son reales? ¿Funciona sin conexión? ¿Está en español? Su creadora responde todo sobre esta app de afirmaciones para iPhone.",
    "faq_h1": "¿Dudas? Tengo respuestas, amiga.",
    "faq_script": "pregúntame lo que quieras",
    "faq_lead": "Todo lo que la gente me pregunta sobre DIVA, la app de CDs de afirmaciones para iPhone. ¿No encuentras tu pregunta? Escríbeme, de verdad leo todos los emails.",
}

HOME = {
    "title": "DIVA: app de afirmaciones y manifestación para iPhone",
    "description": "DIVA es una app de afirmaciones para iPhone donde cada tema es un CD. Elige tu era y una voz cálida, y escucha tu vida soñada. Gratis, sin cuenta ni anuncios.",
    "og_alt": "El logo DIVA de pedrería rosa sobre un tocador rosa brillante con leopardo y la frase “You are the main character” (tú eres la protagonista).",
    "hero_eyebrow": "Nueva en el App Store ✦ iPhone",
    "hero_script": "hola, preciosa",
    "hero_h1": "Afirmaciones para tu era de protagonista",
    "hero_lead": "DIVA es una app de afirmaciones donde cada tema es un CD. Elige tu era, elige una voz, dale play y escucha tu vida soñada, como si protagonizaras tu propia peli de supermodelos de los 2000.",
    "hero_cta": "Consigue DIVA, es gratis",
    "hero_cta2": "Escucha una demo primero",
    "hero_badges": ["Sin cuenta", "Sin anuncios", "Sin rastreo", "Funciona sin conexión"],
    "phone_from": "Gül Eda",
    "phone_time": "ahora",
    "phone_msgs": ["Amiga. OMG.", "Te hice una app 💿", "Es literalmente tu vida soñada en un CD. Dale play ✨"],
    "eras_kicker": "La colección",
    "eras_h2": "Elige tu era. Cada era es un CD.",
    "eras_lead": "20 CDs de afirmaciones en 12 eras: de la confianza y el brillo al dinero, el amor, tu carrera, la casa de tus sueños y el descanso de belleza. Cada uno es una sesión completa con intro, las afirmaciones y un cierre suave.",
    "eras_note": "12 CDs son gratis para siempre; el resto viene con DIVA PRO. Los títulos y el audio de los CDs están en inglés.",
    "demo_kicker": "Pruébala antes de descargarla",
    "demo_h2": "Dale play. Escucha tu vida soñada.",
    "demo_lead": "Son clips reales de la app, con las voces reales de DIVA. Elige un CD, cambia de voz y activa o quita el paisaje sonoro Pink Aura.",
    "demo_pick": "Elige un CD",
    "demo_voice": "Elige tu voz",
    "demo_aura": "Paisaje sonoro Pink Aura",
    "demo_play": "Reproducir",
    "demo_pause": "Pausa",
    "demo_now": "Sonando ahora",
    "demo_note": "Los clips de la demo son fragmentos cortos de los CDs reales. En la app, una sesión dura 10, 20 o 60 minutos, con tu paisaje sonoro favorito bajo la voz y un temporizador de apagado si lo necesitas.",
    "demo_lang_note": "Las voces de DIVA hablan inglés (español, todavía no); debajo de cada frase tienes la traducción.",
    "rituals_kicker": "Rituales diarios",
    "rituals_h2": "Glow-up al despertar. Glow-down al acostarte.",
    "rituals_lead": "En lo alto de My CDs (Mis CDs) te esperan dos meditaciones guiadas de afirmaciones. Respira, ponte cómoda, escucha las afirmaciones del día y repítelas mentalmente. Cada día de la semana tiene su propio tema.",
    "morning_title": "Morning Affirmations",
    "morning_body": "Afirmaciones de la mañana: una meditación guiada para empezar el día antes de que tu teléfono empiece a darte órdenes.",
    "night_title": "Bedtime Affirmations",
    "night_body": "Afirmaciones para dormir: una desconexión suave en el reproductor nocturno de luz tenue, con pausas largas y tranquilas. Un ritual para relajarte, no un tratamiento para el sueño.",
    "weekdays": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
    "rituals_note": "Gratis: 5 y 10 minutos. 20 minutos con PRO. Los recordatorios suaves de mañana y noche te llevan directo al ritual.",
    "wish_kicker": "Wishlist y vision board",
    "wish_h2": "Escríbelo como si ya estuviera en camino.",
    "wish_lead": "Tu Wishlist (lista de deseos) es donde los sueños hacen un poquito de papeleo. Viajes, casa, carrera, amor, dinero: escríbelo, sigue su progreso, vincúlalo a un CD y muévelo a Already Mine (¡ya es mío!) cuando llegue.",
    "wish_points": [
        "Sigue tu progreso y celebra cada hito",
        "Crea un vision board con tus propias fotos",
        "Vincula cada sueño al CD que le va",
        "Un recordatorio diario mantiene tu visión a la vista",
    ],
    "wish_dreams": [
        ["Penthouse con vistas", 72, "penthouse-lounge"],
        ["París, asiento de ventanilla", 45, "first-class-window"],
        ["Mi propia marca de skincare", 30, "skincare-satin"],
        ["El vestidor de mis sueños", 100, "walk-in-closet"],
    ],
    "wish_achieved": "ALREADY MINE ♡",
    "card_kicker": "Saca tu carta de diva",
    "card_h2": "¿Esperabas una señal? Es esta.",
    "card_lead": "Elige una era, revela la carta y llévate la frase para hoy. Cada frase sale directamente de un CD de DIVA (aquí, traducida al español).",
    "card_button": "Revelar mi carta",
    "card_again": "Otra, por favor",
    "card_from": "del CD",
    "card_back": "tu señal está cargando…",
    "voices_kicker": "Las voces",
    "voices_h2": "Cuatro voces. Cero energía de robot.",
    "voices_lead": "Voces de IA cálidas y naturales, que narran en inglés. Elige la que suene como tu mejor amiga interior.",
    "voices": {
        "velvet_whisper": ["Suave · Cálida · Para dormir", "La voz que quieres al oído a medianoche. Gratis."],
        "pink_muse": ["Íntima · Dulce · Glam", "Tu fan número uno, con brillo de labios. Gratis."],
        "runway_confidence": ["Segura · Clara · Luminosa", "Entra en la sala antes que tú. PRO."],
        "after_dark": ["Grave · Soñadora · Serena", "Energía de sábanas de seda y luces de ciudad. PRO."],
    },
    "auras_kicker": "Paisajes sonoros",
    "auras_h2": "Un aura para cada mood.",
    "auras_lead": "Escucha tus afirmaciones sobre un paisaje sonoro cálido, o solo con la voz. Pink Aura y Ocean at 2AM son gratis; el resto viene con PRO. Los tonos describen un estado de ánimo, no un efecto médico. Obvio.",
    "priv_kicker": "Privada por diseño",
    "priv_h2": "Sin cuenta. Sin anuncios. Sin rastreo. Punto.",
    "priv_body": "Tus afirmaciones, tus sueños y las fotos de tu vision board se quedan en tu iPhone. DIVA no tiene registro, ni red publicitaria, ni SDK de analítica, así que no hay nada que filtrar. Las protagonistas guardan su diario bajo llave.",
    "priv_link": "Lee la política de privacidad",
    "price_kicker": "Precios",
    "price_h2": "Gratis para empezar. PRO cuando te pones en modo diva total.",
    "free_title": "DIVA",
    "free_price": "Gratis",
    "free_items": [
        "12 CDs gratis con sesiones de 10 minutos",
        "Rituales de mañana y noche (5 y 10 min)",
        "Voces Velvet Whisper y Pink Muse",
        "Paisajes sonoros Pink Aura y Ocean at 2AM",
        "Crea hasta 3 CDs propios",
        "Wishlist con hasta 5 sueños en camino",
    ],
    "pro_title": "DIVA PRO",
    "pro_price": "desde 5,99 US$ al mes",
    "pro_items": [
        "Todos los CDs de la colección",
        "Sesiones completas de 20 y 60 minutos",
        "Todas las voces y todas las auras",
        "Escribe afirmaciones con tus propias palabras",
        "Temas Chrome Angel y Leopard Luxe",
        "Sueños ilimitados y todos los diseños de vision board",
    ],
    "plans": [["Mensual", "5,99 US$"], ["Anual", "29,99 US$"], ["De por vida", "69,99 US$, pago único"]],
    "price_note": "Precios de lanzamiento en EE. UU.; el App Store te muestra el precio en tu moneda. Las suscripciones se renuevan automáticamente salvo que las canceles al menos 24 horas antes de que termine el periodo. Gestiónalas o cancélalas cuando quieras en los ajustes de tu cuenta de Apple.",
    "letter_kicker": "Una nota de tu mejor amiga",
    "letter_h2": "Por qué creé DIVA",
    "letter_body": """
<p>Ok, momento storytime. Era la una de la madrugada y yo estaba tirada en el suelo, viendo videos de afirmaciones que sonaban como un GPS leyendo una galleta de la fortuna. Voz de robot. Fondo beige. Cero brillo. Y pensé: <em>perdona, ¿dónde está el glamour?</em></p>
<p>Crecí con la energía de las supermodelos de los 2000. Teléfonos de tapa, brillo de labios, leopardo en todo, chicas que entraban en una sala como si la sala tuviera que darles las gracias. Yo quería afirmaciones que se sintieran <em>así</em>. Como un CD que te pones mientras te arreglas para la noche de tu vida.</p>
<p>Así que la creé. Cada tema es un CD. Las voces son cálidas y suaves. Las frases están escritas para que suenen verdaderas en tu boca, sin cringe. Y es privada, porque tus sueños no son asunto de nadie más que tuyo.</p>
<p>No voy a fingir que una app puede regalarte un penthouse. Pero sé lo que se siente al empezar el día escuchando <em>“mi presencia ya es una entrada triunfal”</em> en lugar de mi propio doomscroll. De eso se trata. Dale play. Elígete a ti.</p>
""",
    "letter_sign": "xoxo, Gül Eda",
    "diaries_kicker": "Diarios de Diva",
    "diaries_h2": "Recién salido del blog",
    "diaries_lead": "Guías sobre manifestación, rituales y energía de protagonista, escritas como una nota de voz de tu mejor amiga.",
    "diaries_all": "Leer todas las guías",
    "faq_kicker": "Preguntas frecuentes",
    "faq_h2": "¿Dudas? Tengo respuestas.",
    "faq_all": "Ver todas las preguntas",
    "final_script": "modo protagonista: activado",
    "final_h2": "Tu era empieza cuando le das play.",
    "final_body": "Gratis en iPhone. Sin cuenta, sin anuncios. Solo tú, un CD y tu vida soñada en bucle.",
}

# Overrides for app text the app itself doesn't ship in Spanish. CD titles stay in English
# (that's what Spanish speakers see in the app), so CD_TEXT only carries subtitle and summary.
CATEGORIES = {
    "confidence": "Confianza",
    "beauty": "Belleza y brillo",
    "dream_life": "Vida soñada",
    "money": "Dinero y abundancia",
    "love": "Amor y relaciones",
    "sleep": "Dormir",
    "morning": "Mañanas",
    "gratitude": "Gratitud",
    "dream_home": "Casa soñada",
    "career": "Carrera",
    "self_worth": "Autoestima",
    "calm": "Pausa de calma",
}

CD_TEXT = {
    "that_girl_energy": {
        "subtitle": "Imperturbable. Magnética. Toda tú.",
        "summary": "Un CD de confianza, juguetón, para escuchar de día. Oirás frases en primera persona sobre sentirte a gusto contigo misma, ocupar tu espacio y llevar tu valor con ligereza. Dale play cuando quieras un momento para reconectar con tu propia energía.",
    },
    "born_to_be_iconic": {
        "subtitle": "Un brillo que nace por dentro.",
        "summary": "Un CD cálido sobre sentirte radiante y cómoda en tu propia piel. Las frases se centran en tratarte con cariño, cuidarte y disfrutar de que te vean, sin compararte con nadie. Escúchalo mientras te arreglas o cuando quieras un momento tierno frente al espejo.",
    },
    "the_life_i_ordered": {
        "subtitle": "Tu vida soñada, en bucle.",
        "summary": "Un CD lento y soñador para la noche. Oirás frases tranquilas en primera persona que imaginan una vida que te encanta como si ya la estuvieras viviendo, desde mañanas suaves hasta un hogar en paz. Es una práctica de imaginación para relajarte, no una promesa de resultados.",
    },
    "rich_girl_frequency": {
        "subtitle": "Opciones. Buen gusto. Tiempo.",
        "summary": "Un CD seguro y sin prisas sobre tu relación con el dinero. Las frases exploran sentirte en calma, tener opciones y disfrutar de las cosas bonitas sin culpa. Tómalo como una práctica de intención e imaginación, no como asesoramiento financiero ni como una promesa de resultados.",
    },
    "love_looks_good_on_me": {
        "subtitle": "No persigues. Atraes.",
        "summary": "Un CD nocturno, suave y susurrado, sobre el amor y las relaciones. Empieza recordándote que ya eres valiosa y luego recorre seis partes: conocer tu valor, el amor que llega con naturalidad, la relación con la que sueñas, atraer en lugar de perseguir, sentirte adorada y la gratitud por el amor que te rodea. Escúchalo como una reflexión tranquila sobre el tipo de amor que eliges.",
    },
    "whisper_to_your_future_self": {
        "subtitle": "Palabras suaves para cerrar el día.",
        "summary": "Un CD muy tranquilo para la hora de dormir, narrado despacio y con pausas largas. Las frases hablan de dar el día por terminado, sentirte a salvo para descansar y hablarle con cariño a la persona en la que te estás convirtiendo. Es un ritual suave para desconectar, no un tratamiento para el sueño.",
    },
    "wake_up_icon": {
        "subtitle": "Un comienzo divertido para tu día.",
        "summary": "Un CD de mañana corto y luminoso, con un guiño. Oirás frases juguetonas en primera persona sobre elegir tu estado de ánimo, arreglarte y entrar en el día siendo tú misma. Ponlo con el café o mientras te vistes.",
    },
    "thank_you_universe": {
        "subtitle": "Gracias suaves por lo que ya está aquí.",
        "summary": "Un CD tranquilo para la noche, construido en torno a apreciar el presente. Las frases van de los pequeños placeres a las personas que quieres y a todo lo que has avanzado. Úsalo como un momento de reflexión tranquila al final del día.",
    },
    "penthouse_state_of_mind": {
        "subtitle": "Vuelve a casa, a la comodidad y la calma.",
        "summary": "Un paseo lento por la noche a través de un hogar que se parece a ti. Las frases imaginan luz suave, una vista preciosa y la sencilla sensación de estar a salvo y cómoda donde vives. Escúchalo como una visualización acogedora mientras te preparas para la noche.",
    },
    "ceo_after_hours": {
        "subtitle": "Capaz, valorada y en calma.",
        "summary": "Un CD sereno y seguro sobre tu vida laboral. Las frases reflexionan sobre tu talento, el reconocimiento, el crecimiento y saber cuándo desconectar para volver a ser tuya. Ponlo antes de un gran día o de camino a casa, como una charla motivadora personal.",
    },
    "im_the_prize": {
        "subtitle": "Límites elegantes. Valor firme.",
        "summary": "Un CD con aplomo sobre el respeto propio y los límites. Las frases hablan de elegirte a ti, decir que no con amabilidad y saber que tu valor es el mismo estés donde estés. Escúchalo cuando quieras recordar tus propios estándares.",
    },
    "soft_girl_reset": {
        "subtitle": "Exhala. Suaviza. Vuelve a empezar.",
        "summary": "Una pausa suave para los momentos en que todo se siente demasiado. Las frases siguen tu respiración, hacen espacio para lo que sientes y te devuelven a la calma a tu propio ritmo. Es un ritual tranquilo para reflexionar, no un tratamiento.",
    },
    "pretty_girls_dont_chase": {
        "subtitle": "Sin esfuerzo. Magnética. Suficiente.",
        "summary": "Un CD seguro para el día sobre sentirte a gusto con tu propia belleza. Oirás frases en primera persona sobre dejar que las cosas buenas lleguen a ti, no competir por la atención y saber que tu presencia es suficiente. Ponlo mientras te arreglas.",
    },
    "everything_works_out": {
        "subtitle": "Con suerte, en sintonía y justo a tiempo.",
        "summary": "Un CD ligero de lucky girl para el día. Las frases hablan de que las cosas encajan, de afrontar las sorpresas con calma y de notar lo bueno que ya te rodea. Un reinicio de mentalidad divertido para cualquier día que lo necesite.",
    },
    "million_dollar_energy": {
        "subtitle": "Dinero inteligente. Vida suave. Grandes planes.",
        "summary": "Un CD pulido para el día sobre el dinero y la libertad. Oirás frases en primera persona sobre decisiones inteligentes, hacer crecer tu patrimonio y sentirte tranquila y capaz con el dinero. Una reflexión sobre tu relación con el dinero, no asesoramiento financiero.",
    },
    "princess_treatment": {
        "subtitle": "Querida, adorada, cuidada.",
        "summary": "Un CD suave para la noche sobre que te traten con cariño. Las frases hablan de respeto, afecto y atención con detalle, de tu pareja, de las personas que te rodean y de ti misma. Escrito para todo tipo de amor.",
    },
    "first_class_only": {
        "subtitle": "Ventanilla. Champán. El mundo está abierto.",
        "summary": "Un CD jet set para el día sobre viajar y la libertad. Oirás frases en primera persona sobre moverte por el mundo con comodidad, descubrir lugares preciosos y sentirte en casa allí donde aterrices. Ponlo de camino, o mientras planeas tu próximo viaje.",
    },
    "dream_body_dream_energy": {
        "subtitle": "Fuerte, con energía, amable con mi cuerpo.",
        "summary": "Un CD animado para el día sobre sentirte bien en tu cuerpo. Las frases hablan de fuerza, energía, moverte de una forma que disfrutes y ser amable contigo misma, nunca de perseguir un aspecto concreto. Ponlo antes de entrenar, de un paseo o de unos estiramientos lentos.",
    },
    "perfect_inner_circle": {
        "subtitle": "Mi gente. Mi mesa. Mis personas favoritas.",
        "summary": "Un CD cálido y chispeante para el día sobre la amistad. Oirás frases en primera persona sobre amistades auténticas, que te celebren y hacer sitio a las personas que se sienten como en casa. Ponlo antes de salir de noche, o un día tranquilo en que extrañes a tu gente.",
    },
    "beauty_sleep_for_divas": {
        "subtitle": "Sábanas de seda. Respiración lenta. Descanso profundo.",
        "summary": "Un CD muy tranquilo para la hora de dormir, narrado despacio y con pausas largas. Las frases hablan de dejar que tu cuerpo se relaje, que tu mente se calme y de despertar descansada. Un ritual relajante para desconectar, no un tratamiento para el sueño.",
    },
}

RITUAL_THEMES = {
    "morning": [
        "Un nuevo comienzo",
        "Confianza",
        "Enfoque en calma",
        "Abundancia",
        "Alegría y brillo",
        "Amor propio",
        "Gratitud",
    ],
    "night": [
        "Soltar",
        "A salvo para descansar",
        "Orgullosa de hoy",
        "Soñar en grande",
        "Sentirme querida",
        "Paz",
        "Lista para la semana",
    ],
}

CARD_LINES = {
    "that_girl_energy:3": "Mi energía es única.",
    "that_girl_energy:4": "No compito. Yo marco el ambiente.",
    "that_girl_energy:6": "Mi presencia ya es una entrada triunfal.",
    "that_girl_energy:7": "Ocupo mi espacio con naturalidad.",
    "that_girl_energy:10": "Nunca fui del montón. De eso se trata.",
    "pretty_girls_dont_chase:5": "No persigo. Atraigo.",
    "born_to_be_iconic:1": "Soy bella sin esfuerzo, tal como soy.",
    "born_to_be_iconic:2": "Mi rostro cuenta mi historia, y me encanta esa historia.",
    "born_to_be_iconic:5": "Mi brillo nace por dentro.",
    "born_to_be_iconic:6": "El descanso me sienta bien. La alegría, todavía mejor.",
    "dream_body_dream_energy:0": "Me siento fuerte, sana y llena de energía.",
    "dream_body_dream_energy:6": "Bebo mi agua, y brillo.",
    "rich_girl_frequency:1": "Pienso en el dinero con calma.",
    "rich_girl_frequency:3": "Tengo opciones. Tengo buen gusto. Tengo tiempo.",
    "rich_girl_frequency:6": "La abundancia me resulta natural.",
    "rich_girl_frequency:8": "Disfruto de las cosas bonitas sin culpa.",
    "million_dollar_energy:1": "Mi riqueza crece de forma constante.",
    "million_dollar_energy:6": "Gasto con alegría y ahorro con orgullo.",
    "love_looks_good_on_me:0": "Soy magnética por naturaleza.",
    "love_looks_good_on_me:4": "Soy alguien a quien es una suerte amar.",
    "love_looks_good_on_me:6": "Yo soy el premio, y lo sé.",
    "princess_treatment:1": "Me siento valorada y querida cada día.",
    "princess_treatment:4": "Me adoran en los pequeños detalles.",
    "princess_treatment:6": "Me miman con amor, y lo disfruto.",
    "the_life_i_ordered:2": "Vivo una vida que me parece preciosa.",
    "the_life_i_ordered:4": "Mis mañanas son suaves y sin prisas.",
    "everything_works_out:0": "Todo me está saliendo bien.",
    "everything_works_out:4": "Siempre estoy en el lugar correcto en el momento justo.",
    "first_class_only:1": "El mundo está abierto para mí.",
    "first_class_only:6": "Siempre encuentro el asiento de ventanilla con la mejor vista.",
    "im_the_prize:1": "Soy más que suficiente, incluso en los días tranquilos.",
    "im_the_prize:2": "Mi valor no está en discusión.",
    "im_the_prize:4": "Mis límites son elegantes y firmes.",
    "im_the_prize:5": "Digo que no, y sigo siendo amable.",
    "im_the_prize:6": "Me quedo donde me valoran.",
}

DEMO_TRANSLATION = {
    "that_girl_energy": [
        "Hola, diva. Hombros atrás, barbilla relajada. Este momento es todo tuyo.",
        "Mi energía es única.",
        "No compito. Yo marco el ambiente.",
        "Mi presencia ya es una entrada triunfal.",
        "Nunca fui del montón. De eso se trata.",
    ],
    "rich_girl_frequency": [
        "Hola, diva. Ponte cómoda. Vamos a sintonizar con la abundancia.",
        "Tengo opciones. Tengo buen gusto. Tengo tiempo.",
        "La abundancia me resulta natural.",
        "Disfruto de las cosas bonitas sin culpa.",
        "Construyo riqueza con confianza y con cuidado.",
    ],
    "beauty_sleep_for_divas": [
        "Buenas noches, diva. Luces bajas. Es hora de tu sueño de belleza.",
        "Mis sábanas son suaves, y me hundo en ellas.",
        "Mi rostro se relaja.",
        "Descansar es parte de mi rutina de belleza.",
        "Me despierto descansada y radiante.",
    ],
}

FAQ = [
    {"group": "Sobre DIVA", "items": [
        {"q": "¿Qué es DIVA?", "a": "<p>DIVA es una app de afirmaciones y manifestación para iPhone creada por la desarrolladora independiente Gül Eda Aydemir. Cada tema es un CD de afirmaciones, como <em>That Girl Energy</em>, <em>Rich Girl Frequency</em> o <em>Beauty Sleep for Divas</em>. Eliges un CD, una voz y un paisaje sonoro, y escuchas afirmaciones tranquilas en primera persona durante 10, 20 o 60 minutos. También tiene meditaciones de afirmaciones para la mañana y la noche, la función Make Your Own CD (crea tu propio CD) y una Wishlist con vision board. La app está en inglés y turco.</p>"},
        {"q": "¿DIVA es gratis?", "a": "<p>Sí. DIVA se descarga gratis y la versión gratuita incluye 12 CDs con sesiones de 10 minutos, los rituales de mañana y noche (5 y 10 minutos), dos voces, dos paisajes sonoros, hasta 3 CDs propios y hasta 5 sueños activos en tu Wishlist. DIVA PRO es opcional y desbloquea todo lo demás. Sin anuncios, nunca, en ninguna de las dos versiones.</p>"},
        {"q": "¿Quién creó DIVA?", "a": "<p>¡Yo! Soy Gül Eda Aydemir, desarrolladora independiente de iOS. Diseño, escribo y programo DIVA yo misma. Sin gran empresa, sin inversores: solo una chica con una funda de leopardo para el portátil y opiniones muy claras sobre cómo deberían sonar las afirmaciones.</p>"},
        {"q": "¿En qué dispositivos funciona DIVA?", "a": "<p>DIVA es una app para iPhone y necesita iOS 17 o posterior. Por ahora no hay versión para Android ni para web.</p>"},
        {"q": "¿En qué idiomas está DIVA? ¿Está en español?", "a": "<p>Los menús y textos de la app están en inglés y en turco, y los CDs se narran en inglés; todavía no hay versión en español. DIVA sigue el idioma de tu iPhone cuando es inglés o turco (si tu iPhone está en español, normalmente la verás en inglés), y puedes cambiarlo en Settings (Ajustes) dentro de la app. Esta web sí está en español, y en la demo tienes la traducción de cada frase.</p>"},
        {"q": "¿Necesito una cuenta?", "a": "<p>Para nada. Sin registro, sin email, sin contraseña. Abre la app y dale play.</p>"},
    ]},
    {"group": "Escuchar", "items": [
        {"q": "¿Cuánto duran las sesiones de DIVA?", "a": "<p>Los CDs se escuchan en sesiones de 10, 20 o 60 minutos. Los CDs gratis te dan 10 minutos; 20 y 60 minutos vienen con DIVA PRO. Los rituales de mañana y noche duran 5, 10 o 20 minutos (5 y 10 son gratis). Los CDs PRO tienen un breve adelanto para que los escuches antes.</p>"},
        {"q": "¿Puedo escuchar con la pantalla bloqueada o mientras me duermo?", "a": "<p>Sí. DIVA sigue sonando en segundo plano y tienes controles en la pantalla de bloqueo. Hay temporizador de apagado, y el ritual de la noche se abre en un reproductor nocturno de luz tenue. Mantén un volumen cómodo, sobre todo con auriculares por la noche.</p>"},
        {"q": "¿DIVA funciona sin conexión?", "a": "<p>Sí. Todos los CDs y las voces vienen dentro de la app, así que puedes escuchar en un avión, en el metro o en una cabaña sin cobertura.</p>"},
        {"q": "¿Las voces son personas reales?", "a": "<p>No. La narración de DIVA es voz generada por IA. Las voces (Velvet Whisper, Pink Muse, Runway y After Dark) no son grabaciones de personas reales ni imitan a nadie, y hablan inglés. Las afirmaciones que escribes con tus propias palabras se convierten en voz en tu iPhone.</p>"},
        {"q": "¿Puedo crear mi propio CD de afirmaciones?", "a": "<p>¡Sí! En la pestaña <strong>Create</strong> (crear) eliges las afirmaciones que suenan a ti y las guardas en My CDs (Mis CDs). En la versión gratis puedes tener hasta 3 CDs propios. Escribir afirmaciones con tus propias palabras es una función de DIVA PRO.</p>"},
        {"q": "¿Qué son los paisajes sonoros y sirven de algo los tonos de 528 Hz?", "a": "<p>Los paisajes sonoros son la base musical bajo la voz: Pink Aura, Ocean at 2AM, Hotel Rain, Dreamy Static, Silk Noise, Celestial Drift y tonos suaves de 111, 432, 528, 639, 777, 888 y 963 Hz. Respuesta honesta sobre los tonos: sus nombres describen un estado de ánimo, no un efecto. Están ahí porque suenan de ensueño, no porque curen nada.</p>"},
        {"q": "¿Qué son los rituales de mañana y noche?", "a": "<p>Dos meditaciones guiadas de afirmaciones en lo alto de My CDs (Mis CDs): Morning Affirmations y Bedtime Affirmations. Respiras, te acomodas y escuchas las afirmaciones del día con espacio para repetirlas mentalmente. Cada día de la semana tiene su tema, como Confianza el martes o Gratitud el domingo. Los recordatorios opcionales te llevan directo al ritual.</p>"},
    ]},
    {"group": "Wishlist y vision board", "items": [
        {"q": "¿Qué es la Wishlist de DIVA?", "a": "<p>Es tu lista de manifestación. Apunta los sueños que estás llamando (viajes, hogar, carrera, amor, dinero), sigue tu progreso, celebra los hitos y márcalos como logrados. Puedes añadir tus propias fotos para crear un vision board (tablero de visión), vincular cada sueño a un CD que le vaya y activar un recordatorio diario de tu visión. En la versión gratis puedes tener hasta 5 sueños en camino a la vez; con PRO, ilimitados.</p>"},
        {"q": "¿Mi vision board es privado?", "a": "<p>Totalmente. Tus sueños, notas y fotos se guardan solo en tu iPhone. DIVA usa la cámara solo cuando decides sacar una foto para tu tablero, y guarda una tarjeta de logro en tus fotos solo cuando tocas guardar.</p>"},
    ]},
    {"group": "DIVA PRO y pagos", "items": [
        {"q": "¿Qué incluye DIVA PRO?", "a": "<p>Todos los CDs de la colección, sesiones completas de 20 y 60 minutos, las cuatro voces y todos los paisajes sonoros, escribir afirmaciones con tus propias palabras, los temas Chrome Angel y Leopard Luxe, sueños ilimitados y todos los diseños de vision board.</p>"},
        {"q": "¿Cuánto cuesta DIVA PRO?", "a": "<p>En el lanzamiento en EE. UU.: 5,99 US$ al mes, 29,99 US$ al año o 69,99 US$ en un solo pago por Lifetime (de por vida). El App Store te muestra el precio exacto en tu país y tu moneda antes de confirmar.</p>"},
        {"q": "¿Cómo cancelo mi suscripción?", "a": "<p>En tu iPhone abre <strong>Ajustes → [tu nombre] → Suscripciones → DIVA PRO → Cancelar suscripción</strong>. Mantienes PRO hasta el final del periodo que pagaste. Cancela al menos 24 horas antes de la renovación para evitar el siguiente cobro.</p>"},
        {"q": "¿Cómo restauro mi compra en un iPhone nuevo?", "a": "<p>Inicia sesión con la misma cuenta de Apple, abre DIVA y ve a <strong>Settings → See DIVA PRO → Restore Purchases</strong> (Ajustes → Ver DIVA PRO → Restaurar compras). Lifetime y las suscripciones activas vuelven al momento.</p>"},
        {"q": "¿Puedo pedir un reembolso?", "a": "<p>Los pagos pasan por Apple, así que los reembolsos también. Solicítalo en <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>. Yo no puedo ver ni reembolsar pagos del App Store, pero escríbeme si algo salió mal y te ayudo en todo lo que pueda.</p>"},
    ]},
    {"group": "Privacidad y honestidad", "items": [
        {"q": "¿DIVA recopila mis datos?", "a": "<p>No. DIVA no tiene cuenta, ni anuncios, ni SDK de analítica, ni servidor. Tus favoritos, tu historial, tus CDs, tus sueños y tus fotos se quedan en tu iPhone. Las compras las gestiona Apple. Lee la <a href=\"{{privacy}}\">política de privacidad</a> completa.</p>"},
        {"q": "¿Las afirmaciones funcionan de verdad?", "a": "<p>Hablando claro: las afirmaciones son una herramienta para tu enfoque y tu estado de ánimo, no un hechizo. Mucha gente nota que repetir frases amables, concretas y en presente le ayuda a empezar el día con más calma o a fijarse en sus propios logros. La investigación sobre la autoafirmación es prometedora en algunos aspectos y dispar en otros. DIVA no promete resultados; te da un ritual que sienta lo bastante bien como para mantenerlo de verdad.</p>"},
        {"q": "¿DIVA es terapia o consejo médico?", "a": "<p>No. DIVA es para la reflexión personal y la relajación. No es consejo médico, psicológico ni financiero, y el ritual de la noche es para desconectar, no un tratamiento para el sueño. Si estás pasando por algo difícil, por favor, habla con un profesional. Te mereces apoyo de verdad, amiga.</p>"},
    ]},
]

GUIDES = [
    {
        "id": "manifest",
        "slug": "como-manifestar-con-afirmaciones",
        "title": "Cómo manifestar con afirmaciones (el método supermodelo)",
        "description": "Cómo manifestar con afirmaciones en 4 pasos: elige una era, escríbela en presente, escúchala cada día y da un pequeño paso real. Una guía honesta y con chispa.",
        "kicker": "Manifestación 101",
        "image": "pink-closet",
        "image_alt": "Un vestidor rosa brillante con vestidos de lentejuelas, tacones de cristal y una lámpara de araña",
        "date": "2026-11-14",
        "quick": "Para manifestar con afirmaciones, elige un área concreta de tu vida (tu “era”), escribe de 5 a 10 frases cortas en presente que te resulten creíbles, escúchalas o dilas cada día en el mismo momento y acompáñalas de una pequeña acción real. Las afirmaciones trabajan tu enfoque y tu estado de ánimo; lo que mueve las cosas es la acción.",
        "body": """
<p>Amiga. Siéntate. Tenemos que hablar de manifestar, porque internet lo ha convertido en un hechizo o en una estafa, y no es ninguna de las dos cosas. Es un <em>hábito</em>. Un hábito muy glamuroso, si lo haces a mi manera.</p>
<h2 id="what">¿Qué significa de verdad manifestar con afirmaciones?</h2>
<p>Manifestar es decidir lo que quieres, decirlo como si ya fuera verdad y luego comportarte como la chica que ya lo tiene. Las afirmaciones son la parte de decirlo: frases cortas, en primera persona y en presente que repites hasta que dejan de sentirse como un disfraz y empiezan a sentirse como tu propia piel.</p>
<p>La versión honesta: las afirmaciones no meten dinero en tu cuenta. Mueven tu <em>atención</em>. Y la atención decide en qué te fijas, a qué le dices que sí y cómo entras en una sala.</p>
<h2 id="steps">El método supermodelo, en 4 pasos</h2>
<ol>
<li><strong>Elige una era.</strong> No doce. Una. Confianza, dinero, amor, la casa de tus sueños, tu carrera. La chica que lo quiere todo a la vez solo manifiesta un dolor de cabeza.</li>
<li><strong>Escríbela en presente.</strong> “Voy a tener confianza” es una sala de espera. “Entro en una sala y me siento en casa dentro de mí” es la sala.</li>
<li><strong>Que sea más o menos creíble.</strong> Si “soy multimillonaria” hace que tu cerebro se ría, prueba con “pienso en el dinero con calma”. Estira, no rompas.</li>
<li><strong>Repítela cada día en el mismo momento.</strong> El café, el trayecto, el skincare, la hora de dormir. Engánchala a algo que ya haces y se queda.</li>
</ol>
[[img:vanity-roses|Un tocador rosa con rosas, frascos de perfume, labial y un rubor compacto con forma de estrella]]
<h2 id="listen">Por qué escuchar gana a leer un pósit</h2>
<p>Leer afirmaciones está bien. <em>Escucharlas</em> es otra película. Una voz cálida en tus auriculares, un paisaje sonoro suave de fondo, diez minutos en los que nadie te pide nada. Por eso creé <a href="{{home}}">DIVA</a> en forma de CDs: le das play y el ritual se hace solo.</p>
<p>En DIVA, cada era es un CD con una intro, una veintena de afirmaciones y un cierre. Tú eliges la voz (Velvet Whisper es mi chica para dormir, Pink Muse es mi chica para arreglarme) y la duración: 10, 20 o 60 minutos. Un detalle importante: las voces hablan inglés (o turco), no español.</p>
<h2 id="action">La parte que nadie sube a TikTok: una acción pequeñita</h2>
<p>Después de tu sesión, haz una cosa pequeña que haría la chica de tus sueños. ¿Era del dinero? Mira un número en la app de tu banco con curiosidad, no con miedo. ¿Era de la confianza? Manda ese email. ¿Era de la casa soñada? Guarda una foto en tu vision board. Pequeño. Diario. Icónico.</p>
<h2 id="mistakes">Errores típicos al manifestar</h2>
<ul>
<li><strong>Afirmaciones que odias en secreto.</strong> Si una frase te da cringe, reescríbela. Tus palabras, tu era.</li>
<li><strong>Buscar resultados cada hora.</strong> Estás sembrando, no calentando algo en el microondas.</li>
<li><strong>Usarlas para saltarte lo que sientes.</strong> Las afirmaciones acompañan a las emociones reales; no las sustituyen. Si lo estás pasando mal, habla con alguien de confianza o con un profesional.</li>
</ul>
[[cta]]
""",
        "faq": [
            ["¿Cuánto se tarda en manifestar con afirmaciones?", "No hay un plazo fijo, y quien te dé uno te está vendiendo algo. Mucha gente nota un cambio en su estado de ánimo y su enfoque tras un par de semanas de práctica diaria. Los cambios en la vida real vienen de lo que haces con ese enfoque."],
            ["¿Las afirmaciones deben estar en presente?", "Sí. Las frases en presente y en primera persona (“soy”, “tengo”, “elijo”) se sienten como una descripción de quien eres ahora, y es más fácil meterte en ellas que en una promesa para algún día."],
            ["¿Es mejor decir las afirmaciones o escucharlas?", "Las dos cosas funcionan. Escucharlas es más fácil de mantener porque no requiere esfuerzo: te pones los auriculares y le das play. Mucha gente escucha y repite las frases mentalmente."],
        ],
        "cds": ["the_life_i_ordered", "that_girl_energy", "everything_works_out"],
    },
    {
        "id": "sleep",
        "slug": "afirmaciones-para-dormir",
        "title": "Afirmaciones para dormir: cómo escucharlas por la noche",
        "description": "¿Puedes escuchar afirmaciones mientras duermes? Sí, y te cuento cómo: el mejor momento, el volumen, las voces y lo que pueden (y no pueden) hacer por ti.",
        "kicker": "Sueño de belleza",
        "image": "skincare-satin",
        "image_alt": "Frascos rosas de skincare, una vela encendida y un gua sha de cuarzo rosa sobre satén rosa",
        "date": "2026-11-14",
        "quick": "Sí, puedes escuchar afirmaciones mientras te quedas dormida. Usa una voz tranquila y lenta, mantén el volumen bajo, pon un temporizador para que el audio se apague cuando te duermas y elige frases suaves sobre el descanso y la seguridad. Las afirmaciones para dormir son un ritual relajante para desconectar, no un tratamiento para el sueño.",
        "body": """
<p>Luces bajas. Funda de almohada de seda. El antifaz en la frente porque todavía no estás lista. Esta es la parte más infravalorada de la rutina de una diva: lo que escuchas en los últimos diez minutos del día.</p>
<h2 id="work">¿Funcionan las afirmaciones para dormir?</h2>
<p>Déjame ser tu amiga honesta. No hay buena evidencia de que puedas “reprogramar” tu cerebro mientras duermes profundamente. Lo que sí <em>pueden</em> hacer las afirmaciones para dormir es ayudarte a desconectar: una voz lenta, pausas largas y palabras amables le dan a una mente acelerada algo más suave a lo que agarrarse que la lista de tareas de mañana. Esa es la magia. Es más silenciosa de lo que prometía internet y, sinceramente, mejor.</p>
<h2 id="how">Cómo escuchar afirmaciones por la noche</h2>
<ol>
<li><strong>Elige una voz lenta y grave.</strong> En DIVA son Velvet Whisper (gratis) o After Dark (PRO).</li>
<li><strong>Baja el volumen.</strong> Más de lo que crees. Tus oídos también merecen su sueño de belleza.</li>
<li><strong>Pon un temporizador.</strong> Así el audio se apaga cuando ya te has ido, en vez de sonarles a tus sueños toda la noche.</li>
<li><strong>Usa un paisaje sonoro suave.</strong> Ocean at 2AM es gratis y suena a hotel junto al mar.</li>
<li><strong>A la misma hora cada noche.</strong> Los rituales aman la rutina.</li>
</ol>
[[img:lily-vanity|Un tocador de terciopelo rosa con lirios, perfume, un cepillo con joyas y un coletero de leopardo]]
<h2 id="lines">Afirmaciones para dormir que puedes probar esta noche</h2>
<ul>
<li>“El día ya terminó, y lo dejo ir.”</li>
<li>“Estoy a salvo y puedo descansar.”</li>
<li>“Mis sábanas son suaves, y me hundo en ellas.”</li>
<li>“Descansar es parte de mi rutina de belleza.”</li>
<li>“Me despierto descansada y radiante.”</li>
</ul>
<p>Todas salen de CDs reales de DIVA: <em>Whisper to Your Future Self</em> y <em>Beauty Sleep for Divas</em>, los dos gratis. En la app las escuchas en inglés; aquí te las dejo traducidas.</p>
<h2 id="ritual">El ritual de la noche de DIVA</h2>
<p>Si quieres que te lo den hecho, DIVA tiene una meditación de afirmaciones para dormir, <strong>Bedtime Affirmations</strong>, en lo alto de My CDs (Mis CDs). Se abre en un reproductor nocturno de luz tenue, te guía con unas cuantas respiraciones lentas y reproduce las afirmaciones de la noche con pausas largas y suaves. Cada noche de la semana tiene un tema (Soltar el lunes, Paz el sábado) y un recordatorio opcional a la hora de dormir te lo abre al instante.</p>
<h2 id="safety">Una pequeña nota de seguridad</h2>
<p>Mantén un volumen cómodo, no duermas con auriculares grandes si te molestan y, si tienes problemas de sueño que no se van, habla con un médico. Las afirmaciones son la vela, no la receta.</p>
[[cta]]
""",
        "faq": [
            ["¿Está bien dormirse escuchando afirmaciones?", "Sí, siempre que el volumen sea bajo y cómodo. Usa un temporizador para que la reproducción se detenga cuando te duermas."],
            ["¿Las afirmaciones pueden reprogramar tu subconsciente mientras duermes?", "No hay evidencia sólida de que se pueda aprender o reprogramar nada durante el sueño profundo. Las afirmaciones para dormir funcionan mejor como un ritual relajante mientras todavía estás despierta y te vas quedando dormida."],
            ["¿Cuál es la mejor voz para afirmaciones para dormir?", "Una voz lenta, grave y cálida, con pausas largas. En DIVA son Velvet Whisper (gratis) o After Dark (PRO), que hablan inglés."],
        ],
        "cds": ["beauty_sleep_for_divas", "whisper_to_your_future_self", "the_life_i_ordered"],
    },
    {
        "id": "morning",
        "slug": "rutina-de-afirmaciones-de-la-manana",
        "title": "Afirmaciones de la mañana: rutina That Girl de 10 minutos",
        "description": "Rutina realista de afirmaciones de la mañana en 10 minutos: qué hacer antes de mirar el teléfono, qué afirmaciones decir y un tema para cada día de la semana.",
        "kicker": "Rituales de mañana",
        "image": "vanity-tray",
        "image_alt": "Una bandeja de tocador con espejo, brochas de maquillaje rosas, crema, labial y una copa de martini con cereza",
        "date": "2026-11-14",
        "quick": "Una buena rutina de afirmaciones de la mañana dura de 5 a 10 minutos: antes de mirar el teléfono, respira despacio tres veces, fija una intención para el día y escucha o di de 5 a 8 afirmaciones en presente. Rotar un tema para cada día de la semana (confianza, enfoque en calma, abundancia, amor propio) la mantiene fresca.",
        "body": """
<p>Levanta la mano si lo primero que ves cada mañana son 47 notificaciones y el anillo de compromiso de alguien. Yo también. Por eso ahora los primeros diez minutos son sagrados. Esta es la rutina que hago de verdad (en bata, obviamente).</p>
<h2 id="routine">La rutina de 10 minutos</h2>
<ol>
<li><strong>Minuto 0: no toques el teléfono.</strong> Bueno, tócalo una vez, para darle play.</li>
<li><strong>Minutos 1–2: tres respiraciones lentas.</strong> Inhala por la nariz, exhala largo. Baja esos hombros de las orejas, diva.</li>
<li><strong>Minuto 3: una intención.</strong> Una frase para hoy. “Hoy voy despacio y llego a tiempo.”</li>
<li><strong>Minutos 4–9: afirmaciones.</strong> Escucha y repite cada frase mentalmente. Siéntela como un perfume que te estás probando.</li>
<li><strong>Minuto 10: una acción pequeñita.</strong> Agua, luz del sol, hacer la cama. Las protagonistas se hidratan.</li>
</ol>
<h2 id="week">Un tema para cada día de la semana</h2>
<p>Repetir las mismas frases todos los días cansa rápido. Esta es la rotación del ritual de la mañana de DIVA (en la app se llama <strong>Morning Affirmations</strong>):</p>
<ul>
<li><strong>Lunes:</strong> Un nuevo comienzo</li>
<li><strong>Martes:</strong> Confianza</li>
<li><strong>Miércoles:</strong> Enfoque en calma</li>
<li><strong>Jueves:</strong> Abundancia</li>
<li><strong>Viernes:</strong> Alegría y brillo</li>
<li><strong>Sábado:</strong> Amor propio</li>
<li><strong>Domingo:</strong> Gratitud</li>
</ul>
[[img:dream-body-neon|Un letrero de neón rosa que dice Dream Body sobre mancuernas rosas, una esterilla de yoga y una botella de agua de cristal]]
<h2 id="lines">Afirmaciones de la mañana que no suenan a póster</h2>
<ul>
<li>“Buenos días a mí misma.”</li>
<li>“Hoy lleva mi nombre.”</li>
<li>“Me desperté siendo yo, y es una noticia excelente.”</li>
<li>“Elijo mi estado de ánimo antes de mirar el teléfono.”</li>
<li>“Mi energía está fresca y es toda mía.”</li>
</ul>
<p>Son de <em>Wake Up, Icon</em>, un CD gratis de DIVA hecho justo para esto. En la app suena en inglés; aquí va traducido.</p>
<h2 id="diva">Cómo hacerlo en DIVA</h2>
<p>Abre My CDs (Mis CDs) y toca <strong>Morning Affirmations</strong> arriba del todo. Elige 5 o 10 minutos (gratis) o 20 (PRO). Activa el recordatorio de la mañana en Settings (los ajustes de la app) y te abrirá el ritual directamente, ya con el tema de hoy. Aprobado por las chicas perezosas.</p>
[[cta]]
""",
        "faq": [
            ["¿Cuál es el mejor momento para decir afirmaciones por la mañana?", "Justo después de despertarte y antes de mirar el teléfono, cuando tu mente está tranquila y nada te ha marcado todavía el estado de ánimo."],
            ["¿Cuántas afirmaciones debo decir por la mañana?", "Entre cinco y ocho es más que suficiente. Pocas frases que sientes de verdad valen más que cincuenta dichas a toda prisa."],
            ["¿Puedo hacer una rutina de afirmaciones de la mañana en 5 minutos?", "Sí. Tres respiraciones, una intención y una sesión corta de afirmaciones. El ritual de la mañana de DIVA tiene una versión gratis de 5 minutos."],
        ],
        "cds": ["wake_up_icon", "that_girl_energy", "born_to_be_iconic"],
    },
    {
        "id": "money",
        "slug": "afirmaciones-de-dinero",
        "title": "Afirmaciones de dinero y abundancia que no dan cringe",
        "description": "Afirmaciones de dinero y abundancia que sí te crees, cómo usarlas para vivir el dinero con más calma y por qué ser rich girl va de opciones, gusto y tiempo.",
        "kicker": "Mentalidad de dinero",
        "image": "money-bag",
        "image_alt": "Un bolso de cocodrilo rosa fucsia brillante lleno de billetes de dólar, rodeado de diamantes y un martini",
        "date": "2026-11-14",
        "quick": "Las afirmaciones de dinero funcionan mejor cuando apuntan a cómo te sientes con el dinero, no a una cifra mágica: frases como “Pienso en el dinero con calma” y “Tengo opciones. Tengo buen gusto. Tengo tiempo”. Úsalas a diario junto a una pequeña acción con tu dinero. Apoyan una mentalidad más tranquila con el dinero; no son asesoramiento financiero.",
        "body": """
<p>Hablemos de dinero, reina. No en plan gurú de las finanzas. En plan “quiero abrir la app del banco sin tener que acostarme un rato después”.</p>
<h2 id="what">¿Qué es una afirmación de “rich girl”?</h2>
<p>La energía rich girl no consiste en fingir que eres multimillonaria. Son opciones, buen gusto y tiempo. Es calma. Las rich girls no actualizan su saldo con pánico; miran los números como quien mira un menú. Por eso las mejores afirmaciones de dinero hablan de la <em>sensación</em>, no de la cifra.</p>
<h2 id="lines">Afirmaciones de dinero para robar</h2>
<ul>
<li>“Pienso en el dinero con calma.”</li>
<li>“Tengo opciones. Tengo buen gusto. Tengo tiempo.”</li>
<li>“El dinero sostiene la vida que elijo crear.”</li>
<li>“Disfruto de las cosas bonitas sin culpa.”</li>
<li>“Miro mis números con curiosidad, no con miedo.”</li>
<li>“Tomo decisiones financieras inteligentes.”</li>
<li>“Gasto con alegría y ahorro con orgullo.”</li>
</ul>
<p>Las cinco primeras son de <em>Rich Girl Frequency</em> (gratis en DIVA); las dos últimas, de <em>Million Dollar Energy</em> (PRO). En la app suenan en inglés; aquí van traducidas.</p>
[[img:ceo-desk|Un bolso de cocodrilo rosa, un fajo de billetes, una tarjeta dorada, un reloj de diamantes y un portátil rosa sobre satén]]
<h2 id="believe">Por qué lo creíble gana a lo enorme</h2>
<p>Si dices “tengo un millón de dólares” y tu cerebro te contesta <em>amiga, tienes 43 en la cuenta</em>, la afirmación pierde. Empieza donde tu sistema nervioso pueda seguirte: calma, curiosidad, opciones. Después estira. “Construyo riqueza con confianza y con cuidado” es una frase en la que puedes ir creciendo.</p>
<h2 id="action">Combínala con un movimiento de dinero</h2>
<p>Después de tu sesión, haz una cosa pequeñita: revisa una cuenta, cancela una suscripción que habías olvidado, pasa un poco a tus ahorros, apunta el precio que cobrarías por lo que sabes hacer. La afirmación pone el ambiente; el movimiento hace la película.</p>
<h2 id="honest">La parte honesta</h2>
<p>DIVA es un ritual de mentalidad, no asesoramiento financiero, y ningún CD va a elegirte acciones en bolsa. Si necesitas ayuda real con tu dinero, habla con un asesor cualificado. Y después ve a escuchar tu CD como la CEO que eres.</p>
[[cta]]
""",
        "faq": [
            ["¿Funcionan las afirmaciones de dinero?", "Pueden ayudarte a sentirte más tranquila e intencional con el dinero, y eso facilita dar pasos prácticos. No crean dinero por sí solas y no son asesoramiento financiero."],
            ["¿Cuál es la mejor afirmación de dinero?", "Una que puedas creerte hoy. “Pienso en el dinero con calma” es un gran punto de partida, porque cambia cómo te acercas a tus finanzas."],
            ["¿Qué significa “rich girl frequency”?", "Es una forma divertida de describir sentirte a gusto con el dinero: tener opciones, buen gusto y tiempo, y disfrutar de las cosas bonitas sin culpa. También es el nombre de un CD gratis de DIVA."],
        ],
        "cds": ["rich_girl_frequency", "million_dollar_energy", "ceo_after_hours"],
    },
    {
        "id": "lucky",
        "slug": "lucky-girl-syndrome-afirmaciones",
        "title": "Lucky girl syndrome: qué es y afirmaciones para probar",
        "description": "El lucky girl syndrome explicado: la idea, por qué sienta tan bien, dónde falla y afirmaciones de chica con suerte como “todo me está saliendo bien”.",
        "kicker": "Era lucky girl",
        "image": "jet-set",
        "image_alt": "Una maleta rosa fucsia, gafas de sol de pedrería y un pasaporte al atardecer con un jet privado detrás",
        "date": "2026-11-14",
        "quick": "El lucky girl syndrome es la tendencia de repetir que tienes suerte y que todo te sale bien, para empezar a esperar y a notar las cosas buenas. Prueba afirmaciones como “Todo me está saliendo bien” y “Siempre estoy en el lugar correcto en el momento justo”, y sigue arriesgándote en la vida real: la suerte adora a la chica que se presenta.",
        "body": """
<p>“Tengo muchísima suerte, todo me sale siempre bien.” Si lo acabas de decir en voz alta, felicidades: estás oficialmente en tu era lucky girl. Vamos a hacerlo chic y no delulu.</p>
<h2 id="what">¿Qué es el lucky girl syndrome?</h2>
<p>Es una tendencia de manifestación en la que decides que eres una persona con suerte y lo repites hasta que te lo crees. Entonces empiezas a fijarte en la mesa libre junto a la ventana, en la respuesta, en el upgrade. Parte de su encanto es psicología: cuando esperas cosas buenas, te fijas más en ellas y es más probable que digas que sí cuando aparecen.</p>
<h2 id="lines">Afirmaciones de lucky girl</h2>
<ul>
<li>“Todo me está saliendo bien.”</li>
<li>“Todo está encajando en su sitio.”</li>
<li>“Siempre estoy en el lugar correcto en el momento justo.”</li>
<li>“Las buenas noticias me encuentran con facilidad.”</li>
<li>“Veo oportunidades preciosas por todas partes.”</li>
<li>“Afronto cada reto con confianza.”</li>
</ul>
<p>Son de <em>Everything Works Out For Me</em>, un CD gratis de DIVA (en la app, en inglés). Póntelo antes de una entrevista, de una primera cita o de un lunes.</p>
[[img:rooftop-party|Una fiesta en una azotea de noche con una bola de discoteca rosa, copas de champán y un clutch de pedrería]]
<h2 id="wrong">Dónde falla el lucky girl syndrome</h2>
<ul>
<li><strong>Esperar que la suerte haga tus deberes.</strong> Las lucky girls también envían el currículum, escriben, piden y dan la cara. Solo que lo hacen como si esperaran un sí.</li>
<li><strong>Culparte por los días malos.</strong> Las lucky girls también tienen días malos. Son el clima, no un veredicto.</li>
<li><strong>Ignorar problemas reales.</strong> Las afirmaciones van al lado de la vida real, no en su lugar.</li>
</ul>
<h2 id="practice">Reto lucky girl de 3 días</h2>
<ol>
<li>Cada mañana, escucha <em>Everything Works Out For Me</em> durante 10 minutos.</li>
<li>Antes de dormir, apunta tres cosas en las que tuviste suerte. Lo pequeñito cuenta. Sobre todo lo pequeñito.</li>
<li>Di que sí a una pequeña oportunidad cada día.</li>
</ol>
<p>Al tercer día serás la chica que dice “obvio que salió bien” con un movimiento de melena.</p>
[[cta]]
""",
        "faq": [
            ["¿El lucky girl syndrome es real?", "No es un síndrome médico; es una tendencia de mentalidad. Lo útil es que esperar cosas buenas puede hacer que sea más probable que notes las oportunidades y que actúes."],
            ["¿Qué se dice en el lucky girl syndrome?", "Frases cortas y seguras como “Todo me está saliendo bien”, “Tengo muchísima suerte” y “Las buenas noticias me encuentran con facilidad”, repetidas cada día."],
            ["¿El lucky girl syndrome es lo mismo que manifestar?", "Es una variante de la manifestación centrada en sentirte con suerte en general, más que en un objetivo concreto."],
        ],
        "cds": ["everything_works_out", "first_class_only", "pretty_girls_dont_chase"],
    },
    {
        "id": "vision",
        "slug": "vision-board-en-iphone",
        "title": "Cómo hacer un vision board (tablero de visión) en iPhone",
        "description": "Haz un vision board digital en iPhone: elige tus sueños, añade fotos, sigue tu progreso y tenlo a la vista cada día. Y cómo funciona la Wishlist de DIVA.",
        "kicker": "Vision boards",
        "image": "walk-in-closet",
        "image_alt": "Un vestidor rosa con vistas a la ciudad al anochecer, rosas, perfume y una manta de leopardo",
        "date": "2026-11-14",
        "quick": "Para hacer un vision board en iPhone, escribe de 3 a 5 sueños concretos, elige para cada uno una foto que te haga sentirlo, reúnelos en un lugar que veas a diario y revisa tu progreso cada semana. La Wishlist de DIVA lo hace en una sola app: sueños, fotos, progreso, hitos, vision board y un recordatorio diario, todo guardado de forma privada en tu teléfono.",
        "body": """
<p>El pegamento y los recortes de revista tienen su encanto, pero tu vision board debería vivir donde de verdad miras 96 veces al día: tu teléfono. Así se hace uno que no acaba olvidado detrás del armario.</p>
<h2 id="steps">Cómo hacer un vision board en iPhone, paso a paso</h2>
<ol>
<li><strong>Escribe de 3 a 5 sueños.</strong> Lo concreto gana a lo vago. No “viajar más”, sino “París, asiento de ventanilla, primavera”.</li>
<li><strong>Elige una foto por sueño.</strong> Una que te dé un pequeño subidón. Tus propias fotos pegan más fuerte que Pinterest.</li>
<li><strong>Dale a cada sueño un siguiente paso.</strong> Un sueño sin paso es un salvapantallas.</li>
<li><strong>Ponlo donde lo veas cada día.</strong> Un recordatorio, un widget, un ritual.</li>
<li><strong>Revísalo cada semana.</strong> Mueve la barra de progreso, celebra los logros, edita los sueños que han cambiado.</li>
</ol>
[[img:penthouse-lounge|Un salón de terciopelo rosa con palmeras al atardecer, una lámpara de araña de cristal y una chimenea]]
<h2 id="diva">Cómo funciona la Wishlist de DIVA</h2>
<p>Creé la Wishlist porque mis sueños estaban repartidos entre Notas, capturas de pantalla y un diario que perdí en 2019. En DIVA:</p>
<ul>
<li>Escribe cada sueño con una categoría (viajes, hogar, carrera, amor, dinero y más) y una nota opcional.</li>
<li>Añade fotos de tu galería o saca una con la cámara para crear tu vision board.</li>
<li>Sigue tu progreso y tus hitos, toca <strong>It's Already Mine ♡</strong> (ya es mío) y llévate una tarjeta para guardar.</li>
<li>Vincula un sueño a un CD, para que tu sueño de la casa ideal suene a <em>Penthouse State of Mind</em>.</li>
<li>Activa el recordatorio diario de tu visión para tener tu sueño siempre a la vista.</li>
</ul>
<p>En la versión gratis puedes tener hasta 5 sueños en camino a la vez (los logrados no cuentan) con el tablero en cuadrícula; PRO desbloquea sueños ilimitados y todos los diseños de tablero. Tus sueños los escribes con tus palabras; los menús de la app están en inglés.</p>
<h2 id="private">Que quede entre tú y tu iPhone</h2>
<p>Tu vision board es personal. DIVA guarda tus sueños, notas y fotos solo en tu iPhone: sin cuenta, sin nube, sin nadie mirando a escondidas. Protagonista, diario bajo llave.</p>
[[cta]]
""",
        "faq": [
            ["¿Cuál es la mejor forma de hacer un vision board en iPhone?", "Usar una app que reúna sueños, fotos y progreso y te lo recuerde cada día. La Wishlist de DIVA combina un vision board con seguimiento del progreso y CDs de afirmaciones a juego."],
            ["¿Cuántos objetivos debe tener un vision board?", "De tres a cinco es lo ideal: suficientes para inspirarte y pocos como para poder centrarte de verdad."],
            ["¿Los vision boards digitales son tan buenos como los de papel?", "Pueden ser mejores, porque los ves más a menudo. Lo que importa es mirarlo cada día y dar pasos pequeños."],
        ],
        "cds": ["penthouse_state_of_mind", "first_class_only", "the_life_i_ordered"],
    },
    {
        "id": "confidence",
        "slug": "afirmaciones-de-confianza",
        "title": "Afirmaciones de confianza para tu energía de protagonista",
        "description": "Afirmaciones de confianza que suenan naturales, cómo usarlas antes de los grandes momentos y cómo crear energía de protagonista sin fingir ser otra persona.",
        "kicker": "Energía de protagonista",
        "image": "poolside-muse",
        "image_alt": "Una mujer glamurosa con gafas de sol de pedrería junto a una piscina rosa al atardecer, con un martini",
        "date": "2026-11-14",
        "quick": "Las afirmaciones de confianza funcionan mejor cuando describen soltura, no perfección: “Ocupo mi espacio con naturalidad”, “Mi energía es única”, “No compito. Yo marco el ambiente”. Escúchalas a diario y justo antes de los grandes momentos, y acompáñalas con tu postura: hombros atrás, respiración lenta, barbilla relajada.",
        "body": """
<p>La energía de protagonista no es ser la chica que más grita en la sala. Es ser la chica que está completamente en casa dentro de sí misma. Imperturbable. Magnética. Ligeramente icónica.</p>
<h2 id="lines">Mis afirmaciones de confianza de cabecera</h2>
<ul>
<li>“Mi energía es única.”</li>
<li>“No compito. Yo marco el ambiente.”</li>
<li>“Mi presencia ya es una entrada triunfal.”</li>
<li>“Ocupo mi espacio con naturalidad.”</li>
<li>“Nunca fui del montón. De eso se trata.”</li>
<li>“Soy magnética porque soy yo misma.”</li>
</ul>
<p>Todas son de <em>That Girl Energy</em>, el primer CD que hice para DIVA. Es gratis. Obvio. En la app suena en inglés; aquí te lo dejo traducido.</p>
<h2 id="when">Cuándo usar afirmaciones de confianza</h2>
<ul>
<li><strong>Mientras te arreglas.</strong> Póntelo mientras te maquillas. Brilla al ritmo del audio.</li>
<li><strong>Antes de algo grande.</strong> Una entrevista, una cita, una presentación, ese gimnasio que te da miedo. Cinco minutos antes de entrar.</li>
<li><strong>Después de un tambaleo.</strong> ¿Alguien te dijo algo raro? Dale play y vuelve a ti.</li>
</ul>
[[img:rhinestone-gym|Auriculares de pedrería, mancuernas rosa fucsia y una botella de agua de cristal sobre estampado de leopardo]]
<h2 id="body">Combínalo con tu cuerpo</h2>
<p>La confianza vive tanto en la postura como en las palabras. Mientras suena cada frase: hombros atrás, barbilla relajada, exhala despacio. Literalmente así empieza <em>That Girl Energy</em>: “Hey, diva. Shoulders back, chin soft. This one is all you.” (Hola, diva. Hombros atrás, barbilla relajada. Este momento es todo tuyo.)</p>
<h2 id="fake">¿“Finge hasta que lo consigas”?</h2>
<p>Yo prefiero decir “pruébatelo hasta que te quede perfecto”. Las afirmaciones de confianza no van de fingir ser otra persona; van de recordar quién eres cuando no estás dudando de ti. Si una frase te queda como un disfraz, cámbiala por una que te quede como tus jeans favoritos.</p>
[[cta]]
""",
        "faq": [
            ["¿Cuáles son buenas afirmaciones de confianza?", "Frases cortas, en presente, sobre la soltura y la confianza en ti misma, como “Ocupo mi espacio con naturalidad”, “Mi energía es única” y “Confío en mis ideas”."],
            ["¿Cómo consigo energía de protagonista?", "Empieza el día con intención, vístete para ti, háblate con cariño y deja de competir. Las afirmaciones de confianza diarias te ayudan a ensayar esa sensación."],
            ["¿Con qué frecuencia debo escuchar afirmaciones de confianza?", "A diario durante unas semanas, y también justo antes de los grandes momentos. La constancia importa más que la duración."],
        ],
        "cds": ["that_girl_energy", "pretty_girls_dont_chase", "im_the_prize"],
    },
    {
        "id": "love",
        "slug": "afirmaciones-de-amor-propio",
        "title": "Afirmaciones de amor propio y de amor: atrae, no persigas",
        "description": "Afirmaciones de amor propio y de amor para tus relaciones: conoce tu valor, pon límites elegantes y atrae el amor sin perseguirlo. Con ejemplos.",
        "kicker": "Era del amor",
        "image": "diamond-bust",
        "image_alt": "Un busto joyero de terciopelo con collares de diamantes superpuestos, un estuche de anillo y tacones de cristal",
        "date": "2026-11-14",
        "quick": "Las afirmaciones de amor propio te recuerdan que tu valor no se discute: “Soy más que suficiente, incluso en los días tranquilos”, “Mis límites son elegantes y firmes”. Las afirmaciones de amor se construyen sobre eso: “No persigo. Atraigo”. Primero tu valor, después el amor. Una chica que conoce su valor atrae a gente que también lo ve.",
        "body": """
<p>Amiga, antes de manifestar al chico, a la chica o la versión mejorada de tu casi algo, vamos a manifestarte a <em>ti</em>. Primero el amor propio. Siempre. Después, el amor te queda precioso.</p>
<h2 id="worth">Afirmaciones de amor propio</h2>
<ul>
<li>“Soy más que suficiente, incluso en los días tranquilos.”</li>
<li>“Mi valor no está en discusión.”</li>
<li>“Mis límites son elegantes y firmes.”</li>
<li>“Digo que no, y sigo siendo amable.”</li>
<li>“Me quedo donde me valoran.”</li>
</ul>
<p>Son de <em>I'm the Prize</em>, mi CD para un respeto propio con mucha clase.</p>
<h2 id="love">Afirmaciones de amor: atrae, no persigas</h2>
<ul>
<li>“Soy magnética por naturaleza.”</li>
<li>“Sé exactamente lo que aporto a una relación.”</li>
<li>“No compito por la atención, y no mendigo cariño.”</li>
<li>“Me tratan con amabilidad y respeto.”</li>
<li>“Recibo el cariño con el corazón abierto.”</li>
</ul>
<p>De <em>Love Looks Good On Me</em> (un CD nocturno susurrado en seis partes, gratis) y <em>Princess Treatment</em> (gratis). En la app suenan en inglés; aquí van traducidas.</p>
[[img:lily-vanity|Un tocador rosa con lirios, frascos de perfume de cristal, labial y un coletero de leopardo]]
<h2 id="how">Cómo usar afirmaciones de amor sin volverte delulu</h2>
<ul>
<li><strong>Afirma cualidades, no a una persona concreta.</strong> “Atraigo un amor amable y constante” gana a “Me contesta antes de las 9”.</li>
<li><strong>Deja que marquen tus estándares.</strong> Escuchar “Me quedo donde me valoran” cada noche hace más fácil irte de verdad de donde no te valoran.</li>
<li><strong>Quiérete en voz alta.</strong> Invítate a una cita. Cómprate las flores. El trato de princesa empieza en casa.</li>
</ul>
<h2 id="honest">Nota honesta</h2>
<p>Las afirmaciones pueden ayudarte a sentirte valiosa, pero no pueden arreglar una relación que te hace daño. Si no te sientes a salvo o te sientes atrapada, acude a una amiga de confianza o a un profesional. Te mereces apoyo de verdad.</p>
[[cta]]
""",
        "faq": [
            ["¿Cuál es una buena afirmación de amor propio?", "“Soy más que suficiente, incluso en los días tranquilos” es preciosa, porque no depende de lograr nada."],
            ["¿Las afirmaciones pueden ayudarte a atraer el amor?", "Pueden ayudarte a sentirte valiosa, a subir tus estándares y a mostrarte más abierta, y eso cambia a quién atraes y a quién mantienes a tu lado. No pueden controlar a otra persona."],
            ["¿Debo decir afirmaciones de amor sobre una persona concreta?", "Es más sano afirmar las cualidades que quieres en el amor, como la amabilidad y la constancia, que centrarte en una persona concreta."],
        ],
        "cds": ["love_looks_good_on_me", "princess_treatment", "im_the_prize"],
    },
    {
        "id": "write",
        "slug": "como-escribir-tus-propias-afirmaciones",
        "title": "Cómo escribir tus propias afirmaciones (que suenen a ti)",
        "description": "Cómo escribir afirmaciones que se sientan verdad: en primera persona, en presente, concretas y creíbles. Fórmula de 5 pasos, ejemplos y cómo hacer tu propio CD.",
        "kicker": "Diva DIY",
        "image": "vanity-roses",
        "image_alt": "Un tocador rosa con rosas, un frasco de perfume de cristal, labial y pinzas de pelo de pedrería",
        "date": "2026-11-14",
        "quick": "Para escribir tus propias afirmaciones, usa la primera persona y el presente (“soy”, “tengo”, “elijo”), haz cada frase corta y concreta, que sea lo bastante creíble como para no rechazarla, exprésala en positivo (lo que quieres, no lo que temes) y léela en voz alta: si suena a ti, quédatela.",
        "body": """
<p>Las afirmaciones de serie están bien. Las hechas a medida son alta costura. Esta es mi fórmula para escribir frases que de verdad se sientan tuyas.</p>
<h2 id="formula">La fórmula de afirmaciones en 5 pasos</h2>
<ol>
<li><strong>Primera persona.</strong> Habla desde el “yo”: “soy”, “tengo”, “mi…”. Eres la protagonista, no la narradora.</li>
<li><strong>Presente.</strong> “Soy”, no “seré”. El futuro deja el sueño en el futuro.</li>
<li><strong>Corta y concreta.</strong> Menos de 12 palabras. “Mis mañanas son suaves y sin prisas” gana a un párrafo.</li>
<li><strong>Más o menos creíble.</strong> Estírala, no la rompas. Si tu cerebro discute, suavízala: “Estoy aprendiendo a…” está permitido.</li>
<li><strong>En positivo.</strong> “Estoy en calma” en vez de “No estoy ansiosa”. El cerebro oye la palabra que repites.</li>
</ol>
<h2 id="examples">Antes y después</h2>
<ul>
<li>“Ya no voy a estar sin dinero” → “Tomo decisiones de dinero con la mente tranquila y clara.”</li>
<li>“Ojalá le caiga bien a la gente” → “Soy alguien a quien es una suerte conocer.”</li>
<li>“Tengo que dejar de ser tan perezosa” → “Muevo mi cuerpo porque me encanta.”</li>
</ul>
[[img:vanity-tray|Una bandeja de tocador con espejo, brochas de maquillaje, crema, polveras con brillo y un martini con cereza]]
<h2 id="voice">Léela en voz alta</h2>
<p>Esta es la prueba. Dila con tu voz normal. Si te daría cringe decírsela a tu mejor amiga, reescríbela. Si se la mandarías por mensaje con tres emojis de brillitos, es para quedártela.</p>
<h2 id="cd">Convierte tus afirmaciones en tu propio CD</h2>
<p>En DIVA, abre la pestaña <strong>Create</strong> (crear) y elige de la colección las afirmaciones que suenan a ti; guárdalo en My CDs (Mis CDs) y dale play cuando quieras (en la versión gratis puedes tener hasta 3). Con DIVA PRO también puedes escribir frases con tus propias palabras, y DIVA les pone voz en tu iPhone, en privado. Tus palabras nunca salen de tu teléfono. Un detalle: las lee una voz en inglés, así que suenan mejor si las escribes en inglés.</p>
[[cta]]
""",
        "faq": [
            ["¿Qué hace que una afirmación sea buena?", "Primera persona, presente, corta, concreta, en positivo y lo bastante creíble como para que no la discutas al instante."],
            ["¿Las afirmaciones deben empezar por “soy”?", "“Soy” es un clásico, pero “tengo”, “elijo”, “mi…” y “estoy aprendiendo a…” también funcionan de maravilla."],
            ["¿Puedo grabar mis propias afirmaciones en DIVA?", "DIVA no graba tu voz. Puedes crear un CD con las afirmaciones de la app y, con DIVA PRO, escribir tus propias frases, que DIVA convierte en voz en tu iPhone (con una voz en inglés)."],
        ],
        "cds": ["born_to_be_iconic", "im_the_prize", "wake_up_icon"],
    },
    {
        "id": "app",
        "slug": "mejor-app-de-afirmaciones-iphone",
        "title": "Cómo elegir la mejor app de afirmaciones para iPhone",
        "description": "¿Qué hace buena a una app de afirmaciones? Voces naturales, uso sin conexión, privacidad, cero anuncios, sesiones para dormir y precios claros. Lista honesta.",
        "kicker": "Hablemos de apps",
        "image": "lily-vanity",
        "image_alt": "Un tocador rosa con lirios, perfume de cristal, un cepillo con joyas y un coletero de leopardo sobre terciopelo",
        "date": "2026-11-14",
        "quick": "Una buena app de afirmaciones tiene voces cálidas y naturales (no robóticas), te deja escuchar sin conexión y en segundo plano, ofrece sesiones para dormir y para la mañana, protege tus datos, no mete anuncios en un momento de calma y es clara con sus precios. DIVA es una app de afirmaciones para iPhone creada en torno a esos puntos, con CDs de afirmaciones, 4 voces de IA, rituales y vision board; eso sí, la app está en inglés y turco, no en español.",
        "body": """
<p>Te lo digo de entrada, amiga: creé una app de afirmaciones, así que tengo opiniones. Pero te paso la lista que usé, y puedes aplicársela a <em>cualquier</em> app, incluida la mía.</p>
<h2 id="checklist">La lista para elegir app de afirmaciones</h2>
<ol>
<li><strong>La voz no suena a robot.</strong> Si la narradora suena como un GPS, no vas a seguir escuchando. Busca voces cálidas y naturales, y que haya más de una para elegir.</li>
<li><strong>Funciona sin conexión y en segundo plano.</strong> Aviones, metro, pantalla apagada por la noche. Innegociable.</li>
<li><strong>Tiene opción para dormir.</strong> Voz lenta, pausas largas, temporizador.</li>
<li><strong>Tiene opción para la mañana.</strong> Sesiones cortas que puedes hacer antes de que el teléfono te coma el cerebro.</li>
<li><strong>Sin anuncios en tu meditación.</strong> Nada mata más el ambiente que un anuncio de un videojuego entre “estoy en calma” y “estoy a salvo”.</li>
<li><strong>Una privacidad que se pueda leer.</strong> Las afirmaciones y los sueños son algo íntimo. Comprueba si necesitas una cuenta y qué sale del teléfono.</li>
<li><strong>Promesas de bienestar honestas.</strong> Huye de las apps que te prometen dinero o amor garantizados, o frecuencias que curan.</li>
<li><strong>Precios claros.</strong> Qué es gratis, qué es de pago y cómo se cancela.</li>
</ol>
[[img:diamond-bust|Un busto joyero de terciopelo con collares de diamantes, un anillo de cóctel y una copa de cristal]]
<h2 id="diva">Cómo sale DIVA en su propia lista</h2>
<ul>
<li><strong>Voces:</strong> cuatro voces de IA (Velvet Whisper, Pink Muse, Runway, After Dark), que narran en inglés. Etiqueta honesta: están generadas por IA, no son personas reales.</li>
<li><strong>Sin conexión y en segundo plano:</strong> todo viene incluido en la app; suena con la pantalla bloqueada y tiene controles en la pantalla de bloqueo.</li>
<li><strong>Dormir y mañana:</strong> meditaciones rituales de noche y de mañana con un tema para cada día de la semana, temporizador y un reproductor nocturno de luz tenue.</li>
<li><strong>Anuncios:</strong> ninguno. Ni en la versión gratis ni en PRO.</li>
<li><strong>Privacidad:</strong> sin cuenta, sin rastreo, sin SDK de analítica; tus datos se quedan en tu iPhone.</li>
<li><strong>Promesas:</strong> DIVA lo dice claramente: es para la reflexión y la relajación, no es consejo médico ni financiero, y los tonos tipo 528 Hz describen un estado de ánimo, no un efecto.</li>
<li><strong>Precios:</strong> gratis con 12 CDs; DIVA PRO mensual, anual o con una compra única Lifetime (de por vida).</li>
</ul>
<h2 id="not">Lo que DIVA no hace (para que elijas bien)</h2>
<ul>
<li>Por ahora es solo para iPhone (iOS 17 o posterior). No hay Android.</li>
<li>Los menús de la app están en inglés y turco, y las voces hablan inglés; todavía no está en español ni en otros idiomas. Esta web sí, pero los CDs, las voces y los menús los verás en inglés.</li>
<li>No graba tu propia voz.</li>
<li>No es terapia, ni coaching, ni un tratamiento para el sueño.</li>
</ul>
[[cta]]
""",
        "faq": [
            ["¿Cuál es la mejor app de afirmaciones para iPhone?", "La mejor es la que de verdad vas a seguir usando: voces naturales, escucha sin conexión, sesiones para dormir y para la mañana, sin anuncios y con una privacidad clara. DIVA se creó justo en torno a esa lista; ten en cuenta que la app está en inglés y turco."],
            ["¿Hay alguna app de afirmaciones sin anuncios?", "Sí. DIVA no tiene anuncios ni en la versión gratis ni en DIVA PRO."],
            ["¿Hay alguna app de afirmaciones que no necesite cuenta?", "Sí. DIVA no requiere registro y guarda tus datos en tu iPhone."],
        ],
        "cds": ["that_girl_energy", "love_looks_good_on_me", "beauty_sleep_for_divas"],
    },
]

SUPPORT = {
    "title": "Soporte de DIVA: ayuda, solución de problemas y contacto",
    "description": "Ayuda con DIVA: audio, recordatorios, restaurar o cancelar DIVA PRO, reembolsos, idioma de la app y borrar tus datos. Escribe directamente a Gül Eda.",
    "h1": "Soporte, pero con brillo.",
    "script": "aquí tienes ayuda",
    "lead": "¿Algo no va bien? Cuéntamelo y lo arreglo. Soy un estudio de una sola chica, así que le escribes a la persona que creó DIVA.",
    "body": """
<section class="contact-card">
<h2 id="contact">Escríbeme</h2>
<p>Escribe a <a href="mailto:solostaseraofficial@gmail.com?subject=DIVA%20support">solostaseraofficial@gmail.com</a> con el modelo de tu iPhone, tu versión de iOS y lo que ha pasado. Las capturas de pantalla ayudan muchísimo. Suelo responder en un plazo de 2 días hábiles.</p>
<p>Instagram: <a href="https://instagram.com/solo.stasera">@solo.stasera</a></p>
</section>
<h2 id="fixes">Soluciones rápidas</h2>
<details><summary>No oigo nada cuando le doy a play</summary>
<p>Sube el volumen con los botones laterales mientras suena un CD, comprueba que tus auriculares o tu altavoz Bluetooth estén conectados (o desconectados) y asegúrate de que ninguna otra app esté usando el audio. ¿Sigue sin sonar? Fuerza el cierre de DIVA y vuelve a abrirla. Si te pasa a menudo, escríbeme con el nombre del CD y la voz.</p></details>
<details><summary>La reproducción se para cuando bloqueo el iPhone</summary>
<p>DIVA sigue sonando en segundo plano, con controles en la pantalla de bloqueo. Si se para antes de tiempo, comprueba si hay un temporizador activado (lo encontrarás en el reproductor) o si otra app, una llamada o una alarma se ha quedado con el audio. Dale a play en la pantalla de bloqueo para continuar.</p></details>
<details><summary>No me aparece el recordatorio de la mañana o de la noche</summary>
<p>En tu iPhone, abre <strong>Ajustes → Notificaciones → DIVA</strong> y permite las notificaciones. Después, en Settings (los ajustes de DIVA), comprueba que el recordatorio está activado y a la hora correcta. Los modos de concentración también pueden silenciar los recordatorios.</p></details>
<details><summary>¿Cómo cambio la voz o el paisaje sonoro?</summary>
<p>En el reproductor, toca el botón de la voz o del paisaje sonoro y elige otro. Tu elección se recuerda para la próxima vez. Runway, After Dark y la mayoría de los paisajes sonoros requieren DIVA PRO.</p></details>
<details><summary>¿Cómo cambio el idioma? ¿Hay español?</summary>
<p>DIVA está en inglés y turco; por ahora no tiene español. Se abre en el idioma de tu iPhone si es uno de esos dos (con el iPhone en español, normalmente la verás en inglés). Para cambiarlo, abre <strong>Settings → Language</strong> (Ajustes → Idioma) dentro de DIVA.</p></details>
<details><summary>Compré DIVA PRO pero no se ha desbloqueado</summary>
<p>En DIVA, ve a <strong>Settings → See DIVA PRO → Restore Purchases</strong> (Ajustes → Ver DIVA PRO → Restaurar compras), con la sesión iniciada en la misma cuenta de Apple que usaste para comprar. La primera vez, comprueba tu conexión a internet.</p></details>
<details><summary>¿Cómo cancelo DIVA PRO?</summary>
<p>En el iPhone: <strong>Ajustes → [tu nombre] → Suscripciones → DIVA PRO → Cancelar suscripción</strong>. Mantienes PRO hasta el final del periodo pagado. Lifetime (de por vida) es una compra única, así que no hay nada que cancelar.</p></details>
<details><summary>¿Puedo pedir un reembolso?</summary>
<p>Todos los pagos del App Store los gestiona Apple, así que los reembolsos se piden en <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. Yo no tengo acceso a tus datos de pago.</p></details>
<details><summary>¿Cómo borro mis datos?</summary>
<p>Todo vive en tu iPhone. En DIVA, abre <strong>Settings → Storage &amp; data</strong> (Ajustes → Almacenamiento y datos) para borrar el historial de escucha, eliminar tus creaciones o eliminar tu Manifest List (tu Wishlist, con sus fotos y notas). Si eliminas la app, se borra todo.</p></details>
<details><summary>¿Mi Wishlist pasará a mi iPhone nuevo?</summary>
<p>DIVA no tiene cuenta ni nube propias, así que tus datos solo se mueven si los transfieres con una copia de seguridad del iPhone o con Inicio rápido al configurar el teléfono nuevo.</p></details>
<h2 id="more">Más ayuda</h2>
<p>Encontrarás muchas respuestas en las <a href="{{faq}}">preguntas frecuentes</a>, y los <a href="{{guides}}">Diarios de Diva</a> tienen guías sobre rituales, afirmaciones para dormir y vision boards.</p>
""",
}

PRIVACY = {
    "title": "Política de privacidad de DIVA",
    "description": "Política de privacidad de DIVA: sin cuenta, sin anuncios, sin rastreo, sin analítica. Tus afirmaciones, tu Wishlist y tus fotos se quedan en tu iPhone.",
    "h1": "Política de privacidad",
    "script": "tus secretos están a salvo",
    "updated": "2026-11-14",
    "lead": "La versión corta: DIVA no recopila tus datos. Sin cuenta, sin anuncios, sin rastreo, sin analítica, sin servidor. Lo que haces en DIVA se queda en tu iPhone.",
    "body": """
<p>Esta política explica cómo trata la información la app DIVA para iPhone (“DIVA”, “la app”). DIVA está hecha por Gül Eda Aydemir, desarrolladora independiente (“yo”).</p>
<h2 id="collect">1. Información que recopila DIVA</h2>
<p>Ninguna. DIVA no recopila datos personales, ni los almacena en un servidor, ni los vende, ni los comparte. La app no tiene sistema de cuentas, ni publicidad, ni SDK de analítica o de rastreo, ni un servidor propio.</p>
<h2 id="device">2. Información guardada solo en tu dispositivo</h2>
<p>Para funcionar, DIVA guarda algunas cosas localmente en tu iPhone, dentro del almacenamiento privado de la app:</p>
<ul>
<li>tus favoritos, tu historial de escucha y tus preferencias (voz, paisaje sonoro, tema, idioma, horas de los recordatorios);</li>
<li>los CDs que creas y las afirmaciones que escribes;</li>
<li>tu Wishlist (Manifest List): sueños, notas, progreso, hitos y cualquier foto que añadas a tu vision board;</li>
<li>el audio de narración ya preparado, guardado en caché para que los CDs empiecen al instante.</li>
</ul>
<p>Esta información nunca sale de tu dispositivo a través de DIVA. Puede incluirse en tus propias copias de seguridad del iPhone o de iCloud, que controlan tú y Apple. Las afirmaciones que escribes con tus propias palabras se convierten en voz en tu iPhone.</p>
<h2 id="permissions">3. Permisos</h2>
<ul>
<li><strong>Cámara</strong>: solo cuando decides sacar una foto para tu vision board.</li>
<li><strong>Fotos</strong>: eliges las fotos para tu vision board con el selector de fotos de iOS, que solo comparte las fotos que seleccionas. DIVA solo pide permiso para añadir fotos a tu fototeca cuando decides guardar una tarjeta de logro.</li>
<li><strong>Notificaciones</strong>: solo si activas los recordatorios. Se programan en tu dispositivo; no interviene ningún servidor de notificaciones.</li>
</ul>
<p>Puedes cambiar estos permisos cuando quieras en los Ajustes del iPhone.</p>
<h2 id="purchases">4. Compras</h2>
<p>Las suscripciones a DIVA PRO y la compra Lifetime (de por vida) las procesa Apple a través del App Store. Yo nunca recibo tu nombre, tu email ni tus datos de pago. Apple proporciona a los desarrolladores informes de ventas anónimos y agregados. A tu cuenta de Apple se le aplica la política de privacidad de la propia Apple.</p>
<h2 id="apple">5. Información que Apple puede compartir</h2>
<p>Si has elegido compartir análisis con los desarrolladores de apps en los Ajustes del iPhone, Apple puede proporcionarme informes de fallos anónimos y estadísticas de uso agregadas. Puedes desactivarlo en <strong>Ajustes → Privacidad y seguridad → Análisis y mejoras</strong>.</p>
<h2 id="delete">6. Borrar tus datos</h2>
<p>En DIVA, abre <strong>Settings → Storage &amp; data</strong> (Ajustes → Almacenamiento y datos) para borrar tu historial de escucha, eliminar tus creaciones o eliminar tu Manifest List. Al eliminar la app se borra todo lo que DIVA guardó en tu iPhone.</p>
<h2 id="kids">7. Menores</h2>
<p>DIVA no recopila a sabiendas información de nadie, incluidos los menores, porque no recopila ninguna información personal.</p>
<h2 id="wellness">8. Aviso sobre bienestar</h2>
<p>DIVA es para la reflexión personal y la relajación. No es consejo médico, psicológico ni financiero y no promete resultados. La narración es voz generada por IA y no imita a ninguna persona real.</p>
<h2 id="changes">9. Cambios en esta política</h2>
<p>Si DIVA cambia alguna vez su forma de tratar la información (por ejemplo, al añadir una sincronización opcional en la nube), esta página se actualizará antes de que se publique esa versión, y la fecha de arriba cambiará.</p>
<h2 id="contact">10. Contacto</h2>
<p>¿Preguntas? Escribe a <a href="mailto:solostaseraofficial@gmail.com?subject=DIVA%20privacy">solostaseraofficial@gmail.com</a>.</p>
""",
}
