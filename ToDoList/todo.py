#todo.py
import argparse

from task import read_json, write_json
from commands import todo_list, todo_add, todo_done, todo_clear

def main():
    lists = read_json() # JSONファイルの読み込み
    parser = argparse.ArgumentParser( # 引数の指定
        description='コマンドを指定する'
    )
    parser.add_argument('command', help='コマンド', type=str, nargs='*')
    args = parser.parse_args()
    
    # 受け取った引数により処理を分岐
    if len(args.command) >= 3:
        print('too many args, 2')
    elif args.command[0] == 'list':
        todo_list(lists)
    elif args.command[0] == 'clear':
        todo_clear(lists)
    elif args.command[0] == 'add':
        if len(args.command) == 2:
            todo_add(lists, args.command[1])
        else:
            print('2 arguments are required.')
    elif args.command[0] == 'done':
        if len(args.command) == 2:
            todo_done(lists, args.command[1])
        else:
            print('2 arguments are required.')
    else:
        print('unknown command.')
    
        
    write_json(lists) # JSONファイルの書き込み
    
    
    return


if __name__ == "__main__":
    main()
