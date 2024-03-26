def longest_sequence(input_list):
    sorted_list = sorted(set(input_list))
    result = []

    for i in range(len(sorted_list)):
        current_sequence = [sorted_list[i]]

        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] == current_sequence[-1] + 1:
                current_sequence.append(sorted_list[j])

        if len(current_sequence) > len(result):
            result = current_sequence

    return result


def validate_input(input_str):
    input_str = input_str.replace(",", " ").split()
    for elem in input_str:
        if not elem.lstrip('-').isdigit():
            return False
    return True


# Ввод списка с консоли с проверкой
input_list_str = input("Введите список чисел через запятую: ")
while not validate_input(input_list_str):
    print("Пожалуйста, введите только числа через запятую.")
    input_list_str = input("Введите список чисел через запятую: ")

input_list = [int(x) for x in input_list_str.replace(",", " ").split()]

result = longest_sequence(input_list)
print("Максимально длинный новый список с числами, идущими по порядку:", result)