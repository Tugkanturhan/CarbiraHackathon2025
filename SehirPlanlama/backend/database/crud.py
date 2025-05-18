import json
import os

# data.json dosyasının yolunu belirle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "database", "data.json")

# Veriyi oku
def read_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Veriyi yaz
def write_data(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Belirli bir bölümü getir
def get_section(section):
    data = read_data()
    return data.get(section, {})

# Belirli bir bölümü güncelle (tamamını)
def update_section(section, new_data):
    data = read_data()
    data[section] = new_data
    write_data(data)
    return new_data

# Liste olan bir bölüme öğe ekle
def add_item(section, item):
    data = read_data()
    if section not in data:
        data[section] = []
    data[section].append(item)
    write_data(data)
    return item

# Liste olan bir bölümdeki belirli bir öğeyi güncelle
def update_item(section, index, new_item):
    data = read_data()
    if section in data and 0 <= index < len(data[section]):
        data[section][index] = new_item
        write_data(data)
        return new_item
    raise IndexError("Geçersiz indeks")

# Liste olan bir bölümdeki öğeyi sil
def delete_item(section, index):
    data = read_data()
    if section in data and 0 <= index < len(data[section]):
        item = data[section].pop(index)
        write_data(data)
        return item
    raise IndexError("Geçersiz indeks")
