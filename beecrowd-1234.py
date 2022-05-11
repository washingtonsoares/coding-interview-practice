# https://www.beecrowd.com.br/judge/pt/problems/view/1234

while True:
    try:
        sentence = input()

        dacingSentence = ""
        isUpper = False

        for index, char in enumerate(sentence):
            if char == " ":
                dacingSentence += char
                continue
            isUpper = not isUpper
            if (isUpper):
                dacingSentence += char.upper()
            else:
                dacingSentence += char.lower()

        print(dacingSentence)

    except EOFError:
        break
