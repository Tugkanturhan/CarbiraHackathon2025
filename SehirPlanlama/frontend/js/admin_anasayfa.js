// frontend/js/admin_ana_sayfa.js

// Veri çekme
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
  });

// Güncelleme gönderme
document.getElementById("guncelleBtn").addEventListener("click", () => {
  const payload = {
    genel_goc: document.getElementById("genel_goc").value,
    genel_dogum: document.getElementById("genel_dogum").value,
    genel_olum: document.getElementById("genel_olum").value,
    toplam_dogurganlik: document.getElementById("toplam_dogurganlik").value,
    toplam_nufus: document.getElementById("toplam_nufus").value,
    yatak_orani: document.getElementById("yatak_orani").value,
    hastane_sayisi: document.getElementById("hastane_sayisi").value,
    hastane_yatak: document.getElementById("hastane_yatak").value,
    ambulans: document.getElementById("ambulans").value,
    vakalar: document.getElementById("vakalar").value,
    doktor_orani: document.getElementById("doktor_orani").value,
    toplu_tasima: document.getElementById("toplu_tasima").value,
    konut_satis: document.getElementById("konut_satis").value,
  };

  fetch("http://localhost:8000", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
    .then(res => res.json())
    .then(() => alert("Veriler başarıyla güncellendi!"))
    .catch(err => console.error("Güncelleme hatası:", err));
});
