from bible_to_dicts.bible_dictionary import *


class DictTwo(BibleDictionary):
    def __init__(self, bible_lst: []):
        super().__init__()
        self.data = self.bible_to_dict(bible_lst)

    # dictionary where words in the KJV bible are key, the value is a list of the occurrence of the word and a nested dictionary
    # of all the Strong's for that given word.
    def bible_to_dict(self, bible_lst: []):
        words_dict = {}

        for word in bible_lst:
            # case only if strong's concordance
            word, strongs = self.separate_strongs(word)

            # don't want to add chapter and verse numbers
            if word.isdigit() is False:
                # add word and count if word already in dict
                if word not in words_dict:
                    words_dict[word] = [1, {}]
                else:
                    words_dict[word][0] += 1

                # if there is a Strong's add it to the word's nested dictionary as a key
                # and count it if the Strong's already exists for the word
                if strongs:
                    for s in strongs:
                        if s not in words_dict[word][1]:
                            words_dict[word][1][s] = 1
                        elif s in words_dict[word][1]:
                            words_dict[word][1][s] += 1

        return words_dict

    # returns word occurrence count given a word
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
