import pymongo




def IMDB(username, password, email, name1, name2):
    myConnection = pymongo.MongoClient("mongodb+srv://zizodevzeroinhero:DlSvN1b1Y2xpfZsJ@counten.r8lj62g.mongodb.net/?retryWrites=true&w=majority&appName=counten")

    mydb = myConnection["app"]

    mycoll = mydb["appertest"]

    myins = {"username" : username, "password" : password, "email" : email, "firstname" : name1, "lastname" : name2}
    myresult = mycoll.insert_one(myins)

