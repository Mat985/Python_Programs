#Another known problem - read the words from a text file and count them with the assistance of the Python set.
# When splitting the strings to words, mind that there can be multiple symbols separating the words 
# - spaces, full stops, commas, semicolons, quotation marks ... Try to find a universal way how to collect all of them.
import re
file=open("textfile1.txt", "r", encoding = "utf-8" )
text=file.read()
text=text.replace("\n"," ")
words = re.findall(r'[A-Za-z]+', text)
unique_words = set(words)

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
for word, count in word_counts.items():
    print(f"{word}: {count}")

print(f"Number of unique words: {len(unique_words)}")

file.close()