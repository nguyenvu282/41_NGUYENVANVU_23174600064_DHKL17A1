import json 
py_dict = {"name":'nguyenvu',"tuoi":"19","que":'haiduong'}
sx = dict(sorted(py_dict.items()))
# chuyen sang chuoi json
print(json.dumps(sx,indent=4))