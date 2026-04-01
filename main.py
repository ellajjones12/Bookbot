import sys
from stats import (
    get_num_words,
    get_avg_word_length,
    get_word_frequency,
    get_unique_words, 
    get_top_words, 
    get_longest_word, 
    get_sentence_count, 
    get_avg_sentence,
    get_reading_estimate,
)
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, unique_word_count, avg_word_length, top_words, longest_word, sentence_count, avg_sentence, hours, mins):
    book_name = book_path.replace("books/", "").replace(".txt", "")
    print(f"\033[1;95m•┈୨♡୧┈┈୨♡୧┈• BOOKBOT •┈୨♡୧┈┈୨♡୧┈•\033[0m")
    print(f"Analyzing {book_name}")
    print(f"Reading time estimate: {hours:.0f} hours and {mins:.0f} mins")
    print(f"\033[35m♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡\033[0m")
    print(f"Found {num_words:,} total words")
    print(f"Found {unique_word_count:,} different words")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Longest word: {longest_word}")
    print("Most common words (excluding some stop words):")
    for word in top_words:
        print(f"\033[35m●\033[0m {word['word']} ({word['num']:,} times)")
    print("\033[35m♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡\033[0m")
    print(f"{sentence_count:,} sentences")
    print(f"{avg_sentence:.0f} words per sentence")
    print("\033[1;95m•┈୨♡୧┈┈୨♡୧┈• END •┈୨♡୧┈┈୨♡୧┈•\033[0m")
    print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    for book_path in sys.argv[1:]:
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        word_frequency = get_word_frequency(text)
        unique_word_count = get_unique_words(word_frequency)
        top_words = get_top_words(word_frequency, 10)
        avg_word_length = get_avg_word_length(word_frequency, num_words)
        longest_word = get_longest_word(text)
        sentence_count = get_sentence_count(text)
        avg_sentence = get_avg_sentence(sentence_count, num_words)
        hours, mins = get_reading_estimate(num_words)
        print_report(book_path, num_words, unique_word_count, avg_word_length, top_words, longest_word, 
        sentence_count, avg_sentence, hours, mins)
main()