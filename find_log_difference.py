with open('data/gupdate-exec-chbrowser.log') as file:
    logfile = file.readlines()
    # import ast
    #
    # colors = ast.literal_eval(logfile)
file.close()


def find_log_differences(log):

    target = 'eid:' # target log
    pen_eid = dict()
    last_eid = dict()
    iterator = 0

    for elem in reversed(log):
        if iterator == 0:
            if target in elem:
                holder = elem.split()
                holder = holder[3].split(';')
                x = 0
                y = 1
                for val in holder:
                    key_value = val.split('.')
                    last_eid[key_value[x]] = key_value[y]
                iterator += 1
        elif iterator == 1:
            if target in elem:
                holder = elem.split()
                holder = holder[3].split(';')
                x = 0
                y = 1
                for val in holder:
                    key_value = val.split('.')
                    pen_eid[key_value[x]] = key_value[y]
                iterator += 1
        else:
            continue

    print("Last eid: " + str(last_eid))
    print("Penultimate eid: " + str(pen_eid))

    diff1 = last_eid.copy()
    diff2 = pen_eid.copy()

    for x in last_eid.items():
        for y in pen_eid.items():
            if x == y:
                del diff1[x[0]]
                del diff2[y[0]]

    return diff1, diff2


print(find_log_differences(logfile))
