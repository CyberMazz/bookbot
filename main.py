from stats import count_words, count_letters, sort_on, count_and_sort_letters

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	print("============ BOOKBOT ============")
	contents = get_book_text("books/frankenstein.txt")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	num_words = count_words(contents)
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	char_count = count_and_sort_letters(contents)
	for item in char_count:
		print(f"{item['char']}: {item['num']}")

main()


