from bible_to_dicts.bible_dictionary import BibleDictionary


class DictTwo(BibleDictionary):
    def __init__(self, bible_lst: []):
        super().__init__()
        self.data = self.bible_to_dict(bible_lst)

    # dictionary where words in the KJV bible are key, the value is a list of the occurrence of the word and a nested dictionary
    # of all the Strong's for that given word.
    def bible_to_dict(self, b_lst: []):
        words_dict = {}
        book = chapter = ''
        verse_num = 0

        for i, word in enumerate(b_lst):
            # case only if strong's concordance
            word, strongs = self.separate_strongs(word)

            if (word == 'chapter' or word == 'psalm') and b_lst[i + 1].isdigit():
                # reset verse for every new chapter
                chapter = int(b_lst[i + 1])
                # if chapter name is 1, we can grab the book name one index behind
                if chapter == 1:
                    book = self._book_name_helper(b_lst, i)

            if not self._is_ch_or_book(b_lst, i, book, word):
                if word.isdigit():
                    verse_num = int(word)

            self._add_to_dict(words_dict, word, strongs, book, chapter, verse_num)

        return words_dict

    '''helper method(s) for biblle_to_dict()'''
    def _add_to_dict(self, words_dict, word, strongs, book, chapter, verse_num):
        if not word.isdigit():
            # add word and count if word already in dict
            if word not in words_dict:
                words_dict[word] = [1, {}]
            else:
                words_dict[word][0] += 1

            if strongs:
                for s in strongs:
                    if s not in words_dict[word][1]:
                        words_dict[word][1][s] = [1, []]
                    elif s in words_dict[word][1]:
                        words_dict[word][1][s][0] += 1
                    if book and chapter and verse_num:
                        words_dict[word][1][s][1].append([book, chapter, verse_num])
    '''end helper method(s) for bible_to_dict()'''

    '''returns word occurrence count given a word'''
    def get_count_of_word(self, word: str) -> int:
        print('There is a total of {} occurrences for the word {}.'.format(occurrences := self.data[word][0], word))
        return occurrences

    # count total number of a specific Strong's given a word
    def get_strongs_count_for_word(self, word: str) -> int:
        count = 0
        for k in self.data[word][1].keys():
            count += self.data[word][1][k]
        return count

    # iterates through dictionary to count and returns the occurrences of each Strong's given any word
    def get_word_strongs_tuple_for(self, word: str) -> tuple:
        return tuple((word, [k for k in self.data[word][1].keys()]))
