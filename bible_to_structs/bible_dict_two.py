from bible_to_structs.bible_dict_parent import *


class DictTwo(BibleDictionary):
    def __init__(self, bible_lst: []):
        super().__init__()
        self.data = self.bible_to_dict(bible_lst)

    def bible_to_dict(self, bible_lst: []):
        words_dict = {}

        for word in bible_lst:
            # case only if strong's concordance
            word, strongs = self.remove_strongs(word)

            if word.isdigit() is False:
                if word not in words_dict:
                    words_dict[word] = [1, {}]
                else:
                    words_dict[word][0] += 1

                if strongs:
                    for s in strongs:
                        if s not in words_dict[word][1]:
                            words_dict[word][1][s] = 1
                        elif s in words_dict[word][1]:
                            words_dict[word][1][s] += 1
        return words_dict

    # returns word occurrence count
    def get_word_occ(self, word: str) -> int:
        print('There is a total of {} occurrences for the word {}.'.format(occurrences := self.data[word][0], word))
        return occurrences

    def get_strongs(self, word: str):
        return self.data[word][1]

    def get_total_strongs(self, word: str) -> int:
        keys = self.data[word][1].keys()
        count = 0
        for key in keys:
            count += self.data[word][1][key]
        return count

    def get_strongs_occ_per_word(self, word: str) -> []:
        lst = []
        for k, v in self.data[word][1].items():
            print('There is a total of {} occurrences of the index {} for the word {}.'.format(v, k, word))
            lst.append((k, v))
        # keys = words_dict['and'][1].keys()
        # for key in keys:
        #     count += words_dict['and'][1][key]
        return lst

