from flask import Blueprint, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

kullanici_bp = Blueprint('kullanici_bp', __name__, url_prefix='/api/kullanici')

# Veritabanı bağlantısı ayarları
DB_HOST = "localhost"
DB_NAME = "veritabani_adi"
DB_USER = "kullanici_adi"
DB_PASS = "sifre"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=5432
    )
    return conn

@kullanici_bp.route('', methods=['GET'])
def kullanici_giris():
    try:
        data = request.json
        tc_kimlik = data.get('tc_kimlik')
        sifre = data.get('sifre')

        if not tc_kimlik or not sifre:
            return jsonify({"error": "tc_kimlik ve sifre gerekli"}), 400

        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT sifre, ad_soyad, roller FROM users WHERE tc_kimlik = %s"
        cur.execute(query, (tc_kimlik,))
        kullanici = cur.fetchone()
        cur.close()
        conn.close()

        if not kullanici:
            return jsonify({"error": "Kullanıcı bulunamadı"}), 404

        # Basit şifre kontrolü (üretim için hash kullan)
        if sifre != kullanici['sifre']:
            return jsonify({"error": "Şifre yanlış"}), 401

        # Başarılı giriş
        return jsonify({
            "ad_soyad": kullanici['ad_soyad'],
            "roller": kullanici['roller']
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
