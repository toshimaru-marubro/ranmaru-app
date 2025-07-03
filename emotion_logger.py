import streamlit as st
from datetime import datetime

st.title("📊 らんまる - トレード＆感情ログ with エントリー補助")

# --- 入力フォーム ---
st.header("📝 今日のトレード記録")

entry_type = st.selectbox("エントリー種別", ["買い", "売り", "なし"])
entry_price = st.number_input("エントリーポイント（価格）", value=0.0, format="%.2f")
take_profit = st.number_input("利確ポイント", value=0.0, format="%.2f")
stop_loss = st.number_input("損切りポイント", value=0.0, format="%.2f")
reason = st.text_input("トレード理由（テクニカル、ファンダ、勘など）")

st.header("💬 今の気持ちをひとこと")
emotion = st.text_input("感情ログ", placeholder="例：冷静、自信あり、ちょっと不安…")

# --- エントリー補助ロジック ---
st.subheader("🔎 らんまるの判断")

if "不安" in emotion or "焦り" in emotion:
    st.warning("今の感情が不安定みたい…。今は様子見したほうがいいかも💡")
elif "なんとなく" in reason or reason.strip() == "":
    st.warning("理由が曖昧だと勝率が下がるよ。もう一度分析してみて？")
elif entry_type in ["買い", "売り"] and abs(take_profit - entry_price) < 0.1:
    st.warning("利確幅が狭いかも。リスクリワードを見直そう💡")
elif entry_type == "なし":
    st.info("今日はエントリーしない選択も立派だよ✨")
else:
    st.success("うん、感情も理由も整ってるね！チャンスかも✨")

# --- ログ保存（オプション：後で拡張） ---
if st.button("記録する"):
    with open("logs.csv", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{now},{entry_type},{entry_price},{take_profit},{stop_loss},{reason},{emotion}\n")
    st.success("ログを保存しました📁")

