from textblob import TextBlob

file_path = input("Enter the full path to your text file: ")

try:
    with open(file_path, "r") as f:
        content = f.read()
    print("\n=>File loaded successfully.\n")
except IOError as e:
    print(f"=>Could not open the file: {e}")
    exit()

corrected = TextBlob(content).correct()

print("=>Original Text:\n")
print(content)
print("\n=>Corrected Text:\n")
print(corrected)

with open("corrected_output.txt", "w") as f:
    f.write(str(corrected))

print("\n=>Corrected text saved as 'corrected_output.txt' in same folder.")
