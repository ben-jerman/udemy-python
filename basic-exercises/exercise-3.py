question_words = ('what', 'which', 'who', 'here', 'why', 'when', 'how', 'whose', 'is')
sentences = []

def is_question(string_in):
    if string_in.split()[0].lower() in question_words:
        return True
    else:
        return False

while True:
    str_input = input('Say something: ')

    if str_input == '\end':
        break

    if is_question(str_input) is True:
        sentences.append(str_input + '?')
    else:
        sentences.append(str_input + '.')

for sentence in sentences:
    print(sentence)