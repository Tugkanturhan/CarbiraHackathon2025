import pandas as pd
import random

# 1. Veriyi oku (tam yol ile)
df = pd.read_csv(r'D:/SehirPlanlama/ai_traning/dataset/mahaller.csv')

# 2. Nüfus artışı fonksiyonu
def generate_nufus_artisi(mevcut_nufus, artis_orani=0.02, noise_ratio=0.1):
    artis = mevcut_nufus * artis_orani
    noise = random.uniform(-noise_ratio, noise_ratio)
    artis = artis * (1 + noise)
    yeni_nufus = mevcut_nufus + artis
    return max(0, round(yeni_nufus))

# 3. Zaman serisi oluşturma (5 yıl için)
def generate_nufus_time_series(df, years=5, artis_orani=0.02, noise_ratio=0.1):
    records = []
    for year_offset in range(years):
        yil = 2019 + year_offset
        for _, row in df.iterrows():
            if year_offset == 0:
                nufus = row['nufus']
            else:
                onceki_nufus = [r['nufus'] for r in records if r['mahalle'] == row['mahalle_adi'] and r['yil'] == yil-1][0]
                nufus = generate_nufus_artisi(onceki_nufus, artis_orani, noise_ratio)
            records.append({
                'mahalle': row['mahalle_adi'],
                'yil': yil,
                'nufus': nufus
            })
    return pd.DataFrame(records)

# 4. Veriyi üret
df_nufus_timeseries = generate_nufus_time_series(df)

# 5. Yeni dosyaya kaydet
df_nufus_timeseries.to_csv(r'D:/SehirPlanlama/ai_traning/dataset/artirilmis_dataset/artirilmis_mahaller.csv', index=False)

print("Nüfus artışı zaman serisi başarıyla oluşturuldu!")
print(df_nufus_timeseries.head(15))
