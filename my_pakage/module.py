import csv
import pickle

# загрузка/сохранение табличных данных 

def load_table(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            table = {'table': [row for row in reader], 'data_type': 'str'}
        return table
    except FileNotFoundError:
         print('Файл не найден')
    except PermissionError:
         print('У вас нет доступа к этому файлу')
    finally:
         print('Работа с файлом завершена')
         
def save_table(table, file_path):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(table)
    except PermissionError:
         print('У вас нет доступа к этому файлу')
    finally:
         print('Работа с файлом завершена')
         
def load_table(file_path):
    try:
        with open(file_path, 'rb') as file:
            table = {'table': pickle.load(file), 'data_type': 'str'}
        return table
    except FileNotFoundError:
         print('Файл не найден')
    except PermissionError:
         print('У вас нет доступа к этому файлу')
    finally:
         print('Работа с файлом завершена')

def save_table(table, file_path):
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(table, file)
    except PermissionError:
         print('У вас нет доступа к этому файлу')
    finally:
         print('Работа с файлом завершена')

# Базовые операции над таблицами

def save_table(table, file_path):
    with open(file_path, 'w') as file:
        for row in table:
            file.write('\t'.join(str(cell) for cell in row) + '\n')

def get_rows_by_number(table, start, stop=None, copy_table=False):
        if copy_table:
            new_table = [row[:] for row in table['table'][start:stop]]
        else:
            new_table = table['table'][start:stop]
        return new_table

def get_rows_by_index(table, *args, copy_table=False):
        if copy_table:
            new_table = [row[:] for row in table['table'] if row[0] in args]
        else:
            new_table = [row for row in table['table'] if row[0] in args]
        return new_table

def get_column_types(table, by_number=True):
        if by_number:
            table['data_type'] = {i: t for i, t in enumerate([type(col[1]) for col in zip(*table['table'])])}
            return table
        else:
            table['data_type'] = {str(i): t for i, t in enumerate([type(col[1]) for col in zip(*table['table'])])}
            return table

def set_column_types(table, types_dict, by_number=True):
        if by_number:
            table['data_type'] = types_dict
            return table
        else:
            table['data_type'] = types_dict
            return table

def get_values(table, column=0):
     column = [col for col in zip(*table['table'])][column]
     return list(column)
      
def get_value(table, column=0):
    pass

def set_values(table, values, column=0):
    column = [list(col) for col in zip(*table['table'])][column]
    for ind, _ in enumerate(column):
         column[ind] = values[ind]
    return column

def set_value(values, column=0):
    pass

def print_table():
     return table['table']

#Примеры

#table = [['Name', 'Age', 'Gender'],
#        ['John', '20', 'Male'],
#        ['Jane', '30', 'Female']]

table = {'table':[['Name', 'Age', 'Gender'],
         ['John', '20', 'Male'],
         ['Jane', '30', 'Female']], 'data_type': str}


#save_table_csv(table, 'table.csv')
#load_table_csv('table.csv')
#save_table_pickle(table, 'table.pickle')
#get_rows_by_number(table, 1, 3)
#get_rows_by_index(table, 'John')
#get_column_types(table)
#set_column_types(table, {0: int, 1: int, 2: int})
#print_table()
#get_values(table)
#set_values(table, [1, 1, 1], column=0)