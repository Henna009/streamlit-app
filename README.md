# linux_rästitehtävä 
# Helsinki sää 15min välein

Tehtävä hakee Helsingin säätietoja OpenWeatherMap API:sta ja näyttää datan Streamlit palvelussa.

# Käytetty toimintoja

- Python
- Streamlit
- MySQL
- Nginx
- OpenWeatherMap API
- Cron

# Toiminnallisuutta

1. Python-skripti hakee säätiedot API:sta
2. Data tallennetuu MySQL
3. Cron ajaa skriptin 15 minuutin välein
4. Streamlit-sovellus näyttää:
   - taulukon
   - graafisen kuvan
5. Sivusto päivittyy automaattisesti
