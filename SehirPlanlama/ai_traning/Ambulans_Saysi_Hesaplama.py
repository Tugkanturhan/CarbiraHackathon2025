import psycopg2

def ambulans_dagilimi_ve_guncelle(toplam_ambulans):
    try:
        # Bağlantı
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            
            user="postgres",
            password="123456"
        )
        cur = conn.cursor()

        # Hastane verilerini al
        cur.execute("SELECT id, ad, yatak_sayisi FROM hastaneler")
        hastaneler = cur.fetchall()

        # Toplam yatak sayısını hesapla
        toplam_yatak = sum(h[2] for h in hastaneler)

        # Her hastane için ambulans hesapla ve güncelle
        for id_, ad, yatak in hastaneler:
            oran = yatak / toplam_yatak
            ambulans = round(oran * toplam_ambulans)

            # Güncelle
            cur.execute(
                "UPDATE hastaneler SET ambulans_sayisi = %s WHERE id = %s",
                (ambulans, id_)
            )
            print(f"{ad}: {yatak} yatak → {ambulans} ambulans")

        # Değişiklikleri kaydet
        conn.commit()

        # Bağlantıyı kapat
        cur.close()
        conn.close()

    except Exception as e:
        print("Veritabanı bağlantı veya işlem hatası:", e)

# Kullanım
ambulans_dagilimi_ve_guncelle(86)
