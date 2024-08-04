from bson import BSON
from bson.json_util import dumps, loads
import datetime

# 创建一个示例文档
document = {
    "name": "John Doe",
    "age": 30,
    "created_at": datetime.datetime.utcnow()
}

# 将文档编码为 BSON
bson_data = BSON.encode(document)
print(bson_data)

# 从 BSON 解码为文档
decoded_document = BSON.decode(bson_data)
print(decoded_document)


from bson import ObjectId

# 创建一个新的 ObjectId
oid = ObjectId()
print(oid)

# 将 ObjectId 转换为字符串
oid_str = str(oid)
print(oid_str)

# 从字符串转换为 ObjectId
oid_from_str = ObjectId(oid_str)
print(oid_from_str)
