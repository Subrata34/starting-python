studentInfo={
    "Labib" :{
        "Location" :"Banani",
        "study"    :"12",
        "Subject"  :"Science",
        "Roll"     :12,
        "Number"   : 17499903987
    },
    "Habib" :{
        "Location" :"Banani",
        "study"    :"12",
        "Subject"  :"Science",
        "Roll"     :20,
        "Number"   : 17499903987677

    },
    "year" :1971
}
print(studentInfo["Labib"]["Number"])

#Acess Item

print(studentInfo["year"])
x=studentInfo.get("Habib")
p=studentInfo.keys()
print(x)
print(p)
print(studentInfo.values())

#dictionary Item remove and add Item 
studentInfo.pop("Labib")
print("Labib remove: ",studentInfo)