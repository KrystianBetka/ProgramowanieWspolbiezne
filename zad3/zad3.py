import os
import re

def count_word_occurrences(file_name, word):
    stack = [file_name]
    occurrences = 0

    while stack:
        current_file = stack.pop()
        if not os.path.exists(current_file):
            continue

        with open(current_file, 'r') as file:
            content = file.read()
            matches = re.findall(rf'\b{word}\b', content)
            occurrences += len(matches)

            input_directives = re.findall(r'\\input{([^}]*)}', content)
            for directive in input_directives:
                included_file_name = os.path.join(os.path.dirname(current_file), directive)
                stack.append(included_file_name)

    return occurrences

def main():
    p = 'plikA.txt'  # Zmień na nazwę pliku, który chcesz analizować
    s = 'z'  # Zmień na szukane słowo
    total_occurrences = count_word_occurrences(p, s)
    print(f"Total occurrences of '{s}' in the text: {total_occurrences}")

if __name__ == '__main__':
    main()
