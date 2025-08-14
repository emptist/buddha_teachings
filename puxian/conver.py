#conver.py

import opencc
from pxxyp import *

converter = opencc.OpenCC('s2t.json')

str = converter.convert(book)  # 漢字

print(str)