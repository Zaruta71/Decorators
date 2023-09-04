from datetime import datetime

def logger1(old_function):
    def new_function(*args, **kwargs):
        with open('main1.log', 'a', encoding='utf-8') as log_file:
            result = f'''\nДата и время запуска программы: {datetime.now()}
Название функции: {old_function.__name__}
Аргументы: {args} и {kwargs}
Результат выполнения: {old_function(*args, **kwargs)}\n'''
            log_file.writelines(result)
            return old_function(*args, **kwargs)
    return new_function

def logger2(path):
    
    def __logger(old_function):
        
        def new_function(*args, **kwargs):
            nonlocal path
            with open(path, 'a', encoding='utf-8') as log_file:
                result = f'''\nДата и время запуска программы: {datetime.now()}
Название функции: {old_function.__name__}
Аргументы: {args} и {kwargs}
Результат выполнения: {old_function(*args, **kwargs)}\n'''
                log_file.writelines(result)
                return old_function(*args, **kwargs)

        return new_function

    return __logger
