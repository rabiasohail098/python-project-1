import streamlit as st

# Page Title
st.title("📝 To-Do List App")

# Initialize session state for tasks and edit mode
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = {}

# Sidebar Heading
st.sidebar.header("📌 Manage Your Tasks")

# Task Input
new_task = st.sidebar.text_input("➕ Add a new task:", placeholder="Enter your task here...")

if st.sidebar.button("Add Task", key="add_task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.sidebar.success("Task added successfully! ✅")
        st.rerun()  # Updated to st.rerun()
    else:
        st.sidebar.warning("Task cannot be empty! ❌")

# Function to Delete Task
def delete_task(index):
    if 0 <= index < len(st.session_state.tasks):
        del st.session_state.tasks[index]
        st.rerun()  # Updated to st.rerun()

# Function to Toggle Edit Mode
def toggle_edit_mode(index):
    st.session_state.edit_mode[index] = not st.session_state.edit_mode.get(index, False)

# Display Tasks
st.subheader("📋 Your To-Do List")
if not st.session_state.tasks:
    st.info("No tasks added yet. Start by adding a task from the sidebar!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Checkbox to Mark Task as Completed
        completed = col1.checkbox(f"**{task['task']}**", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Initialize Edit Mode
        if index not in st.session_state.edit_mode:
            st.session_state.edit_mode[index] = False

        # Edit Task
        if st.session_state.edit_mode[index]:
            new_text = col1.text_input("Edit Task:", task["task"], key=f"input_{index}")
            if col2.button("💾 Save", key=f"save_{index}"):
                if new_text.strip():
                    st.session_state.tasks[index]["task"] = new_text
                    st.session_state.edit_mode[index] = False
                    st.rerun()  # Updated to st.rerun()
                else:
                    st.warning("Task cannot be empty! ❌")
        else:
            if col2.button("✏️Edit", key=f"edit_{index}"):
                toggle_edit_mode(index)
                st.rerun()  # Updated to st.rerun()

        # Delete Button
        if col3.button("❌ Del", key=f"delete_{index}"):
            delete_task(index)  # Call function to delete

# Clear All Button
if st.button("🗑 Clear All Tasks", key="clear_all"):
    st.session_state.tasks = []
    st.rerun()  # Updated to st.rerun()

# Footer
st.markdown("---")
st.caption("✅ Stay organized & productive with this simple To-Do List App!")
