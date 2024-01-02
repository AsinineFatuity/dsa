def max_substr(s):
    if len(s)==0:
        return 0
    left,right,max_substr = 0,0,1
    for i in range(1,len(s)):
        if s[i] in s[left:i]:
            left = s[left:i].index(s[i])+left+1
        right = i
        max_substr = max(max_substr,right-left+1)
    return max_substr

