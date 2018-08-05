
text="Aell7oZ?"
text2= "".join([chr(((ord(i)-62)%26)+65) for i in text.upper() if i.isalpha()])
encrypted_text=""
for i in text.upper():
    if i.isalpha():
        encrypted_text+=chr(((ord(i)-62)%26)+65)
    else:
        encrypted_text+=i
print(text,encrypted_text)
