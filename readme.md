# KJV Bible Project/Application:


## Had to put this on hold due to school.


### Under GitHub's 'No Licence' Policy:


**All rights are retained to this source code by the author zweatshirt (Zachery Linscott).  
No one may reproduce, distribute, or create derivative works from this repository.**

For questions about potentially collaborating feel free to message me at zach7307@gmail.com

## Goal of Project:
The goal of this project is to create an interactive mobile application 
centered around the 1611 King James Bible. 
The application will include:
1. A (free) reader of the bible.
2. Ability to press on words as you read to get immediate definitions,   
and a list of other verses where the word is located in the bible.
3. A stand-alone dictionary of all the words.
4. Phrase searching using an NLP library. 
5. Ability to get counts of all word occurrences. 
Occurrences will be countable by the entire bible, by book, and by chapter.
6. Ability to bookmark verses.
7. A standalone Strong's Concordance


## What is finished: 
Two dictionary datasets:
1. "Dictionary One" that allows O(1) accessing to any verse, chapter, or book of the bible. 
2. "Dictionary Two" of all words in the bible, with (most) definitions successfully mapped,
   all verses where that word appears, the total occurences of the word,
   and the total occurences of the Strongs.
   - These dictionaries are designed to interact with one another.
   - Dictionary Two contains the keys to access Dictionary One for accessing a list of all verses that contain the key word in O(n) time.
      - Can probably be sped up to O(log(n)) or something...
Real time database:
     - intend to load the database in on the site by chunks and categories to reduce computational and spatial complexity issues
Skeleton of the Flutter web application (it just needs to be populated with data, then front end work)

Script to access definitions API:
 - the current API used will need to be replaced ASAP (I am implementing ChatGPT API), it doesn't support many Old English words
[Free Dictionary API](https://dictionaryapi.dev)


## Work to be finished:
1. Implementing OpenAI API to find word definitions that the current API is unable to find.
2. An NLP library needs to be implemented for phrase searching still.
3. The front end work that needs to be finished:
   - Currently, a Flutter application exists but needs to populated with the data from the DB.
   - Standalone dictionary for definitions
   - Click on words to retreive definitions and other locations
   - Verse searching field


## Special thanks to:
1. Jesus for saving me and motivating me daily to put forth light and love into the world.
2. [meetDeveloper](https://github.com/meetDeveloper?tab=repositories), 
the creator of [Free Dictionary API](https://dictionaryapi.dev). 
This is an excellent API for getting word definitions for free.
