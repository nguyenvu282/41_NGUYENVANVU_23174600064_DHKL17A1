import json
# chuyen doi tuonh python sang json dung dumps
data = {
    "name ":" vunguyenvan",
    "sothich":"boiloi",
    "favorit_food":"dauran"

}
# chuyen doi tuong python thanh json
js_1 = json.dumps(data)
print(js_1)
print(type(js_1)) 