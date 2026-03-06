from stats import count_words, count_letters, sort_on, count_and_sort_letters
import sys

if len(sys.argv) != 2:
	print("Usage: python main.py <path_to_book>")
	sys.exit(1)
book = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	print("============ BOOKBOT ============")
	contents = get_book_text(book)
	print(f"Analyzing book found at {book}...")
	print("----------- Word Count ----------")
	num_words = count_words(contents)
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	char_count = count_and_sort_letters(contents)
	for item in char_count:
		print(f"{item['char']}: {item['num']}")

main()


