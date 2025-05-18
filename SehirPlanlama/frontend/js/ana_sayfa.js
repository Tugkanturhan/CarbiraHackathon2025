const BASE_URL = "http://localhost:8000";

fetch("http://localhost:8000")
  .then(res => res.json())
  .then(data => {
    document.getElementById("genel_goc").value = data.genel_goc;
    document.getElementById("genel_dogum").value = data.genel_dogum;
    document.getElementById("genel_olum").value = data.genel_olum;
    document.getElementById("toplam_dogurganlik").value = data.toplam_dogurganlik;
    document.getElementById("toplam_nufus").value = data.toplam_nufus;

    document.getElementById("yatak_orani").value = data.yatak_orani;
    document.getElementById("hastane_sayisi").value = data.hastane_sayisi;
    document.getElementById("hastane_yatak").value = data.hastane_yatak;
    document.getElementById("ambulans").value = data.ambulans;
    document.getElementById("vakalar").value = data.vakalar;
    document.getElementById("doktor_orani").value = data.doktor_orani;

    document.getElementById("toplu_tasima").value = data.toplu_tasima;
    document.getElementById("konut_satis").value = data.konut_satis;
  })
  .catch(err => console.error("Veri alınamadı:", err));

  // Sayfa yüklendiğinde verileri çek
window.addEventListener("DOMContentLoaded", () => {
    fetch(`${BASE_URL}/nufus/`)
      .then(res => res.json())
      .then(data => {
        document.getElementById("genel_goc").value = data.genel_goc || "";
        document.getElementById("genel_dogum").value = data.genel_dogum || "";
        // diğer inputları ekle
      })
      .catch(err => console.error("Veri alınırken hata:", err));
  });
  
  // Güncelleme butonuna basıldığında veri gönder
  document.getElementById("guncelleBtn").addEventListener("click", () => {
    const payload = {
      genel_goc: document.getElementById("genel_goc").value,
      genel_dogum: document.getElementById("genel_dogum").value
      // diğer inputları ekle
    };
  
    fetch(`${BASE_URL}/nufus/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(res => res.json())
      .then(data => {
        alert("Veriler başarıyla güncellendi!");
      })
      .catch(err => {
        console.error("Güncelleme hatası:", err);
      });
  });
  