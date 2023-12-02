from bible_to_structs.helpers import remove_strongs
from pprint import PrettyPrinter


# bible -> book -> chapter -> verse -> words
class PrimaryBibleDict:
    def __init__(self, bible_lst: []):
        self.dict = self.bible_to_dict(bible_lst)

    def bible_to_dict(self, bible_lst: []) -> {}:

        # bible_list = [[[]]]  # books -> chapters -> verses
        bible_dict = {}
        book = None
        chapter = None
        verse_num = None
        verse = []

        len_words = len(bible_lst)

        for i, word in enumerate(bible_lst):

            word, strongs = remove_strongs(word)

            if (word == 'chapter' or word == 'psalm') and bible_lst[i + 1].isdigit():

                # reset verse for every new chapter
                verse = []

                # get chapter name
                chapter = int(bible_lst[i + 1])

                # if chapter name is 1, we can grab the book name one index behind
                if chapter == 1:
                    book = bible_lst[i - 1]

                    # add book to bible_dict
                    if book and book not in bible_dict:
                        bible_dict[book] = {}

                # add chapter to bible_dict[book]
                if book and chapter and chapter not in bible_dict[book]:
                    bible_dict[book][chapter] = {}

            # final word of bible case
            if i == len_words - 1:
                word, strongs = remove_strongs(word)
                verse.append(word)
                break
            print("out", word, "i", bible_lst[i])
            print("out", word, "i + 1", bible_lst[i + 1])
            # look at anything that isn't a chapter, psalm, or book title

            if i != 0 and bible_lst[i - 1] != book:
                if not (word == 'chapter' or word == 'psalm') and not bible_lst[i + 1].isdigit():
                    print("in", word, bible_lst[i])
                    # check for Strongs, save, and remove from word

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
                    if i == 30:
                        break
        return bible_dict

    # def __repr__(self):
    #     pp = PrettyPrinter(depth=4)
    #     pp.pprint(self.dict)
