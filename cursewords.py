def read_text():
    text=open(r"C:\Users\Ciprian\Desktop\Learning Python\cursewordsread.txt")
    content=text.read()
    
    if(cursed(content)):
        print "No curse words"
    else:
        print "you fucker"
def cursed(content):
    list=["shit","cunt","fuck"]
    for word in list:
        
        if(word  in content):
            return False
        
    return True
read_text()
