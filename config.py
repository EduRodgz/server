import pymongo
import certifi


developer = {
    "first":"Eduardo",
    "last":"Rodriguez",
    "email":"edurodgz.usmc@icloud.com",
    "hobbies":["gym","video games","code"],
    "address":{
        "num":741,
        "street":"dartmouth ln",
        "city":"deer park"
    }
}


con_str = "mongodb+srv://edurodgzusmc:Test1234@cluster0.qlc5qbo.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("bootpog")