import random
import time

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and challenging.",
        "Python is a versatile programming language.",
        "Practice makes perfect.",
        "Type as fast as you can!"
    ]
    return random.choice(sentences)

def calculate_typing_speed(sentence, start_time, end_time):
    words = sentence.split()
    elapsed_time = end_time - start_time
    words_per_minute = len(words) / (elapsed_time / 60)
    return words_per_minute

def main():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")
    
    sentence = get_random_sentence()
    print("\nType the following sentence:")
    print(sentence)
    
    input("Press Enter when you're ready to start typing...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    words_per_minute = calculate_typing_speed(sentence, start_time, end_time)
    
    print("\nYour typing speed: {:.2f} words per minute".format(words_per_minute))

if __name__ == "__main__":
    main()
