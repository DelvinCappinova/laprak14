import re
import random
import string

email = [
    "anton@mail.com dimiliki oleh antonius",
    "budi@gmail.co.id dimiliki oleh budi anwari",
    "slamet@getnada.com dimiliki oleh slamet slumut",
    "matahari@tokopedia.com dimiliki oleh toko matahari"
]
all_characters = string.ascii_letters + string.digits
length = 8
pattern = r'([a-zA-Z0-9._%+-]+)@'
for e in email:
    match = re.search(pattern,e)
    if match:
        username = match.group(1)
        password = ''.join(random.choices(all_characters, k=length))
        print(f"{e.split()[0]} username: {username}, password: {password}")