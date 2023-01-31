import model



def input_class():
    return input('С каким классом работем? ').upper()


def input_subject():
    our_subject = str(input('Какой предмет? ').lower()) 
    if our_subject.startswith('ли'):
        subject = 'литература'
        return subject
    if our_subject.startswith('ма'):
        subject = 'математика'
        return subject
    if our_subject.startswith('ру'):
        subject = 'русский язык'
        return subject
    else:
        print('такого предмета нет, проверьте что написали ')

    

def who_answer():
    return input('Кто будет отвечать? ')


def what_mark():
    return int(input('На какую оценку ответил? '))
        

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')
