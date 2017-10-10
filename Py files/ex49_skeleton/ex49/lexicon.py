def analyse(word):
    """Analyse the word, return its type based on the dictionary"""
    categories = {
        "direction": ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
        "verb": ['go', 'stop', 'kill', 'eat'],
        "stop": ['the', 'in', 'of', 'from', 'at', 'it'],
        "noun": ['door', 'bear', 'princess', 'carbinet']
    }

    if word.isdigit():
        return "number"

    # Iterate the keys and their corresponding values (list of words)
    for category, word_list in categories.items():
        # If the word is a member of a list, returns the category
        if word in word_list:
            return category

    # If nothing matches, returns error
    return "error"

def scan(sentence):
    """Scan the input sentence, split them up into list of words"""
    words = sentence.split(' ')
    results = []
    for word in words:
        word_category = analyse(word.lower())
        result.append((word_category, word))

    return results
