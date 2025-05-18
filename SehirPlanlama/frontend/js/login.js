function login() {
  const tc_kimlik = document.getElementById("tc").value;
  const sifre = document.getElementById("password").value;

  fetch("http://localhost:5000/api/kullanici", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ tc_kimlik, sifre })
  })
  .then(res => res.json())
  .then(data => {
    if (!data.error) {  // Backend hatalıysa 'error' dönüyor
      alert("Giriş başarılı!");
      window.location.href = "/admin_home.html"; // yönlendirme
    } else {
      alert("Hatalı kimlik no veya şifre!");
    }
  })
  .catch(err => {
    console.error("Sunucu hatası:", err);
  });
}
