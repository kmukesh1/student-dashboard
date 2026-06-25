import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Student Dashboard", page_icon="🎓", layout="wide")

st.title("🎓 Student Dashboard")
st.subheader("Welcome back! Here's your personal study space.")

st.info("Full Notes + Tasks features are being added. This is version 1.")

with st.expander("📝 My Notes (Coming soon)"):
    st.write("You will be able to add, search and organize your study notes here.")

with st.expander("✅ Tasks & To-Do (Coming soon)"):
    st.write("Track assignments, due dates and completed tasks.")

st.success("Your dashboard is live! More features coming in the next update.")