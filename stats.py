import string

STOP_WORDS = {
    "that", "with", "this", "they", "from",
    "have", "been", "were", "said", "which",
    "their", "there", "would", "could", "should",
    "about", "after", "before", "where", "while",
    "then", "than", "when", "what", "will",
    "into", "upon", "your", "more", "some",
    "also", "over", "such", "them", "these",
    "those", "very", "much", "must", "shall",
    "each", "even", "only", "just", "like",
    "know", "come", "came", "went", "back",
    "down", "away", "here", "made", "make",
    "take", "took", "look", "looked", "felt",
    "feel", "seem", "seemed", "though", "through",
    "again", "never", "every", "other", "another",
    "still", "being", "having", "doing", "going",
    "without", "because", "between", "against",
    "however", "whether", "nothing", "something",
    "anything", "everything", "himself", "herself",
    "myself", "yourself", "itself", "ourselves",
}

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def sort_on(count):
    return count["num"]

def get_avg_word_length(word_frequency, num_words):
    total = 0
    for word in word_frequency:
        total += len(word) * word_frequency[word]
    avg_word_length = total / num_words
    return avg_word_length

def get_word_frequency(text):
    word_frequency = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        word = word.replace("'", "").replace("’", "").replace(",", "").replace("“", "")
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency

def get_unique_words(word_frequency):
    return len(word_frequency)

def get_top_words(word_frequency, n):
    top_words = []
    for word, num in word_frequency.items():
        if len(word) <= 3 or word in STOP_WORDS:
            continue
        top_words.append({"word": word, "num": num})
    top_words.sort(reverse = True, key = sort_on)
    return top_words[:n]

def get_longest_word(text):
    longest_word = ""
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if not word.isalpha():
            continue
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def get_sentence_count(text):
    sentence_count = 0
    for char in text:
        if char == "." or char == "!" or char == "?":
            sentence_count += 1
    return sentence_count

def get_avg_sentence(sentence_count, num_words):
    avg_sentence = num_words / sentence_count
    return avg_sentence

def get_reading_estimate(num_words):
    total = num_words / 238
    hours = total // 60
    mins = total % 60
    return hours, mins
    




        








        
            
    
