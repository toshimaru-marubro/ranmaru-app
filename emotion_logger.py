import streamlit as st
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="らんまる感情ログ", layout="centered")

st.title("📝 らんまる感情ログ")

# 入力UIを縦並びに変更
with st.form("log_form"):
    emotion = st.text_area("今の気持ちを入力してね", height=100)
    submitted = st.form_submit_button("記録する")
    if submitted and emotion.strip() != "":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logs.csv", "a", encoding="utf-8") as f:
            f.write(f"{now},{emotion.strip()}\n")
        st.success("記録したよ！")

# ログファイルが存在すれば表示
if os.path.exists("logs.csv"):
    st.subheader("📚 過去の記録")
    df = pd.read_csv("logs.csv", names=["日時", "感情"], encoding="utf-8")

    # 表示エリアをスクロール可能に
    with st.container():
        st.markdown(
            """
            <div style='max-height: 300px; overflow-y: scroll; padding: 10px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;'>
            """,
            unsafe_allow_html=True
        )
        for i in range(len(df)-1, -1, -1):
            st.markdown(f"**{df.iloc[i]['日時']}**")
            st.markdown(f"{df.iloc[i]['感情']}")
            st.markdown("---")
        st.markdown("</div>", unsafe_allow_html=True)
