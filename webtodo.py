import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip()
    if todo:
        todos.append(todo + '\n')
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''


st.title("Todo App")
st.subheader("Just another todo app")
st.write("App")
st.markdown("This app from <a href='https://www.udemy.com/course/the-python-mega-course/?couponCode=LETSLEARNNOWPP'>Udemy</a>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    clean_todo = todo.strip().replace(' ', '').replace('\n', '')
    key = functions.sanitize_string(clean_todo + f"_{index}")

    checkbox = st.checkbox(todo.strip(), key=key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[key]
        st.experimental_rerun()

st.text_input(label="Write a new todo", placeholder="Add some task", on_change=add_todo, key='new_todo')


