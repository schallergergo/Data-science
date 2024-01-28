import pymongo
import mysql.connector


myclient = pymongo.MongoClient("mongodb+srv://pythonuser:9DAWpaclJDvCtQUV@cluster0.jrojckw.mongodb.net/PythonZh?retryWrites=true&w=majority")
print(myclient)
#Adatbázis kiválasztása
mydb = myclient["PythonZh"]
print(myclient.list_database_names())

#Collection kiválasztása
mycol = mydb["vehicles"]
cars = mycol.find({"type":"car"})


class Transfer:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
            host="sql.freedb.tech",
            user="freedb_zhuser",
            password="2TRg#SecNJrKg8?",
            database="freedb_pythonzh" )
            self.fuel = self.__getFuelDict()
        except mysql.connector.Error as err:
            print(err)
    
    def __getFuelDict(self):
        fuel ={}
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM fuels")
        for x in mycursor.fetchall():
            print(x)
            fuel[x[1]]=x[2]
        return fuel

    def upload(self,carList):
        for car in carList:
            consumption = car["consumptions"]
            fuelType = car["fuel type"]
            avgCost = sum(consumption)/len(consumption)*self.fuel[fuelType]
            print(car,avgCost)
            self.uploadToDB(car,avgCost,"IITGNR")

    def uploadToDB(self,car,avgCost,neptun):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO vehicles (brand, model,avgcost,uploader) VALUES (%s, %s,%s, %s)"
        val = (car["brand"],car["model"],avgCost,neptun,)
        mycursor.execute(sql, val)
        self.mydb.commit()        


    #extra for testing
    def showInserts(self):
        print("\n*** Show inserts ***\n")
        fuel ={}
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM vehicles where uploader='IITGNR'")
        for x in mycursor.fetchall():
            print(x)
    def delete(self):
        fuel ={}
        mycursor = self.mydb.cursor()
        mycursor.execute("delete FROM vehicles where uploader='IITGNR'")
        self.mydb.commit()
        print("\n*** Inserts deleted ***\n")


transfer = Transfer()
transfer.upload(cars)
transfer.showInserts()
#transfer.delete()


