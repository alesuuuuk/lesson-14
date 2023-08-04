# # #  task 1

if __name__ == "__main__":
    # while True:
    #
    #     try:
    #         temp_num = 1
    #         factorial_num = int(input("Введітть додатнє число, щоб я вивів вам його факторіал"))
    #         if factorial_num <= 0:
    #             print("з цього числа не можна добути факторіал ")
    #         else:
    #             for i in range(faktorial_num):
    #                 temp_num *= faktorial_num
    #                 factorial_num -= 1
    #             print(temp_num)
    #             choice = input("Введіть ex щоб вийти з програми ")
    #             if choice == "ex":
    #                 break
    #     except ValueError:
    #         print("Вводити можна лице цифри, спробуйте ще раз")


# # # task 2 version 1


    # def factorial_ver_first(num):
    #     temp_num = 1
    #     for i in range(num):
    #         temp_num *= num
    #         num -= 1
    #     return temp_num
    #
    #
    # while True:
    #
    #     try:
    #
    #         factorial_num = int(input("Введітть додатнє число, щоб я вивів вам його факторіал"))
    #         if factorial_num <= 0:
    #             print("з цього числа не можна добути факторіал ")
    #         else:
    #             print(factorial_ver_first(faktorial_num))
    #         choice = input("Введіть ex щоб вийти з програми ")
    #         if choice == "ex":
    #             break
    #     except ValueError:
    #         print("Вводити можна лице цифри, спробуйте ще раз")
    #


# # #  task 2 version 2

    # def factorial_ver_second(num):
    #
    #     temp_num = 1
    #     if num <= 0:
    #         return "з цього числа не можна добути факторіал "
    #     else:
    #         for i in range(num):
    #             temp_num *= num
    #             num -= 1
    #         return temp_num
    #
    #
    # while True:
    #     try:
    #         factorial_num = int(input("Введітть додатнє число, щоб я вивів вам його факторіал"))
    #         print(factorial_ver_second(factorial_num))
    #         choice = input("Введіть ex щоб вийти з програми ")
    #         if choice == "ex":
    #             break
    #     except ValueError:
    #         print("ВВодити можна лице цифри, спробуйте ще раз")


    # # # task 3
    num_arr = [45, 42, 76, -89, 23333, 654]


    while True:
        # start program
        try:
            temp_num = int(input("Ввведіть число "))
            num_arr.append(temp_num)
            choice = input("stop - щоб перестати заповнювати числа ")
            if choice == "stop":
                break
        except ValueError:
             print("ВВодити можна лице цифри, спробуйте ще раз")



    # main menu
    while True:
        choice = input("Введіть 1 - щоб подивитись увесь список чисел, 2 - щоб побачити максимальне значення спиcку"
                       " 3 - мінімальне, 4 - за індексом побачити значення, 5 - щоб видалити за індексом, ex - exit")


        # see all arr
        if choice == "1":
            print(num_arr)


        # max num ain arr
        elif choice == "2":
            print(max(num_arr))


        # min num in arr
        elif choice == "3":
            print(min(num_arr))


        # see number with index
        elif choice == "4":
            try:
                index = int(input("ВВедіть індекс числа "))
                if index > len(num_arr) or index < 1:
                    print("такого значення не зайдено, спрпобуйте ще раз ")
                else:
                    print(num_arr[index-1])
            except ValueError:
                print("Вводити можна лише цілі цифри")


        # pop num with index
        elif choice == "5":
            try:
                index = int(input("ВВедіть індекс числа "))
                if index > len(num_arr) or index < 1:
                    print("такого значення не зайдено, спрпобуйте ще раз ")
                else:
                    num_arr.pop(index-1)
            except ValueError:
                print("Вводити можна лише цілі цифри")


        # program exit
        elif choice == "ex":
            break


        # no value found
        else:
            print("такого значення не знайдено спробуйте ще раз ")


    # # #  task

    def i_really_dont_know_how_to_name_this_fun(nums_arr):
        while True:
            choice = input("Введіть 1 - щоб подивитись увесь список чисел, 2 - щоб побачити максимальне значення спиcку"
                           " 3 - мінімальне, 4 - за індексом побачити значення, 5 - щоб видалити за індексом, ex - exit")

            # see all arr
            if choice == "1":
                print(num_arr)


            # max num ain arr
            elif choice == "2":
                print(max(num_arr))


            # min num in arr
            elif choice == "3":
                print(min(num_arr))


            # see number with index
            elif choice == "4":
                try:
                    index = int(input("ВВедіть індекс числа "))
                    if index > len(num_arr) or index < 1:
                        print("такого значення не зайдено, спрпобуйте ще раз ")
                    else:
                        print(num_arr[index - 1])
                except ValueError:
                    print("Вводити можна лише цілі цифри")


            # pop num with index
            elif choice == "5":
                try:
                    index = int(input("ВВедіть індекс числа "))
                    if index > len(num_arr) or index < 1:
                        print("такого значення не зайдено, спрпобуйте ще раз ")
                    else:
                        num_arr.pop(index - 1)
                except ValueError:
                    print("Вводити можна лише цілі цифри")


            # program exit
            elif choice == "ex":
                return


            # no value found
            else:
                print("такого значення не знайдено спробуйте ще раз ")

    while True:
        # start program
        try:
            temp_num = int(input("Ввведіть число "))
            num_arr.append(temp_num)
            choice = input("stop - щоб перестати заповнювати числа ")
            if choice == "stop":
                i_really_dont_know_how_to_name_this_fun(num_arr)
                break
        except ValueError:
            print("ВВодити можна лице цифри, спробуйте ще раз")