# counts the "words" in a given string
def count_words(text: str) -> int:
    text_list = text.split()
    return len(text_list)

# counts the frequencies of all characters (alphanum, symbols, etc), return dictionary {char : count}
def char_freq(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}

    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

# helper function for .sort() key argument in sort_chars() method
def sort_on(items: dict):
    return items["num"]

# sorts dictionary of {char : count} by its value and returns a list of dictionaries
def sort_chars(char_counts: dict) -> list:
    counts = []
    for ch, num in char_counts.items():
        if ch.isalpha():
            counts.append({"char" : ch, "num" : num})
    counts.sort(reverse=True, key=sort_on)
    return counts
