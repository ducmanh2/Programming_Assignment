def next_string(s):
    s=list(s)
    if all(c =='d' for c in s):
        return 'a'* (len(s)+1)
    for i in range(len(s)-1,-1,-1):
        if s[i] != 'd':
            s[i]=chr(ord(s[i])+1)
            break
    
        else :
            s[i]='a'
            s[i-1]=chr(ord(s[i-1])+1)
            break 
    return "".join(s)
  
print(f'chuoi tiep theo la:',next_string('abd'))
