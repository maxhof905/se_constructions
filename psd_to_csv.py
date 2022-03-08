# convert .psd (parsed format from CorpusSearch) format to csv
import re

with open('CARDS2146.psd') as infile:
    sentence_list = [line.strip() for line in infile]
    # print(sentence_list)


    start_index = [i for i, item in enumerate(sentence_list) if item.startswith('( (IP-MAT')]
    # print(start_index)

    output = []
    prev = 0

    for index in start_index:
        output.append(sentence_list[prev:index])
        prev = index

    output.append(sentence_list[start_index[-1]:])

    se_index = 1
    se_dict = dict()
    for sentence in output:
            for token in sentence:
                if r' se)' in token: # TODO adjust match pattern
                    se_dict[se_index] = token # adjust to innermost label
                    se_index += 1

                word = re.sub(r'\b[A-Z]+\b', '', token)
                # word = re.sub(r'[^A-z]', '', token)

                # word = ''.join(ch for ch in token if not ch.isupper())
                print(token)