s="radkar"
def solution(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            print(f"I ran {s[i],s[n-i-1],n-i-1}")
            left = s[:i] + s[i+1:]
            right = s[:n-i-1] + s[n-i:]
            return left == left[::-1] or right == right[::-1]
    return True
print(solution(s))