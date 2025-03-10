import re


# Function to split the paragraph into sentences using the lookahead pattern
def split_paragraph(paragraph):
    # Regular expression for splitting sentences based on uppercase starting letters and sentence-ending punctuation
    sentence_pattern = r'[A-Z].*?[.!?](?= [A-Z] |$)'

    # Split the paragraph into sentences
    sentences = re.findall(sentence_pattern, paragraph, flags=re.MULTILINE | re.DOTALL)
    return sentences


# Function to display sentences and their count
def displaying_sentences(paragraph):
    sentences = split_paragraph(paragraph)
    sentence_count = len(sentences)

    print(f'Total number of sentences: {sentence_count}')

    for index, sentence in enumerate(sentences, 1):
        print(f'Sentence {index}: {sentence.strip()}')


# Main function to handle user input
def main():
    paragraph = input('Enter a paragraph: ')
    displaying_sentences(paragraph)


if __name__ == "__main__":
    main()