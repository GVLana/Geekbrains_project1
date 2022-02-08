import os
import random

os.mkdir('data')
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
for _ in range(10 ** 3):
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
    f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
    with open(os.path.join('data', f'{f_name}.bin'), 'wb') as f:
        f.write(f_content)


