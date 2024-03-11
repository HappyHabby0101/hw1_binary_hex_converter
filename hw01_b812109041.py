def check_input():
    while True:
        user_input = int(input("請輸入一個為10進位的數字："))
        if user_input < 0 or user_input > 255:
            print("請輸入0-255之間的數字")
            continue
        else:
            return user_input
            
def converter_two(user_input):
    n = 8
    answerlist = []
    while n >= 0:
        if (user_input > 2 ** n) or (user_input == 2 ** n):
            answerlist.append(1)
            user_input -= (2 ** n)
        
        elif user_input < 2 ** n:
            answerlist.append(0)
        
        n -= 1 
        # 確認流程無誤
        # print(answerlist)
        # print(user_input)

    # 刪除多餘的 "0"
    show_list = answerlist.copy()
    for i in range(len( show_list)):
        if show_list[i] == 0:
            show_list.pop(i)
        else:
            break
    
    result_string = ' '.join(str(x) for x in  show_list)
    result_string = result_string.replace(" ", "")  # 去除空格
    print("二進位表示法：" + result_string)

    return result_string
    
def compute_sixteen(two_string):
    code = [1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    store_list = []

    for i in range(0, len(two_string), 4):
        two_string_in4 = two_string[i:i+4]
        num_16form_index = 0
        for j in range(len(two_string_in4)):
            num_16form_index += int(two_string_in4[j]) * (2 ** (len(two_string_in4) - j - 1))

        num_16form = code[num_16form_index-1] 
        store_list.append(str(num_16form))

    sixteen_string = ''.join(store_list)
    print("十六進位表示法：" + sixteen_string)

# TEST 
input_ten = check_input()
result_two = converter_two(input_ten)
result_sixteen = compute_sixteen(result_two)




