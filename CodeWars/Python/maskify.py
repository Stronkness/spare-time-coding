# return masked string
def maskify(cc):
    if(len(cc) <= 4):
        return cc
    else:
        temp = list(cc)
        for i in range(len(cc)-4):
            temp[i] = '#'
        string = ''.join(temp)
        return string
      
# Better solution: return "#"*(len(cc)-4) + cc[-4:]
