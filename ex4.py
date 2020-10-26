import requests

hyperlink = 'https://jsonplaceholder.typicode.com/todos'
title_in = input()
completed_in = bool(input())


def find_dict(hyperlink, title, completed):
    res = requests.get(hyperlink)
    lst = res.json()
    lstout = []
    for one in lst:
        if title in one['title'] and completed == one["completed"]:
            i = one["id"]
            lstout.append(lst[i - 1])
    return lstout


for i in find_dict(hyperlink, title_in, completed_in):
    print(i)

