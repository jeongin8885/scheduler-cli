# 검색 후 결과 문자열 만드는 함수
def make_string(schedule_list):
    string = 'id\t|due\t\t|content\t\t|category\t|done\n'
    string += '-' * 80 + '\n'
    done = ['undone', 'done']
    color = ['red', 'green']
    if schedule_list:
        string += 'No result found. To show all schedule, enter \"show all\"'
    for x in schedule_list:
        string += '%-7s |%-14s |%-22s |%-14s |%-15s\n'%(str(x[0]), x[2], x[3], x[1], colored(done[x[4]], color[x[4]]))
    return string.strip()