#Anagram: Rearranging the letters of a word to form a new word or phrase.

def is_anagram(word1, word2):
    # Remove spaces and convert to lowercase to make the comparison case-insensitive
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Sort the letters in both words and compare
    return sorted(word1) == sorted(word2)

# Example usage
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
