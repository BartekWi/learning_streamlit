import streamlit as st

from task import Task
from jokes import generate_joke
api_key = st.secrets["jokes_api"]["api_key"]
if "joke" not in st.session_state:
    st.session_state.joke=generate_joke(api_key)
if "task_list" not in st.session_state:
    st.session_state.task_list=[]
task_list =  st.session_state.task_list
st.info(st.session_state.joke)
def add_task(task_name:str):
    task_list.append((Task(task_name)))
def mark_done(task:Task):
    task.is_done=True
def mark_not_done(task:Task):
    task.is_done=False
def del_task(idx:int):
    del task_list[idx]


with st.sidebar:
    task=st.text_input("Enter a task")
    if st.button("Add task",type="primary"):
        add_task(task)
n_tasks=len(task_list)
n_completed=sum(1 for task in task_list if task.is_done)
metric_display=f"{n_completed}/{n_tasks} done."
st.metric("Task completion",metric_display,delta=None)
st.header("Today's to-dos:",divider='gray')
st.info(f"task_list: {task_list}")
for i,task in enumerate(task_list):
    label=f"~~{task.name}~~" if task.is_done else task.name
    task_col,del_col=st.columns([0.8,0.2])
    checked=task_col.checkbox(label,task.is_done,key=f"task_{i}")
    if checked and not task.is_done:
        mark_done(task)
        st.rerun()
    elif not checked and task.is_done:
        mark_not_done(task)
        st.rerun()
    if del_col.button("Delete",key=f"delete_{i}"):
        del_task(i)
        st.rerun()