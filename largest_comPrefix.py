def prefix(strings):
    if not strings:
        return""
    strings.sort()
    first=strings[0]
    last=strings[-1]

    i=0
    while i<len(first) and i<len(last) and first[i] == last[i]:
        i += 1
    return first[:i]
ob= prefix(["first","fir","finally"]) 
print(ob)