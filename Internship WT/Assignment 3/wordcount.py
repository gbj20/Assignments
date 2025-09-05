# 1. Word Counter – Count words, characters, and sentences in a given text file

def count_text_stats(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Count characters
        characters = len(text)

        # Count words
        words = len(text.split())

        # Count sentences
        sentences = text.count('.') + text.count('!') + text.count('?')

        print("File:", file_path)
        print("Characters:", characters)
        print("Words:", words)
        print("Sentences:", sentences)

    except FileNotFoundError:
        print("Error: File not found.")

file_path = "Assignment 3\sample.txt"  
count_text_stats(file_path)
