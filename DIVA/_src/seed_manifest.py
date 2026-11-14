#!/usr/bin/env python3
"""Writes a sample Wishlist (manifest.json) for app screenshots, in English or Turkish.

    python3 seed_manifest.py en|tr <output manifest.json>

The file goes into the simulator's data container at
Library/Application Support/DIVA/Manifest/manifest.json (FileManifestationRepository format).
"""
import datetime, json, sys, uuid

lang, out = sys.argv[1], sys.argv[2]
now = datetime.datetime(2026, 11, 14, 9, 41, tzinfo=datetime.timezone.utc)


def iso(days_ago):
    return (now - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def uid(n):
    return str(uuid.UUID(int=0x6E2B9B9A3F514D0C9E0A000000000000 + n)).upper()


T = {
    "en": {
        "home": ("Penthouse with a view", "I live in a beautiful home that feels like me. Soft light, a view I adore, and peace in every room.",
                 "White walls, palm trees, a pool that glows at night.",
                 ["Visualize it daily", "Listen to my home affirmations", "Open a home savings account", "Save inspiration photos"]),
        "paris": ("Paris, window seat", "The world is open to me. I travel comfortably and beautifully."),
        "brand": ("My own skincare line", "My work is valued, and my talent is recognized."),
        "money": ("Financial freedom", "I am calm when I think about money."),
        "body": ("Dream body, dream energy", "I feel strong, healthy, and energized."),
        "italy": ("Italy summer", "I am walking through Positano, sun on my skin.", "Thank you, universe."),
    },
    "tr": {
        "home": ("Manzaralı bir penthouse", "Bana benzeyen, çok güzel bir evde yaşıyorum. Yumuşak ışık, bayıldığım bir manzara ve her odada huzur.",
                 "Beyaz duvarlar, palmiyeler, geceleri parlayan bir havuz.",
                 ["Her gün hayal et", "Ev olumlamalarımı dinle", "Ev için birikim hesabı aç", "İlham fotoğrafları biriktir"]),
        "paris": ("Paris, cam kenarı", "Dünya bana açık. Rahat ve şık seyahat ediyorum."),
        "brand": ("Kendi cilt bakım markam", "Emeğim değerli, yeteneğim görülüyor."),
        "money": ("Finansal özgürlük", "Parayı düşünürken içim rahat."),
        "body": ("Hayalimdeki beden", "Kendimi güçlü, sağlıklı ve enerjik hissediyorum."),
        "italy": ("İtalya yazı", "Positano'da yürüyorum, güneş tenimde.", "Teşekkürler, evren."),
    },
}[lang]


def media(n, art, days):
    return {"id": uid(100 + n), "kind": "curated", "reference": art, "addedAt": iso(days)}


h = T["home"]
dreams = [
    {"id": uid(1), "title": h[0], "categoryID": "dream_home", "affirmation": h[1], "details": h[2],
     "media": [media(1, "cover_dream_home", 30), media(2, "backdrop_palms", 20)],
     "milestones": [{"id": uid(201 + i), "title": t, "isDone": i < 2, **({"completedAt": iso(20 - i * 10)} if i < 2 else {})} for i, t in enumerate(h[3])],
     "status": "becoming", "progress": 72, "isFavorite": True, "linkedCDID": "penthouse_state_of_mind", "templateID": "dream_home",
     "createdAt": iso(30), "updatedAt": iso(2), "sortIndex": 0},
    {"id": uid(2), "title": T["paris"][0], "categoryID": "travel", "affirmation": T["paris"][1],
     "media": [media(3, "cover_first_class", 14)], "status": "becoming", "progress": 45, "linkedCDID": "first_class_only",
     "createdAt": iso(14), "updatedAt": iso(3), "sortIndex": 1},
    {"id": uid(3), "title": T["brand"][0], "categoryID": "career", "affirmation": T["brand"][1],
     "media": [media(4, "cover_princess", 12)], "status": "becoming", "progress": 30, "linkedCDID": "ceo_after_hours",
     "createdAt": iso(12), "updatedAt": iso(4), "sortIndex": 2},
    {"id": uid(4), "title": T["body"][0], "categoryID": "wellness", "affirmation": T["body"][1],
     "media": [media(5, "cover_dream_body", 9)], "status": "becoming", "progress": 60, "linkedCDID": "dream_body_dream_energy",
     "createdAt": iso(9), "updatedAt": iso(1), "sortIndex": 3},
    {"id": uid(5), "title": T["money"][0], "categoryID": "money", "affirmation": T["money"][1],
     "media": [media(6, "cover_money", 5)], "status": "wishlist", "progress": 10, "linkedCDID": "rich_girl_frequency",
     "createdAt": iso(5), "updatedAt": iso(5), "sortIndex": 4},
    {"id": uid(6), "title": T["italy"][0], "categoryID": "travel", "affirmation": T["italy"][1],
     "media": [media(7, "backdrop_sunset", 60)], "status": "alreadyMine", "progress": 85,
     "achievement": {"achievedAt": iso(3), "gratitudeNote": T["italy"][2], "previousStatus": "becoming", "previousProgress": 85},
     "createdAt": iso(60), "updatedAt": iso(3), "sortIndex": 5},
]
json.dump({"schemaVersion": 1, "manifestations": dreams, "customCategories": []}, open(out, "w"), ensure_ascii=False, indent=1)
print("wrote", out)
