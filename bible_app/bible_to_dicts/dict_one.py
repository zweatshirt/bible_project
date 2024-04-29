from bible_to_dicts.bible_dictionary import BibleDictionary


# bible -> book -> chapter -> verse -> words
class DictOne(BibleDictionary):
    def __init__(self, bible_lst):
        """
            BibleDictionary inherits from UserDict, which is a wrapper of the dict class.
            To access the actual dictionary of UserDict we must use the data instance var.
        """
        super().__init__()
        # initialize dictionary. Read bible_to_dict for more information.
        self.data = self.bible_to_dict(bible_lst)


    @staticmethod
    def clean_verse(verse):
        return ' '.join([word[0] for word in verse])


    @staticmethod
    def pprint_verse(verse):
        print(DictOne.clean_verse(verse))


    # write
    def pprint_chapter(self, chapter):
        for key in self.yield_all_keys(chapter):
            pass


    @staticmethod
    def num_chapters(dct):
        return len(dct)


    def bible_to_dict(self, b_lst):
        """
            Initializing method returning nested dict of 
            the entire bible mapped by book, chapter, and verse.
        """
        bible_dict = {}
        book = chapter = verse_num = None
        verse = []

        for i, word in enumerate(b_lst):

            word, strongs = self.separate_strongs(word)

            if (word == 'Chapter' or word == 'Psalm') and b_lst[i + 1].isdigit():

                chapter = int(b_lst[i + 1])
                if chapter == 1:
                    book = self._book_name_helper(b_lst, i)

                self._add_book_to_dict(bible_dict, book)
                self._add_ch_to_dict(bible_dict, book, chapter)

            if i == len(b_lst) - 1:  # if last word in bible
                verse.append((word, strongs)) if strongs else verse.append((word))
                return bible_dict

            # look at any word that isn't a chapter, psalm, or book title
            if not self._is_book(book, word, b_lst[i + 1]) and not self._is_ch(word, b_lst[i + 1]):
                
                if word.isdigit():
                    verse_num = int(word)
                    verse = []  # reset verse list for every new verse num
                else:
                    verse.append((word, strongs)) if strongs else verse.append((word))
 
            # get rid of occurrences where book names end up at end of verse
            if self._b_name_at_end(b_lst, i):
                verse.pop()

            if verse:
                self._add_verse_to_dict(bible_dict, book, chapter, verse_num, verse)

        return bible_dict


    ''' helper methods for bible_to_dict() '''
    def _add_book_to_dict(self, bible_dict, book):
        if book and book not in bible_dict:
            bible_dict[book] = {}


    def _add_ch_to_dict(self, bible_dict, book, chapter):
        if book and chapter and chapter not in bible_dict[book]:
            bible_dict[book][chapter] = {}


    def _add_verse_to_dict(self, bible_dict, book, chapter, verse_num, verse):
        if verse_num and verse_num not in bible_dict[book][chapter]:
            bible_dict[book][chapter][verse_num] = verse


    def _b_name_at_end(self, bible_lst, i):
        """
        Used for the edge case that the next book name is appended to
        the end of the verse of the current book. A bandaid and needs to be improved...
        """
        ch1 = [c + ' 1' for c in self.ch]
        if not i < len(bible_lst) - 2:
            return False
        return True if (f"{bible_lst[i + 1]} {bible_lst[i + 2]}" in ch1) else False
    
    '''end helper methods for bible_to_dict()'''
