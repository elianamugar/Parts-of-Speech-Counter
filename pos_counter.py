"""
Count broad part-of-speech categories in .txt files.

This script uses NLTK to tokenize and POS-tag text files, then counts
selected categories such as nouns, verbs, adjectives, adverbs, pronouns,
prepositions, and proper nouns.
"""

from collections import Counter
from pathlib import Path

import nltk


POS_CATEGORIES = {
    "Adjectives": {"JJ", "JJR", "JJS"},
    "Nouns": {"NN", "NNS"},
    "Prepositions": {"IN"},
    "Proper Nouns": {"NNP", "NNPS"},
    "Personal Pronouns": {"PRP"},
    "Possessive Pronouns": {"PRP$"},
    "Adverbs": {"RB", "RBR", "RBS"},
    "Verbs": {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"},
}


def count_pos_categories(text):
    """Tokenize text and count broad POS categories."""
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    counts = Counter()

    for word, tag in tagged_tokens:
        for category, tag_set in POS_CATEGORIES.items():
            if tag in tag_set:
                counts[category] += 1
                break

        if word.lower() == "chad":
            counts["Chads"] += 1

    return counts


def analyze_file(file_path):
    """Analyze one text file."""
    text = file_path.read_text(encoding="utf-8")
    return count_pos_categories(text)


def format_results(file_path, counts):
    """Format POS counts for one file."""
    lines = [f"File: {file_path.name}"]

    for category in POS_CATEGORIES:
        lines.append(f"{category}: {counts.get(category, 0)}")

    lines.append(f"Chads: {counts.get('Chads', 0)}")

    return "\n".join(lines)


def analyze_directory(input_dir):
    """Analyze every .txt file in a directory."""
    results = []

    for file_path in sorted(input_dir.glob("*.txt")):
        counts = analyze_file(file_path)
        results.append(format_results(file_path, counts))

    return "\n\n".join(results)


def main():
    """Run the POS counter."""
    input_dir = Path(input("Enter folder path containing .txt files: ").strip())
    output_file = Path(input("Enter output filename, e.g. pos_counts.txt: ").strip())

    if not input_dir.exists() or not input_dir.is_dir():
        print("Error: input folder does not exist.")
        return

    results = analyze_directory(input_dir)

    if not results:
        print("No .txt files found in the selected folder.")
        return

    output_file.write_text(results, encoding="utf-8")
    print(f"Saved POS counts to {output_file}")


if __name__ == "__main__":
    main()
