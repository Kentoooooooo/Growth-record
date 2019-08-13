# task.py
import json

TASK_PATH = './tasks.json'
ENCODING = 'utf-8'


def read_json(): # クラスじゃないからself入らない
    '''jsonファイルからデータを読み取って、辞書を返す
    '''
    with open(TASK_PATH,encoding=ENCODING) as f:
        data = json.load(f)
        
    return data['tasks']

def write_json(lists):
    '''ToDoリストの辞書listsをjsonファイルに書き込む
    '''
    data = {}
    with open(TASK_PATH, mode='w', encoding=ENCODING) as f:
        data['tasks'] = lists
        json.dump(data, f, ensure_ascii=False)

class Task:
    '''タスク（ToDoリストではない）
    '''
    def __init__(self, body, done):
        self.body = body
        self.done = False
