def reconstructQueue(people):
    people = sorted(people, key=lambda x: (-x[0], x[1]))
    i = 0
    while i < len(people):
        if i > people[i][1]:
            people.insert(people[i][1], people[i])
            people.pop(i + 1)
        i += 1
    return people


print(reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
print(reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
