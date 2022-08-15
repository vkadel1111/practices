
def solution(s):

   largest = get_palindromes(s)
   while len(get_palindromes(s))>2:
       s=s.replace(get_palindromes(s),"",1)
       print(s)
   return s

def get_palindromes(s):
    ongoing = ""
    palis = []
    biggest = ""
    for e in s:
        ongoing+=e
        if ongoing==ongoing[::-1]:
            palis.append(ongoing)
            if len(ongoing)>=len(biggest):
                biggest=ongoing
    print(ongoing)
    return biggest

if __name__ == '__main__':
    solution("aaacodedoc")
