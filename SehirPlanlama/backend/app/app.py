from flask import Flask
import sys
import os

# backend klasörünü sys.path'e ekle
sys.path.append(os.path.dirname(__file__))

from api.endpoints.kullanici import kullanici_bp

app = Flask(__name__)

app.register_blueprint(kullanici_bp)

if __name__ == '__main__':
    app.run(debug=True)
