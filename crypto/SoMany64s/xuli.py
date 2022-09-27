import base64

file = open('flag.txt', 'r')
text = file.read()
while True:
    text=base64.b64decode(text).decode('utf-8')
    if "}" in text:
        print(text)
        break
    