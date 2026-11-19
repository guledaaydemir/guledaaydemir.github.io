# Turkish copy for the MULA website. Facts must match ../FACTS.md. Same structure as en.py, plus "species".
# {email} is replaced with the support address, {{link:ID}} with a page URL in the same language.
# The app's interface is English: quoted in-app labels stay in English, with a short Turkish translation.

T = {
    "lang_name": "Türkçe",
    "skip": "İçeriğe geç",
    "menu": "Menü",
    "language": "Dil",
    "close": "Kapat",
    "home_label": "MULA ana sayfa",
    "theme": "Kâğıt havası",
    "theme_light": "Açık Kâğıt",
    "theme_dark": "Koyu Orman",
    "nav": {"home": "Ana sayfa", "about": "Neden MULA", "guides": "Rehberler", "faq": "SSS", "support": "Destek",
            "privacy": "Gizlilik", "terms": "Koşullar"},
    "get": "İndir",
    "badge": {"top": "App Store’dan", "big": "İndirin",
              "aria": "MULA: Plant Care uygulamasını App Store’dan indir"},
    "llms_title": "Yapay zekâ asistanları için düz metinle MULA",
    "free": "Ücretsiz",
    "premium": "Premium",
    "months": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim",
               "Kasım", "Aralık"],
    "store_name": "MULA: Plant Care",
    "seasons": ["İlkbahar", "Yaz", "Sonbahar", "Kış"],
    "season_months": ["Mar – May", "Haz – Ağu", "Eyl – Kas", "Ara – Şub"],
    "light": {"low": "Az ışık", "bright": "Aydınlık, dolaylı", "direct": "Doğrudan güneş"},
    "place": {"inside": "İç mekân", "balcony": "Balkon", "outside": "Dış mekân"},
    "intro": {"skip": "Girişi atla", "tagline": "Bakım · Büyüme · Çiçeklenme"},

    "foot": {
        "tagline": "iPhone için sakin bir bitki ve çiçek bakım uygulaması. Emir vermez, önce toprağı sorar.",
        "app": "MULA", "learn": "Rehberler", "help": "Yardım", "more": "Geliştiricinin diğer uygulamaları",
        "demo": "Toprak kontrolünü dene", "all_guides": "Tüm rehberler", "privacy": "Gizlilik politikası",
        "terms": "Kullanım koşulları",
        "made": "Acele etmeden, sevgiyle yapan:",
        "apple": "Apple, iPhone, Apple Watch ve Siri, Apple Inc.’in ticari markalarıdır.",
        "apps": [("Solo.Shots", "Bitkin için hızlandırılmış video", "https://apps.apple.com/app/id6762450478"),
                 ("Solora", "Nazik bir yaşam planlayıcısı", "https://apps.apple.com/app/id6778808618")],
    },
    "cta_box": {"h": "Bırak, MULA senin yerine sorsun",
                "p": "iPhone ve iPad için App Store’da ücretsiz; Apple Watch ve widget’larla birlikte. Reklam yok, hesap yok."},

    "article": {"by": "Yazan", "updated": "Güncellendi", "read": "{n} dk okuma", "answer": "Kısa cevap",
                "takeaways": "Öne çıkanlar", "toc": "Bu sayfada", "faq": "Sorular", "sources": "Kaynaklar",
                "related": "Okumaya devam et", "tip": "MULA ipucu", "all": "Tüm rehberler",
                "art_label": "Kâğıt portre"},
    "cats": {"app": "MULA’yı kullanmak", "care": "Sulama ve bakım", "seasons": "Mevsimler ve hava", "light": "Işık"},

    # ------------------------------------------------------------------ home
    "home": {
        "title": "Bitki bakım uygulaması MULA: sakin sulama hatırlatıcı",
        "description": "Bitki bakım uygulaması MULA, sulamadan önce toprağın nasıl olduğunu sorar, mevsimleri takip "
                       "eder ve sessiz kalır. iPhone için; reklam yok, hesap yok.",
        "og_alt": "iPhone’da MULA bitki bakım uygulaması: deve tabanı ve nazik sulama görevleriyle Today (Bugün) "
                  "ekranı",
        "eyebrow": "iPhone için bitki ve çiçek bakımı",
        "h1": "Bitkilerine sakin bir özenle bak.",
        "lead": "MULA sana asla “sula” diye emretmez. Toprağın nasıl olduğunu sorar, her bitkiye mevsimler boyunca "
                "eşlik eder ve yalnızca bir bitkinin sana gerçekten ihtiyacı olduğunda sesini çıkarır.",
        "cta_demo": "Toprak kontrolünü dene",
        "badges": ["Asla reklam yok", "Hesap yok", "Bahçen iPhone’unda kalır", "Apple Watch ve widget’lar"],
        "phone_alt": "MULA’nın açılış ekranı parça parça bir araya geliyor, ardından Today (Bugün) ekranı",
        "replay": "Açılışı yeniden oynat",
        "ribbon_label": "MULA’nın tanıdığı bitkiler, mevsim mevsim",

        "faces_kicker": "Her bitkiye bir yüz",
        "faces_h2": "Bahçen, fotoğraflarda ve kâğıt portrelerde",
        "faces_lead": "Her bitki adını, resmini ve ritmini tek bir sakin yerde saklar. MULA’nın ona eşlik ettirdiği "
                      "kâğıt kesme portreyi görmek için bir kartı çevir.",
        "faces_hint": "Çevirmek için bir karta dokun",
        "faces": [("Momo", "monstera", "Monstera deliciosa"), ("Tsubaki", "camellia", "Camellia japonica"),
                  ("Nori", "ficus", "Ficus elastica"), ("Ajisai", "hydrangea", "Hydrangea macrophylla"),
                  ("Ran", "orchid", "Phalaenopsis"), ("Mame", "pilea", "Pilea peperomioides")],

        "soil_kicker": "Toprak kontrolü",
        "soil_h2": "Emir değil, bir toprak kontrolü",
        "soil_lead": "Saksı bitkilerinin çoğu susuzluktan değil, fazla sudan kaybedilir. Bu yüzden bir bitkinin "
                     "sulama aralığı dolduğunda MULA “hemen sula” demez. Toprağın nasıl olduğunu sorar; kararı senin "
                     "cevabın verir.",
        "soil_eyebrow": "Sulama · Momo",
        "soil_q": "Momo’nun toprağı dokununca nasıl?",
        "soil_opts": [("dry", "Kuru", "Su vakti"), ("moist", "Biraz nemli", "2 gün sonra yine bak"),
                      ("wet", "Islak", "Bu turu atla"), ("unsure", "Emin değilim", "Nasıl bakılır, göster")],
        "soil_res": {
            "dry": "Sulama kaydedildi. Momo’nun bir sonraki toprak kontrolü {n} gün sonra; bir deve tabanı için "
                   "sonbahar ritmi bu.",
            "moist": "Hiçbir şey kaydedilmedi. MULA 2 gün sonra yeniden soracak.",
            "wet": "Hiçbir şey kaydedilmedi. Bu tur atlandı; bir sonraki kontrol {n} günlük tam bir aralığın "
                   "ardından gelecek.",
            "unsure": "Parmağını toprağa 3 cm kadar bastır. Temiz ve kuru çıkarsa sulama vakti gelmiştir. Parmağına "
                      "toprak yapışıyorsa bekle.",
        },
        "soil_btn": {"dry": "Momo’yu suladım", "moist": "2 gün sonra yine bak", "wet": "Bu turu atla",
                     "unsure": "Toprağın durumunu seç"},
        "soil_points": [
            "Sulamayı yalnızca “Dry” (Kuru) cevabı kaydeder; böylece geçmiş, gerçekte ne olduğunu gösterir.",
            "Uygulamayı açmadan bildirimden, bir widget’tan, Apple Watch’undan ya da Siri’yle cevap ver.",
            "Fazla bekleyen bir kontrol 7 gün sonra “Emergency Care” (Acil bakım) olur. Gün sayısını sen seçersin.",
        ],
        "soil_layers": {"dry": "kuru", "moist": "nemli", "wet": "ıslak"},

        "seasons_kicker": "Mevsimlik bakım planları",
        "seasons_h2": "Her bitkinin bir ritmi var",
        "seasons_lead": "Bitkiler soğuk aylarda daha az su içer ve dinlenir. MULA her bitkiye dört mevsimlik bir plan "
                        "verir ve mevsim döndüğünde hatırlatıcıları da ona göre kaydırır.",
        "seasons_pick": "Bir bitki seç",
        "seasons_water": "Sulama",
        "seasons_water_v": "Toprağı her {n} günde bir kontrol et",
        "seasons_feed": "Gübre",
        "seasons_feed_v": "Her {n} günde bir",
        "seasons_rest": "Bu mevsim dinleniyor",
        "seasons_temp": "Sıcaklık",
        "seasons_temp_v": "{a} ile {b}°C arasında mutlu",
        "seasons_note": "Planlar kural değil, nazik başlangıç noktalarıdır. Onlara bakmak ücretsiz; sayıları "
                        "değiştirmek Premium. “Southern hemisphere” (Güney yarımküre) anahtarı mevsimleri tersine "
                        "çevirir.",

        "features_kicker": "MULA’nın içinde",
        "features_h2": "Bahçenin ihtiyacı olan her şey, fazlası değil",
        "features": [
            ("drop", "Nazik hatırlatıcılar", "Yalnızca bir bitkinin sana ihtiyacı olduğunda. Asla gece değil, aynı "
                                             "bitki için asla günde bir kereden fazla değil; kalimba ya da Tibet "
                                             "çanağı gibi sakin seslerle.", "free"),
            ("leaf", "Bugün, sırasıyla", "Önce geciken kontroller, sonra sıradakiler. “Emergency Care” yalnızca bir "
                                         "kontrol çok geciktiğinde öne çıkar.", "free"),
            ("season", "Dört mevsimlik planlar", "İlkbahar, yaz, sonbahar ve kış için sulama ve gübre aralıkları. "
                                                 "Bitki dinlenirken gübreye ara verilir.", "free"),
            ("frost", "Don ve sıcak uyarıları", "Apple Weather’ın tahmini, her balkon bitkisinin rahat ettiği "
                                                "sıcaklık aralığıyla karşılaştırılır. Soğuk bir geceden önceki "
                                                "akşam bir uyarı gelir.", "premium"),
            ("sun", "Işık ölçer", "iPhone’unu bitkinin yaşayacağı yerde tut. Arka kamera ışığı lüks cinsinden tahmin "
                                  "eder ve o köşeyi hangi bitkilerin seveceğini gösterir.", "premium"),
            ("camera", "“Not sure what it is?” (Ne olduğundan emin değil misin?)",
             "Bir fotoğraf çek, MULA iPhone’unda ona bir göz atsın. Orkide, gül ya da eğrelti gibi bitki çeşitlerini "
             "adlandırır ve asla gelişigüzel tahmin yürütmez.", "free"),
            ("book", "Günlük ve posterler", "İlk çiçek, yeni bir yaprak, güzel bir pazar günü. Fotoğraflar sakin bir "
                                            "kâğıt portrenin yanında durur ve her bitki bir postere dönüşebilir.",
             "free"),
            ("suitcase", "Tatil modu", "Hatırlatıcıları duraklat, açık bırak ya da sana yardım eden kişiyle bir bakım "
                                       "listesi paylaş. Hiçbir şey senin yerine yapıldı diye işaretlenmez.",
             "premium"),
            ("widget", "Widget’lar", "Sıradaki bitkiyi Ana Ekran’da ve Kilitli Ekran’da gör. Daha büyük "
                                     "widget’larda doğrudan “Dry”, “Moist” ya da “Wet” (Kuru, Nemli, Islak) diye "
                                     "cevap ver.", "free"),
            ("watch", "Apple Watch", "Sana ihtiyacı olan bitkiler bileğinde; saat kadranı için bir komplikasyonla.",
             "free"),
            ("wave", "Siri ve Kestirmeler", "“I watered Momo in MULA.” “What needs care in MULA?” İngilizce söyle; "
                                            "kurulum gerekmez.", "free"),
            ("moon", "İki kâğıt havası", "“Light Paper” ve “Dark Forest” (Açık Kâğıt ve Koyu Orman), kâğıt dokusu, "
                                         "sakin hareketler ve kuş sesli yumuşak bir bahçe müziği.", "free"),
        ],
        "tier_note": "Ücretsiz özellikler “Ücretsiz” olarak işaretli. Gerisini Premium ekler.",

        "screens_kicker": "Gerçek ekranlar",
        "screens_h2": "Kâğıt ve sakin sabahlar gibi hissettirsin diye yapıldı",
        "screens_lead": "Bu sayfadaki her görsel, örnek bir bahçeyle uygulamadan alınmış gerçek bir ekran.",
        "screens": [("today", "Today (Bugün): önce seni bekleyenler"), ("soil", "Toprak kontrolü"),
                    ("garden", "My Garden (Bahçem)"), ("plant", "Bir bitkinin sayfası"),
                    ("poster", "Poster: fotoğraf ve kâğıt portre"), ("seasons", "Bir bitkinin yılı"),
                    ("weather", "Sırasıyla bakım, bir don uyarısıyla birlikte"),
                    ("whatplant", "“Looks like: Orchid” (Orkideye benziyor)"), ("lightmeter", "Işık ölçer"),
                    ("vacation", "Tatil modu"), ("reminders", "Nazik ve yalnızca gerektiğinde"),
                    ("dark", "Dark Forest (Koyu Orman)")],

        "light_kicker": "Işık",
        "light_h2": "Bu köşe yeterince aydınlık mı?",
        "light_lead": "Işığın nasıl tarif edildiğini ve MULA’nın 20 bitkisinden hangilerinin orada mutlu olacağını "
                      "görmek için güneşi kaydır.",
        "light_label": "Bu köşedeki ışık",
        "light_value": "Yaklaşık {lux} lüks",
        "light_fits": "Burayı sevecek bitkiler",
        "light_note": "Uygulamada ışık ölçer (Premium), ışığı tahmin etmek için iPhone’unun arka kamerasını kullanır. "
                      "Fotoğraf çekilmez ya da kaydedilmez; bu bir laboratuvar aleti değil, bir tahmindir.",

        "every_kicker": "Neredeysen orada",
        "every_h2": "Uygulamayı açmadan cevap ver",
        "every_lead": "Aynı toprak kontrolü bildirimlerinde, widget’larında, Apple Watch’unda ve Siri’de yaşar. "
                      "Neredeysen oradan cevap ver; MULA tek ve dürüst bir geçmiş tutar.",
        "every_items": [
            ("Bildirimler", "Hatırlatıcının üzerinde “Dry · I watered it” (Kuru · Suladım), “A little moist” (Biraz "
                            "nemli) ya da “Wet” (Islak). Gübre hatırlatıcıları “Fed today” (Bugün gübreledim) ya da "
                            "“Later” (Sonra) seçeneklerini sunar."),
            ("Widget’lar", "Küçük ve Kilitli Ekran widget’ları sıradaki bitkiyi ücretsiz gösterir. Orta ve büyük "
                           "widget’lara Premium ile cevap düğmeleri eklenir."),
            ("Apple Watch", "Sana ihtiyacı olan bitkilerin listesi ve saat kadranı için bir komplikasyon. Bilekten "
                            "cevap vermek Premium’dur."),
            ("Siri", "MULA’yla İngilizce konuş; kurulum gerekmez."),
        ],
        "siri_phrases": ["I watered Momo in MULA", "What needs care in MULA", "Soil check for Momo in MULA",
                         "I fed Momo in MULA"],
        "widgets_alt": "MULA widget’ları: sıradaki bitki, Dry, Moist ve Wet düğmeleriyle bir toprak sorusu ve bugünün "
                       "listesi",
        "watch_alt": "Apple Watch’ta MULA: Momo, Mame ve Nori bakım bekliyor",

        "why_kicker": "İsim",
        "why_h2": "MULA, kök demek",
        "why_p": [
            "MULA, Sanskritçede kök çakra olan Mūlādhāra’dan gelir: mūla kök, ādhāra destek demektir. Yedi çakranın "
            "ilkidir; bizi topraklanmış, güvende ve dengede tutan çakradır.",
            "Bir bitki yapraklarını gösterir ama kökleriyle yaşar. Bu yüzden MULA asla sulama emri vermez. Önce "
            "toprağa dokunmanı ister ve kararı cevaba bırakır.",
        ],
        "why_link": "MULA’yı neden yaptık",

        "plans_kicker": "Ücretsiz ve Premium",
        "plans_h2": "Başlamak ücretsiz. Bahçen büyüdüğünde Premium.",
        "plans_free_h": "Ücretsiz",
        "plans_free": ["10 bitkiye kadar, her biri için 5 fotoğraf", "Cevap düğmeli toprak kontrolü hatırlatıcıları",
                       "Dört mevsimlik planları görüntüleme", "Balkon bitkileri için mevsimlik sıcaklık kontrolü",
                       "iPhone’unda fotoğrafla bitki tanıma",
                       "Küçük ve Kilitli Ekran widget’ları, Apple Watch listesi, Siri",
                       "Light Paper ve Dark Forest temaları, sakin sesler, bahçe müziği"],
        "plans_premium_h": "MULA Premium",
        "plans_premium": ["Sınırsız bitki ve portre", "Her mevsimlik planı değiştirme",
                          "Fotoğraf günlüğünün tamamı ve posterler", "Tatil modu ve bakım listeleri",
                          "Her köşe için ışık ölçer", "Apple Weather’dan don ve sıcak uyarıları",
                          "Orta ve büyük widget’lardan ve Apple Watch’tan cevap verme"],
        "plans_note": "1 haftalık ücretsiz denemeyle Yıllık plan ya da Ömür Boyu: bir kez öde, sonsuza dek senin olsun. "
                      "Fiyatlar App Store’da kendi para biriminle gösterilir. Hiçbir sürümde reklam yok.",

        "privacy_kicker": "Gizlilik",
        "privacy_h2": "Bahçen seninle kalır",
        "privacy_points": [("Hesap yok", "Uygulamayı aç ve başla. Kaydolman gereken hiçbir şey yok."),
                           ("Reklam yok, takip yok", "Reklam yok, veri satışı yok. Yalnızca anonim kullanım istatistikleri; bitkilerinin adları ya da fotoğrafları asla."),
                           ("iPhone’unda", "Bitkiler, fotoğraflar ve geçmiş cihazında yaşar ve kendi iCloud’una "
                                           "yedeklenir."),
                           ("Sessizce cihazda", "Fotoğrafla tanıma ve ışık ölçer iPhone’unda çalışır.")],
        "privacy_link": "Gizlilik politikasını oku",

        "guides_kicker": "Rehberler",
        "guides_h2": "Gerçek bitki sorularına nazik cevaplar",
        "guides_link": "Tüm rehberler",

        "faq_h2": "Sorular ve cevaplar",
        "faq": [
            ("MULA nedir?", "MULA; Apple Watch uygulaması, widget’ları ve Siri desteğiyle iPhone ve iPad için sakin bir bitki "
                            "ve çiçek bakım uygulamasıdır. Sabit bir günde sulamanı söylemek yerine toprağı kontrol "
                            "etmeni hatırlatır, her bitki için mevsimleri takip eder ve bir fotoğraf günlüğü tutar. "
                            "Reklam yok, hesap yok."),
            ("MULA ücretsiz mi?", "Evet. MULA’yı indirmek ücretsiz; ücretsiz sürüm tüm hatırlatıcılar, toprak "
                                  "kontrolleri ve mevsimlik planlarla birlikte 10 bitkiye kadar saklar. MULA Premium "
                                  "(1 haftalık ücretsiz denemeli Yıllık ya da Ömür Boyu) sınırsız bitki, plan "
                                  "düzenleme, tatil modu, ışık ölçer, don ve sıcak uyarıları ve daha fazlasını ekler."),
            ("MULA ne zaman sulamam gerektiğini nasıl biliyor?", "Tahmin yürütmez. Her bitkinin, içinde bulunulan "
                                                                 "mevsime göre bir toprak kontrolü aralığı vardır. "
                                                                 "Süre dolunca MULA toprağın nasıl olduğunu sorar: "
                                                                 "“Dry” (Kuru) bir sulama kaydeder, “A little moist” "
                                                                 "(Biraz nemli) 2 gün sonra yeniden sorar, “Wet” "
                                                                 "(Islak) o turu atlar."),
            ("MULA bitkimi tanıyabilir mi?", "Bir fotoğraftan, iPhone’unda, bitkinin çeşidini önerebilir: orkide, "
                                             "gül, lale, kaktüs, eğrelti ve toplamda yaklaşık 20 çeşit. Tam türü "
                                             "belirlemez ya da hastalık teşhisi koymaz; emin olmadığında bunu "
                                             "söyler."),
            ("MULA için hesap ya da internet gerekir mi?", "Hesap gerekmez. MULA çevrimdışı çalışır. İnternete "
                                                           "bağlıyken bahçeni kendi iCloud’un üzerinden yedekler ve "
                                                           "eşitler, anonim kullanım istatistikleri gönderir ve "
                                                           "açarsan don ve sıcak uyarıları için Apple Weather’dan "
                                                           "hava tahmini ister."),
            ("MULA hangi cihazlarda çalışır?", "iOS 17 veya üstü yüklü iPhone’da, iPadOS 17 veya üstü yüklü iPad’de, "
                                               "Apple çipli Mac’lerde (iPad uygulaması olarak) ve watchOS 10 veya "
                                               "üstü yüklü Apple Watch’ta. iCloud ile eşitleme açıkken hepsi aynı "
                                               "bahçeyi gösterir."),
            ("Uygulama Türkçe ya da İspanyolca mı?", "Uygulamanın arayüzü şimdilik İngilizce. Bu web sitesi ise "
                                                     "İngilizce, Türkçe ve İspanyolca."),
        ],
        "faq_more": "Daha fazla soru",

        "final_h2": "Biraz daha yeşile yer aç.",
        "final_p": "MULA her bitkinin adını, yüzünü ve ritmini tek bir sakin yerde saklar.",

        "ld_features": ["Toprak kontrolüyle sulama hatırlatıcıları (Kuru / Biraz nemli / Islak)",
                        "Dört mevsimlik bakım planları",
                        "Dinlenme mevsiminde duran gübre hatırlatıcıları",
                        "Balkon bitkileri için Apple Weather’dan don ve sıcak uyarıları",
                        "iPhone kamerasıyla ışık ölçer (lüks tahmini)",
                        "Cihazda fotoğrafla bitki tanıma (bitki çeşitleri)", "Fotoğraf günlüğü ve bitki posterleri",
                        "Bakım listesiyle tatil modu", "Ana Ekran ve Kilitli Ekran widget’ları",
                        "Apple Watch uygulaması ve komplikasyonlar", "Siri ve Kestirmeler",
                        "Açık ve koyu kâğıt temaları", "Reklam yok, hesap yok"],
        "ld_keywords": "bitki bakım uygulaması, bitki sulama hatırlatıcı, saksı bitkisi uygulaması, iPhone bitki "
                       "sulama uygulaması, toprak kontrolü, mevsimlik bitki bakımı, bitki ışık ölçer, don uyarısı, "
                       "bitki günlüğü",
    },

    # ------------------------------------------------------------------ about
    "about": {
        "title": "Bitki bakım uygulaması MULA’yı neden yaptık?",
        "description": "Bitki bakım uygulaması MULA’nın hikâyesi: sulama emri vermek yerine toprağın nasıl olduğunu "
                       "soran uygulamanın adı, fikirleri ve bağımsız geliştiricisi.",
        "kicker": "Neden MULA",
        "h1": "Bir bitki yapraklarını gösterir ama kökleriyle yaşar.",
        "lead": "MULA basit bir dilekle başladı: kâğıt ve sakin sabahlar gibi hissettiren, susamamış bir bitkiyi sana "
                "asla sulatmayan bir bitki uygulaması.",
        "sections": [
            ("“Her pazar sula” yaklaşımının sorunu",
             "<p>Bitki uygulamalarının çoğu bir çalar saat gibi çalışır: bu bitkiyi her yedi günde bir sula. Oysa bir "
             "bitkinin susuzluğu ışıkla, saksıyla, mevsimle ve odayla değişir. Kışın aynı deve tabanının ihtiyacı "
             "yarıya inebilir. Pek çok saksı bitkisi tam da sabit bir takvim yüzünden fazla sulanır; kökleri suya "
             "doyar, yaprakları sararır.</p><p>Bu uygulamaların çoğu ayrıca gürültülüdür: ekranlar arasında reklamlar, "
             "seriler, hesaplar, rozetler. Canlı bir şeye bakmak bundan daha sakin hissettirmeli.</p>"),
            ("Emretme, sor",
             "<p>Bu yüzden MULA sorar. Bir bitkinin aralığı dolduğunda <em>toprak dokununca nasıl?</em> diye sorar. "
             "“Dry” (Kuru), su vaktinin geldiği anlamına gelir ve sulama kaydedilir. “A little moist” (Biraz nemli), "
             "MULA’nın iki gün sonra yeniden soracağı anlamına gelir. “Wet” (Islak) ise bu turun atlandığı anlamına "
             "gelir. Kararı takvim değil, toprağa dokunan parmağın verir.</p><p>Daha fazlası için: "
             "<a href=\"{{link:when-to-water}}\">saksı bitkileri ne sıklıkla sulanmalı</a>.</p>"),
            ("Mevsimleri takip et",
             "<p>MULA’daki her bitkinin ilkbahar, yaz, sonbahar ve kış için bir planı vardır: toprağın ne sıklıkla "
             "kontrol edileceği, ne zaman gübre verileceği ve ne zaman dinlenmeye bırakılacağı. Mevsim döndüğünde "
             "hatırlatıcılar da onunla birlikte döner. Balkon bitkileri mevsimlik bir sıcaklık kontrolü alır; Premium "
             "ile de don olacak bir geceden önceki akşam bir uyarı.</p>"),
            ("İsim: Mūlādhāra",
             "<p>MULA, Sanskritçede kök çakra olan <strong>Mūlādhāra</strong>’dan gelir. <em>Mūla</em> kök, "
             "<em>ādhāra</em> destek demektir. Yedi çakranın ilkidir; topraklanmış, güvende ve dengede hissetmekle "
             "ilişkilendirilir.</p><p>Canlı bir şeye bakmak bizi de topraklar. MULA’nın bütün fikri bu: gürültü yok, "
             "yalnızca bahçenin ihtiyaç duyduğu bir sonraki küçük şey.</p>"),
            ("Plastik değil, kâğıt",
             "<p>MULA kâğıt kesme gibi çizilir: sıcak washi dokusu, bir güneş, birkaç tepe, kökleriyle bir toprak "
             "kâsesi. İki kâğıt havası: “Light Paper” ve “Dark Forest” (Açık Kâğıt ve Koyu Orman). Kitap gibi okunan "
             "tırnaklı yazı tipleri. Alarmlar yerine kalimba ya da Tibet çanağı gibi yumuşak sesler; uygulama açıkken "
             "de kuş sesli, sakin bir bahçe müziği. Her bitki, fotoğraflarının yanında duracak kâğıt kesme bir portre "
             "alır.</p>"),
            ("Özünde gizli",
             "<p>Ne MULA hesabı var ne de MULA sunucusu. Bitkilerin, fotoğrafların ve geçmişin iPhone’unda kalır. "
             "Reklam ve takip yok; MULA yalnızca anonim kullanım istatistikleri gönderir, bitkilerinin adlarını, "
             "notlarını ya da fotoğraflarını asla. Fotoğrafla tanıma ve ışık ölçer cihazda çalışır. "
             "<a href=\"{{link:privacy}}\">Gizlilik politikasını</a> oku.</p>"),
            ("MULA’yı kim yapıyor",
             "<p>MULA’yı, Solo.Shots ve Solora’yı da yapan bağımsız iOS geliştiricisi <strong>Gül Eda "
             "Aydemir</strong> yapıyor. Uygulamadaki her ekran, her ses ve her kelime özenle, acele etmeden yapılıyor. "
             "Bir fikrin varsa ya da bir şey yolunda gitmiyorsa <a href=\"mailto:{email}\">{email}</a> adresine yaz "
             "ya da Instagram’da <a href=\"https://www.instagram.com/solo.stasera/\" rel=\"noopener\">@solo.stasera</a> "
             "hesabına merhaba de.</p>"),
        ],
        "principles_h": "Beş sessiz söz",
        "principles": [("Emretme, sor", "Her sulamadan önce bir toprak kontrolü."),
                       ("Mevsimleri takip et", "Bitki dinlenirken dinlenen planlar."),
                       ("Yalnızca gerektiğinde", "Asla gece değil, bir bitki için asla günde iki kez değil."),
                       ("Sana satacak bir şey yok", "Reklam yok, hesap yok, takip yok."),
                       ("Kâğıt gibi yapıldı", "Bakması sakin, kullanması sakin.")],
    },

    # ------------------------------------------------------------------ guides index
    "guides_page": {
        "title": "Bitki bakım rehberleri: sulama, ışık, mevsimler | MULA",
        "description": "Bitki bakım rehberleri, sakin ve pratik: ne sıklıkla sulamalı, fazla sulama belirtileri, "
                       "saksı bitkileri için ışık, mevsimlik bakım, don, sıcak, tatil ve MULA.",
        "kicker": "Rehberler",
        "h1": "Gerçek bitki soruları için nazik rehberler",
        "lead": "Önce kısa cevaplar, sonra ayrıntılar. Bitkileri seven ama botanik diploması istemeyenler için yazıldı "
                "ve güvenilir bahçecilik kaynaklarıyla karşılaştırıldı.",
        "all": "Tümü",
    },

    # ------------------------------------------------------------------ faq
    "faq_page": {
        "title": "Bitki bakım uygulaması MULA: sık sorulan sorular",
        "description": "Bitki bakım uygulaması MULA hakkında cevaplar: toprak kontrolü hatırlatıcıları, mevsimler, "
                       "ücretsiz ve Premium, widget’lar, Apple Watch, gizlilik ve diller.",
        "kicker": "SSS",
        "h1": "MULA hakkında sorular",
        "lead": "Cevabını bulamadın mı? {email} adresine yaz.",
        "groups": [
            ("MULA’yı kullanmak", [
                ("Nasıl bitki eklerim?", "“Garden” (Bahçe) ya da “Today” (Bugün) sekmesinde + simgesine dokun. "
                                         "Bitkine bir ad ver, bir tür seç (ya da genel bakım planında kal), nerede "
                                         "yaşadığını (“Indoor”, “Balcony” ya da “Outdoor”: iç mekân, balkon ya da dış "
                                         "mekân) ve ne kadar ışık aldığını belirt. MULA, sonradan değiştirebileceğin "
                                         "nazik bir başlangıç planı önerir."),
                ("MULA neden bana sulamamı söylemek yerine toprağı soruyor?",
                 "Çünkü toprak takvimden daha iyi bilir. Bir sulama yalnızca toprağın kuru olduğunu söylediğinde "
                 "kaydedilir; “A little moist” (Biraz nemli) 2 gün sonra yeniden sorar, “Wet” (Islak) o turu atlar. "
                 "Böylece saksı bitkilerinin en yaygın sorunundan, fazla sudan kaçınılır."),
                ("“Emergency Care” (Acil bakım) nedir?", "Bir toprak kontrolü belirlediğin eşikten uzun süre "
                                                         "beklediğinde (varsayılan 7 gün; “Settings → Emergency care "
                                                         "after” (Ayarlar → Acil bakım eşiği) bölümünden "
                                                         "değiştirebilirsin) bitki, fazladan bir hatırlatmayla "
                                                         "“Today” ekranının en üstüne çıkar."),
                ("MULA hangi bitkileri tanıyor?", "Mevsimlik planlarıyla 20 bitki: deve tabanı, kamelya, kauçuk, "
                                                  "ortanca, orkide, Çin para bitkisi, paşa kılıcı, barış çiçeği, "
                                                  "salon sarmaşığı (pothos), lavanta, aloe vera, gül, lale, kaktüs, "
                                                  "Boston eğreltisi, sarmaşık, begonya, Atatürk çiçeği, biberiye ve "
                                                  "areka palmiyesi. Başka her bitki, senin ayarlayacağın genel bir "
                                                  "bakım planını kullanabilir."),
                ("MULA bir bitkiyi fotoğraftan tanıyabilir mi?", "iPhone’unda Apple’ın görüntü tanıma teknolojisiyle "
                                                                 "bitkinin çeşidini önerir (orkide, gül, lale, kaktüs, "
                                                                 "eğrelti ya da palmiye gibi yaklaşık 20 çeşit). Tam "
                                                                 "türü söylemez ve asla zararlı ya da hastalık "
                                                                 "teşhisi koymaz."),
                ("MULA, Güney Yarımküre’de mevsimleri takip ediyor mu?", "Evet. “Settings → Southern hemisphere” "
                                                                        "(Ayarlar → Güney yarımküre) seçeneğini aç, "
                                                                        "mevsimler tersine döner."),
                ("Tatildeyken ne olur?", "Premium ile “Vacation mode” (Tatil modu) hatırlatıcıları duraklatmanı, açık "
                                         "tutmanı ya da sana yardım eden biriyle bir bakım listesi paylaşmanı sağlar. "
                                         "Hiçbir şey senin yerine yapıldı diye işaretlenmez; döndüğünde MULA, herkesin "
                                         "nasıl olduğunu görmene yardım eder."),
            ]),
            ("Hatırlatıcılar, widget’lar ve cihazlar", [
                ("Hatırlatıcılar ne zaman gelir?", "“Settings → Reminders & quiet hours” (Ayarlar → Hatırlatıcılar ve "
                                                   "sessiz saatler) bölümünde seçtiğin saatte (varsayılan 09.00) "
                                                   "gelir; asla sessiz saatlerde (varsayılan 22.00–08.00) gelmez ve "
                                                   "aynı bitki için asla günde bir kereden fazla gelmez."),
                ("Uygulamayı açmadan cevap verebilir miyim?", "Evet. Toprak kontrolü hatırlatıcılarında “Dry · I "
                                                              "watered it” (Kuru · Suladım), “A little moist” ve “Wet” "
                                                              "düğmeleri; gübre hatırlatıcılarında “Fed today” (Bugün "
                                                              "gübreledim) ve “Later” (Sonra) düğmeleri vardır. "
                                                              "Premium ile orta ve büyük widget’lardan ve Apple "
                                                              "Watch’tan da cevap verebilirsin."),
                ("Hangi widget’lar var?", "Küçük (sıradaki bitki) ve Kilitli Ekran (dairesel, dikdörtgen ve satır "
                                          "içi); ikisi de ücretsiz. Bunlara ek olarak, cevap düğmeleri Premium olan "
                                          "orta ve büyük widget’lar."),
                ("MULA Siri’yle çalışır mı?", "Evet, hiçbir kurulum gerekmeden: “I watered Momo in MULA”, “What needs "
                                              "care in MULA”, “Soil check for Momo in MULA”, “I fed Momo in MULA”. "
                                              "İfadeler İngilizcedir."),
                ("iPad, Mac ya da Android sürümü var mı?", "iPad ve Mac için evet; Android için şimdilik hayır. Aynı "
                                                           "uygulama iPhone’da (iOS 17 veya üstü), iPad’de (iPadOS "
                                                           "17 veya üstü) ve Apple çipli Mac’lerde çalışır; geniş "
                                                           "ekranda sakin, telefon genişliğinde bir sütun gösterir. "
                                                           "“Sync with iCloud” (iCloud ile eşitle) açıkken her cihaz "
                                                           "aynı bahçeyi gösterir; Premium, “Restore purchases” ile "
                                                           "gelir. Işık ölçer arka kamera gerektirdiği için Mac’te "
                                                           "kullanılamaz."),
                ("Uygulama başka dillerde de var mı?", "Uygulamanın arayüzü şimdilik İngilizce. Bu web sitesi ise "
                                                       "İngilizce, Türkçe ve İspanyolca olarak sunuluyor."),
            ]),
            ("Ücretsiz ve Premium", [
                ("Neler ücretsiz?", "Her biri 5 fotoğraflı 10 bitkiye kadar, tüm toprak kontrolü ve gübre "
                                    "hatırlatıcıları, mevsimlik planları görüntüleme, mevsimlik sıcaklık kontrolü, "
                                    "fotoğrafla tanıma, küçük ve Kilitli Ekran widget’ları, Apple Watch listesi, Siri, "
                                    "iki tema ve sesler."),
                ("Premium neler ekler?", "Sınırsız bitki ve portre, mevsimlik planları düzenleme, fotoğraf günlüğünün "
                                         "tamamı ve posterler, tatil modu ve bakım listeleri, ışık ölçer, don ve sıcak "
                                         "uyarıları, orta/büyük widget’larda ve Apple Watch’ta cevap düğmeleri."),
                ("Premium ne kadar?", "Premium, Yıllık (1 haftalık ücretsiz denemeyle) ya da Ömür Boyu (tek seferlik "
                                      "satın alma) olarak sunulur. Fiyatlar ülkene göre değişir ve satın almadan önce "
                                      "App Store’da gösterilir."),
                ("Nasıl iptal eder ya da geri yüklerim?", "Yıllık planı dilediğin zaman, yenilenmeden en az 24 saat "
                                                          "önce iPhone’unun Ayarlar → [adın] → Abonelikler "
                                                          "bölümünden iptal et. Bir satın alımı geri yüklemek için "
                                                          "MULA’da “Settings → MULA Premium → Restore purchases” "
                                                          "(Ayarlar → MULA Premium → Satın alımları geri yükle) "
                                                          "yolunu izle."),
                ("Reklam var mı?", "Hayır. Ne ücretsiz sürümde ne de Premium’da; asla."),
            ]),
            ("Gizlilik ve veriler", [
                ("Bahçem nerede saklanıyor?", "iPhone’unda (ya da iPad’inde veya Mac’inde); MULA’nın kendi widget’ları ve Apple Watch uygulamasıyla "
                                              "paylaşılır, ayrıca yalnızca senin görebildiğin kendi iCloud’un "
                                              "üzerinden yedeklenir ve eşitlenir. MULA hesabı ya da MULA sunucusu "
                                              "yok."),
                ("MULA analiz verisi topluyor mu?", "Yalnızca anonim kullanım istatistikleri, Google Analytics for "
                                                    "Firebase aracılığıyla: hangi ekranların açıldığı, hangi bakımın "
                                                    "kaydedildiği ve bir bahçede kaç bitki olduğu gibi. Bitki adları, "
                                                    "notlar, fotoğraf açıklamaları ya da fotoğraflar asla gönderilmez; "
                                                    "reklam kimliği ve takip de yok. “Settings → Your garden → Share "
                                                    "anonymous usage” (Ayarlar → Bahçen → Anonim kullanımı paylaş) "
                                                    "bölümünden kapatabilirsin."),
                ("MULA konumumu neden istiyor?", "Yalnızca don ve sıcak uyarılarını (Premium) açarsan. Yaklaşık konumun "
                                                 "1 km kadar yuvarlanır, iPhone’unda saklanır ve hava tahmini için "
                                                 "Apple Weather’a yalnızca bu yuvarlanmış nokta gönderilir."),
                ("Işık ölçerin fotoğrafları kaydediliyor mu?", "Hayır. Işık ölçer, lüksü tahmin etmek için kameranın "
                                                               "pozlamasını okur; fotoğraf çekilmez ya da saklanmaz."),
                ("Bahçemi yeni bir iPhone’a nasıl taşırım?", "Aynı Apple Hesabıyla giriş yap ve MULA’yı yükle. "
                                                             "Bahçen iCloud’a yedeklendiyse (“Settings → iCloud "
                                                             "backup”, varsayılan olarak açık), MULA tanıtımdan önce "
                                                             "onu bakım geçmişi, fotoğrafları ve ayarlarıyla geri "
                                                             "getirmeyi önerir. Premium, “Restore purchases” "
                                                             "(Satın alımları geri yükle) ile geri gelir."),
                ("MULA’yı birden fazla cihazda kullanabilir ya da bahçemi paylaşabilir miyim?", "Evet. “Sync with "
                                                             "iCloud” (iCloud ile eşitle) açıkken (“Settings → Sync & "
                                                             "sharing”, Ayarlar → Eşitleme ve paylaşım), Apple "
                                                             "Hesabınla giriş yapılmış her cihaz aynı bahçeyi gösterir. "
                                                             "Premium ile bahçeni partnerin ya da ev arkadaşınla da "
                                                             "paylaşabilirsin; biriniz sulayınca diğerinin "
                                                             "hatırlatıcısı sessizce kaybolur."),
            ]),
        ],
    },

    # ------------------------------------------------------------------ support
    "support": {
        "title": "Bitki sulama hatırlatıcı MULA: destek ve yardım",
        "description": "Bitki sulama hatırlatıcı MULA için yardım: gelmeyen hatırlatıcılar, widget’lar, Apple Watch, "
                       "don uyarıları, ışık ölçer, Premium’u geri yükleme ve yeni iPhone.",
        "kicker": "Destek",
        "h1": "Nasıl yardımcı olabiliriz?",
        "lead": "Dilediğin zaman {email} adresine yaz. Lütfen iPhone modelini ve iOS sürümünü de belirt. Çoğu soru iki "
                "iş günü içinde cevaplanır.",
        "write": "Destek için e-posta gönder",
        "write_subject": "MULA destek",
        "faq_link": "SSS’yi oku",
        "h_fix": "Hızlı çözümler",
        "fixes": [
            ("Hatırlatıcılar gelmiyor", "<ul><li>iPhone’da Ayarlar → Bildirimler → MULA bölümünde bildirimlere izin "
                                        "verildiğini kontrol et.</li><li>MULA’da “Settings → Reminders & quiet hours” "
                                        "(Ayarlar → Hatırlatıcılar ve sessiz saatler) bölümünü aç; anahtarları ve "
                                        "hatırlatma saatini kontrol et.</li><li>Hatırlatıcılar asla sessiz saatlerde "
                                        "gelmez ve her bitki için günde yalnızca bir kez gelir.</li><li>Odak modları "
                                        "bildirimleri bekletebilir; Odak ayarlarında MULA’ya izin ver.</li><li>Saat "
                                        "dilimini değiştirdikten sonra hatırlatıcıların yeniden kurulması için "
                                        "MULA’yı bir kez aç.</li></ul>"),
            ("Widget düğmeleri cevap vermiyor", "<p>Orta ve büyük widget’lardaki cevap düğmeleri MULA Premium’un "
                                                "parçasıdır. Bir düğme, yalnızca o görev hâlâ bekliyorsa cevap "
                                                "kaydeder; başka bir yerden zaten cevap verdiysen hiçbir şey yapmaz. "
                                                "Widget güncel görünmüyorsa kaldırıp yeniden ekle.</p>"),
            ("Apple Watch hiçbir şey göstermiyor", "<p>Güncel listeyi saate gönderebilmesi için MULA’yı iPhone’unda "
                                                   "bir kez aç. iPhone yakında değilse saatten verilen cevaplar bekler "
                                                   "ve iPhone yakına geldiğinde uygulanır. Saatten cevap vermek "
                                                   "Premium’dur.</p>"),
            ("Don ve sıcak uyarıları", "<p>Bunlar için MULA Premium, yaklaşık konum izni ve Apple Weather için "
                                       "internet bağlantısı gerekir. Uyarılar yalnızca “Balcony” (Balkon) ya da "
                                       "“Outdoor” (Dış mekân) olarak ayarlanmış bitkiler içindir. Son güncellemenin "
                                       "saatini “Settings → Reminders & quiet hours” bölümünde görebilirsin.</p>"),
            ("Işık ölçer tuhaf değerler gösteriyor", "<p>iPhone’u bitkinin yaşayacağı yerde, arka kamera pencereye "
                                                     "bakacak şekilde tut ve ölçümün oturması için bir an bekle. "
                                                     "Okunan değer bir tahmindir; eşikler (yaklaşık 800 ve 10.000 "
                                                     "lüks) kesin bilim değil, kaba ölçütlerdir.</p>"),
            ("Premium’u geri yükle", "<p>Satın alırken kullandığın Apple ID ile oturum açmışken “Settings → MULA "
                                     "Premium → Restore purchases” (Ayarlar → MULA Premium → Satın alımları geri yükle) "
                                     "yolunu izle. İadeler Apple tarafından <a href=\"https://reportaproblem"
                                     ".apple.com\" rel=\"noopener\">reportaproblem.apple.com</a> adresinde ele "
                                     "alınır.</p>"),
            ("Yeni iPhone", "<p>Aynı Apple Hesabıyla iCloud’a giriş yap ve MULA’yı yükle. Bahçen yedeklendiyse "
                            "(“Settings → iCloud backup”, Ayarlar → iCloud yedeği), MULA tanıtımdan önce onu geri "
                            "yüklemeyi önerir. Daha sonra da aynı ekrandan geri yükleyebilirsin. Premium, “Settings "
                            "→ MULA Premium → Restore purchases” (Satın alımları geri yükle) ile geri gelir.</p>"),
            ("Her şeyi sil", "<p>MULA uygulamasını silmek bitkilerini, fotoğraflarını ve geçmişini iPhone’dan "
                             "kaldırır. iCloud yedeğin ve eşitlenen bahçen kendi iCloud’unda kalır, böylece geri "
                             "gelebilir; bunları kaldırmak için iPhone’unun Ayarlar → adın → iCloud depolama "
                             "bölümünden MULA’nın verilerini sil. Bende saklanan, silinecek hiçbir şey yok.</p>"),
        ],
        "h_contact": "İletişim",
        "contact": "<p>E-posta: <a href=\"mailto:{email}\">{email}</a><br>Instagram: <a href=\"https://www.instagram.com"
                   "/solo.stasera/\" rel=\"noopener\">@solo.stasera</a><br>Geliştirici: Gül Eda Aydemir</p>",
    },

    # ------------------------------------------------------------------ privacy
    "privacy": {
        "title": "MULA gizlilik politikası: reklamsız, hesapsız, iPhone’unda",
        "description": "MULA gizlilik politikası: reklam, hesap, takip yok. Bitkilerin, fotoğrafların ve geçmişin "
                       "iPhone’unda kalır; yalnızca anonim kullanım istatistikleri Google Analytics for Firebase’e "
                       "gönderilir.",
        "kicker": "Gizlilik",
        "h1": "Gizlilik politikası",
        "lead": "Kısaca: MULA bahçeni iPhone’unda tutar. Hesap, sunucu, reklam ya da takip yok. MULA anonim kullanım "
                "istatistikleri gönderir (Google Analytics for Firebase); bitkilerinin adlarını, notlarını ya da "
                "fotoğraflarını asla. Bunu ayarlardan kapatabilirsin. Don ve sıcak uyarıları, yalnızca açarsan, "
                "Apple Weather’a yuvarlanmış bir konum gönderir.",
        "effective": "Yürürlük tarihi",
        "badges": ["Reklam yok", "Hesap yok", "Takip yok", "Yalnızca anonim istatistik", "Bahçe iPhone’unda"],
        "sections": [
            ("1. Biz kimiz", "<p>MULA: Plant Care (“MULA”, “uygulama”), bağımsız bir geliştirici olan Gül Eda Aydemir "
                             "(“ben”) tarafından yapılmıştır. Bu politika; iPhone, iPad, Mac ve Apple Watch için MULA "
                             "uygulamasını, widget’larını ve bu web sitesini kapsar. Sorular için: "
                             "<a href=\"mailto:{email}\">{email}</a>.</p>"),
            ("2. Uygulama neleri, nerede saklar", "<p>Uygulama; bitkilerini (adları, türleri, nerede yaşadıkları, "
                                                  "ışık durumları), bakım planlarını, bakım geçmişini, günlük "
                                                  "fotoğraflarını ve notlarını ve ayarlarını saklar. Bunlar "
                                                  "<strong>iPhone’unda</strong>, MULA’nın kendi widget’ları ve Apple "
                                                  "Watch uygulamasıyla paylaşılan bir kapsayıcıda saklanır. MULA’nın "
                                                  "hesabı ve kendine ait sunucusu yoktur; bu verilerin hiçbirini "
                                                  "göremem.</p><ul><li><strong>iCloud yedeği</strong> (varsayılan "
                                                  "olarak açık): MULA bahçeni, fotoğraflar dahil, kendi iCloud’undaki "
                                                  "özel alanına yedekler; böylece yeni bir iPhone’da ya da MULA "
                                                  "silindikten sonra geri gelebilir. Onu yalnızca sen görebilirsin. "
                                                  "“Settings → iCloud backup” (Ayarlar → iCloud yedeği) bölümünden "
                                                  "kapatabilirsin.</li><li><strong>iCloud ile eşitleme</strong> "
                                                  "(varsayılan olarak açık): Apple Hesabınla giriş yapılmış "
                                                  "cihazlar, Apple’ın CloudKit hizmeti aracılığıyla özel iCloud "
                                                  "veritabanında aynı bahçeyi gösterir. “Settings → Sync & sharing” "
                                                  "(Ayarlar → Eşitleme ve paylaşım) bölümünden kapatabilirsin.</li>"
                                                  "<li><strong>Ortak bahçe</strong> (yalnızca birini davet edersen "
                                                  "ya da bir daveti kabul edersen): içindeki kişiler aynı bitkileri, "
                                                  "bakım geçmişini ve fotoğrafları, iCloud’un gösterdiği şekliyle de "
                                                  "birbirlerinin adlarını görür. Ayrılan kişi bitkilerin bir "
                                                  "kopyasını tutar.</li></ul><p>Yedekleme ve eşitleme için iCloud’a "
                                                  "giriş yapmış olman gerekir. iCloud Apple’ın hizmetidir ve Apple’ın "
                                                  "<a href=\"https://www.apple.com/legal/privacy/\" rel=\"noopener\">gizlilik politikası</a> kapsamında çalışır. Kullanıyorsan bahçen "
                                                  "iPhone’unun kendi yedeklerine de dahil edilir.</p>"),
            ("3. Anonim kullanım istatistikleri", "<p>MULA’nın nasıl kullanıldığını anlamak ve onu geliştirmek için "
                                                 "uygulama, Google’ın bir hizmeti olan <strong>Google "
                                                 "Analytics for Firebase</strong>’e anonim kullanım istatistikleri "
                                                 "gönderir:</p><ul><li>hangi ekranların açıldığı, hangi bakımın "
                                                 "kaydedildiği ya da ertelendiği (örneğin “sulandı” ya da “hâlâ "
                                                 "nemli”) ve bunun nereden yapıldığı (uygulama, hatırlatma, widget, "
                                                 "Apple Watch ya da Siri);</li><li>sözlerin değil, yalnızca "
                                                 "kategoriler ve sayılar: bir bitkinin MULA kataloğundaki türü, "
                                                 "nerede yaşadığı ve ışığı, bir bahçede kaç bitki, fotoğraf ve bakım "
                                                 "kaydı olduğu, hangi ayarların açık ya da kapalı olduğu ve hangi "
                                                 "özelliklerin kullanıldığı;</li><li>MULA Premium ile ilgili "
                                                 "adımlar: teklifin ne zaman gösterildiği, hangi planın seçildiği ve "
                                                 "satın alma, ücretsiz deneme, iptal ya da iade olup olmadığı (adın "
                                                 "ya da ödeme bilgilerin asla);</li><li>Firebase’in otomatik "
                                                 "topladığı temel teknik bilgiler: cihaz modeli, iOS ve uygulama "
                                                 "sürümü, dil, rastgele bir uygulama kurulum kimliği ve IP adresinden "
                                                 "çıkarılan yaklaşık bölge.</li></ul><p>MULA bitkilerinin adlarını, "
                                                 "notlarını, fotoğraf açıklamalarını, sana yardım eden kişinin adını, "
                                                 "fotoğraflarını ya da yazdığın başka hiçbir şeyi asla göndermez. Bu "
                                                 "istatistikler adına, e-postana ya da Apple Hesabına bağlanmaz. MULA "
                                                 "reklam kimliğini (IDFA) kullanmaz, reklam kişiselleştirmesini kapatır "
                                                 "ve seni başka şirketlerin uygulamaları ya da web siteleri arasında "
                                                 "takip etmez. Google bu verileri benim adıma, <a href=\"https://"
                                                 "firebase.google.com/support/privacy\" rel=\"noopener\">Firebase "
                                                 "gizlilik koşulları</a> kapsamında işler ve yalnızca sınırlı bir süre "
                                                 "saklar. Hiçbir şey satılmaz ya da veri aracılarıyla paylaşılmaz."
                                                 "</p><p><strong>Kapatmak için</strong> “Settings → Your garden” "
                                                 "(Ayarlar → Bahçen) bölümünü aç ve “Share anonymous usage” (Anonim "
                                                 "kullanımı paylaş) seçeneğini kapat. MULA istatistik göndermeyi "
                                                 "bırakır ve iPhone’undaki analiz verilerini temizler. MULA’da hesap "
                                                 "olmadığı için adını, e-postanı ya da telefon numaranı asla istemez; "
                                                 "reklam ya da çökme raporlama aracı da yoktur.</p>"),
            ("4. İzinler", "<ul><li><strong>Bildirimler</strong>: seçtiğin hatırlatıcıları iletmek için. Bunlar iOS "
                           "tarafından cihazda yerel olarak planlanır.</li><li><strong>Kamera</strong>: bitki "
                           "fotoğrafı çekmek ve ışık ölçer için kameranın pozlamasını okumak üzere. Işık ölçümleri "
                           "asla kaydedilmez ve bunlar için fotoğraf çekilmez.</li><li><strong>Fotoğraflar</strong>: "
                           "sistemin fotoğraf seçicisi aracılığıyla MULA’ya yalnızca senin seçtiğin fotoğraflar "
                           "verilir.</li><li><strong>Yaklaşık konum (uygulama kullanılırken)</strong>: yalnızca don ve "
                           "sıcak uyarılarını açarsan.</li></ul><p>Her izni iOS Ayarlar’dan "
                           "değiştirebilirsin.</p>"),
            ("5. Don ve sıcak uyarıları (Apple Weather)", "<p>Hava uyarılarını (MULA Premium) açarsan MULA yaklaşık "
                                                          "konumunu bir kez ister, bunu yaklaşık 1 km’ye yuvarlar ve "
                                                          "iPhone’unda saklar. Hava tahminini almak için Apple’ın "
                                                          "WeatherKit hizmetine yalnızca bu yuvarlanmış nokta "
                                                          "gönderilir. Apple bu isteği kendi <a href=\"https://www."
                                                          "apple.com/legal/privacy/\" rel=\"noopener\">gizlilik "
                                                          "politikası</a> kapsamında işler. Uyarıları kapatırsan hiçbir "
                                                          "istek yapılmaz.</p>"),
            ("6. Cihaz üzerindeki özellikler", "<p>Fotoğrafla tanıma, iPhone’unda Apple’ın görüntü tanıma "
                                               "teknolojisini kullanır; fotoğraf cihazdan asla çıkmaz. Işık ölçer de "
                                               "cihazda çalışır.</p>"),
            ("7. Satın alımlar", "<p>MULA Premium, Apple’ın App Store’u üzerinden satılır. Ödemeyi Apple işler; ödeme "
                                 "bilgilerini ben asla görmem. Uygulama, Premium’un kilidini açmak için satın alımını "
                                 "Apple’la (StoreKit) doğrular.</p>"),
            ("8. Diğer uygulamalara bağlantılar", "<p>“Settings → Grow further” (Ayarlar → Büyümeye devam), diğer "
                                                  "uygulamalarımın (Solo.Shots ve Solora gibi) App Store sayfalarını "
                                                  "açabilir. Bahçenle ilgili hiçbir bilgi onlara aktarılmaz.</p>"),
            ("9. Çocuklar", "<p>MULA genel kitleye yönelik bir uygulamadır. Çocuklar dahil hiç kimseden kişisel bilgi "
                            "istemez. 3. bölümde anlatılan anonim kullanım istatistikleri herkes için aynıdır ve "
                            "kimseyi tanımlamak için kullanılmaz.</p>"),
            ("10. Verilerin saklanması ve silinmesi", "<p>Verilerin, sen silene kadar kalır. Silinen bir bitki 30 gün "
                                                      "“Settings → Recently deleted” (Son silinenler) bölümünde "
                                                      "bekler, sonra kaldırılır. Uygulamayı silmek MULA’nın iPhone’da "
                                                      "sakladığı her şeyi kaldırır; iCloud yedeğin ve eşitlenen "
                                                      "bahçen ise iOS Ayarlar → adın → iCloud depolama bölümünden "
                                                      "MULA’nın verilerini silene kadar iCloud’unda kalır. Bahçen bana hiçbir zaman ulaşmaz. Kurulumuna "
                                                      "ait anonim kullanım istatistiklerinin silinmesini istersen "
                                                      "“Share anonymous usage” seçeneğini kapat ve bana e-posta "
                                                      "gönder. Bana e-posta gönderirsen yazışmayı "
                                                      "yalnızca sana yardım etmek için saklarım ve talep edersen "
                                                      "silerim.</p>"),
            ("11. Bu web sitesi", "<p>Bu web sitesinde çerez, analiz ya da reklam yoktur; üçüncü taraf yazı tipi ya da "
                                  "betik yüklenmez. Site GitHub Pages üzerinde barındırılır; GitHub Pages güvenlik "
                                  "amacıyla IP adresleri gibi teknik verileri kaydedebilir. Site, birkaç küçük "
                                  "tercihini kendi tarayıcı depolamanda hatırlar (kâğıt havası, işaretlediğin kontrol "
                                  "listesi maddeleri, kapattığın bir dil ipucu ve girişi görüp görmediğin); bunlar "
                                  "tarayıcından asla çıkmaz.</p>"),
            ("12. Hakların", "<p>Sana uygulanan yasaların, örneğin 6698 sayılı Kişisel Verilerin Korunması Kanunu’nun "
                             "(KVKK) ya da AB Genel Veri Koruma Tüzüğü’nün (GDPR) tanıdığı haklara sahipsin. MULA "
                             "adını ya da iletişim bilgilerini toplamaz ve kullanım istatistikleri anonimdir; bu "
                             "yüzden genellikle erişilecek ya da düzeltilecek bir şey olmaz, "
                             "ama bana her zaman yazabilirsin.</p>"),
            ("13. Değişiklikler", "<p>Bu politika değişirse yeni sürüm, yeni bir yürürlük tarihiyle bu sayfada "
                                  "yayımlanır.</p>"),
        ],
    },

    # ------------------------------------------------------------------ terms
    "terms": {
        "title": "MULA kullanım koşulları: bitki bakım uygulaması",
        "description": "MULA: Plant Care kullanım koşulları; Premium abonelikleri, 1 haftalık ücretsiz deneme, Ömür "
                       "Boyu satın alma ve uygulamadaki bitki bakım bilgileri dahil.",
        "kicker": "Koşullar",
        "h1": "Kullanım koşulları",
        "lead": "Sakin bir uygulama için sade koşullar. MULA, bu koşullarla birlikte Apple’ın standart EULA’sı "
                "kapsamında lisanslanır.",
        "effective": "Yürürlük tarihi",
        "sections": [
            ("1. Sözleşme", "<p>MULA, bu koşullarla birlikte Apple’ın <a href=\"https://www.apple.com/legal/"
                            "internet-services/itunes/dev/stdeula/\" rel=\"noopener\">Lisanslı Uygulama Son Kullanıcı "
                            "Lisans Sözleşmesi</a> (standart EULA) kapsamında sana lisanslanır. MULA’yı kullanarak her "
                            "ikisini de kabul etmiş olursun.</p>"),
            ("2. MULA nedir", "<p>MULA, bitki bakımı için bir hatırlatıcı ve günlük aracıdır. Bakım planları, aralıklar "
                              "ve sıcaklık aralıkları, değiştirebileceğin genel başlangıç noktalarıdır. Profesyonel "
                              "bahçecilik tavsiyesi değildir ve MULA zararlıları, hastalıkları ya da bitki sağlığını "
                              "teşhis edemez. Fotoğrafla tanıma ve ışık ölçümleri birer tahmindir.</p>"),
            ("3. MULA Premium", "<ul><li>Premium, uygun kullanıcılar için <strong>1 haftalık ücretsiz deneme</strong> "
                                "içeren ve otomatik olarak yenilenen <strong>Yıllık</strong> abonelik ya da tek "
                                "seferlik <strong>Ömür Boyu</strong> satın alma olarak sunulur. Fiyatlar satın almadan "
                                "önce App Store’da gösterilir.</li><li>Ödeme, satın alma onaylandığında (Yıllık planda "
                                "ücretsiz deneme sona erdiğinde) Apple ID hesabından tahsil edilir.</li><li>Abonelik, "
                                "geçerli dönemin bitiminden en az 24 saat önce iptal edilmedikçe otomatik olarak "
                                "yenilenir; yenileme ücreti dönemin bitiminden önceki 24 saat içinde tahsil "
                                "edilir.</li><li>Aboneliğini iPhone’unun Ayarlar → [adın] → Abonelikler bölümünden "
                                "yönet ya da iptal et.</li><li>Bir abonelik satın aldığında ücretsiz denemenin "
                                "kullanılmayan kısmı sona erer.</li><li>İadeler Apple tarafından kendi politikalarına "
                                "göre ele alınır.</li></ul>"),
            ("4. Hava durumu verileri", "<p>Don ve sıcak uyarıları Apple Weather’ın tahmin verilerini kullanır. "
                                        "Tahminler yanlış olabilir; risk altındaki bitkiler için lütfen kendi "
                                        "değerlendirmeni de kullan. Apple Weather işareti ve veri kaynakları "
                                        "uygulamada gösterilir.</p>"),
            ("5. İçeriğin", "<p>Bitkilerin, fotoğrafların ve notların sana aittir. Cihazında ve iCloud yedeği ya da "
                            "eşitleme kullanıyorsan kendi iCloud’unda kalır; bende bir kopyası yoktur. Yedekleme, "
                            "örneğin iCloud doluysa ya da kapalıysa başarısız olabilir; bu yüzden kendi "
                            "yedeklerini de al.</p>"),
            ("6. Kullanılabilirlik", "<p>MULA’nın iyi çalışması için emek veriyorum ama her zaman hatasız olacağını "
                                     "garanti edemem. Özellikler zamanla değişebilir.</p>"),
            ("7. Sorumluluk", "<p>Yasaların izin verdiği ölçüde MULA “olduğu gibi” sunulur ve kullanımından kaynaklanan "
                              "bitki ya da veri kaybından veya diğer dolaylı zararlardan sorumlu değilim.</p>"),
            ("8. İletişim", "<p>Bu koşullarla ilgili sorular için: <a href=\"mailto:{email}\">{email}</a>.</p>"),
        ],
    },

    # ------------------------------------------------------------------ species (site only; not in en.py)
    "species": {
        "monstera": {"common": "Deve tabanı", "tips": [
            "Yeni yapraklar yolda. Ayda bir gübrele, toprağı hafif nemli tut.",
            "Aydınlık, dolaylı ışık ve haftada bir toprak kontrolüyle yapraklar yarılmaya devam eder.",
            "Daha seyrek sula, gübreye marta kadar ara ver. 15°C’nin üzerinde tut.",
            "Dinlenme zamanı. Toprağın üstü kurusun; soğuk camlardan uzak tut.",
        ]},
        "camellia": {"common": "Kamelya", "tips": [
            "Çiçeklenmeden sonra asidik bir gübreyle besle ve hafifçe buda.",
            "Toprağı eşit biçimde nemli tut, öğle güneşinden koru.",
            "Toprağı eşit biçimde nemli tut, saksının yerini değiştirme.",
            "Çiçek zamanı. Tomurcukları ve çiçekleri dondan koru.",
        ]},
        "ficus": {"common": "Kauçuk", "tips": [
            "Yeni bir kırmızı kın, yeni bir yaprak demek. Ayda bir gübrele.",
            "Yaprakları sil, toprağı her hafta kontrol et.",
            "Daha seyrek sula. Bu dönemde yerinin değişmesini sevmez.",
            "Hava akımından uzak tut, toprağın yarısına kadar kurumasını bekle.",
        ]},
        "hydrangea": {"common": "Ortanca", "tips": [
            "Tomurcuklar kabarıyor. Gübrelemeye başla, saksının kurumasına asla izin verme.",
            "Sıcakta çok su içer. Toprağı iki günde bir kontrol et.",
            "Çiçekler soluyor. Gübrelemeyi bırak, daha az sula.",
            "Uykuda ve dayanıklı. Koruması için eski çiçek başlarını yerinde bırak.",
        ]},
        "orchid": {"common": "Orkide", "tips": [
            "Kökler gümüşi renge dönünce sula. İki haftada bir hafif gübre ver.",
            "Doğrudan güneşten uzak tut, sıcak günlerde köklerine su püskürt.",
            "Serin geceler yeni bir çiçek sapı çıkarmasına yardım eder.",
            "Sabahları az sula, soğuk pencere önlerinden uzak tut.",
        ]},
        "pilea": {"common": "Çin para bitkisi", "tips": [
            "Dengeli büyümesi için saksıyı her hafta biraz çevir.",
            "Toprağı sık sık kontrol et; sarkan yapraklar su istiyor demektir.",
            "Suyu azalt, gübrelemeyi bırak.",
            "İki sulama arasında toprağın üstteki üçte birinin kurumasını bekle.",
        ]},
        "sansevieria": {"common": "Paşa kılıcı"},
        "spathiphyllum": {"common": "Barış çiçeği"},
        "pothos": {"common": "Salon sarmaşığı"},
        "lavender": {"common": "Lavanta"},
        "aloe": {"common": "Aloe vera"},
        "rose": {"common": "Gül"},
        "tulip": {"common": "Lale"},
        "cactus": {"common": "Kaktüs"},
        "fern": {"common": "Boston eğreltisi"},
        "ivy": {"common": "Sarmaşık"},
        "begonia": {"common": "Begonya"},
        "poinsettia": {"common": "Atatürk çiçeği"},
        "rosemary": {"common": "Biberiye"},
        "palm": {"common": "Areka palmiyesi"},
    },
}
