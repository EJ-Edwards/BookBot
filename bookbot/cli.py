#BookBot 


def main():
    with open("bookbot/books/frankenstein.txt") as f:
        # do something with f (the file) here
        file_contents = f.read()
        print(file_contents)

    
    return file_contents