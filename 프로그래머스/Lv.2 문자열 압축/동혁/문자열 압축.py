def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        word=''
        stack=[]

        for j in range(0,len(s)+i-1,i):
            # print(s[j:j+i],stack,word)
            if not stack:
                stack.append(s[j:j+i])
            elif s[j:j+i] == stack[0]:
                stack.append(s[j:j+i])
            else:
                if len(stack)!=1:
                    # print(stack)
                    word += str(len(stack)) + str(stack[0][:i])
                else:
                    word += str(stack[0][:i])
                stack=[]
                stack.append(s[j:j + i])

        if len(stack) != 1:
            word += str(len(stack)) + str(stack[0][:i])
        else:
            word += str(stack[0][:i])

        if answer>len(word):
            answer=len(word)
    return answer