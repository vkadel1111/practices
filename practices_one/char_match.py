def solution(s):
    stack = ""
    while len(s)>0:
        l = s[0]
        s = s[1:len(s)]
        if l!= ")":
            stack += l
        elif l == ")":
            print("Time to look back")
            Notfound = True
            for i in reversed(range(len(stack))):
                if stack[i] =="(" and Notfound:
                    Notfound = False
                    stack=stack[0:i]+stack[i:len(stack)][::-1].replace("(","",1).replace(")","",1)
    return stack





if __name__ == '__main__':
    s = solution("foo(bar(baz))blim")
    solution("foo(bar)baz(blim)")
