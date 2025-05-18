// frontend/js/register.js
function register() {
    const tc = document.getElementById("tc").value;
    const name = document.getElementById("name").value;
    const password = document.getElementById("password").value;
  
    fetch("http://localhost:5000/api/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ tc, name, email, password })
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        alert("Kayıt başarılı!");
        window.location.href = "./login.html"; // kullanıcıyı giriş ekranına yönlendir
      } else {
        alert("Kayıt başarısız: " + data.message);
      }
    })
    .catch(err => {
      console.error("Sunucu hatası:", err);
    });
  }
  