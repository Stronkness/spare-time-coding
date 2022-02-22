def square_digits(num):
    answer = ""
    for element in str(num):
        answer += str(int(element)**2)
    return int(answer)
