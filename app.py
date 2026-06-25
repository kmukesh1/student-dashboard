import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Algolex Student Dashboard", page_icon="🎓", layout="wide")

# Algolex Branding
st.markdown("<style>.main-header {font-size:2.5rem; font-weight:700; color:#1E40AF} .company {color:#64748B; font-size:1.1rem;}</style>", unsafe_allow_html=True)

st.sidebar.title("🎓 Algolex")
st.sidebar.caption("Student Dashboard")

if 'notes' not in st.session_state: st.session_state.notes = []
if 'tasks' not in st.session_state: st.session_state.tasks = []

page = st.sidebar.radio("Menu", ["Dashboard", "My Notes", "Tasks", "Upload Files"])

if page == "Dashboard":
    st.markdown('<p class="main-header">Algolex Student Dashboard</p>', unsafe_allow_html=True)
    st.caption("Welcome back! Your personal learning space.")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Notes", len(st.session_state.notes))
    with c2: st.metric("Pending Tasks", len([t for t in st.session_state.tasks if not t.get('completed', False)]))
    with c3: st.metric("Overdue", 0)
    with c4: st.metric("Completed", len([t for t in st.session_state.tasks if t.get('completed', False)]))

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
    f = st.file_uploader("Upload PDF or Image")
    if f:
        st.success(f"File uploaded: {f.name}")
        if st.button("Save to Notes"):
            st.session_state.notes.append({"title": f.name})
            st.success("Saved to Notes!")
            st.rerun()