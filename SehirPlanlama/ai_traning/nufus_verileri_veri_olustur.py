import pandas as pd
import random

df = pd.read_csv('D:/SehirPlanlama/ai_traning/dataset/nufus_verileri.csv')

def arti_nufus(df):
    yeni_satirlar = []
    for _, row in df.iterrows():
        mevcut_nufus = row['nufus']
        artis_orani = random.uniform(0.01, 0.05)
        yeni_nufus = int(mevcut_nufus * (1 + artis_orani))
        yeni_satir = row.copy()
        yeni_satir['yil'] = row['yil'] + 1
        yeni_satir['nufus'] = yeni_nufus
        yeni_satirlar.append(yeni_satir)
    df_yeni = pd.DataFrame(yeni_satirlar)
    df_artirilmis = pd.concat([df, df_yeni], ignore_index=True)
    return df_artirilmis

df_artirilmis = arti_nufus(df)
df_artirilmis.to_csv('D:/SehirPlanlama/ai_traning/dataset/artirilmis_dataset/nufus_verileri_artirilmis.csv', index=False)
print('Nüfus verileri artırıldı ve kaydedildi.')
