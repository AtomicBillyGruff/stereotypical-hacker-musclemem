import os
import re
from os.path import join
import code
import random


def find(files, root):
    for file in files:
        # print(os.path.join(root, file))
        f = open(os.path.join(root, file), encoding="utf8")
        for line in f:
            if re.search('!!', line):
                typelist.append(line)
        f.close()

def run():
    select = str(input("select folder to start or *"))
    # select = '*'
    if select == '*':
        folder = 'vault of fun'
    else:
        folder = select
    root = 'C:/Users/Jake/Documents/'
    vault = 'C:/Users/Jake/Documents/{}'.format(folder)
    for root, dirs, files in os.walk(vault):
        for file in files:
            with open(os.path.join(root, file), encoding='utf-8') as lines:
                linecount = 0
                for line in lines:
                    linecount += 1
                    search = re.findall('!!!!', line)
                    if search:
                        typelist[file + str(linecount)] = line
            lines.close()

    # enumerate resultes

    keys = list(typelist.keys())
    if is_random == 1:
        random.shuffle(keys)
    print("COUNT: ", len(typelist.keys()))
    for key in keys:
        value = typelist[key]
        value = value.strip('!!!!  ')
        print(key)
        print('--------------- -- -')
        print(value)
        yourtype = input('')




        if re.match(value, yourtype):
            randomnum = random.randrange(0,6)
            print(randomnum)
            print(accolades[randomnum])
        #





if __name__ == '__main__':
    accolades = ['Great!, Great Job!', 'Great!', "WONDER!", 'You Did IT!', 'cool!', ':D']
    typelist = {}
    is_random = 1
    run()
