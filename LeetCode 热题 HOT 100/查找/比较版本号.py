def compare(version1, version2):
    version1 = list(map(int, version1.split(".")))
    version2 = list(map(int, version2.split(".")))

    if len(version1) > len(version2):
        for _ in range(len(version1) - len(version2)):
            version2.append(0)
    else:
        for _ in range(len(version2) - len(version1)):
            version1.append(0)

    index1, index2 = 0, 0
    while index1 < len(version1) or index2 < len(version2):
        if version1[index1] < version2[index2]:
            return -1
        elif version1[index1] > version2[index2]:
            return 1
        index1 += 1
        index2 += 1
    return 0


print(compare("1.1", "2.1"))
print(compare("1.1", "1.01"))
print(compare("1.1", "1.1.1"))
