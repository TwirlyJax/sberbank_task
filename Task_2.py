import re
import os
import string

def read_my_file():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	document_text = open(os.path.join(current_dir, "test1.xml"), "r", encoding="utf-8")
	text = document_text.read().lower()
	document_text.close()
	return text
	
def my_little_program():

	text = read_my_file()
	match_words = re.findall(r'\b\w+\b(?![^<]*>)', text)

	frequency = {}
	for word in match_words:
		count = frequency.get(word,0)
		frequency[word] = count + 1
		
	frequency_list = frequency.items()
	frequency_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)
	frequency_list = frequency_list[:15]

	for word in frequency_list:
		print(word[0], word[1])
	
if __name__ == "__main__":
	my_little_program()


