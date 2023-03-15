def findNaivy(pattern, text):
    patternLength = len(pattern)
    textLength = len(text)
    postionList = []
    if(patternLength == 0): return 0
    if(textLength == 0): return 0
    if(patternLength > textLength): return -1

    for i in range(textLength - patternLength + 1):
        j = 0
        while j < patternLength:
            if(text[i+j] != pattern[j]):
                break
            j += 1
        if(j == patternLength):
            postionList.append(i)
    return postionList





























