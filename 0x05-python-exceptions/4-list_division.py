#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            try:
                result = my_list_1[1] / my_list_2[i]
                if not isinstance(result, (int, float)):
                    raise TypeError("Wrong type")
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except TypeError:
                result = 0
                print("Wrong type")
        except IndexError as e:
            print(e)
            result = 0
        finally:
            result_list.append(result)
    return result_list
