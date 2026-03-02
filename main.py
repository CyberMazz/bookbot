def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def count_words(text):
	words = text.split()
	num_words = len(words)
	return num_words

def main():
	contents = get_book_text("books/frankenstein.txt")
	num_words = count_words(contents)
	print(f"Found {num_words} total words")

main()


