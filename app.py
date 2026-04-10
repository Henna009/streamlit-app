import streamlit as st
from streamlit_autorefresh import st_autorefresh
import mysql.connector
import pandas as pd

st.title("📊 Hennan serveri")

st_autorefresh(interval=1800000, limit=None, key="refresh")

conn = mysql.connector.connect(
    host="localhost",
    user="exampleuser",
    password="salasana123",
    database="exampledb"
)



import pandas as pd

st.subheader("🌤️ Helsinki sää")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="salasana123",
        database="exampledb"
    )

    df = pd.read_sql("SELECT * FROM weather ORDER BY created_at DESC LIMIT 10", conn)

    st.write(df)
    st.subheader("📈 Lämpötila")

# varmista että aika on oikeassa muodossa
    df["created_at"] = pd.to_datetime(df["created_at"])

    st.line_chart(df.set_index("created_at")["temperature"])
    conn.close()

except Exception as e:
    st.error(f"Virhe: {e}")
