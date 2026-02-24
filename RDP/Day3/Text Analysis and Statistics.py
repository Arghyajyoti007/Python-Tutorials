# Assignment 15:Text Analysis and Statistics:
# Provide a text containing a lengthy article or essay.
# Create a Python program that reads this file and calculates the following statistics:
# Total word count
# Total sentence count
# Average word length
# Paragraph to analyze:
# The metaverse is an emerging digital realm that is captivating imaginations worldwide. In essence, it represents a collective virtual universe where individuals can interact, socialize, work, and play within a vast interconnected space. Imagine a sprawling digital landscape, akin to a science fiction dream, where people utilize avatars to navigate this immersive environment. Within the metaverse, possibilities are seemingly limitless, encompassing everything from virtual reality gaming and educational experiences to social gatherings and commerce.
# Key technologies driving the metaverse include augmented reality (AR), virtual reality (VR), blockchain, and advanced artificial intelligence (AI). Companies like Facebook's Meta, Roblox, and Fortnite's Epic Games are already investing heavily in metaverse development, envisioning a future where it becomes an integral part of our daily lives. The metaverse's potential extends far beyond entertainment; it could revolutionize remote work, education, and even healthcare, offering new ways to connect and collaborate across distances.

def word_count(paragraph):
    words = paragraph.split()
    return len(words)


def sentence_count(paragraph):
    count = 0
    for char in paragraph:
        if char in ".?!":
            count += 1
    return count


def avg_word_length(paragraph):
    words = paragraph.split()
    if len(words) == 0:
        return 0

    total_length = 0
    for word in words:
        total_length += len(word)

    return total_length / len(words)


paragraph = """Key technologies driving the metaverse include augmented reality(AR), virtual reality(VR), blockchain, and advanced artificial intelligence(AI). Companies like Facebook's Meta, Roblox, and Fortnite's Epic Games are already investing heavily in metaverse development, envisioning a future where it becomes an integral part of our daily lives. The metaverse's potential extends far beyond entertainment; it could revolutionize remote work, education, and even healthcare, offering new ways to connect and collaborate across distances."""
print(f"Word Count : {word_count(paragraph)}")
print(f"Sentence Count : {sentence_count(paragraph)}")
print(f"Average Word Length : {avg_word_length(paragraph)}")
print(f"Average Word Length : {avg_word_length(paragraph)}")
