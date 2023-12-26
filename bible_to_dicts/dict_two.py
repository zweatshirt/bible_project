from bible_to_dicts.bible_dictionary import BibleDictionary


class DictTwo(BibleDictionary):
    def __init__(self, bible_lst: []):
        super().__init__()
        self.data = self.bible_to_dict(bible_lst)

    def bible_to_dict(self, b_lst: []):
        """returns nested dict of all words in the bible."""
        words_dict = {}
        book = chapter = ''
        verse_num = 0

        for i, word in enumerate(b_lst):
            word, strongs = self.separate_strongs(word)

            if (word == 'chapter' or word == 'psalm') and b_lst[i + 1].isdigit():
                chapter = int(b_lst[i + 1])

                if chapter == 1:
                    book = self._book_name_helper(b_lst, i)  # grab book ame

            if not self._is_ch_or_book(b_lst, i, book, word):
                if word.isdigit():
                    verse_num = int(word)  # grab verse num

            self._add_to_dict(words_dict, word, strongs, book, chapter, verse_num)

        return words_dict

    def _add_to_dict(self, words_dict, word, strongs, book, chapter, verse_num):
        """helper method for bible_to_dict(). Adds all the keys and values to the dict"""
        if not word.isdigit():
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

    def get_count_of_word(self, word: str) -> int:
        """returns word occurrence count given a word"""
        print('There is a total of {} occurrences for the word {}.'.format(occurrences := self.data[word][0], word))
        return occurrences

    def get_strongs_count_for_word(self, word: str) -> int:
        """returns the count of all Strong's vals occurrences for a given word"""
        count = 0
        for k in self.data[word][1].keys():
            count += self.data[word][1][k]
        return count

    def get_word_strongs_tuple_for(self, word: str) -> tuple:
        """return the word with a list of all the Strong's val related to the word"""
        return tuple((word, [k for k in self.data[word][1].keys()]))
