from pyquery import PyQuery as pq


def WhatIs(Item=""):
    Punctuation = [ '.', '?', '!' ]
    
    d = pq(url="https://en.wikipedia.org/wiki/"+str(Item.lower()))
    p = d('p')
    
    p = p.text()
    
    text = ""
    
    for i in p:
        if i in Punctuation:
            text += i
            return text
        else:
            text += i
            
    return "Nothing found"


print(WhatIs("pickleball"))