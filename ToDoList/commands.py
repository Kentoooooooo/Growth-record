# commands.py

def todo_list(lists):
    '''引数としてlistを受け取ったときの処理
    '''
    print('# Todo')
    for task in lists:
        if task['done'] == False:
            print(task['body'])
    
    print('\n# Done')
    for task in lists:
        if task['done'] == True:
            print(task['body'])
            
def todo_add(lists, task_name):
    lists.append({'body': task_name, 'done': False})


def todo_done(lists, task_name):
    # タスクがないときは例外処理
    for task in lists:
        if task_name in task['body']:
            task['done'] = True


def todo_clear(lists):
    chg_lists = lists
    rmv = []
    for task in lists:
        if task['done'] == True:
            rmv.append(task)
    for task in rmv:
        lists.remove(task)
            
