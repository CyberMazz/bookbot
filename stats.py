def count_words(text):
	words = text.split()
	num_words = len(words)
	return num_words

def count_letters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1  # first occurrence
    return counts
