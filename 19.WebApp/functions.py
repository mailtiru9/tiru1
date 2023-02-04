FILEPATH = 'todo.txt'

def read_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()  # No need to declare list variable it default retuns list
    return todos
def write_todo(todoarg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todoarg)

if __name__ == "__main__":
    print("Bye!")


# /*def todo_amend():
#     while True :
#         user_action = input("Type add or show or exit or edit or remove: ")
#         user_action = user_action.strip()
#         match user_action :
#             case 'add' :
#                 todo = input("Enter a Todo: ") + "\n"
#                 todos = read_todo(FILEPATH)
#
#                 todos.append(todo)
#
#             case 'show':
#                 file = open('todo.txt', 'r')
#                 todos = file.readlines()
#                 file.close()
#
#                 for index, item in enumerate(todos):
#                     row = f"{index}-{item}"
#                     print(row)
#                 print(f"Indent check{index}and{item}")
#             case 'edit':
#                 position = int(input("Enter the position you want to replace:"))
#                 todos[position-1] = input("Enter a replace Todo:")
#             case 'remove':
#                 position = int(input("Enter the position you want to remove:"))
#                 todos.pop(position)
#
#             case 'exit':
#                 break


