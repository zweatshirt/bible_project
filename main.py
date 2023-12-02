# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
import string


# bible -> book -> chapter -> verse
def read_bible(f_name: str) -> str:
    with open(f_name, encoding='utf-8') as file:
        bible_data = file.read()
    return bible_data


def remove_strongs(word: str) -> (str, str):
    strongs = ''
    if '{' in word:
        strongs = tuple(re.findall('\{.*?\}', word))
        word = re.sub('\{.*?\}', '', word)
    return word, strongs


# turn into more complex nested list bible -> book -> chapter -> verse -> words
def bible_to_dict(bible: str) -> {}:
    strip = string.punctuation.replace('{', '').replace('}', '')
    cleaned_words = bible.lower().translate(str.maketrans('', '', strip)).split()

    # bible_list = [[[]]]  # books -> chapters -> verses
    bible_dict = {}
    book = None
    chapter = None
    verse_num = None
    verse = []

    len_words = len(cleaned_words)

    for i, word in enumerate(cleaned_words):
        if word == 'chapter' or word == 'psalm' and cleaned_words[i + 1].isdigit():

            # reset verse for every new chapter
            verse = []

            # get chapter name
            chapter = int(cleaned_words[i + 1])

            # if chapter name is 1, we can grab the book name one index behind
            if chapter == 1:
                book = cleaned_words[i - 1]

                # add book to bible_dict
                if book and book not in bible_dict:
                    bible_dict[book] = {}

            # add chapter to bible_dict[book]
            if book and chapter not in bible_dict[book]:
                bible_dict[book][chapter] = {}

        # final word of bible case
        if i == len_words - 1:
            word, strongs = remove_strongs(word)
            verse.append(word)
            break

        # look at anything that isn't a chapter, psalm, or book title
        if ((word != 'chapter' or word != 'psalm') and not cleaned_words[i + 1].isdigit()) and cleaned_words[
            i - 1] != book and i != 0:

            # check for Strongs, save, and remove from word
            word, strongs = remove_strongs(word)

            # if word is a verse num
            if word.isdigit():
                verse_num = int(word)
                # reset verse list for every new verse num
                verse = []
            else:
                # add word to verse list
                verse.append(word)

            if verse_num not in bible_dict[book][chapter]:
                bible_dict[book][chapter][verse_num] = verse

    return bible_dict

    # change this to search a "words to strong dict" and "word counter" dict of the overall bible list
    # def words_to_dict(words_list: []) -> {}:
    #
    #     words_dict = {}
    #
    #     for word in words_list:
    #         strongs = None
    #         # case only if strong's concordance
    #         if '{' in word:
    #             strongs = tuple(re.findall('\{.*?\}', word))
    #             word = re.sub('\{.*?\}', '', word)
    #
    #         if word not in words_dict:
    #             words_dict[word] = [1, {}]
    #         else:
    #             words_dict[word][0] += 1
    #
    #         if strongs:
    #             for s in strongs:
    #                 if s not in words_dict[word][1]:
    #                     words_dict[word][1][s] = 1
    #                 elif s in words_dict[word][1]:
    #                     words_dict[word][1][s] += 1
    #     return words_dict


# returns word occurrence count
def occ(word: str, bible_dict: {}) -> int:
    return bible_dict[word][0]


def total_strongs(word: str, strongs_dict: {}) -> int:
    keys = strongs_dict[word][1].keys()
    count = 0
    for key in keys:
        count += strongs_dict[word][1][key]
    return count


def strongs_occ_per_word(word: str, strongs_dict: {}):
    for k, v in strongs_dict[word][1].items():
        print('There is a total of {} occurrences of the index {} for the word {}.'.format(word, v, k))
    # keys = words_dict['and'][1].keys()
    # for key in keys:
    #     count += words_dict['and'][1][key]
    # print(count)


# map strongs to words
def strongs_dict():
    ...


if __name__ == '__main__':
    bible = read_bible('kjv_strongs.txt')
    # words_list = bible.lower().replace('.', '').replace(',', '').replace.split()
    bible_dct = bible_to_dict(bible)
    print(bible_dct)

    # print(words_dict)
    # print(total_strongs('god', words_dict))
    # print(strongs_occ_per_word('god', words_dict))

    # keys = words_dict['and'][1].keys()
    # for key in keys:
    #     count += words_dict['and'][1][key]
    # print(count)
