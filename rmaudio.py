# 对所有大于1MB的ipynb文件，删除音频
import os
import json
def isaudio(out):
    return (out["output_type"]=="execute_result" and out["data"]["text/plain"]==["<IPython.lib.display.Audio object>"])

for filename in os.listdir("."):
    if(filename.endswith(".ipynb")):
        if(os.path.getsize(filename)>1000000):
            print(filename)
            with open(filename,encoding="utf8") as file:
                content=json.load(file)
            for cell in content["cells"]:
                if("outputs" in cell):
                    cell["outputs"]=[out for out in cell["outputs"] if not(isaudio(out))]
            outstr=json.dumps(content,indent=1)
            with open(filename,"w",encoding="utf8") as file:
                file.write(outstr)
