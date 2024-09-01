import string

split_contents = ""
alphabet = string.ascii_lowercase
alphabet_count = {}

def main():
    file_contents = ""
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    except Exception as e:
        print(e)

    number_of_words = GetString(file_contents)
    chars = CountChars(file_contents)
    sorted_dict = convert_to_list_of_dicts(alphabet_count)
    sorted_dict.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of books/frankenstein.txt ---\n{number_of_words} found in the document\n\n")
    
    for item in sorted_dict:
        char = item['char']
        num = item['num']
        print(f"The '{char}' character was found {num} times")

def GetString(file_contents):
    split_contents = file_contents.split()
    return len(split_contents)

def CountChars(split_contents):
    lowered_string = split_contents.lower()

    key = 0

    for char in alphabet:
        char_count = 0

        for letter in lowered_string:
            
            if (char == letter):
                char_count += 1

        alphabet_count[alphabet[key]] = char_count
        key += 1
    return alphabet_count

def convert_to_list_of_dicts(alphabet_count):
    char_list = []
    for char, num in alphabet_count.items():
        char_dict = {'char': char, 'num': num}
        char_list.append(char_dict)
    return char_list

def DictionaryList(alphabet_count):
    return alphabet_count["num"]

def sort_on(dict):
    return dict["num"]

if __name__ == "__main__":
    main()