import streamlit as st
import functions


todos = functions.read_todo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)
    print(todo)

st.title("My Todo App")
st.subheader("This is my Todo App")

st.write("This App is to improve the productivity")

for index,todo in enumerate(todos):
   checkbox = st.checkbox(todo, key=todo)  #each check box becomes a key
   if checkbox :
       todos.pop(index)
       functions.write_todo(todos)
       del st.session_state[todo]
       st.experimental_rerun()

st.text_input(label="Hi", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')

# print("Hello")

#st.session_state