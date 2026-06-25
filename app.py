import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Student Dashboard", page_icon="🎓", layout="wide")

st.title("🎓 Student Dashboard")
st.subheader("Welcome back! Manage your notes and tasks.")

if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

page = st.sidebar.radio("Menu", ["Dashboard", "Notes", "Tasks"])

if page == "Dashboard":
    st.metric("Total Notes", len(st.session_state.notes))
    st.metric("Pending Tasks", len([t for t in st.session_state.tasks if not t.get('completed', False)]))
    
    with st.expander("Quick Note"):
        t = st.text_input("Title")
        if st.button("Save") and t:
            st.session_state.notes.append({"title": t})
            st.success("Saved")
            st.rerun()

elif page == "Notes":
    st.header("My Notes")
    t = st.text_input("New Note Title")
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
    t = st.text_input("New Task")
    if st.button("Add Task") and t:
        st.session_state.tasks.append({"title": t, "completed": False})
        st.rerun()
    for i, task in enumerate(st.session_state.tasks):
        done = st.checkbox(task['title'], value=task['completed'], key=i)
        if done != task['completed']:
            task['completed'] = done
            st.rerun()