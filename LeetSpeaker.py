# Program made by Syntax Terminator

def leetspeak(user_input):

	replacable_words = ["o", "l", "s", "a", "e", "t"]
	replaced_words = ["0", "!", "$", "4", "3", "+"]

	for i in user_input:
		if i in replacable_words:
                        for x in range(len(replacable_words)):
                                user_input = user_input.replace(replacable_words[x], replaced_words[x])
                                

	print(user_input)


flag = True

while flag:
	word = str(input("Enter the word: "))
	leetspeak(word)

	choice_to_continue = input("Enter 1 or yes to continue: ")

	if choice_to_continue == "yes" or choice_to_continue == 1:
		continue

	else:
		flag = False

