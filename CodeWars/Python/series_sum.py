def series_sum(n):
    return str(format(round(sum(1/(1+3*num) for num in range(n)),2),'.2f'))

# str() not needed, automaticlly becomes string when printing to terminal (?)
# format automaticlly rounds up to the decimal stated (in this case 2 decimals), round() is not needed
