import random

reader = open('hungerGames.txt')
pairList = {}
window = []

for line in reader:
    for word in line.split():
        line.replace('  ', ' ')
        clean_word = word.strip('.;,-“’”:?—‘!()_|0123456789 ').lower()
        window.append(clean_word)

        if len(window) == 2:
            key = window[0]
            value = window[1]
            if key not in pairList:
                pairList[key] = [value]
            else:
                pairList[key].append(value)
            window.pop(0)
def prompt():
    word1 = input('please enter a word from the text database: ')
    while word1 not in pairList:
        word1 = input('please enter a word from the text database: ')
    length = int(input('please enter response length : '))
    for i in range(length):
        print(word1, end=" ")
        successors = pairList[word1]
        word2 = random.choice(successors)
        word1 = word2
prompt()
response = input('\n\nplease enter r to restart or q to quit : ')
while response not in ['r', 'q']:
    response = input('please enter r to restart or q to quit : ')
if response == 'r':
    prompt()
