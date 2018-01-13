easy_lib = 'HTML is the standard markup __1__ for creating web pages and web applications. With __2__ Style Sheets (CSS) and JavaScript it forms a triad of cornerstone technologies for the World Wide Web. __3__ browsers receive HTML documents from a web server or from local storage and render them into multimedia web pages. HTML elements are the building __4__ of HTML pages and are delineated by __5__, written using angle brackets.'
easy_answer = ['language', 'cascading', 'web', 'blocks', 'tags']

medium_lib = 'SQL stands for Structured __1__ Language. SQL is used to communicate with a __2__. According to ANSI (American National Standards Institute), it is the standard language for __3__ database management systems. SQL statements are used to perform tasks such as update data on a database, or __4__ data from a database. It is also used for __5__ creation and modification, and data access control.'
medium_answer = ['query', 'database', 'relational', 'retrieve', 'schema']

hard_lib = 'Python is a widely used high-level __1__ language for general-purpose programming. An __2__ language, Python has a design philosophy that emphasizes code __3__ (notably using __4__ indentation to delimit code blocks rather than curly brackets or keywords), and a __5__ that allows programmers to express concepts in fewer lines of code. The language provides constructs intended to enable writing clear programs on both a small and large scale.'
hard_answer = ['programming', 'interpreted', 'readability', 'whitespace', 'syntax']

def get_difficulty():
  '''Prompt the user to provide the difficulty level.
  If invalid response is given, will prompt the user again
  Input:  difficulty - 'easy', 'medium' or 'hard'
  Output: lib        - return mad_lib chosen based on difficulty
          answers    - return answers chosen based on difficulty'''
  
  difficulty = raw_input('Please select a difficulty level (easy, medium, hard): ')
  if difficulty.lower() == 'easy':
    lib = easy_lib
    answers = easy_answer
    return lib, answers
  if difficulty.lower() == 'medium':
    lib = medium_lib
    answers = medium_answer
    return lib, answers
  if difficulty.lower() == 'hard':
    lib = hard_lib
    answers = hard_answer
    return lib, answers
  else:
    print 'You selected an invalid difficulty level'
    return get_difficulty()

def get_max_try():
  '''Let the user specify how many attempts to be given.
  If it is not a positive integer after conversion, will prompt again.
  Input:  max_input - string
  Output: max_try - change max_input into integer'''
  
  max_input = raw_input('Please indicate maximum attempts for this quiz: ')
  max_try = int(max_input)
  if type(max_try) != int:
    print 'You selected an invalid number of attempts'
    return get_max_try()    
  if max_try < 1:
    print 'You selected an invalid number of attempts'
    return get_max_try()
  else:
    return max_try

def check(blank_number, lib, answer, answers, max_try):
  '''Check the guesses whether they are correct. If so, will replace the __X__ with answer.
  Else, will prompt the user for answer again and deduct the number of attempts by 1.
  
  Input:  blank_number - starts with 1st one '__1__' and incrementing up to 5th
          lib          - the mad_lib chosen
          answer       - answer of that particular blank_number
          answers      - list of answers based on difficulty chosen
          max_try      - number of attempts chosen, will decrease with wrong answers given
  Output: lib          - updated madlib based on the progress 
          blank_number - return the progress, if 3 means first 2 were answered correctly
          status       - True if game still going on, False if game over.'''
  
  blank_box = '__' + str(blank_number) + '__'
  guess = raw_input('Please enter the answer for __' + str(blank_number) + '__: ')
  if guess == answer:
    lib = lib.replace(blank_box, answer)
    print lib + '\n'
    blank_number += 1
    return (lib, blank_number, True)
  else:
    while max_try >1:
      print 'Try again.\n'
      max_try -= 1
      print 'You have ' + str(max_try) + ' attempts left.'
      return check(blank_number, lib, answer, answers, max_try)
    return (lib, blank_number, False)

def play_game():
  '''Prompt difficulty, number of attempts, answers and repeat until game over or completed
  If status returns false, end game.
  If game completed, print congratulation statement.'''
  
  lib, answers = get_difficulty()
  max_try = get_max_try()
  print '\n' + lib + '\n' + str(max_try) + ' attempts left' + '\n'
  
  blank_number = 1
  for answer in answers:
    lib, blank_number, status = check(blank_number, lib, answer, answers, max_try)
    if status == False:
        print 'Game Over.'
        return False
  print ('Congratulations, you have completed the challenges!')

play_game()