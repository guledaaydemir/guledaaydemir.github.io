# DIVA website copy — Turkish (Türkçe).
#
# Localized from en.py. Same structure, keys and list lengths; same rules:
#   * Never promise outcomes. Affirmations are a ritual for mindset and mood, not magic, therapy,
#     medical, financial or sleep treatment.
#   * The voices are AI-generated (not real people, not imitating anyone).
#   * The app interface is English and Turkish; narration is English only for now (Turkish voices paused).
#     iPhone only, iOS 17 or later.
#   * No account, no ads, no tracking; everything stays on the iPhone.
#   * Placeholders the builder replaces — keep them exactly, never translate them:
#       {{home}} {{guides}} {{faq}} {{support}} {{privacy}} {{guide:<id>}} {{appstore}}
#       [[img:<photo-slug>|<alt text>]]   [[cd:<cd_id>]]   [[cta]]
#     ([[img]] alt text after the "|" IS translated.)
#   * CD titles and quoted affirmation lines are the app's own Turkish text (app.json);
#     in-app UI names come from the app's Localizable.xcstrings.

LANG = "tr"
OG_LOCALE = "tr_TR"
NAME = "Türkçe"

PATHS = {
    "home": "/DIVA/tr/",
    "guides": "/DIVA/tr/rehber/",
    "faq": "/DIVA/tr/sss/",
    "support": "/DIVA/tr/destek/",
    "privacy": "/DIVA/tr/gizlilik/",
}

UI = {
    "skip": "İçeriğe geç",
    "nav_guides": "Diva Günlükleri",
    "nav_faq": "SSS",
    "nav_support": "Destek",
    "nav_privacy": "Gizlilik",
    "nav_cta": "DIVA'yı indir",
    "menu": "Menü",
    "close": "Kapat",
    "lang_label": "Dil",
    "appstore_small": "Hemen indir",
    "appstore_big": "App Store",
    "appstore_aria": "DIVA'yı App Store'dan indir",
    "qr_caption": "Bilgisayardan mı bakıyorsun? iPhone'unla okut beni, aşkım.",
    "byline": "Gül Eda",
    "byline_role": "en yakın arkadaşın ve DIVA'yı yapan kız",
    "published": "Yayınlandı",
    "updated": "Güncellendi",
    "min_read": "{n} dk okuma",
    "quick_answer": "Kısa cevap, canım",
    "toc": "Bu rehberde",
    "faq_in_guide": "Hızlı sorular",
    "related": "Okumaya devam, güzelim",
    "cds_in_guide": "Bunlara bir bas",
    "back_guides": "Tüm rehberler",
    "home_crumb": "DIVA",
    "cta_title": "Başrol dönemine hazır mısın?",
    "cta_body": "DIVA, iPhone'da ücretsiz indirilir. Bir CD seç, oynat'a bas ve hayalindeki hayatı dinle.",
    "free": "ÜCRETSİZ",
    "pro": "PRO",
    "lang_hint": "Psst, bu sayfa Türkçe de var.",
    "lang_hint_go": "Türkçesine geç",
    "lang_hint_close": "Kalsın, sağ ol",
    "footer_tagline": "Başrol kızlar için olumlama CD'leri. Gül Eda'dan sevgiyle (ve biraz da leoparla).",
    "footer_disclaimer": "DIVA kişisel düşünme ve rahatlama içindir. Tıbbi, psikolojik ya da finansal tavsiye değildir ve herhangi bir sonuç vaat etmez. Seslendirmeler yapay zekâ ile üretilmiş konuşmadır.",
    "footer_app": "Uygulama",
    "footer_help": "Yardım",
    "footer_terms": "Kullanım Koşulları (Apple EULA)",
    "footer_contact": "E-posta desteği",
    "footer_rights": "© 2026 Gül Eda Aydemir. DIVA bağımsız bir uygulamadır.",
    "guides_title": "Diva Günlükleri: Olumlama ve Manifest Rehberleri",
    "guides_desc": "DIVA'yı yapan Gül Eda'dan cesur ve dürüst rehberler: olumlamalarla manifest, uyku ve sabah ritüelleri, para bilinci, hayal panosu ve fazlası.",
    "guides_h1": "Diva Günlükleri",
    "guides_script": "sevgili günlük,",
    "guides_lead": "Olumlamalar, manifest ve başrol ritüelleri hakkında bildiğim her şey; en yakın arkadaşıma mesaj atar gibi yazdım. Çünkü öyle. Selam.",
    "faq_title": "DIVA SSS: Olumlama Uygulaması Hakkında Her Şey",
    "faq_desc": "DIVA ücretsiz mi? Sesler gerçek mi? İnternetsiz ya da uyurken çalışır mı? iPhone olumlama uygulaması DIVA hakkındaki tüm sorular, yapan kızdan.",
    "faq_h1": "Soru mu var? Cevaplar bende, aşkım.",
    "faq_script": "bana her şeyi sor",
    "faq_lead": "iPhone'un olumlama CD'si uygulaması DIVA hakkında bana en çok sorulanlar. Seninki burada yok mu? Mail at, gerçekten okuyorum.",
}

HOME = {
    "title": "DIVA: iPhone için Olumlama ve Manifest Uygulaması",
    "description": "DIVA, her temanın bir CD olduğu iPhone olumlama uygulaması. Dönemini seç, sıcak bir ses seç, hayalindeki hayatı dinle. Ücretsiz, hesapsız, reklamsız.",
    "og_alt": "Parlak pembe ve leopar desenli bir makyaj masasının üzerinde pembe taşlı DIVA logosu ve şu cümle: Başrol sensin.",
    "hero_eyebrow": "App Store'da yeni ✦ iPhone",
    "hero_script": "selam, güzelim",
    "hero_h1": "Başrol dönemin için olumlamalar",
    "hero_lead": "DIVA, her temanın bir CD olduğu bir olumlama uygulaması. Dönemini seç, sesini seç, oynat'a bas ve hayalindeki hayatı dinle; sanki kendi 2000'ler süpermodel filminin başrolündesin.",
    "hero_cta": "DIVA'yı indir, ücretsiz",
    "hero_cta2": "Önce bir demo dinle",
    "hero_badges": ["Hesap yok", "Reklam yok", "Takip yok", "İnternetsiz çalışır"],
    "phone_from": "Gül Eda",
    "phone_time": "şimdi",
    "phone_msgs": ["Aşkım, inanmayacaksın.", "Sana bir uygulama yaptım 💿", "Resmen hayalindeki hayat, bir CD'de. Oynat'a bas ✨"],
    "eras_kicker": "Koleksiyon",
    "eras_h2": "Dönemini seç. Her dönem bir CD.",
    "eras_lead": "12 dönemde 20 olumlama CD'si: özgüvenden ışıltıya, paradan aşka, kariyerden hayalindeki eve ve güzellik uykusuna kadar. Her biri bir giriş, olumlamalar ve yumuşacık bir kapanıştan oluşan tam bir dinleme seansı.",
    "eras_note": "12 CD sonsuza kadar ücretsiz. Gerisi DIVA PRO ile geliyor.",
    "demo_kicker": "İndirmeden önce dene",
    "demo_h2": "Oynat'a bas. Hayalindeki hayatı dinle.",
    "demo_lead": "Bunlar uygulamadan gerçek klipler, gerçek DIVA sesleriyle. Bir CD seç, sesler arasında gezin ve Pink Aura ses atmosferini aç ya da kapat.",
    "demo_pick": "Bir CD seç",
    "demo_voice": "Sesini seç",
    "demo_aura": "Pink Aura ses atmosferi",
    "demo_play": "Oynat",
    "demo_pause": "Duraklat",
    "demo_now": "Şimdi çalıyor",
    "demo_note": "Demo klipleri gerçek CD'lerden kısa kesitler. Uygulamada bir seans 10, 20 ya da 60 dakika sürer; sesin altında en sevdiğin ses atmosferi çalar, istersen bir uyku zamanlayıcısı da kurarsın.",
    "demo_lang_note": "Anlatım şimdilik İngilizce; her cümlenin altında Türkçesi var.",
    "rituals_kicker": "Günlük ritüeller",
    "rituals_h2": "Sabahları ışılda. Geceleri yumuşa.",
    "rituals_lead": "CD'lerim sekmesinin en üstünde iki rehberli olumlama meditasyonu seni bekliyor. Nefes al, yerleş, günün olumlamalarını dinle ve içinden tekrarla. Haftanın her gününün kendi teması var.",
    "morning_title": "Sabah Olumlamaları",
    "morning_body": "Telefonun sana patronluk taslamaya başlamadan önce güne başlaman için rehberli bir meditasyon.",
    "night_title": "Uyku Öncesi Olumlamalar",
    "night_body": "Loş gece oynatıcısında, uzun ve yumuşak duraklarla tatlı bir gün kapanışı. Sakinleştirici bir ritüel, uyku tedavisi değil.",
    "weekdays": ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"],
    "rituals_note": "Ücretsiz: 5 ve 10 dakika. 20 dakika PRO ile. Nazik sabah ve uyku öncesi hatırlatmaları seni doğrudan ritüele götürür.",
    "wish_kicker": "Dileklerim ve hayal panosu",
    "wish_h2": "Sanki çoktan kargoya verilmiş gibi yaz.",
    "wish_lead": "Dileklerim, hayallerinin biraz resmiyete döküldüğü yer. Seyahat, ev, kariyer, aşk, para: yaz, takip et, bir CD'ye bağla ve geldiğinde GERÇEKLEŞTİ diye işaretle.",
    "wish_points": [
        "İlerlemeni takip et, dönüm noktalarını kutla",
        "Kendi fotoğraflarınla bir hayal panosu yap",
        "Her hayali ona uyan CD'ye bağla",
        "Günlük vizyon hatırlatması hayalini gözünün önünde tutar",
    ],
    "wish_dreams": [
        ["Manzaralı bir penthouse", 72, "penthouse-lounge"],
        ["Paris, cam kenarı", 45, "first-class-window"],
        ["Kendi cilt bakım markam", 30, "skincare-satin"],
        ["O giyinme odası", 100, "walk-in-closet"],
    ],
    "wish_achieved": "ARTIK BENİM ♡",
    "card_kicker": "Diva kartını çek",
    "card_h2": "İşaret mi bekliyorsun? İşte o.",
    "card_lead": "Bir dönem seç, kartı çevir ve bugünün cümlesini yanına al. Her cümle bir DIVA CD'sinden: uygulamada İngilizce dinlersin, burada Türkçesi var.",
    "card_button": "Kartımı çevir",
    "card_again": "Bir tane daha, lütfen",
    "card_from": "şu CD'den",
    "card_back": "işaretin yükleniyor…",
    "voices_kicker": "Sesler",
    "voices_h2": "Dört ses. Sıfır robot enerjisi.",
    "voices_lead": "Sıcak ve doğal tınılı yapay zekâ sesleri; anlatım şimdilik İngilizce. İçindeki en yakın arkadaşa benzeyeni seç.",
    "voices": {
        "velvet_whisper": ["Yumuşak · Sıcak · Uyku öncesi", "Gece yarısı kulağında duymak isteyeceğin ses. Ücretsiz."],
        "pink_muse": ["Samimi · Tatlı · Işıltılı", "Dudağında parlatıcıyla sana gaz veren kankan. Ücretsiz."],
        "runway_confidence": ["Kendinden emin · Net · Parlak", "Odaya senden önce o girer. PRO."],
        "after_dark": ["Alçak · Rüya gibi · Sakin", "İpek çarşaf, şehir ışıkları enerjisi. PRO."],
    },
    "auras_kicker": "Ses atmosferleri",
    "auras_h2": "Her moda bir aura.",
    "auras_lead": "Olumlamalarını sıcak bir ses atmosferi eşliğinde ya da yalnızca sesle dinle. Pink Aura ve Ocean at 2AM ücretsiz; gerisi PRO ile geliyor. Tonların adları bir havayı anlatır, tıbbi bir etkiyi değil. Belli ki.",
    "priv_kicker": "Tasarımı gereği gizli",
    "priv_h2": "Hesap yok. Reklam yok. Takip yok. Nokta.",
    "priv_body": "Olumlamaların, hayallerin ve hayal panondaki fotoğrafların iPhone'unda kalır. DIVA'da kayıt yok, reklam ağı yok, analiz SDK'sı yok; yani sızacak bir şey de yok. Başrol kızlar günlüklerini kilitli tutar.",
    "priv_link": "Gizlilik politikasını oku",
    "price_kicker": "Fiyatlar",
    "price_h2": "Başlamak ücretsiz. Tam diva moduna geçince PRO.",
    "free_title": "DIVA",
    "free_price": "Ücretsiz",
    "free_items": [
        "10 dakikalık seanslarla 12 ücretsiz CD",
        "Sabah ve Uyku Öncesi ritüelleri (5 ve 10 dk)",
        "Velvet Whisper ve Pink Muse sesleri",
        "Pink Aura ve Ocean at 2AM ses atmosferleri",
        "En fazla 3 tane kendi CD'ni yarat",
        "Dileklerim'de aynı anda en fazla 5 aktif hayal",
    ],
    "pro_title": "DIVA PRO",
    "pro_price": "aylık $5,99'dan itibaren",
    "pro_items": [
        "Koleksiyondaki tüm CD'ler",
        "20 ve 60 dakikalık tam seanslar",
        "Her ses ve her aura",
        "Olumlamaları kendi sözlerinle yaz",
        "Chrome Angel ve Leopard Luxe temaları",
        "Sınırsız hayal ve tüm hayal panosu düzenleri",
    ],
    "plans": [["Aylık", "$5,99"], ["Yıllık", "$29,99"], ["Ömür boyu", "tek seferde $69,99"]],
    "price_note": "Fiyatlar ABD'deki lansman fiyatlarıdır; App Store fiyatı senin para biriminde gösterir. Abonelikler, dönem bitmeden en az 24 saat önce iptal edilmezse otomatik olarak yenilenir. İstediğin zaman Apple Hesabı ayarlarından yönetebilir ya da iptal edebilirsin.",
    "letter_kicker": "En yakın arkadaşından bir not",
    "letter_h2": "DIVA'yı neden yaptım",
    "letter_body": """
<p>Tamam, hikâye zamanı. Gece 1'de yerde yatıyorum ve sanki navigasyon cihazı kahve falı bakıyormuş gibi konuşan olumlama videolarını kaydırıyorum. Robot ses. Bej arka plan. Sıfır ışıltı. Ve içimden dedim ki: <em>pardon, glamour nerede?</em></p>
<p>Ben 2000'lerin süpermodel enerjisiyle büyüdüm. Kapaklı telefonlar, dudak parlatıcısı, her yer leopar; bir odaya, oda ona teşekkür etmeliymiş gibi giren kızlar. Olumlamaların da <em>öyle</em> hissettirmesini istedim. Hayatının gecesine hazırlanırken taktığın bir CD gibi.</p>
<p>Ben de yaptım. Her tema bir CD. Sesler sıcak ve yumuşak. Cümleler ağzında doğru hissettirsin diye yazıldı, cringe olsun diye değil. Ve her şey gizli, çünkü hayallerin senden başka kimseyi ilgilendirmez.</p>
<p>Bir uygulamanın sana penthouse hediye edebileceğini iddia etmeyeceğim. Ama güne sabah sabah doomscroll yerine <em>"benim gelişim başlı başına bir giriş"</em> cümlesini duyarak başlamanın nasıl hissettirdiğini biliyorum. Bütün mesele bu. Oynat'a bas. Kendini seç.</p>
""",
    "letter_sign": "xoxo, Gül Eda",
    "diaries_kicker": "Diva Günlükleri",
    "diaries_h2": "Blogdan taze taze",
    "diaries_lead": "Manifest, ritüeller ve başrol enerjisi üzerine rehberler; en yakın arkadaşından gelen bir sesli mesaj gibi yazıldı.",
    "diaries_all": "Tüm rehberleri oku",
    "faq_kicker": "SSS",
    "faq_h2": "Soru mu var? Cevaplar bende.",
    "faq_all": "Tüm sorulara bak",
    "final_script": "resmen başrol enerjisi",
    "final_h2": "Dönemin, oynat'a bastığın an başlar.",
    "final_body": "iPhone'da ücretsiz. Hesap yok, reklam yok. Sadece sen, bir CD ve tekrar tekrar çalan hayalindeki hayat.",
}

# Overrides for app text the app itself doesn't ship in this language (empty for EN and TR:
# the builder reads those from the app catalog). Spanish fills these in.
CATEGORIES = {}
CD_TEXT = {}
RITUAL_THEMES = {}
CARD_LINES = {}
DEMO_TRANSLATION = {}

FAQ = [
    {"group": "DIVA hakkında", "items": [
        {"q": "DIVA nedir?", "a": "<p>DIVA, bağımsız geliştirici Gül Eda Aydemir'in yaptığı, iPhone için bir olumlama ve manifest uygulaması. Her tema bir olumlama CD'si: <em>O Kız Benim</em>, <em>Zengin Kız Frekansı</em> ya da <em>Divalar İçin Güzellik Uykusu</em> gibi. Bir CD, bir ses ve bir ses atmosferi seçiyorsun; sonra 10, 20 ya da 60 dakika boyunca sakin, birinci ağızdan olumlamalar dinliyorsun. Uygulamada ayrıca Sabah ve Uyku Öncesi olumlama meditasyonları, Kendi CD'ni Yarat özelliği ve hayal panolu Dileklerim de var.</p>"},
        {"q": "DIVA ücretsiz mi?", "a": "<p>Evet. DIVA'yı indirmek ücretsiz. Ücretsiz sürümde 10 dakikalık seanslarla 12 CD, Sabah ve Uyku Öncesi ritüelleri (5 ve 10 dakika), iki ses, iki ses atmosferi, en fazla 3 kendi CD'n ve Dileklerim'de aynı anda en fazla 5 aktif hayal var. DIVA PRO isteğe bağlı ve geri kalan her şeyi açıyor. İki sürümde de asla reklam yok.</p>"},
        {"q": "DIVA'yı kim yaptı?", "a": "<p>Ben! Ben Gül Eda Aydemir, bağımsız bir iOS geliştiricisiyim. DIVA'yı kendim tasarlıyor, yazıyor ve geliştiriyorum. Büyük şirket yok, yatırımcı yok; sadece leopar desenli laptop kılıfı olan ve olumlamaların kulağa nasıl gelmesi gerektiği konusunda fikirleri olan bir kız.</p>"},
        {"q": "DIVA hangi cihazlarda çalışır?", "a": "<p>DIVA bir iPhone uygulaması ve iOS 17 veya sonrasını gerektiriyor. Şu an Android ya da web sürümü yok.</p>"},
        {"q": "DIVA hangi dillerde?", "a": "<p>Uygulamanın menüleri ve yazıları İngilizce ve Türkçe; CD'lerin anlatımı ise şimdilik İngilizce. DIVA iPhone'unun diliyle açılır, istersen DIVA'nın Ayarlar bölümünden değiştirebilirsin. Bu web sitesinin İspanyolcası da var ama uygulamanın kendisi henüz İspanyolca konuşmuyor.</p>"},
        {"q": "Hesap açmam gerekiyor mu?", "a": "<p>Hayır. Kayıt yok, e-posta yok, şifre yok. Uygulamayı aç ve oynat'a bas.</p>"},
    ]},
    {"group": "Dinleme", "items": [
        {"q": "DIVA seansları ne kadar sürüyor?", "a": "<p>CD'ler 10, 20 ya da 60 dakikalık seanslar halinde çalar. Ücretsiz CD'lerde 10 dakika var; 20 ve 60 dakika DIVA PRO ile geliyor. Sabah ve Uyku Öncesi ritüelleri 5, 10 ve 20 dakikalık (5 ve 10 ücretsiz). PRO CD'lerin kısa bir ön dinlemesi var, yani önce kulak verebilirsin.</p>"},
        {"q": "Ekran kilitliyken ya da uykuya dalarken dinleyebilir miyim?", "a": "<p>Evet. DIVA arka planda çalmaya devam eder ve kilit ekranından kontrol edebilirsin. Bir uyku zamanlayıcısı var; Uyku Öncesi ritüeli de loş bir gece oynatıcısında açılır. Sesi rahat bir seviyede tut, özellikle gece kulaklıkla dinlerken.</p>"},
        {"q": "DIVA internetsiz çalışır mı?", "a": "<p>Evet. Tüm CD'ler ve sesler uygulamanın içinde; yani uçakta, metroda ya da hiç çekmeyen bir dağ evinde bile dinleyebilirsin.</p>"},
        {"q": "Sesler gerçek insanlar mı?", "a": "<p>Hayır. DIVA'daki seslendirmeler yapay zekâ ile üretilmiş konuşma. Sesler (Velvet Whisper, Pink Muse, Runway ve After Dark) gerçek insanların kayıtları değil ve kimseyi taklit etmiyor. Kendi sözlerinle yazdığın olumlamalar iPhone'unda, şimdilik İngilizce bir sesle seslendirilir.</p>"},
        {"q": "Kendi olumlama CD'mi yapabilir miyim?", "a": "<p>Evet! Kendi CD'ni Yarat ile sana benzeyen olumlamaları seçip CD'lerim sekmesine kaydediyorsun. Ücretsiz kullanıcılar en fazla 3 kendi CD'sini saklayabilir. Olumlamaları kendi sözlerinle yazmak bir DIVA PRO özelliği.</p>"},
        {"q": "Ses atmosferleri ne, 528 Hz tonları bir işe yarıyor mu?", "a": "<p>Ses atmosferleri sesin altındaki müzik katmanı: Pink Aura, Ocean at 2AM, Hotel Rain, Dreamy Static, Silk Noise, Celestial Drift ve 111, 432, 528, 639, 777, 888 ve 963 Hz'lik yumuşak tonlar. Tonlar hakkında dürüst cevap: adları bir etkiyi değil, bir havayı anlatıyor. Bir şeyi iyileştirdikleri için değil, kulağa rüya gibi geldikleri için oradalar.</p>"},
        {"q": "Sabah ve Uyku Öncesi ritüelleri nedir?", "a": "<p>CD'lerim sekmesinin en üstündeki iki rehberli olumlama meditasyonu. Nefes alıyor, yerleşiyor ve günün olumlamalarını, içinden tekrar edebileceğin boşluklarla dinliyorsun. Haftanın her gününün kendi teması var; Salı Özgüven, Pazar Şükran gibi. İsteğe bağlı hatırlatmalar seni doğrudan ritüele götürür.</p>"},
    ]},
    {"group": "Dileklerim ve hayal panosu", "items": [
        {"q": "DIVA'daki Dileklerim nedir?", "a": "<p>Senin manifest listen. Hayatına çağırdığın hayalleri (seyahat, ev, kariyer, aşk, para) yaz, ilerlemeni takip et, dönüm noktalarını kutla ve gerçekleştiklerinde işaretle. Kendi fotoğraflarını ekleyerek bir hayal panosu yapabilir, her hayali ona uyan bir CD'ye bağlayabilir ve günlük vizyon hatırlatmasını açabilirsin. Ücretsiz kullanıcılar aynı anda yolda olan en fazla 5 hayal tutabilir; PRO'da sınır yok.</p>"},
        {"q": "Hayal panom gizli mi?", "a": "<p>Tamamen. Hayallerin, notların ve fotoğrafların yalnızca iPhone'unda saklanır. DIVA kamerayı sadece panon için fotoğraf çekmeyi seçtiğinde kullanır; bir başarı kartını da yalnızca kaydet'e dokunduğunda fotoğraflarına kaydeder.</p>"},
    ]},
    {"group": "DIVA PRO ve ödeme", "items": [
        {"q": "DIVA PRO'da neler var?", "a": "<p>Koleksiyondaki tüm CD'ler, 20 ve 60 dakikalık tam seanslar, dört sesin hepsi ve tüm ses atmosferleri, olumlamaları kendi sözlerinle yazmak, Chrome Angel ve Leopard Luxe temaları, sınırsız hayal ve tüm hayal panosu düzenleri.</p>"},
        {"q": "DIVA PRO ne kadar?", "a": "<p>ABD'deki lansman fiyatları: aylık $5,99, yıllık $29,99 ya da Ömür boyu için tek seferde $69,99. App Store, sen onaylamadan önce kesin fiyatı kendi ülkende ve para biriminde gösterir.</p>"},
        {"q": "Aboneliğimi nasıl iptal ederim?", "a": "<p>iPhone'unda <strong>Ayarlar → [adın] → Abonelikler → DIVA PRO → Aboneliği İptal Et</strong> yolunu izle. Ödediğin dönemin sonuna kadar PRO'da kalırsın. Bir sonraki ücretlendirmeden kaçınmak için yenilemeden en az 24 saat önce iptal et.</p>"},
        {"q": "Yeni iPhone'da satın alımımı nasıl geri yüklerim?", "a": "<p>Aynı Apple Hesabı ile giriş yap, DIVA'yı aç ve <strong>Ayarlar → DIVA PRO'ya göz at → Satın Alımları Geri Yükle</strong> yolunu izle. Ömür boyu ve aktif abonelikler hemen geri gelir.</p>"},
        {"q": "Para iadesi alabilir miyim?", "a": "<p>Ödemeler Apple üzerinden yapılıyor, iadeler de öyle. <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a> adresinden talep edebilirsin. App Store ödemelerini ben göremiyor ve iade edemiyorum ama bir şeyler ters gittiyse bana mail at, elimden geldiğince yardım ederim.</p>"},
    ]},
    {"group": "Gizlilik ve dürüstlük", "items": [
        {"q": "DIVA verilerimi topluyor mu?", "a": "<p>Hayır. DIVA'da hesap, reklam, analiz SDK'sı ve sunucu yok. Favorilerin, geçmişin, CD'lerin, hayallerin ve fotoğrafların iPhone'unda kalır. Satın alımları Apple yönetir. <a href=\"{{privacy}}\">Gizlilik politikasının</a> tamamını oku.</p>"},
        {"q": "Olumlamalar gerçekten işe yarıyor mu?", "a": "<p>Açık konuşalım: olumlamalar sihirli bir büyü değil, odak ve ruh hali için bir araç. Pek çok kişi nazik, net ve şimdiki zamanda kurulmuş cümleleri tekrar etmenin güne daha sakin başlamalarına ya da kendi küçük zaferlerini fark etmelerine yardımcı olduğunu görüyor. Kendini olumlama üzerine yapılan araştırmalar bazı alanlarda umut verici, bazılarında ise karışık. DIVA sonuç vaat etmiyor; sana gerçekten sürdürebileceğin kadar iyi hissettiren bir ritüel sunuyor.</p>"},
        {"q": "DIVA terapi ya da tıbbi tavsiye mi?", "a": "<p>Hayır. DIVA kişisel düşünme ve rahatlama içindir. Tıbbi, psikolojik ya da finansal tavsiye değildir; Uyku Öncesi ritüeli de bir gün kapanışıdır, uyku tedavisi değil. Ağır bir şeyler yaşıyorsan lütfen bir uzmanla konuş. Gerçek bir desteği hak ediyorsun, canım.</p>"},
    ]},
]

GUIDES = [
    {
        "id": "manifest",
        "slug": "olumlamalarla-manifest-nasil-yapilir",
        "title": "Olumlamalarla Manifest Nasıl Yapılır? (Süpermodel Usulü)",
        "description": "Olumlamalarla manifest 4 adımda: tek bir dönem seç, şimdiki zamanda yaz, her gün dinle ve küçük bir adım at. Cesur ve dürüst bir rehber.",
        "kicker": "Manifest 101",
        "image": "pink-closet",
        "image_alt": "Payetli elbiseler, kristal topuklular ve bir avizeyle parlak pembe bir giyinme odası",
        "date": "2026-11-14",
        "quick": "Olumlamalarla manifest yapmak için hayatının belirli bir alanını (yani 'dönemini') seç, kulağa inandırıcı gelen 5 ila 10 kısa cümleyi şimdiki zamanda yaz, bunları her gün aynı anda dinle ya da söyle ve gerçek hayatta küçük bir adımla eşleştir. Olumlamalar odağın ve ruh halin üzerinde çalışır; işleri yürüten şey ise attığın adımdır.",
        "body": """
<p>Aşkım. Otur. Manifest hakkında konuşmamız lazım, çünkü internet onu ya sihirli bir büyüye ya da dolandırıcılığa çevirdi; oysa ikisi de değil. Manifest bir <em>alışkanlık</em>. Benim usulümle yaparsan da çok ama çok göz alıcı bir alışkanlık.</p>
<h2 id="what">Olumlamalarla manifest aslında ne demek?</h2>
<p>Manifest; ne istediğine karar vermek, onu çoktan gerçekmiş gibi söylemek ve sonra ona sahip olan kız gibi davranmak. Olumlamalar işin söyleme kısmı: kostüm gibi hissettirmeyi bırakıp tenin gibi hissettirene kadar tekrar ettiğin kısa, birinci ağızdan, şimdiki zamanda kurulmuş cümleler.</p>
<p>Dürüst versiyonu şu: olumlamalar hesabına para yatırmaz. <em>Dikkatini</em> yönlendirir. Dikkatin de neyi fark ettiğine, neye evet dediğine ve bir odaya nasıl girdiğine karar verir.</p>
<h2 id="steps">4 adımda süpermodel usulü</h2>
<ol>
<li><strong>Tek bir dönem seç.</strong> On iki değil. Bir. Özgüven, para, aşk, hayalindeki ev, kariyer. Her şeyi aynı anda isteyen kız, baş ağrısı manifest eder.</li>
<li><strong>Şimdiki zamanda yaz.</strong> "Kendime güveneceğim" bir bekleme salonu. "Girdiğim her ortamda kendim gibiyim" ise salonun ta kendisi.</li>
<li><strong>Az buçuk inandırıcı olsun.</strong> "Milyarderim" dediğinde beynin kahkaha atıyorsa, "Parayı düşünürken içim rahat" ile başla. Esnet ama koparma.</li>
<li><strong>Her gün aynı anda tekrarla.</strong> Kahve, yol, cilt bakımı, yatmadan önce. Zaten yaptığın bir şeye iliştir, yapışıp kalsın.</li>
</ol>
[[img:vanity-roses|Güller, parfüm şişeleri, ruj ve yıldız şeklinde bir allık kutusuyla pembe bir makyaj masası]]
<h2 id="listen">Dinlemek neden yapışkan nottan okumaktan iyidir</h2>
<p>Olumlamaları okumak fena değil. Ama onları <em>duymak</em> bambaşka bir film. Kulaklığında sıcak bir ses, altında yumuşak bir ses atmosferi, kimsenin senden bir şey istemediği on dakika. <a href="{{home}}">DIVA'yı</a> bu yüzden CD'ler halinde yaptım: oynat'a basıyorsun, ritüel kendi kendine akıyor.</p>
<p>DIVA'da her dönem bir CD: bir giriş, yirmi küsur olumlama ve bir kapanış. Sesi sen seçiyorsun (Velvet Whisper yatmadan önceki kızım, Pink Muse hazırlanırkenki kızım) ve süreyi de: 10, 20 ya da 60 dakika.</p>
<h2 id="action">TikTok'ta kimsenin anlatmadığı kısım: küçücük bir adım</h2>
<p>Seansından sonra hayalindeki kızın yapacağı küçük bir şey yap. Para dönemindesin? Bankacılık uygulamanda bir rakama korkuyla değil, merakla bak. Özgüven dönemindesin? O maili gönder. Hayalindeki ev dönemindesin? Hayal panona bir fotoğraf kaydet. Küçük. Her gün. İkonik.</p>
<h2 id="mistakes">Sık yapılan manifest hataları</h2>
<ul>
<li><strong>İçten içe nefret ettiğin olumlamalar.</strong> Bir cümle cringe geliyorsa yeniden yaz. Senin sözlerin, senin dönemin.</li>
<li><strong>Saat başı sonuç kontrol etmek.</strong> Tohum ekiyorsun, mikrodalgada yemek ısıtmıyorsun.</li>
<li><strong>Duygularını atlamak için kullanmak.</strong> Olumlamalar gerçek duyguların yanında durur, onların yerine geçmez. Zorlanıyorsan güvendiğin biriyle ya da bir uzmanla konuş.</li>
</ul>
[[cta]]
""",
        "faq": [
            ["Olumlamalarla manifest ne kadar sürer?", "Sabit bir süre yok; sana bir süre veren biri muhtemelen bir şey satıyordur. Çoğu insan, her gün pratik yaptığında birkaç hafta içinde ruh halinde ve odağında bir değişim fark eder. Gerçek hayattaki değişimler ise o odakla ne yaptığından gelir."],
            ["Olumlamalar şimdiki zamanda mı olmalı?", "Evet. 'Sakinim', 'Seçeneklerim var', 'Seçiyorum' gibi birinci ağızdan, şimdiki zamanda kurulmuş cümleler şu anki halinin tarifi gibi hissettirir; bu da onların içine girmeyi 'bir gün olacak' vaadinden çok daha kolay kılar."],
            ["Olumlamaları söylemek mi daha iyi, dinlemek mi?", "İkisi de işe yarar. Dinlemeyi sürdürmek daha kolay, çünkü hiç çaba istemez: kulaklığı tak ve oynat'a bas. Birçok kişi dinlerken cümleleri içinden tekrar ediyor."],
        ],
        "cds": ["the_life_i_ordered", "that_girl_energy", "everything_works_out"],
    },
    {
        "id": "sleep",
        "slug": "uyku-olumlamalari",
        "title": "Uyku Olumlamaları: Uyurken Olumlama Nasıl Dinlenir?",
        "description": "Uyurken olumlama dinlenir mi? Evet, işte nasıl: en doğru zaman, ses seviyesi, ses seçimi ve uyku olumlamalarının yapabildikleri (ve yapamadıkları).",
        "kicker": "Güzellik uykusu",
        "image": "skincare-satin",
        "image_alt": "Pembe saten üzerinde pembe cilt bakım şişeleri, yanan bir mum ve pembe kuvars bir gua sha",
        "date": "2026-11-14",
        "quick": "Evet, uykuya dalarken olumlama dinleyebilirsin. Sakin ve yavaş bir ses seç, sesi kısık tut, sen daldıktan sonra sesin durması için uyku zamanlayıcısı kur ve dinlenmek ve güvende hissetmek üzerine yumuşak cümleler seç. Uyku olumlamaları rahatlatıcı bir gün kapanışı ritüelidir, uyku tedavisi değildir.",
        "body": """
<p>Işıklar kısık. İpek yastık kılıfı. Uyku maskesi alnında, çünkü daha hazır değilsin. Diva rutininin en hafife alınan kısmı bu: gününün son on dakikasında ne duyduğun.</p>
<h2 id="work">Uyku olumlamaları işe yarar mı?</h2>
<p>Burada dürüst kankan olayım. Derin uykudayken beynini "yeniden programlayabileceğine" dair sağlam bir kanıt yok. Uyku olumlamalarının <em>yapabildiği</em> şey, günü kapatmana yardım etmek: yavaş bir ses, uzun duraklar ve nazik sözler, koşturan bir zihne yarının yapılacaklar listesinden çok daha yumuşak bir tutunacak yer verir. Sihir bu. İnternetin vaat ettiğinden daha sessiz ve açıkçası daha güzel.</p>
<h2 id="how">Geceleri olumlama nasıl dinlenir</h2>
<ol>
<li><strong>Yavaş ve alçak bir ses seç.</strong> DIVA'da bu Velvet Whisper (ücretsiz) ya da After Dark (PRO).</li>
<li><strong>Sesi kıs.</strong> Düşündüğünden de kısık. Kulakların da güzellik uykusunu hak ediyor.</li>
<li><strong>Uyku zamanlayıcısı kur.</strong> Böylece ses bütün gece rüyalarına eşlik etmek yerine, sen daldıktan sonra yavaşça kapanır.</li>
<li><strong>Yumuşak bir ses atmosferi kullan.</strong> Ocean at 2AM ücretsiz ve deniz kenarındaki bir otel gibi duyuluyor.</li>
<li><strong>Her gece aynı saatte.</strong> Ritüeller rutini sever.</li>
</ol>
[[img:lily-vanity|Zambaklar, parfüm, mücevherli bir saç fırçası ve leopar desenli bir tokayla pembe kadife bir makyaj masası]]
<h2 id="lines">Bu gece deneyebileceğin uyku olumlamaları</h2>
<ul>
<li>"Gün bitti ve bitmesine izin veriyorum."</li>
<li>"Güvendeyim, dinlenebilirim."</li>
<li>"Çarşaflarım yumuşacık ve içlerine gömülüyorum."</li>
<li>"Dinlenmek güzellik rutinimin bir parçası."</li>
<li>"Dinlenmiş ve pırıl pırıl uyanıyorum."</li>
</ul>
<p>Bunların hepsi gerçek DIVA CD'lerinden: <em>Geleceğine Fısılda</em> ve <em>Divalar İçin Güzellik Uykusu</em>, ikisi de ücretsiz.</p>
<h2 id="ritual">DIVA'nın Uyku Öncesi ritüeli</h2>
<p>Her şeyin senin yerine hazırlanmasını istiyorsan, DIVA'da CD'lerim sekmesinin en üstünde bir <strong>Uyku Öncesi Olumlamalar</strong> meditasyonu var. Loş bir gece oynatıcısında açılıyor, seni birkaç yavaş nefesten geçiriyor ve gecenin olumlamalarını uzun, yumuşak duraklarla çalıyor. Haftanın her gecesinin bir teması var (Pazartesi Bırakmak, Cumartesi Huzur) ve isteğe bağlı uyku öncesi hatırlatması onu doğrudan açıyor.</p>
<h2 id="safety">Minik bir güvenlik notu</h2>
<p>Sesi rahat bir seviyede tut, canını acıtıyorsa kocaman kulaklıklarla uyuma ve uyku sorunun devam ediyorsa bir doktorla konuş. Olumlamalar mum, reçete değil.</p>
[[cta]]
""",
        "faq": [
            ["Olumlama dinleyerek uykuya dalmak sorun olur mu?", "Hayır, ses kısık ve rahat bir seviyede olduğu sürece sorun değil. Sen uyuduktan sonra çalmanın durması için bir uyku zamanlayıcısı kullan."],
            ["Olumlamalar uyurken bilinçaltını yeniden programlayabilir mi?", "Derin uykuda öğrenme ya da yeniden programlama için sağlam bir kanıt yok. Uyku olumlamaları en iyi, henüz uyanıkken ve uykuya dalarken sakinleştirici bir gün kapanışı olarak işe yarar."],
            ["Uyku olumlamaları için en iyi ses hangisi?", "Uzun duraklarla konuşan yavaş, alçak ve sıcak bir ses. DIVA'da bu Velvet Whisper (ücretsiz) ya da After Dark (PRO)."],
        ],
        "cds": ["beauty_sleep_for_divas", "whisper_to_your_future_self", "the_life_i_ordered"],
    },
    {
        "id": "morning",
        "slug": "sabah-olumlamalari-rutini",
        "title": "10 Dakikalık Sabah Olumlamaları Rutini (That Girl Usulü)",
        "description": "Gerçekçi, 10 dakikalık bir sabah olumlama rutini: telefondan önce ne yapmalı, hangi olumlamaları söylemeli ve haftanın her günü için ayrı bir tema.",
        "kicker": "Sabah ritüelleri",
        "image": "vanity-tray",
        "image_alt": "Pembe makyaj fırçaları, krem, ruj ve vişneli bir martini kadehiyle aynalı bir makyaj tepsisi",
        "date": "2026-11-14",
        "quick": "İyi bir sabah olumlama rutini 5 ila 10 dakika sürer: telefonuna bakmadan önce üç yavaş nefes al, gün için tek bir niyet belirle, sonra şimdiki zamanda kurulmuş 5 ila 8 olumlamayı dinle ya da söyle. Haftanın her günü için ayrı bir tema (özgüven, sakin odak, bolluk, kendini sevmek) rutini taze tutar.",
        "body": """
<p>Her sabah gördüğün ilk şey 47 bildirim ve birinin nişan paylaşımıysa el kaldır. Aynen. O yüzden ilk on dakika artık kutsal. İşte benim gerçekten yaptığım rutin (bornozla, tabii ki).</p>
<h2 id="routine">10 dakikalık rutin</h2>
<ol>
<li><strong>0. dakika: telefona dokunma.</strong> Tamam, bir kere dokun; oynat'a basmak için.</li>
<li><strong>1–2. dakikalar: üç yavaş nefes.</strong> Burundan al, uzun uzun ver. Omuzlar kulaklarından aşağı, diva.</li>
<li><strong>3. dakika: tek bir niyet.</strong> Bugün için tek bir cümle. "Bugün yavaş ilerliyorum ve tam zamanında varıyorum."</li>
<li><strong>4–9. dakikalar: olumlamalar.</strong> Dinle ve her cümleyi içinden tekrarla. Denediğin bir parfüm gibi üzerinde hisset.</li>
<li><strong>10. dakika: küçücük bir adım.</strong> Su, güneş ışığı, yatağı topla. Başrol kızlar su içer.</li>
</ol>
<h2 id="week">Haftanın her günü için bir tema</h2>
<p>Her gün aynı cümleler çabucak bayatlar. DIVA'nın Sabah Olumlamaları ritüelindeki rotasyon şöyle:</p>
<ul>
<li><strong>Pazartesi:</strong> Yeni bir başlangıç</li>
<li><strong>Salı:</strong> Özgüven</li>
<li><strong>Çarşamba:</strong> Sakin odak</li>
<li><strong>Perşembe:</strong> Bolluk</li>
<li><strong>Cuma:</strong> Neşe ve ışıltı</li>
<li><strong>Cumartesi:</strong> Kendini sevmek</li>
<li><strong>Pazar:</strong> Şükran</li>
</ul>
[[img:dream-body-neon|Pembe dambılların, yoga matının ve kristal bir su şişesinin üzerinde Dream Body yazan pembe bir neon tabela]]
<h2 id="lines">Afiş gibi durmayan sabah olumlamaları</h2>
<ul>
<li>"Günaydın bana."</li>
<li>"Bugünün üstünde benim adım yazıyor."</li>
<li>"Bu sabah da kendim olarak uyandım, harika haber."</li>
<li>"Telefonuma bakmadan önce modumu ben seçiyorum."</li>
<li>"Enerjim taptaze ve tamamen bana ait."</li>
</ul>
<p>Bunlar, tam da bu iş için yaptığım ücretsiz DIVA CD'si <em>Günaydın, İkon</em>'dan.</p>
<h2 id="diva">DIVA'da nasıl yapılır</h2>
<p>CD'lerim sekmesini aç ve en üstteki <strong>Sabah Olumlamaları</strong> kartına dokun. 5 ya da 10 dakikayı (ücretsiz) veya 20 dakikayı (PRO) seç. Ayarlar'dan sabah hatırlatmasını aç; ritüeli doğrudan, bugünün temasıyla açar. Tembel kız onaylı.</p>
[[cta]]
""",
        "faq": [
            ["Sabah olumlamalarını söylemek için en iyi zaman ne?", "Uyandıktan hemen sonra, telefonuna bakmadan önce; zihnin sessizken ve henüz hiçbir şey senin yerine modunu belirlememişken."],
            ["Sabahları kaç olumlama söylemeliyim?", "Beş ila sekiz tane fazlasıyla yeter. Gerçekten hissettiğin birkaç cümle, aceleyle geçtiğin elli cümleden iyidir."],
            ["Sabah olumlama rutini 5 dakikada yapılır mı?", "Evet. Üç nefes, tek bir niyet ve kısa bir olumlama seansı. DIVA'nın Sabah ritüelinin ücretsiz bir 5 dakikalık versiyonu var."],
        ],
        "cds": ["wake_up_icon", "that_girl_energy", "born_to_be_iconic"],
    },
    {
        "id": "money",
        "slug": "para-olumlamalari",
        "title": "Para Olumlamaları: Cringe Olmayan Zengin Kız Cümleleri",
        "description": "İnandırıcı gelen para ve bolluk olumlamaları, daha sakin bir para bilinci için nasıl kullanılır ve 'zengin kız' neden seçenek, zevk ve zaman demek.",
        "kicker": "Para bilinci",
        "image": "money-bag",
        "image_alt": "Dolar banknotlarıyla dolu, etrafı elmaslar ve bir martiniyle çevrili parlak fuşya bir timsah derisi çanta",
        "date": "2026-11-14",
        "quick": "Para olumlamaları sihirli bir rakamı değil, paraya dair nasıl hissettiğini hedeflediğinde en iyi sonucu verir: 'Parayı düşünürken içim rahat' ve 'Seçeneklerim var. Zevkim var. Zamanım var.' gibi cümleler. Bunları her gün küçük bir para adımıyla birlikte kullan. Daha sakin bir para bilincini desteklerler; finansal tavsiye değildirler.",
        "body": """
<p>Para konuşalım, tatlım. Kripto dayısı ağzıyla değil. "Bankacılık uygulamamı açınca uzanıp dinlenmem gerekmesin" ağzıyla.</p>
<h2 id="what">"Zengin kız" olumlaması nedir?</h2>
<p>Zengin kız enerjisi milyarder taklidi yapmak değil. Seçenek, zevk ve zaman demek. Sakinlik demek. Zengin kızlar panikle bakiye yenilemez; rakamlara menüye bakar gibi bakarlar. O yüzden en iyi para olumlamaları rakamla değil, <em>hisle</em> ilgilidir.</p>
<h2 id="lines">Araklaman serbest: para olumlamaları</h2>
<ul>
<li>"Parayı düşünürken içim rahat."</li>
<li>"Seçeneklerim var. Zevkim var. Zamanım var."</li>
<li>"Para, kurmayı seçtiğim hayatı destekliyor."</li>
<li>"Güzel şeylerin keyfini gönül rahatlığıyla çıkarıyorum."</li>
<li>"Hesaplarıma korkuyla değil, merakla bakıyorum."</li>
<li>"Akıllı para kararları veriyorum."</li>
<li>"Keyifle harcıyorum, gururla biriktiriyorum."</li>
</ul>
<p>İlk beşi <em>Zengin Kız Frekansı</em> CD'sinden (DIVA'da ücretsiz); son ikisi <em>Milyon Dolarlık Enerji</em> CD'sinden (PRO).</p>
[[img:ceo-desk|Saten üzerinde pembe timsah derisi bir çanta, bir deste para, altın bir kart, pırlantalı bir saat ve pembe bir laptop]]
<h2 id="believe">İnandırıcı olan neden büyük olanı yener</h2>
<p>"Bir milyon dolarım var" dediğinde beynin <em>hanımefendi, hesabınızda 43 lira var</em> diyorsa, olumlama kaybeder. Sinir sisteminin takip edebileceği yerden başla: sakinlik, merak, seçenekler. Sonra esnet. "Birikimimi güvenle ve özenle büyütüyorum", büyüdükçe içine yerleşebileceğin bir cümle.</p>
<h2 id="action">Bunu tek bir para hamlesiyle eşleştir</h2>
<p>Seansından sonra küçücük bir şey yap: bir hesabına bak, unuttuğun bir aboneliği iptal et, birikime biraz para aktar, yeteneklerin için isteyeceğin bir ücreti yaz. Olumlama havayı belirler; hamle filmi çeker.</p>
<h2 id="honest">Dürüst kısım</h2>
<p>DIVA bir zihniyet ritüeli, finansal tavsiye değil; hiçbir CD senin yerine hisse senedi seçmez. Gerçek bir para desteğine ihtiyacın varsa yetkin bir danışmanla konuş. Sonra git, CD'ni olduğun CEO gibi dinle.</p>
[[cta]]
""",
        "faq": [
            ["Para olumlamaları işe yarar mı?", "Paraya karşı daha sakin ve bilinçli hissetmene yardım edebilirler; bu da pratik adımlar atmayı kolaylaştırır. Kendi başlarına para yaratmazlar ve finansal tavsiye değildirler."],
            ["En iyi para olumlaması hangisi?", "Bugün gerçekten inanabildiğin olanı. 'Parayı düşünürken içim rahat' harika bir başlangıç, çünkü finanslarına yaklaşımını değiştiriyor."],
            ["'Zengin kız frekansı' ne demek?", "Parayla barışık hissetmeyi anlatan eğlenceli bir ifade: seçeneklerinin, zevkinin ve zamanının olması, güzel şeylerin keyfini suçluluk duymadan çıkarmak. Aynı zamanda ücretsiz bir DIVA CD'sinin de adı."],
        ],
        "cds": ["rich_girl_frequency", "million_dollar_energy", "ceo_after_hours"],
    },
    {
        "id": "lucky",
        "slug": "sansli-kiz-sendromu-olumlamalari",
        "title": "Şanslı Kız Sendromu Nedir? Denemen Gereken Olumlamalar",
        "description": "Şanslı kız sendromu (lucky girl syndrome) nedir, neden iyi hissettirir, nerede ters gider? 'Her şey benim için yoluna giriyor' gibi olumlamalarla.",
        "kicker": "Şanslı kız dönemi",
        "image": "jet-set",
        "image_alt": "Gün batımında fuşya bir valiz, taşlı güneş gözlükleri ve pasaport; arkada özel bir jet",
        "date": "2026-11-14",
        "quick": "Şanslı kız sendromu, şanslı olduğunu ve her şeyin senin için yoluna girdiğini tekrar ederek güzel şeyleri beklemeye ve fark etmeye başladığın bir manifest trendi. 'Her şey benim için yoluna giriyor' ve 'Her zaman doğru zamanda doğru yerdeyim' gibi olumlamaları dene ve gerçek hayatta da şansını denemeye devam et: şans, ortaya çıkan kızı sever.",
        "body": """
<p>"Çok şanslıyım, her şey hep benim için yoluna giriyor." Bunu az önce yüksek sesle söylediysen tebrikler, resmen şanslı kız dönemindesin. Gel bunu şık yapalım, delulu değil.</p>
<h2 id="what">Şanslı kız sendromu nedir?</h2>
<p>Şanslı biri olduğuna karar verip buna inanana kadar tekrarladığın bir manifest trendi. Sonra park yerini, gelen cevabı, ücretsiz upgrade'i fark etmeye başlıyorsun. Cazibesinin bir kısmı psikoloji: güzel şeyler beklediğinde onları daha çok fark ediyorsun ve karşına çıktıklarında evet deme ihtimalin artıyor.</p>
<h2 id="lines">Şanslı kız olumlamaları</h2>
<ul>
<li>"Her şey benim için yoluna giriyor."</li>
<li>"Her şey yerli yerine oturuyor."</li>
<li>"Her zaman doğru zamanda doğru yerdeyim."</li>
<li>"Güzel haberler beni kolayca buluyor."</li>
<li>"Her yerde güzel fırsatlar görüyorum."</li>
<li>"Her zorluğu özgüvenle karşılıyorum."</li>
</ul>
<p>Bunlar ücretsiz bir DIVA CD'si olan <em>Her Şey Lehime</em> CD'sinden. Bir iş görüşmesinden, ilk buluşmadan ya da bir pazartesiden önce aç.</p>
[[img:rooftop-party|Pembe bir disko topu, şampanya kadehleri ve taşlı bir clutch ile gece bir çatı partisi]]
<h2 id="wrong">Şanslı kız sendromu nerede ters gider</h2>
<ul>
<li><strong>Şansın ödevini yapmasını beklemek.</strong> Şanslı kızlar da başvurur, gönderir, sorar ve ortaya çıkar. Sadece bunu evet duymayı bekler gibi yaparlar.</li>
<li><strong>Kötü günler için kendini suçlamak.</strong> Zor günler şanslı kızların da başına gelir. Bunlar hava durumu, hüküm değil.</li>
<li><strong>Gerçek sorunları görmezden gelmek.</strong> Olumlamalar gerçek hayatın yanında durur, onun yerine geçmez.</li>
</ul>
<h2 id="practice">3 günlük şanslı kız meydan okuması</h2>
<ol>
<li>Her sabah 10 dakika <em>Her Şey Lehime</em> CD'sini dinle.</li>
<li>Yatmadan önce üç şanslı şeyi yaz. Minicik olanlar da sayılır. Özellikle minicik olanlar.</li>
<li>Her gün küçük bir fırsata evet de.</li>
</ol>
<p>Üçüncü günün sonunda saçını savurup "tabii ki yoluna girdi" diyen kız olacaksın.</p>
[[cta]]
""",
        "faq": [
            ["Şanslı kız sendromu gerçek mi?", "Tıbbi bir sendrom değil; bir zihniyet trendi. İşe yarayan kısmı şu: güzel şeyler beklemek, fırsatları fark etme ve onlara göre harekete geçme ihtimalini artırabilir."],
            ["Şanslı kız sendromu için ne söylenir?", "'Her şey benim için yoluna giriyor', 'Şanslıyım ve bunu biliyorum' ve 'Güzel haberler beni kolayca buluyor' gibi kısa, kendinden emin cümleler; her gün tekrar edilerek."],
            ["Şanslı kız sendromu manifest ile aynı şey mi?", "Manifestin bir çeşidi; belirli bir hedefe odaklanmak yerine genel olarak şanslı hissetmeye odaklanıyor."],
        ],
        "cds": ["everything_works_out", "first_class_only", "pretty_girls_dont_chase"],
    },
    {
        "id": "vision",
        "slug": "iphone-hayal-panosu",
        "title": "iPhone'da Hayal Panosu Nasıl Yapılır? Adım Adım Rehber",
        "description": "iPhone'da dijital hayal panosu yap: hayallerini seç, fotoğraf ekle, ilerlemeni takip et, her gün gözünün önünde tut. DIVA'da Dileklerim nasıl çalışır?",
        "kicker": "Hayal panoları",
        "image": "walk-in-closet",
        "image_alt": "Alacakaranlıkta şehir manzaralı pembe bir giyinme odası; güller, parfüm ve leopar desenli bir şal",
        "date": "2026-11-14",
        "quick": "iPhone'da hayal panosu yapmak için 3 ila 5 net hayal yaz, her biri için sana o hissi veren bir fotoğraf seç, hepsini her gün göreceğin tek bir yerde topla ve ilerlemeni haftada bir gözden geçir. DIVA'daki Dileklerim bunu tek uygulamada yapar: hayaller, fotoğraflar, ilerleme, dönüm noktaları, hayal panosu ve günlük hatırlatma, hepsi gizli şekilde telefonunda saklanır.",
        "body": """
<p>Stick yapıştırıcı ve dergiden kesilmiş resimler tatlı ama hayal panon, günde 96 kere baktığın yerde yaşamalı: telefonunda. İşte gardırobun arkasında unutulup gitmeyecek bir pano yapmanın yolu.</p>
<h2 id="steps">iPhone'da adım adım hayal panosu nasıl yapılır</h2>
<ol>
<li><strong>3 ila 5 hayal yaz.</strong> Net olan, belirsiz olanı yener. "Daha çok seyahat" değil, "Paris, cam kenarı, ilkbahar."</li>
<li><strong>Her hayal için bir fotoğraf seç.</strong> İçini minicik titreten bir fotoğraf. Kendi fotoğrafların Pinterest'ten çok daha fazla işler.</li>
<li><strong>Her hayale bir sonraki adım ver.</strong> Adımı olmayan bir hayal, ekran koruyucudur.</li>
<li><strong>Her gün göreceğin bir yere koy.</strong> Bir hatırlatma, bir widget, bir ritüel.</li>
<li><strong>Haftada bir gözden geçir.</strong> İlerleme çubuğunu ilerlet, kazanımları kutla, değişen hayalleri düzenle.</li>
</ol>
[[img:penthouse-lounge|Gün batımında palmiye ağaçları, kristal bir avize ve şömineyle pembe kadife bir salon]]
<h2 id="diva">DIVA'da Dileklerim nasıl çalışır</h2>
<p>Dileklerim'i yaptım, çünkü hayallerim Notlar'a, ekran görüntülerine ve 2019'da kaybettiğim bir günlüğe dağılmıştı. DIVA'da:</p>
<ul>
<li>Her hayali bir kategoriyle (seyahat, ev, kariyer, aşk, para ve daha fazlası) ve isteğe bağlı bir notla yaz.</li>
<li>Galerinden fotoğraf ekle ya da kamerayla bir tane çekip hayal panonu oluştur.</li>
<li>İlerlemeyi ve dönüm noktalarını takip et, sonra <strong>Artık Benim ♡</strong> ile gerçekleşti olarak işaretle ve kaydedebileceğin bir kart al.</li>
<li>Bir hayali bir CD'ye bağla; mesela hayalindeki ev hayalin <em>Penthouse Modu</em> CD'sini çalsın.</li>
<li>Hayalini gözünün önünde tutmak için günlük vizyon hatırlatmasını aç.</li>
</ul>
<p>Ücretsiz kullanıcılar ızgara panoyla aynı anda yolda olan en fazla 5 hayal tutabilir (gerçekleşenler sayılmaz); PRO sınırsız hayal ve tüm pano düzenlerini açar.</p>
<h2 id="private">Gizli tut</h2>
<p>Hayal panon kişisel. DIVA hayallerini, notlarını ve fotoğraflarını yalnızca iPhone'unda saklar; hesap yok, bulut yok, gizlice bakan kimse yok. Başrol kız, kilitli günlük.</p>
[[cta]]
""",
        "faq": [
            ["iPhone'da hayal panosu yapmanın en iyi yolu ne?", "Hayallerini, fotoğraflarını ve ilerlemeni bir arada tutan ve sana her gün hatırlatan bir uygulama kullanmak. DIVA'daki Dileklerim, hayal panosunu ilerleme takibi ve uyumlu olumlama CD'leriyle birleştiriyor."],
            ["Hayal panosunda kaç hedef olmalı?", "Üç ila beş ideal: sana ilham verecek kadar çok, gerçekten odaklanabileceğin kadar az."],
            ["Dijital hayal panoları kâğıt olanlar kadar iyi mi?", "Daha da iyi olabilirler, çünkü onları daha sık görürsün. Önemli olan her gün bakmak ve küçük adımlar atmak."],
        ],
        "cds": ["penthouse_state_of_mind", "first_class_only", "the_life_i_ordered"],
    },
    {
        "id": "confidence",
        "slug": "ozguven-olumlamalari",
        "title": "Özgüven Olumlamaları: Başrol Enerjisi İçin Cümleler",
        "description": "Doğal hissettiren özgüven olumlamaları, büyük anlardan önce nasıl kullanılır ve başka biri gibi davranmadan başrol enerjisi nasıl kazanılır.",
        "kicker": "Başrol enerjisi",
        "image": "poolside-muse",
        "image_alt": "Gün batımında pembe bir havuz kenarında, taşlı güneş gözlükleri ve elinde martiniyle göz alıcı bir kadın",
        "date": "2026-11-14",
        "quick": "Özgüven olumlamaları kusursuzluğu değil rahatlığı anlattığında en iyi sonucu verir: 'Olduğum yeri rahatça dolduruyorum', 'Enerjim bir tane. Benzeri yok.', 'Kimseyle yarışmıyorum. Havayı ben belirliyorum.' Bunları her gün ve büyük anlardan hemen önce dinle, duruşunla da eşleştir: omuzlar geride, nefes yavaş, çene yumuşak.",
        "body": """
<p>Başrol enerjisi odadaki en gürültülü kız olmak değil. Kendi içinde tamamen evinde hisseden kız olmak. Rahat. Çekici. Hafiften ikonik.</p>
<h2 id="lines">Yemin ederim işe yarayan özgüven olumlamaları</h2>
<ul>
<li>"Enerjim bir tane. Benzeri yok."</li>
<li>"Kimseyle yarışmıyorum. Havayı ben belirliyorum."</li>
<li>"Benim gelişim başlı başına bir giriş."</li>
<li>"Olduğum yeri rahatça dolduruyorum."</li>
<li>"Hiç sıradan olmadım. Zaten mesele de bu."</li>
<li>"Kendim olduğum için bu kadar çekiciyim."</li>
</ul>
<p>Hepsi DIVA için yaptığım ilk CD olan <em>O Kız Benim</em> CD'sinden. Ücretsiz. Tabii ki.</p>
<h2 id="when">Özgüven olumlamaları ne zaman kullanılır</h2>
<ul>
<li><strong>Hazırlanırken.</strong> Makyajını yaparken aç. Sesle birlikte parla.</li>
<li><strong>Büyük bir şeyden önce.</strong> İş görüşmesi, buluşma, sunum, gitmeye korktuğun spor salonu. Arabada beş dakika.</li>
<li><strong>Sarsıldıktan sonra.</strong> Biri tuhaf bir şey mi söyledi? Oynat'a bas ve kendine dön.</li>
</ul>
[[img:rhinestone-gym|Leopar desen üzerinde taşlı kulaklıklar, fuşya dambıllar ve kristal bir su şişesi]]
<h2 id="body">Bedeninle eşleştir</h2>
<p>Özgüven kelimeler kadar duruşta da yaşar. Her cümle çalarken: omuzlar geride, çene yumuşak, yavaş bir nefes ver. DIVA'daki <em>O Kız Benim</em> tam olarak böyle başlıyor: "Selam, diva. Omuzlar geride, çene yumuşak. Bu an tamamen senin."</p>
<h2 id="fake">"Başarana kadar rol yap" mı?</h2>
<p>Ben "tam üstüne oturana kadar dene" demeyi tercih ederim. Özgüven olumlamaları başka biri gibi davranmakla ilgili değil; kendinden şüphe etmediğin anlarda kim olduğunu hatırlamakla ilgili. Bir cümle kostüm gibi geliyorsa, onu en sevdiğin kot pantolon gibi hissettiren bir cümleyle değiştir.</p>
[[cta]]
""",
        "faq": [
            ["İyi özgüven olumlamaları hangileri?", "Rahatlık ve kendine güven üzerine kısa, şimdiki zamanda kurulmuş cümleler; örneğin 'Olduğum yeri rahatça dolduruyorum', 'Enerjim bir tane. Benzeri yok.' ve 'Fikirlerime güveniyorum'."],
            ["Başrol enerjisi nasıl kazanılır?", "Güne bilerek başla, kendin için giyin, kendinle nazik konuş ve yarışmayı bırak. Her gün özgüven olumlamaları dinlemek, bu hissin provasını yapmana yardım eder."],
            ["Özgüven olumlamalarını ne sıklıkla dinlemeliyim?", "Birkaç hafta boyunca her gün, artı büyük anlardan hemen önce. Süreden çok düzenlilik önemli."],
        ],
        "cds": ["that_girl_energy", "pretty_girls_dont_chase", "im_the_prize"],
    },
    {
        "id": "love",
        "slug": "kendini-sevme-olumlamalari",
        "title": "Kendini Sevme ve Aşk Olumlamaları: Kovalama, Çek",
        "description": "Kendini sevme olumlamaları ve ilişkiler için aşk olumlamaları: değerini bil, zarif sınırlar koy, peşinden koşmadan sevgiyi çek. Örneklerle.",
        "kicker": "Aşk dönemi",
        "image": "diamond-bust",
        "image_alt": "Kat kat pırlanta kolyeler, bir yüzük kutusu ve kristal topuklularla kadife bir mücevher büstü",
        "date": "2026-11-14",
        "quick": "Kendini sevme olumlamaları sana değerinin tartışmaya açık olmadığını hatırlatır: 'Sessiz günlerimde bile fazlasıyla yeterliyim', 'Sınırlarım hem zarif hem sağlam.' Aşk olumlamaları bunun üzerine kurulur: 'Kovalamıyorum. Kendime çekiyorum.' Önce değer, sonra aşk. Değerini bilen kız, onu gören insanları çeker.",
        "body": """
<p>Bebeğim, adamı, kadını ya da o adı konmamış ilişkinin yükseltilmiş versiyonunu manifest etmeden önce <em>seni</em> manifest ediyoruz. Önce kendini sevmek. Her zaman. Sonra aşk sana çok yakışır.</p>
<h2 id="worth">Kendini sevme olumlamaları</h2>
<ul>
<li>"Sessiz günlerimde bile fazlasıyla yeterliyim."</li>
<li>"Değerim tartışmaya açık değil."</li>
<li>"Sınırlarım hem zarif hem sağlam."</li>
<li>"Hayır diyorum ve nazik kalıyorum."</li>
<li>"Değer gördüğüm yerde kalıyorum."</li>
</ul>
<p>Bunlar, dimdik bir öz saygı için yaptığım <em>Ödül Benim</em> CD'sinden.</p>
<h2 id="love">Aşk olumlamaları: kovalama, çek</h2>
<ul>
<li>"Doğal bir çekiciliğim var."</li>
<li>"Bir ilişkiye ne kattığımı çok iyi biliyorum."</li>
<li>"İlgi için yarışmıyorum, sevgi için de yalvarmıyorum."</li>
<li>"Bana nezaketle ve saygıyla davranılıyor."</li>
<li>"Sevgiyi açık bir kalple kabul ediyorum."</li>
</ul>
<p><em>Aşk Bana Yakışıyor</em> (altı bölümlük, fısıltılı bir gece CD'si, ücretsiz) ve <em>Prenses Muamelesi</em> (ücretsiz) CD'lerinden.</p>
[[img:lily-vanity|Zambaklar, kristal parfüm şişeleri, ruj ve leopar desenli bir tokayla pembe bir makyaj masası]]
<h2 id="how">Delulu olmadan aşk olumlamaları nasıl kullanılır</h2>
<ul>
<li><strong>Belirli bir kişiyi değil, nitelikleri olumla.</strong> "Nazik ve istikrarlı bir sevgiyi kendime çekiyorum" cümlesi, "Dokuza kadar bana geri yazıyor" cümlesini her zaman yener.</li>
<li><strong>Standartlarını şekillendirmelerine izin ver.</strong> Her gece "Değer gördüğüm yerde kalıyorum" duymak, değer görmediğin yerden gerçekten gitmeyi kolaylaştırır.</li>
<li><strong>Kendini yüksek sesle sev.</strong> Kendini bir randevuya çıkar. Çiçekleri al. Prenses muamelesi evde başlar.</li>
</ul>
<h2 id="honest">Dürüst not</h2>
<p>Olumlamalar değerli hissetmene yardım edebilir ama seni inciten bir ilişkiyi düzeltemez. Kendini güvende hissetmiyorsan ya da sıkışmış hissediyorsan güvendiğin bir arkadaşına ya da bir uzmana ulaş. Gerçek bir desteği hak ediyorsun.</p>
[[cta]]
""",
        "faq": [
            ["İyi bir kendini sevme olumlaması nedir?", "'Sessiz günlerimde bile fazlasıyla yeterliyim' çok güzel bir örnek, çünkü bir şey başarmana bağlı değil."],
            ["Olumlamalar aşkı çekmeye yardım eder mi?", "Değerli hissetmene, standartlarını yükseltmene ve daha açık bir halde ortaya çıkmana yardım edebilirler; bu da kimi çektiğini ve kimi hayatında tuttuğunu değiştirir. Başka birini kontrol edemezler."],
            ["Aşk olumlamalarını belirli bir kişi için mi söylemeliyim?", "Tek bir kişiye odaklanmak yerine aşkta istediğin nitelikleri, örneğin nezaketi ve istikrarı olumlamak çok daha sağlıklı."],
        ],
        "cds": ["love_looks_good_on_me", "princess_treatment", "im_the_prize"],
    },
    {
        "id": "write",
        "slug": "kendi-olumlamani-yaz",
        "title": "Olumlama Nasıl Yazılır? Sana Benzeyen Cümleler",
        "description": "Gerçek gibi hissettiren olumlama nasıl yazılır: birinci ağızdan, şimdiki zamanda, net ve inandırıcı. 5 adımlık formül, örnekler ve kendi CD'n.",
        "kicker": "Kendin yap diva",
        "image": "vanity-roses",
        "image_alt": "Güller, kristal bir parfüm şişesi, ruj ve taşlı saç tokalarıyla pembe bir makyaj masası",
        "date": "2026-11-14",
        "quick": "Kendi olumlamanı yazmak için birinci tekil şahıs ve şimdiki zaman kullan ('Sakinim', 'Seçeneklerim var', 'Seçiyorum' gibi), her cümleyi kısa ve net tut, irkilmeyeceğin kadar inandırıcı yap, olumlu kur (korktuğun şeyi değil, istediğini söyle) ve sesli oku: kulağa senin gibi geliyorsa, o cümle senin.",
        "body": """
<p>Hazır olumlamalar fena değil. Kişiye özel olanlar ise haute couture. İşte gerçekten sana ait hissettiren cümleler yazmak için formülüm.</p>
<h2 id="formula">5 adımlık olumlama formülü</h2>
<ol>
<li><strong>Birinci tekil şahıs.</strong> "Ben" ve "benim" diliyle yaz. Anlatıcı değilsin, başrolsün.</li>
<li><strong>Şimdiki zaman.</strong> "Sakin olacağım" değil, "Sakinim". Gelecek zaman, hayali gelecekte tutar.</li>
<li><strong>Kısa ve net.</strong> 12 kelimenin altında. "Sabahlarım yumuşak ve telaşsız", bir paragrafı yener.</li>
<li><strong>Az buçuk inandırıcı.</strong> Esnet ama koparma. Beynin itiraz ederse yumuşat: "…meyi öğreniyorum" demek serbest.</li>
<li><strong>Olumlu ifade.</strong> "Kaygılı değilim" yerine "Sakinim". Beyin tekrar ettiğin kelimeyi duyar.</li>
</ol>
<h2 id="examples">Önce ve sonra</h2>
<ul>
<li>"Artık beş parasız kalmayacağım" → "Para kararlarımı sakin ve berrak bir zihinle veriyorum."</li>
<li>"Umarım insanlar beni sever" → "Tanıdığı için insanların kendini şanslı hissettiği biriyim."</li>
<li>"Tembelliği bırakmam lazım" → "Bedenimi sevdiğim için hareket ettiriyorum."</li>
</ul>
[[img:vanity-tray|Makyaj fırçaları, krem, simli pudriyerler ve vişneli bir martiniyle aynalı bir makyaj tepsisi]]
<h2 id="voice">Sesli oku</h2>
<p>Test bu. Normal sesinle söyle. En yakın arkadaşına söylerken utanacaksan yeniden yaz. Ona üç tane parıltı emojisiyle mesaj atacaksan, o cümle bir hazine.</p>
<h2 id="cd">Olumlamalarını kendi CD'ne dönüştür</h2>
<p>DIVA'da <strong>Oluştur</strong> sekmesine dokun ve <strong>Kendi CD'ni Yarat</strong> ekranında koleksiyondan sana benzeyen olumlamaları seç; CD'lerim sekmesine kaydet ve istediğin zaman oynat'a bas (ücretsiz kullanıcılar en fazla 3 tane saklayabilir). DIVA PRO ile kendi sözlerinle cümleler de yazabilirsin; DIVA bunları iPhone'unda, gizlice seslendirir. Sözlerin telefonundan hiç çıkmaz. Küçük not: anlatım şimdilik İngilizce olduğu için en güzel İngilizce yazdığın cümlelerde duyulur.</p>
[[cta]]
""",
        "faq": [
            ["İyi bir olumlamayı ne yapar?", "Birinci ağızdan, şimdiki zamanda, kısa, net, olumlu kurulmuş ve anında itiraz etmeyeceğin kadar inandırıcı olması."],
            ["Olumlamalar hep 'Ben …im' diye mi başlamalı?", "'Sakinim', 'Yeterliyim' gibi '…im' kalıbı bir klasik; ama '…m var', '…i seçiyorum', 'Benim …' ve '…meyi öğreniyorum' kalıpları da çok güzel işler."],
            ["DIVA'da kendi olumlamalarımı kaydedebilir miyim?", "DIVA senin sesini kaydetmez. Uygulamadaki olumlamalardan bir CD oluşturabilir, DIVA PRO ile de kendi cümlelerini yazabilirsin; DIVA bunları iPhone'unda, şimdilik İngilizce bir sesle seslendirir."],
        ],
        "cds": ["born_to_be_iconic", "im_the_prize", "wake_up_icon"],
    },
    {
        "id": "app",
        "slug": "en-iyi-olumlama-uygulamasi",
        "title": "En İyi Olumlama Uygulaması Nasıl Seçilir? Dürüst Liste",
        "description": "İyi bir olumlama uygulamasında ne olmalı? Doğal sesler, internetsiz dinleme, gizlilik, reklamsızlık, uyku özellikleri, adil fiyat. DIVA'yı yapan kızdan.",
        "kicker": "Uygulama sohbeti",
        "image": "lily-vanity",
        "image_alt": "Kadife üzerinde zambaklar, kristal parfüm, mücevherli bir saç fırçası ve leopar desenli bir tokayla pembe bir makyaj masası",
        "date": "2026-11-14",
        "quick": "İyi bir olumlama uygulamasında doğal ve sıcak sesler (robotik değil) olur; internetsiz ve arka planda dinlemene izin verir, uyku ve sabah seansları sunar, verilerini gizli tutar, sakin anını bölen reklamlar içermez ve fiyatları konusunda açık sözlüdür. DIVA bu noktalar üzerine kurulmuş bir iPhone olumlama uygulaması: olumlama CD'leri, 4 yapay zekâ sesi, ritüeller ve bir hayal panosu.",
        "body": """
<p>Baştan söyleyeyim aşkım: ben bir olumlama uygulaması yaptım, yani fikirlerim var. Ama sana kendi kullandığım kontrol listesini vereceğim; bunu benimki dahil <em>her</em> uygulamaya uygulayabilirsin.</p>
<h2 id="checklist">Olumlama uygulaması kontrol listesi</h2>
<ol>
<li><strong>Ses robot gibi değil.</strong> Anlatıcı arabanın navigasyonu gibi konuşuyorsa dinlemeye devam etmezsin. Sıcak, doğal sesler ve birden fazla seçenek ara.</li>
<li><strong>İnternetsiz ve arka planda çalışıyor.</strong> Uçaklar, metrolar, gece ekran kapalı. Pazarlık konusu değil.</li>
<li><strong>Uyku seçeneği var.</strong> Yavaş ses, uzun duraklar, uyku zamanlayıcısı.</li>
<li><strong>Sabah seçeneği var.</strong> Telefonun beynini yemeden önce yapabileceğin kısa seanslar.</li>
<li><strong>Meditasyonunda reklam yok.</strong> "Sakinim" ile "Güvendeyim" arasına giren bir mobil oyun reklamı kadar havayı bozan bir şey yok.</li>
<li><strong>Gerçekten okuyabileceğin bir gizlilik.</strong> Olumlamalar ve hayaller çok kişisel. Hesap gerekip gerekmediğine ve telefondan neyin çıktığına bak.</li>
<li><strong>Dürüst sağlık iddiaları.</strong> Garantili para, aşk ya da iyileştiren frekanslar vaat eden uygulamalardan kaç.</li>
<li><strong>Net fiyatlandırma.</strong> Ne ücretsiz, ne ücretli ve nasıl iptal edilir.</li>
</ol>
[[img:diamond-bust|Pırlanta kolyeler, bir kokteyl yüzüğü ve kristal bir kadehle kadife bir mücevher büstü]]
<h2 id="diva">DIVA kendi listesinden nasıl geçiyor</h2>
<ul>
<li><strong>Sesler:</strong> dört yapay zekâ sesi (Velvet Whisper, Pink Muse, Runway, After Dark); anlatım şimdilik İngilizce. Dürüst etiket: yapay zekâ ile üretildiler, gerçek insanlar değiller.</li>
<li><strong>İnternetsiz ve arka planda:</strong> her şey uygulamanın içinde; ekran kilitliyken çalar; kilit ekranından kontrol edilir.</li>
<li><strong>Uyku ve sabah:</strong> haftanın her günü için ayrı bir teması olan Uyku Öncesi ve Sabah ritüel meditasyonları, uyku zamanlayıcısı, loş gece oynatıcısı.</li>
<li><strong>Reklamlar:</strong> yok. Ne ücretsizde ne PRO'da.</li>
<li><strong>Gizlilik:</strong> hesap yok, takip yok, analiz SDK'sı yok; verilerin iPhone'unda kalır.</li>
<li><strong>İddialar:</strong> DIVA bunu açıkça söylüyor: kişisel düşünme ve rahatlama içindir, tıbbi ya da finansal tavsiye değildir ve 528 Hz tarzı tonlar bir etkiyi değil, bir havayı anlatır.</li>
<li><strong>Fiyat:</strong> 12 CD ile ücretsiz; DIVA PRO aylık, yıllık ya da tek seferlik Ömür boyu satın alma olarak.</li>
</ul>
<h2 id="not">DIVA'nın yapmadıkları (iyi seçim yapabilesin diye)</h2>
<ul>
<li>Şimdilik sadece iPhone'da (iOS 17+). Android yok.</li>
<li>Arayüz İngilizce ve Türkçe; anlatım şimdilik yalnızca İngilizce. Başka dil henüz yok.</li>
<li>Kendi sesini kaydetmiyor.</li>
<li>Terapi, koçluk ya da uyku tedavisi değil.</li>
</ul>
[[cta]]
""",
        "faq": [
            ["iPhone için en iyi olumlama uygulaması hangisi?", "En iyisi, gerçekten kullanmaya devam edeceğin olandır: doğal sesler, internetsiz dinleme, uyku ve sabah seansları, reklamsızlık ve net bir gizlilik. DIVA tam olarak bu kontrol listesi üzerine kuruldu."],
            ["Reklamsız bir olumlama uygulaması var mı?", "Evet. DIVA'da ne ücretsiz sürümde ne de DIVA PRO'da reklam var."],
            ["Hesap gerektirmeyen bir olumlama uygulaması var mı?", "Evet. DIVA kayıt gerektirmez ve verilerini iPhone'unda tutar."],
        ],
        "cds": ["that_girl_energy", "love_looks_good_on_me", "beauty_sleep_for_divas"],
    },
]

SUPPORT = {
    "title": "DIVA Destek: Yardım, Sorun Giderme ve İletişim",
    "description": "DIVA ile ilgili yardım: ses, hatırlatmalar, DIVA PRO'yu geri yükleme ya da iptal etme, iade, dil ve verilerini silme. Gül Eda'ya doğrudan yaz.",
    "h1": "Destek, ama tatlısından.",
    "script": "yardım burada",
    "lead": "Bir şey mi ters gitti? Söyle, düzelteyim. Tek kişilik bir stüdyoyum, yani DIVA'yı yapan kişinin ta kendisine yazıyorsun.",
    "body": """
<section class="contact-card">
<h2 id="contact">Bana ulaş</h2>
<p>iPhone modelin, iOS sürümün ve ne olduğuyla birlikte <a href="mailto:solostaseraofficial@gmail.com?subject=DIVA%20support">solostaseraofficial@gmail.com</a> adresine yaz. Ekran görüntüleri çok yardımcı oluyor. Genelde 2 iş günü içinde cevap veriyorum.</p>
<p>Instagram: <a href="https://instagram.com/solo.stasera">@solo.stasera</a></p>
</section>
<h2 id="fixes">Hızlı çözümler</h2>
<details><summary>Oynat'a bastığımda hiçbir şey duymuyorum</summary>
<p>Bir CD çalarken yan tuşlarla sesi aç, kulaklığının ya da Bluetooth hoparlörünün bağlı olduğunu (ya da olmadığını) kontrol et ve sesi başka bir uygulamanın tutmadığından emin ol. Hâlâ ses yok mu? DIVA'yı tamamen kapatıp yeniden aç. Tekrar ederse CD'nin adını ve sesi yazarak bana mail at.</p></details>
<details><summary>Telefonu kilitleyince çalma duruyor</summary>
<p>DIVA arka planda çalmaya devam eder ve kilit ekranından kontrol edilir. Erken duruyorsa bir uyku zamanlayıcısı kurulu olup olmadığına (oynatıcıda bulabilirsin) ya da sesi başka bir uygulamanın, bir aramanın veya bir alarmın devralıp devralmadığına bak. Devam etmek için kilit ekranında oynat'a bas.</p></details>
<details><summary>Sabah ya da uyku öncesi hatırlatmam gelmiyor</summary>
<p>iPhone'unda <strong>Ayarlar → Bildirimler → DIVA</strong> yolunu izleyip bildirimlere izin ver. Sonra DIVA'nın Ayarlar bölümünde hatırlatmanın açık ve saatin doğru olduğunu kontrol et. Odak modları da hatırlatmaları sessize alabilir.</p></details>
<details><summary>Sesi ya da ses atmosferini nasıl değiştiririm?</summary>
<p>Oynatıcıda ses ya da aura düğmesine dokun ve başka birini seç. Seçimin bir dahaki sefere hatırlanır. Runway, After Dark ve çoğu ses atmosferi DIVA PRO gerektirir.</p></details>
<details><summary>Dili nasıl değiştiririm?</summary>
<p>DIVA iPhone'unun diliyle (İngilizce ya da Türkçe) açılır. Değiştirmek için DIVA'nın içinde <strong>Ayarlar → Dil</strong> bölümünü aç. CD'ler, uygulama dili ne olursa olsun şimdilik İngilizce seslendiriliyor.</p></details>
<details><summary>DIVA PRO'yu satın aldım ama açılmadı</summary>
<p>Satın alırken kullandığın Apple Hesabı ile giriş yapmışken DIVA'da <strong>Ayarlar → DIVA PRO'ya göz at → Satın Alımları Geri Yükle</strong> yolunu izle. İlk seferde internet bağlantını kontrol et.</p></details>
<details><summary>DIVA PRO'yu nasıl iptal ederim?</summary>
<p>iPhone'da <strong>Ayarlar → [adın] → Abonelikler → DIVA PRO → Aboneliği İptal Et</strong>. Ödediğin dönemin sonuna kadar PRO'da kalırsın. Ömür boyu tek seferlik bir satın alma, yani iptal edilecek bir şey yok.</p></details>
<details><summary>Para iadesi alabilir miyim?</summary>
<p>Tüm App Store ödemelerini Apple yönetir; iade taleplerini <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> adresinden yapabilirsin. Ödeme bilgilerine erişimim yok.</p></details>
<details><summary>Verilerimi nasıl silerim?</summary>
<p>Her şey iPhone'unda duruyor. DIVA'da <strong>Ayarlar → Depolama ve veriler</strong> bölümünden dinleme geçmişini temizleyebilir, oluşturduklarını silebilir ya da Manifest Listeni (Dileklerim'deki hayallerini, fotoğraflarını ve notlarını) silebilirsin. Uygulamayı silmek hepsini kaldırır.</p></details>
<details><summary>Dileklerim yeni iPhone'uma taşınır mı?</summary>
<p>DIVA'nın kendine ait bir hesabı ya da bulutu yok; yani verilerin yalnızca yeni telefonu kurarken iPhone yedeği ya da Hızlı Başlangıç ile aktarırsan taşınır.</p></details>
<h2 id="more">Daha fazla yardım</h2>
<p>Pek çok cevap <a href="{{faq}}">SSS</a> sayfasında; <a href="{{guides}}">Diva Günlükleri</a> bölümünde de ritüeller, uyku olumlamaları ve hayal panoları üzerine rehberler var.</p>
""",
}

PRIVACY = {
    "title": "DIVA Gizlilik Politikası",
    "description": "DIVA'nın gizlilik politikası: hesap yok, reklam yok, takip yok, analiz yok. Olumlamaların, Dileklerim ve fotoğrafların iPhone'unda kalır.",
    "h1": "Gizlilik Politikası",
    "script": "sırların güvende",
    "updated": "2026-11-14",
    "lead": "Kısaca: DIVA verilerini toplamaz. Hesap yok, reklam yok, takip yok, analiz yok, sunucu yok. DIVA'da yaptığın her şey iPhone'unda kalır.",
    "body": """
<p>Bu politika, iPhone için DIVA uygulamasının ("DIVA", "uygulama") bilgileri nasıl ele aldığını açıklar. DIVA, bağımsız bir geliştirici olan Gül Eda Aydemir ("ben") tarafından yapılmıştır.</p>
<h2 id="collect">1. DIVA'nın topladığı bilgiler</h2>
<p>Hiçbiri. DIVA kişisel verileri toplamaz, bir sunucuda saklamaz, satmaz ya da paylaşmaz. Uygulamanın hesap sistemi, reklamı, analiz ya da takip SDK'sı ve kendine ait bir arka uç sunucusu yoktur.</p>
<h2 id="device">2. Yalnızca cihazında saklanan bilgiler</h2>
<p>Çalışabilmek için DIVA bazı şeyleri iPhone'unda, uygulamanın özel depolama alanında yerel olarak kaydeder:</p>
<ul>
<li>favorilerin, dinleme geçmişin ve tercihlerin (ses, ses atmosferi, tema, dil, hatırlatma saatleri);</li>
<li>oluşturduğun CD'ler ve yazdığın olumlamalar;</li>
<li>Dileklerim (Manifest Listen): hayaller, notlar, ilerleme, dönüm noktaları ve hayal panona eklediğin fotoğraflar;</li>
<li>CD'lerin anında başlaması için önbelleğe alınan, önceden hazırlanmış seslendirme kayıtları.</li>
</ul>
<p>Bu bilgiler DIVA aracılığıyla cihazından asla çıkmaz. Kontrolü sende ve Apple'da olan kendi iPhone ya da iCloud yedeklerine dahil olabilirler. Kendi sözlerinle yazdığın olumlamalar iPhone'unda, şimdilik İngilizce bir sesle sese dönüştürülür.</p>
<h2 id="permissions">3. İzinler</h2>
<ul>
<li><strong>Kamera</strong>: yalnızca hayal panon için fotoğraf çekmeyi seçtiğinde.</li>
<li><strong>Fotoğraflar</strong>: hayal panon için fotoğrafları, yalnızca seçtiğin fotoğrafları paylaşan iOS fotoğraf seçicisiyle seçersin. DIVA, fotoğraf arşivine ekleme iznini yalnızca bir başarı kartını kaydetmeyi seçtiğinde ister.</li>
<li><strong>Bildirimler</strong>: yalnızca hatırlatmaları açarsan. Hatırlatmalar cihazında planlanır; hiçbir bildirim sunucusu kullanılmaz.</li>
</ul>
<p>Bu izinleri istediğin zaman iPhone Ayarlar'ından değiştirebilirsin.</p>
<h2 id="purchases">4. Satın alımlar</h2>
<p>DIVA PRO abonelikleri ve Ömür boyu satın alımı, App Store üzerinden Apple tarafından işlenir. Adını, e-postanı ya da ödeme bilgilerini asla almam. Apple, geliştiricilere anonim ve toplu satış raporları verir. Apple Hesabın için Apple'ın kendi gizlilik politikası geçerlidir.</p>
<h2 id="apple">5. Apple'ın paylaşabileceği bilgiler</h2>
<p>iPhone Ayarlar'ında analiz verilerini uygulama geliştiricileriyle paylaşmayı seçtiysen, Apple bana anonim çökme raporları ve toplu kullanım istatistikleri sağlayabilir. Bunu <strong>Ayarlar → Gizlilik ve Güvenlik → Analiz ve Geliştirmeler</strong> bölümünden kapatabilirsin.</p>
<h2 id="delete">6. Verilerini silmek</h2>
<p>DIVA'da <strong>Ayarlar → Depolama ve veriler</strong> bölümünden dinleme geçmişini temizleyebilir, oluşturduklarını ya da Manifest Listeni silebilirsin. Uygulamayı silmek, DIVA'nın iPhone'unda sakladığı her şeyi kaldırır.</p>
<h2 id="kids">7. Çocuklar</h2>
<p>DIVA hiçbir kişisel bilgi toplamadığı için, çocuklar dahil hiç kimseden bilerek bilgi toplamaz.</p>
<h2 id="wellness">8. Sağlık ve iyi oluş uyarısı</h2>
<p>DIVA kişisel düşünme ve rahatlama içindir. Tıbbi, psikolojik ya da finansal tavsiye değildir ve sonuç vaat etmez. Seslendirmeler yapay zekâ ile üretilmiş konuşmadır ve gerçek bir kişiyi taklit etmez.</p>
<h2 id="changes">9. Bu politikadaki değişiklikler</h2>
<p>DIVA bilgileri ele alma biçimini bir gün değiştirirse (örneğin isteğe bağlı bulut senkronizasyonu eklerse), bu sayfa o sürüm yayınlanmadan önce güncellenir ve yukarıdaki tarih değişir.</p>
<h2 id="contact">10. İletişim</h2>
<p>Soruların mı var? <a href="mailto:solostaseraofficial@gmail.com?subject=DIVA%20privacy">solostaseraofficial@gmail.com</a> adresine yaz.</p>
""",
}
