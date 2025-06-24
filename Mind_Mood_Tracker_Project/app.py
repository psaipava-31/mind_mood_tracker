import streamlit as st
import json 
import matplotlib.pyplot as plt
from datetime import datetime
from mood_db import log_entry
from tracker_agent import analyse_entry


st.set_page_config(page_title="Mind & Mood Tracker",page_icon="🧠")
st.title("🧠 Mind & Mood Tracker Agent")
st.write("Tell me how you're feeling today.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You :" , "")

if st.button("Submit") and user_input:
  with st.spinner("Thinking..."):
   ai_response = analyse_entry(user_input)
  st.session_state.chat_history.append(("You", user_input))
  st.session_state.chat_history.append(("AI", ai_response))
#  st.write(ai_response)
  log_entry(user_input,ai_response)

for sender, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{sender}:** {message}")

def plot_weekly_trend():
    try:
        with open("mood_log.json", "r") as f:
            data = json.load(f)

        if len(data) == 0:
            st.warning("No data to analyze.")
            return

        dates, energy = [], []
        for entry in data:
            try:
                ts = entry.get("timestamp", "")

                dt = datetime.fromisoformat(ts)

                text = entry.get("response", "")
                level = int([s for s in text.split() if "/10" in s][0].split("/")[0])

                dates.append(dt)
                energy.append(level)
            except Exception as inner_error:
                st.warning(f"⚠️ Skipping entry: {entry}")
                continue

        if not dates:
            st.error("No valid mood entries found.")
            return

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(dates, energy, marker="o", linestyle="-", color="green")
        ax.set_title("Weekly Energy Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Energy Level (0–10)")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    except Exception as e:
        st.error("❌ An error occurred while generating the report:")
        st.code(traceback.format_exc())  # Shows full traceback inside Streamlit



if st.button("📊Generate Weekly Report"):
   plot_weekly_trend()




   


