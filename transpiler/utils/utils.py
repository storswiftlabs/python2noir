from logging import getLogger

log = getLogger(__name__)


def table_format_control(data):
    """
    table_format_control: Format output for list [str]
    inputs:
        data: list[str]
    return:
        new_data: Formatted list [str]
    """
    if type(data) is str:
        data = data.split('\n')
    else:
        all_data = ""
        for element in data:
            all_data += element
        data = all_data.split('\n')
    control = 0
    new_data = []
    prev = ''
    first_key = ''
    last_key = ''
    for index in range(0, len(data)):
        if data[index] != '':
            last_key = data[index].rstrip().lstrip()[-1]
            first_key = data[index].rstrip().lstrip()[0]
        else:
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        if last_key == "}":
            control -= 1
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        if prev == "{":
            control += 1
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        if prev != "{" and first_key == "}":
            control -= 1
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        new_data.append(generate_table(control) + data[index] + '\n')
        prev = last_key
    return new_data


def generate_table(num):
    return '\t' * num
