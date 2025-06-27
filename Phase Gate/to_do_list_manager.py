def add_a_task(task_list, task):
  #To add a task to your to-do list.
  task_list.append(task)
  return task_list
  
def view_tasks(view_task, task_list):
  #To view task in the to-do-list.
  users_choice = view_task.lower()
  if view_task == users_choice:
    return task_list
  else:
    return 'Invalid input'
  
def mark_task_as_complete(mark_task, task_list):
  #To mark completed tasks in to do list.
  index = 0
  for item in task_list:
    if item.lower() != mark_task.lower():
      index += 1
    if item.lower() == mark_task.lower():
      task_list[index][0] = '[X]'
      return task_list

def delete_a_task(delete_item, task_list):
  #To delete item from your to-do list.
  for item in task_list:
    if item.lower() == delete_item.lower():
      task_list.remove(item)
      return task_list
  
    
mark_task = ''
view_task = ''
delete_item = ''

print('''
    1. Add a task
    2. View tasks
    3. Mark task as complete
    4. Delete a task
    5. Exit
    ''')

while True:
  user_selection = int(input('Enter your choice: '))
  match user_selection:
    case 1:
      task = str(input('Enter the task: '))
      break
    case 2:
      view_task = input('Enter list to view tasks: ')
      break
    case 3:
      mark_task = input('Enter the task to mark: ')
      break
    case 4:
      delete_item = str(input('Enter task name: '))
      break
    case 5:
      print('Good-Bye...!')
      user_selection = False
      break
    case _:
      user_selection = True
    

task_list = [['[]','Buy groceries'],['[]','Transport'],['[]','Finish homework']]

print(mark_task_as_complete(mark_task, task_list))