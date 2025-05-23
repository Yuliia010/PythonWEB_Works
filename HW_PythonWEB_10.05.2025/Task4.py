text = "україна — країна в східній європі! її населення становить приблизно 40 мільйонів людей. столиця — київ, річка дніпро є однією з найбільших в європі. середньорічна температура коливається від -6 градусів взимку до 24 градусів влітку. українська мова має багаті традиції і використовує латинські та кириличні символи!"
print("\Text:")
print(text)

import re

def capitalize_sentences(txt):
    sentences = re.split(r'([.!?])', txt)
    result = ""
    for i in range(0, len(sentences)-1, 2):
        sentence = sentences[i].strip()
        punctuation = sentences[i+1]
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
        result += sentence + punctuation + " "

    if len(sentences) % 2 != 0:
        tail = sentences[-1].strip()
        if tail:
            tail = tail[0].upper() + tail[1:]
            result += tail
    return result.strip()

fixed_text = capitalize_sentences(text)
print("\nResult:")
print(fixed_text)

digits_count = 0
for ch in text:
    if ch.isdigit():
        digits_count += 1

print("\nDigits count:", digits_count)

commas_count = text.count(',')
print("Commas count:", commas_count)

accent_sign = '!'
accent_count = text.count(accent_sign)
print("Accent count:", accent_count)
