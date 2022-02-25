def solution(number):
    sum = 0;
    for current in range(number):
        if(current % 3 == 0 or current % 5 == 0):
            sum += current;
    
    if(sum < 0):
        return 0;
    else:
        return sum;
      
      # Better solution: return sum(x for x in range(number) if x % == 0 or x % 5 =0 0)
