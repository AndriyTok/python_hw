# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

#import of the type that helps us to typify functions in python (Callable)
from typing import Callable
#this function returns tuple of two functions
def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    #empty list we will work with
    todo_list: list[str] = []

    #this function accept a todo and uses method .append to add it to the list
    def append_todo(todo:str) -> None:
        #we use nonlocal variable and such prompt is necessary to choose the right scope
        nonlocal todo_list
        todo_list.append(todo)

    # this function just copies changed list and returns it for us to be able to work with it afterward
    def get_todo() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return append_todo, get_todo

#initialization of the function
add_task, get_task = notebook()

#adding while to give the opportunity to input many todos:
while True:
    #to input a todo
    tasks = input('Input tasks you wanna do (or q to quit): ')

    #to quit if you input 'q'
    if tasks.lower() == 'q':
        break

    #adding all the todos to the initial list
    add_task(tasks)

tasks_list = get_task()
#using concatenation
print('Your tasks:\n' + '\n'.join(tasks_list))