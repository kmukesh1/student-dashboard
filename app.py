import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Student Dashboard", page_icon="🎓", layout="wide")

st.title("🎓 Student Dashboard")

if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

page = st.sidebar.radio("Menu", ["Dashboard", "Notes", "Tasks", "Upload Files"])

if page == "Dashboard":
    st.metric("Total Notes", len(st.session_state.notes))
    st.metric("Pending Tasks", len([t for t in st.session_state.tasks if not t.get('completed', False)]))

elif page == "Notes":
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
    st.header("Upload Files (PDF, Images, etc.)")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg", "txt"])
    if uploaded_file is not None:
        st.success(f"File uploaded: {uploaded_file.name}")
        st.write("File size:", uploaded_file.size, "bytes")
        if st.button("Save to Notes"):
            st.session_state.notes.append({"title": uploaded_file.name, "content": "Uploaded file"})
            st.success("File saved to Notes!")
            st.rerun()