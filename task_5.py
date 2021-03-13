def my_sum():
    escape = False
    answer = 0
    while escape == False:
        user_num = input('enter numbers or q for exit').split()
        itm_answer = 0
        for num_1 in user_num:
            if 'q' in num_1:
                escape = True
                break
            itm_answer += int(num_1)
        answer += itm_answer
    return answer

