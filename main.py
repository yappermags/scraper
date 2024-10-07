import numpy as np
import time
g = time.time()


with open('Consumer Price Index News Release - 2024 M08 Results.html', 'r') as f:
    html_string = f.read()

def get_element(att,file,att2=''):
    """get_element
    att(str): the attribute/tag you want to find
    file: the file used for 
    """
    counter = 0
    start = "<%s"%att # start block
    end = "/%s>"%att #end block
    walk_att = [[end]] # a list of all the instances and everything inside a certain HTML block
    
    if type(file) == str:
        val = file.splitlines() # if file type is string, split the lines
    elif type(file) == list:
        val = file # if file type is string, keep as-is
    else:
        raise ValueError # if neither, raise error


    for line in val:
        if start in line: # if start block is in line, create new list and add start block to start of list
            walk_att.append([])
            walk_att[-1].append(line)
            counter += 1
        elif end in line or end not in walk_att[-1][-1]: # add end block and anything in between to current list 
            walk_att[-1].append(line)
        else:
            continue

    walk_att.pop(0)
    return walk_att



def get_row_values(start_list,*args):
    """
    """
    # chara = '<br>' #remove line break element; this will be selectable in the function in the future
    # row_num = 0
    final = []
    # # for y in range(len(start_list)): # iterates through every line in the list
    # for x in start_list[1]: # replaced <br> with a space
    #     if chara in x:
    #         # print(x)
    #         start_list[1][0] = x.replace(chara, ' ')
    final.append([])
    # print(start_list)
    count = 0
    for x in start_list:
        # print(x)
        n = 1
        if args[0] in x or args[1] in x:
            final.append([])
            for y in x:
                if y == '>':
                    n = 0
                elif '<' in y:
                    n = 1
                elif n == 0:
                    final[count] += y
                    final[count] = ''.join(final[count])
            count += 1
    # print(final = np.reshape())
    return final

table = get_element("table",html_string)
thead = get_element("thead",table[0])
tbody = get_element("tbody",table[0])

val = get_row_values(tbody[0],'th','td')

print(val)


