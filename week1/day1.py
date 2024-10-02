def linear_search(lst, target):

    for s in range(0, len(lst)):
        if lst[s] == target:
            return s


print(linear_search(["haycorn", "haycorn", "haycorn", "hunny", "haycorn"], "hunny"))
