def main():
    words = {}
    text = input("Text: ")
    for word in text.split(" "):
        if word in words:
            words[word] += 1
        else:
            words[word] = words.get(word, 1)

    keys = list(words.keys())
    longest_word_length = get_longest_word_length(keys)
    keys.sort()

    for key in keys:
        print("{:>{width}} : {}".format(key, words[key],
              width=longest_word_length))


def get_longest_word_length(arr):
    length = 0
    for word in arr:
        word_length = len(word)
        if word_length > length:
            length = word_length
    return length


if __name__ == "__main__":
    main()
