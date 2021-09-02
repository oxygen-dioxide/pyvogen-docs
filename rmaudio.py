# 对所有大于1MB的ipynb文件，删除音频
import os
import json
for filename in os.listdir("."):
    if(filename.endswith(".ipynb")):
        if(os.path.getsize(filename)>1000000):
            print(filename)
            with open(filename,encoding="utf8") as file:
                content=json.load(file)
            input()