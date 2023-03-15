def findKMP(pattern: str, text: str):
    patternLength = len(pattern)
    textLength = len(text)
    postionList = []

    if(patternLength == 0): return 0
    if(textLength == 0): return 0
    if(patternLength > textLength): return -1

    lps = [0] * patternLength
    previousLPSlen = 0
    indexLPS = 1

    while indexLPS < patternLength:
        if pattern[previousLPSlen] == pattern[indexLPS]:
            previousLPSlen += 1
            lps[indexLPS] = previousLPSlen
            indexLPS += 1
        elif previousLPSlen == 0:
            lps[indexLPS] = 0
            indexLPS += 1
        else:
            previousLPSlen = lps[previousLPSlen - 1]

    indexText = 0
    indexPattern = 0
    while (textLength - indexText) >= (patternLength - indexPattern):
        if text[indexText] == pattern[indexPattern]:
            indexText += 1
            indexPattern += 1

        if indexPattern == patternLength:
            postionList.append(indexText - patternLength)
            indexPattern = lps[indexPattern - 1]

        elif indexText < textLength and pattern[indexPattern] != text[indexText]:
            if indexPattern != 0:
                indexPattern = lps[indexPattern - 1]
            else:
                indexText += 1

    return postionList















