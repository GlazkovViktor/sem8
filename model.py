import os
journal = {}
subject = ''
path = ''

def set_class(class_path: str):
    global path
    path = class_path + '.txt'
    if os.path.exists(path):
        if os.path.isfile(path):
            print('\nКласс введен верно\n ')
    else:
        print('\nВведите корректно номер класса\n')



def set_subject(our_subject: str):
    global subject
    subject = our_subject
        
def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = study.split(':')[1].split()

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':'+' '.join(list(map(str, marks))))
    item = subject+ ';'+', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def student_mark(student: str, mark: int):
    marks = journal.get(student)
    if 1<=mark <6:
          marks.append(mark)  
    else:
        print('Введите корректную оценку от 1 до 5')
    journal[student] = marks

def get_journal():
    return journal


