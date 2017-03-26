import shelve
import sys
import colorama

Commands = {
    'a' : add_task, 
    'd' : delete_task, 
    'f' : finish_task,
    'q' : quit
}

Invalid_Command_Message = ''' 
    Not a valid command. Try on of these: \n
    a [task] - add task to task list \n
    d [task] - delete task from task list \n
    f [task] - finish task and move to completed \n
    q - quit tix \n
'''

def add_task(task, db):
    temp = db['tasks']
    temp.append(task)
    return 0

def delete_task(task, db):
    return 0

def finish_task(task, db):
    return 0

def quit():
    exit("Ciao ciao")

def run():
    with shelve.open('tix_data') as db:
        while(True):
            try: 
                c = input("// ").split()
                if len(c) == 1: 
                    Commands[c[0]]
                else:
                    Commands[c[0]](c[1], db) # Calls the function in Commands dictionary
            except Exception:
                print (Invalid_Command_Message)
                break

if __name__ == "__main__":
    run()

    
