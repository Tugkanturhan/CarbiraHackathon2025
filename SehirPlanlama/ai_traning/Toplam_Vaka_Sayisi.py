import psycopg2
#bu mahallelerdeki nufus sayisini bulan kod
def veritabanindan_mahalle_nufuslarini_cek():
    try:
        # Veritabanı bağlantı bilgileri
        conn = psycopg2.connect("host=localhost port=5432 user=postgres password=123456 connect_timeout=10 sslmode=prefer")


        cur = conn.cursor()

        # Mahalle ve nüfusları seç
        cur.execute("SELECT mahalle_adı, nufus FROM mahalleler")
        veriler = cur.fetchall()

        # Verileri listeye ayır
        mahalleler = []
        nufuslar = []

        for mahalle_adı, nufus in veriler:
            mahalleler.append(mahalle_adı)
            nufuslar.append(nufus)

        toplam_nufus = sum(nufuslar)
        print(f"Toplam Nüfus: {toplam_nufus}")

        cur.close()
        conn.close()

        return mahalleler, nufuslar, toplam_nufus

    except Exception as e:
        print("Veritabanı bağlantı hatası:", e)

# Fonksiyonu çağır ve test et
mahalleler, nufuslar, toplam_nufus = veritabanindan_mahalle_nufuslarini_cek()


