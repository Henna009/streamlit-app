# 🌤️ Helsinki sää 15 minuutin välein

Tämä projekti hakee Helsingin säätietoja OpenWeatherMap API:sta, tallentaa datan MySQL ja näyttää ne Streamlit-palvelussa.

---

# Projektin tarkoitus

Projektin tavoitteena on:

* hakea säätietoa ulkoisesta API:sta Pythonilla
* tallentaa data tietokantaan
* Datan päivitys cron-ajastuksella

---

## Järjestelmät

* Python
* Streamlit
* MySQL
* OpenWeatherMap API
* Cron (ajastus Linuxissa)

---

# Miten sovellus toimii

1. `fetch_weather.py` hakee säätiedot OpenWeatherMap API:sta
2. Data (lämpötila ja kosteus) tallennetaan MySQL-tietokantaan
3. Cron ajaa skriptin automaattisesti 15 minuutin välein
4. Streamlit-sovellus (`app.py`) näyttää datan:

   * taulukkona
   * graafisena taulukkona

---

# Asennus

```bash
git clone https://github.com/Henna009/streamlit-app.git
cd streamlit-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# Käynnistys

Käynnistä Streamlit:

```bash
streamlit run app.py
```

Avaa selaimessa:

```
http://localhost:8501
```

---

## ⏱️ Ajastus

Data päivittyy automaattisesti 15 minuutin välein:

```bash
*/15 * * * * /home/ubuntu/streamlit-app/venv/bin/python /home/ubuntu/streamlit-app/fetch_weather.py
```

---

# MySQL

MySQL-taulu:

* `weather`

  * id
  * temperature
  * humidity
  * created_at

---

## 🔑 API

Sovellus käyttää OpenWeatherMap API:a:

https://openweathermap.org/api

API-avain ei julkisesti näkyvissä

---
# Linkki sivustolle
http://128.214.254.92:8501/data-analysis/#my-data-app

## 👩‍💻 Tekijä

Henna009
