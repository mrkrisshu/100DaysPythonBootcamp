todo = []

while True:
    task = input("Enter task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    todo.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(todo, 1):
    print(f"{i}. {task}")
