import json

with open('morse_code.json', 'r') as f:
    morse_dict = json.load(f)

morse_dict_reverse = dict()
for key in morse_dict.keys():
    morse_dict_reverse[morse_dict[key]] = key


def convert_text_to_code_morse(text):
    list_words = text.split(' ')
    list_words_code_morse = []
    for word in list_words:
        code_morse_word = ' '.join(map(lambda x: morse_dict[x.upper()], word))
        list_words_code_morse.append(code_morse_word)
    
    return '   '.join(list_words_code_morse)



def convert_code_morse_to_text(text):
    list_words_code_morse = text.split('   ')
    list_words = []
    for word in list_words_code_morse:
        text = ''.join(map(lambda x: morse_dict_reverse[x],word.split(' ')))
        list_words.append(text)

    return ' '.join(list_words)

if __name__ == '__main__':

    # choose mode
    while True:
        try:
            mode = int(input("""
Which mode:

1 : convert text to morse code
2 : convert morse code to text
3 : close the program

>>"""))

            if mode not in [1, 2, 3]:
                raise ValueError

        except ValueError:
            print('\n>>Wrong value<<\n')
        else:
            break

    if mode == 1:
        text = input('text >> ')
        print(convert_text_to_code_morse(text))
    elif mode == 2:
        text = input('code morse (one space between letter three space between words) >> ')
        print(convert_code_morse_to_text(text))
    else:
        print('Close the program')