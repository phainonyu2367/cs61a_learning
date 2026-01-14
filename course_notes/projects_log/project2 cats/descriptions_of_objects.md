
## Phase 1 Typing
#### choose
"""takes a lists of strings and returns the kth paragragh which 'select' returns true"""

- parameters * 3
	- paragraghs (list: string)
	- select (func)
	- k (none negative __index__)

returns the paragraph: string
#### about

"""takes alist of topic words and returns a fuction which takes a paragraph and returns a boolena indicating whether that paragragh contians any of the words in topic"""

using external functions:
- remove_punctuation(s)
>Return a string with the same contents as s, but with punctuation removed.
- lower(s)
>Return a lowercased version of s.
- split(s)
>Return a list of words contained in s, which are sequences of characters separated by whitespace (spaces, tabs, etc.)

parameters:
inner:
- topic: lists
outer:
- paragraghs

returns the function

#### accuracy
"""Return the accuracy (percentage of words typed correctly) of TYPED. when compared to the prefix of REFERENCE that was typed."""

parameters:
- typed: list
- reference: list

special treatment for empty "reference list".

returns: percentage

#### wpm
"""Return the words-per-minute (WPM) of the TYPED string."""

parameters:
- typed: a string
- elapsed: time

simple to understand, but uses 5 as the length of the word and included ' ' into it instead of using the original length of the words and ignoring ' '.

## Phase 2 Autocorrect
#### autocorrect
   """Returns the element of VALID_WORDS that has the smallest difference from USER_WORD. Instead returns USER_WORD if that difference is greater than LIMIT."""

parameters:
- user_word: string
- valid_words: list of string
- diff_function
	- user_word
	- a word from valid_words
	- limit
	- return a number
- limit: int

#### shifty_shifts
   """A diff function for autocorrect that determines how many letter,in START need to be substituted to create GOAL, then adds the difference intheir lengths."""

requirements:
- difference length
- recursion
- difference length limit

parameters:
- start: string
- goal: string
- limit: int

#### pawssible_patches
There are three kinds of edit operations:
1. Add a letter to `start`,
2. Remove a letter from `start`,
3. Substitute a letter in `start` for another.
"""A diff function that computes the edit distance from START to GOAL."""

it is implemented with tree recursion.

## Phase3 multiplayer
#### report_progress
parameters:
- typed: string list
- prompt: string list
- user_id: string
- send: function


#### time_per_word
parameters:
- times_per_player
	- a list of lists for each player with timestamps indicating when each player finished typing each word
- words
	- a list of words

return:
- game
	- a data abstraction that has a list of words and times 
	- time are differences between consecutive timestamps

game constructor:

	Given timing data, return a game data abstraction, which contains a list of words and the amount of time each player took to type each word.