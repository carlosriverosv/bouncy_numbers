# This code finds the number at which the percentage of bouncy numbers is 99%


def bouncy_numbers(percentage):
    percentage = percentage / 100
    bouncy_percentage = 0
    number = 99
    b_numbers = 0
    while bouncy_percentage < percentage:
        number += 1
        number_list = list(str(number))
        cond1 = cond2 = False
        for i in range(len(number_list) - 1):
            diff = int(number_list[i]) - int(number_list[i + 1])
            if diff < 0:
                cond1 = True
            elif diff > 0:
                cond2 = True
            if cond1 and cond2:
                b_numbers += 1
                bouncy_percentage = b_numbers / number
                break
    print('At number ' + str(number) + ' you get ' + str(percentage * 100) + ' % ' + ' of bouncy numbers')


if __name__ == '__main__':
    bouncy_numbers(float(input('Introduce the percentage of bouncy numbers that you want: ')))
