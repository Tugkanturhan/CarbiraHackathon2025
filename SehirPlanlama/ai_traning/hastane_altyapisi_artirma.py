import pandas as pd
import numpy as np

df = pd.read_csv('hastane_altyapi.csv')

# Örnek olarak yatak ve ambulans sayılarının ortalaması ve std'si
yatak_mean = df['yatak_sayisi'].mean()
yatak_std = df['yatak_sayisi'].std()

ambulans_mean = df['ambulans_sayisi'].mean()
ambulans_std = df['ambulans_sayisi'].std()

# Yeni veri üretmek için fonksiyon
def yeni_veri_uret(df, n):
    yeni_veriler = []
    max_altyapi_id = df['hastane_altyapi_id'].max()
    max_hastane_id = df['hastane_id'].max()

    for i in range(1, n+1):
        altyapi_id = max_altyapi_id + i
        hastane_id = np.random.randint(1, max_hastane_id + 1)
        
        yatak = int(np.random.normal(yatak_mean, yatak_std))
        yatak = max(1, yatak)  # negatif olmasın

        ambulans = int(np.random.normal(ambulans_mean, ambulans_std))
        ambulans = max(0, ambulans)  # negatif olmasın

        # ambulans sayısı yatak sayısına göre çok büyük olmasın (örnek kural)
        if ambulans > yatak * 0.1:
            ambulans = int(yatak * 0.1)

        yeni_veriler.append({
            'hastane_altyapi_id': altyapi_id,
            'hastane_id': hastane_id,
            'yatak_sayisi': yatak,
            'ambulans_sayisi': ambulans
        })
    return pd.DataFrame(yeni_veriler)

df_yeni = yeni_veri_uret(df, 10)
df_artirilmis = pd.concat([df, df_yeni], ignore_index=True)
print(df_artirilmis)
