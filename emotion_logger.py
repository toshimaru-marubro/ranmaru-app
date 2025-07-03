import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os

LOG_FILE = 'emotion_logs.json'

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return []

def save_log(log):
    logs = load_logs()
    logs.append(log)
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)

st.title("らんまる 感情ログ")

with st.form("emotion_form"):
    anxiety = st.slider('不安', 0, 100, 50)
    happiness = st.slider('幸せ', 0, 100, 50)
    anger = st.slider('怒り', 0, 100, 50)
    calm = st.slider('落ち着き', 0, 100, 50)
    submitted = st.form_submit_button("記録する")

if submitted:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {
        'timestamp': now,
        'anxiety': anxiety,
        'happiness': happiness,
        'anger': anger,
        'calm': calm
    }
    save_log(log_entry)
    st.success("感情ログを保存しました！")

logs = load_logs()
if logs:
    st.subheader("過去ログ")
    df = pd.DataFrame(logs)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    st.dataframe(df.sort_values('timestamp', ascending=False))
    st.line_chart(df.set_index('timestamp')[['anxiety','happiness','anger','calm']])
else:
    st.info("まだ感情ログはありません。")
