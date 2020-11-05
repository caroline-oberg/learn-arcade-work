import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    my_file = open("dictionary.txt")

    dictionary_list = []

    for line in my_file:

        line = line.strip()

        dictionary_list.append(line)

    my_file.close()

    # --- Linear search
    print("Linear Search")
    my_file = open("AliceInWonderLand200.txt")

    line_number = 0

    for line in my_file:
        line_number += 1
        word_list = split_line(line)

        for word in word_list:
            key = word.upper()

            current_list_position = 0

            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:
                current_list_position += 1

            if current_list_position == len(dictionary_list):
                print("Line", line_number, "The word misspelled is", word)

    my_file.close()


    print("Binary Search")
    my_file = open("AliceInWonderLand200.txt")

    line_number = 0

    for line in my_file:
        line_number += 1
        word_list = split_line(line)

        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list)-1
            found = False

            while lower_bound <= upper_bound and not found:


                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line", line_number, "The word misspelled is", word)

    my_file.close()
main()