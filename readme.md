# KJV Bible Project/Application:

### Under GitHub's 'No Licence' Policy:

**All rights are retained to this source code by the author zweatshirt (Zachery Linscott).  
No one may reproduce, distribute, or create derivative works from this repository**

For questions about potentially collaborating feel free to message me at zach7307@gmail.com

## Goal of Project:
The goal of this project is to create an interactive mobile application 
centered around the 1611 King James Bible. 
The application will include:
1. A (free) reader of the bible.
2. Ability to press on words as you read to get immediate definitions,   
and a list of other verses where the word is located in the bible per Strong's Concordance.
3. A stand-alone dictionary of all the words.
4. Phrase searching using an NLP library. 
5. Ability to get counts of all word occurrences. 
Occurrences will be countable by the entire bible, by book, and by chapter.
6. Ability to bookmark verses.
7. A standalone Strong's Concordance

## What is finished:
Much of the backend work is done.  
Everything is put cleanly into data structures (mostly nested dicts) and a JSON file.


### Work to be finished:
The backend work that needs to be finished is using the pickle library
to serialize data to save space and allow for faster querying than JSON.
An NLP libray needs to be implemented for phrase searching still.

The front end work that needs to be finished, is well, the entire actual application.

### Special thanks to:
1. Jesus for saving me and motivating me daily to put forth light and love into the world.
2. [meetDeveloper](https://github.com/meetDeveloper?tab=repositories), 
the creator of [Free Dictionary API](https://dictionaryapi.dev). 
This is an excellent API for getting word definitions for free.
