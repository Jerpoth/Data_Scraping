
from utile.object import object1
from utile.ext_num import extract_number




def obj_to_list(obj):
    return list(obj.values())

if __name__ == '__main__':

    print('\n')
    print(f'Imported object :{object1}')

    print('----------------------------')
    print('\n')

    list_obj = obj_to_list(object1)
    print(f'object Value has list:{list_obj}')


    print('-------------------------------')
    print('\n')

    text = input('enter the text with number : ')
    number = extract_number(text)
    print(f'Extracted number :{number}')