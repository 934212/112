s = input()
st = ''
for i in range(len(s)):
    if s[i] != '@':
        st += s[i]
    else:
        break
print(st)