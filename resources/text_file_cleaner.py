import string

digits = string.digits


def file_clean_with_start_num(lines):
    cleaned_lines = []
    for line in lines:
        if line[0] in digits:
            slice_index = line.find('"')
            cleaned_lines.append(line[slice_index:])
    return cleaned_lines


def file_clean_with_one_words(lines):
    cleaned_lines = []
    for line in lines:
        if len(line) < 20 and line != '\n':
            cleaned_lines.append(line)
    return cleaned_lines


with open('positive_adjectives.txt', 'r') as input:
    lines = input.readlines()
    cleaned_lines = file_clean_with_one_words(lines)

with open('positive_adjectives_cleaned.txt', 'w') as output:
    output.writelines(cleaned_lines)