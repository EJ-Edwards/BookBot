from stats import count_words

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Print first line (for BootDev test)
    first_line = text.splitlines()[0]
    print(first_line)

    # Count words and print
    num_words = count_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
