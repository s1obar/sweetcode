def longestCommonPrefix(strs) -> str:
    l = list(zip(*strs))    
    prefix = ""
    for i in l:
        if len(set(i))==1:
            prefix += i[0]
        else:
            break
    return prefix




  #  res = ""

   # for i in range(len(strs[0])):
    #    for s in strs:
     #       if i == len(s) or s[i] != strs[0][i]:
      #          return res
       # res += strs[0][i]
    
 #   return res