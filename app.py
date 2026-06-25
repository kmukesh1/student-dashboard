import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Algolex Student Dashboard", page_icon="🎓", layout="wide")

# ====================== ALGOLEX LOGO ======================
# To add your logo:
# 1. Upload your logo image (logo.png) to this GitHub repo
# 2. Replace the URL below with your logo's raw GitHub URL
# Example: https://raw.githubusercontent.com/kmukesh1/student-dashboard/main/logo.png

try:
    st.sidebar.image("https://via.placeholder.com/150x50?text=Algolex", width=150)
except:
    st.sidebar.write("**Algolex**")

st.sidebar.title("Student Dashboard")
st.sidebar.caption("Powered by Algolex")

# ====================== SESSION STATE ======================
if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# ====================== NAVIGATION ======================
page = st.sidebar.radio("Menu", ["Dashboard", "My Notes", "Tasks", "Upload Files"])

if page == "Dashboard":
    st.title("Algolex Student Dashboard")
    st.metric("Total Notes", len(st.session_state.notes))
    st.metric("Pending Tasks", len([t for t in st.session_state.tasks if not t.get('completed', False)]))

elif page == "My Notes":
    st.header("My Notes")
    t = st.text_input("Note Title")
    if st.button("Add Note") and t:
        st.session_state.notes.append({"title": t})
        st.rerun()
    for i, note in enumerate(st.session_state.notes):
        st.write(note['title'])
        if st.button("Delete", key=i):
            st.session_state.notes.pop(i)
            st.rerun()

elif page == "Tasks":
    st.header("My Tasks")
    t = st.text_input("Task")
    if st.button("Add Task") and t:
        st.session_state.tasks.append({"title": t, "completed": False})
        st.rerun()
    for i, task in enumerate(st.session_state.tasks):
        done = st.checkbox(task['title'], value=task.get('completed', False), key=i)
        if done != task.get('completed', False):
            task['completed'] = done
            st.rerun()

elif page == "Upload Files":
    st.header("Upload Files")
    f = st.file_uploader("Choose a file")
    if f:
        st.success(f"File uploaded: {f.name}")
        if st.button("Save to Notes"):
            st.session_state.notes.append({"title": f.name})
            st.success("Saved!")
            st.rerun()