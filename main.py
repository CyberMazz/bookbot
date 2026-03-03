from stats import count_words, count_letters

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	contents = get_book_text("books/frankenstein.txt")
	num_words = count_words(contents)
	char_counts = count_letters(contents)
	print(f"Found {num_words} total words")
	print(f"The letter counts are: {char_counts}")

main()


