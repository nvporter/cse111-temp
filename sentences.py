import random
words = ["boy", "girl", "cat", "dog", "bird", "house"]
word = random.choice(words)

'''
Grammatical Number	Verb Tense
a.	single	past
b.	plural	past
c.	single	present
d.	plural	present
e.	single	future
f.	plural	future

a determiner
a noun
a verb
a prepositional phrase
'''
''''''
def main():
    for i in range(6):
        gramaticalNum = 2
        tense = "past"

        if(i%2==0):
            gramaticalNum = 1

        if(i>1 and i<4):
            tense = "present"
        if(i>3):
            tense = "future"

        print(get_determiner(gramaticalNum) + " " + get_noun(gramaticalNum) + " " + get_verb(gramaticalNum, tense))
    for i in range(6):
        gramaticalNum = 2
        tense = "past"


        if(i%2==0):
            gramaticalNum = 1

        if(i>1 and i<4):
            tense = "present"
        if(i>3):
            tense = "future"

        print(get_determiner(gramaticalNum) + " " + get_noun(gramaticalNum) + " " + get_verb(gramaticalNum, tense) + " " + get_prepositional_phrase(gramaticalNum))


    
    



def get_determiner(grammatical_number):
    
    if grammatical_number == 1:

        determiner = ["the", "a", "one", "two", "some", "many",1]
        random.choice(determiner)
        

    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    
    output = ""

    if grammatical_number == 1:
        noun = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
        output = random.choice(noun)
        
    else:
        plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
        output = random.choice(plural_nouns)
        
    return output
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

def get_verb(grammatical_number, tense):
    output = ""
    if tense == "past":
        past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        output = random.choice(past_verbs)
        

    elif tense == "present" and grammatical_number == 1:
        present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        output = random.choice(present_verbs)
        
    elif tense == "present" and grammatical_number != 1:
        weird_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        output = random.choice(weird_present_verbs)
        
    elif tense == "future":
        future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        output = random.choice(future_verbs)
        
    else: 
        print("Enter valid answer")
    return output
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    

def get_preposition():
    output = ""
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without" ]
    output = random.choice(preposition)
    
    return output
    
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
def get_prepositional_phrase(quantity):
    return get_preposition() + " "+  get_determiner(quantity) + " " + get_noun(quantity)
    

    
    
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
main()