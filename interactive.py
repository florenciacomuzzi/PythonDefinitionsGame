import glossary
import random
import time
import builtins
#from contextlib import contextmanager

#DATA = glossary.CONCEPTS
#DATA = create_data()

def starts_lowercase_regex(name):
    """return True if starts with lowercase letter"""
    print('calling starts_lowercase_regex')
    import re 
    return re.match('[a-z]', name)

def starts_lowercase_string(name):
    """return True if starts with lowercase letter"""
    print('calling starts_lowercase_string')
    import string
    return any(name.startswith(c) for c in string.ascii_lowercase)

starts_lowercase = starts_lowercase_string   #global pointing to fct

def create_data():
    """return a dictionary of answers to definitions"""    
    data_dict = {}
    for name in dir(builtins): #get name associated with that object
        if starts_lowercase(name):
            
            builtin_function = getattr(builtins, name)
            doc = builtin_function.__doc__
            if doc is not None:
                placeholder = '*' * len(name) # will replace/strip out name with asterisk
                newdoc = placeholder.join(doc.split(name))
                data_dict[name] = newdoc #so name is assoc with its documentation     
    return data_dict

DATA = create_data()


def ask_question(definition, answer):
    """takes definition and answer, quizzes user, returns success(bool)"""
    time.sleep(.5) #half a second wait to look like it's doing computation 
    print('Tell me what name is associated with the following definition: ')
    print(definition)
    response = input('> ') 
    print('') #one more line
    
    success =  response == answer #success is whether or not response is the answer
    if success: 
        print('right!')
    else: 
        print('sorry!')
    return success



def main(): 
    attempts = successes = 0 #local name spaces are dicts, both point to 0 
    keys = list(DATA)
    random.shuffle(keys)
    print(keys)   
    for answer in keys:
        definition = DATA[answer]
        try: 
            success  = ask_question(definition, answer) #returns bool determining if wrong or right answer
        except EOFError:
            break
        attempts += 1
        if success:
            successes += 1
    total = len(keys)
    final_message = '{successes}/{total} right!'.format(successes=successes,total=total)
    print(final_message)
    results_file_name = 'results.log'
    file = open(results_file_name, 'a')
    with open_file as file_: # underscore after name signals builtin 
        file_.write(final_message + '\n') #do not have to close file: context manager will close for us, if there's error will close file 
        



if __name__ == '__main__':
    main()

