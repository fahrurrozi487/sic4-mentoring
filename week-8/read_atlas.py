import pymongo # meng-import library pymongo yang sudah kita install

password = "sXgqDoMQeL9uVvv4"
uri = f"mongodb+srv://anggasetiaw:{password}@cluster0.dxsulqe.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

db = client['sic-mentor-angga'] # ganti sesuai dengan nama database kalian
my_collections = db['mentor'] # ganti sesuai dengan nama collections kalian

try:
    for data in my_collections.find():
        print(data)

except Exception as e:
    print(e)