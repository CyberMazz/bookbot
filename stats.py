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

def sort_on(item):
    return item["num"]

def count_and_sort_letters(text):
    char_counts = count_letters(text)
    char_list = [{"char": char, "num": num} for char, num in char_counts.items() if char.isalpha()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list