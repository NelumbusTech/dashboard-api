import pymongo
from pprint import pprint


DatabaseClient = pymongo.MongoClient()

DatabaseObject = DatabaseClient["UserInformationRecord"]

CollectionObject = DatabaseObject["Users"]

InitialEntries = [{"First Name" : "Nishi", "Last Name" : "Kaithwas", "E-mail" : "nishikaithwas@gmail.com",
                   "Contact No" : "9175933102", "Permanent Address" : "Indore",
                   "Education Qualification" : "Graduate", "Active" : "Yes"},

                  {"First Name" : "Anurag", "Last Name" : "Sahu", "E-mail" : "anuragsahu@gmail.com",
                   "Contact No" : "9095978569", "Permanent Address" : "Korba",
                   "Education Qualification" : "Post Graduate", "Active" : "No"},

                  {"First Name" : "Sonali", "Last Name" : "Gadpandey", "E-mail" : "sonaligadpandey@gmail.com",
                   "Contact No" : "9198563458", "Permanent Address" : "Balaghat",
                   "Education Qualification" : "Graduate", "Active" : "Yes"},

                  {"First Name" : "Rohit", "Last Name" : "Singh", "E-mail" : "rohitsingh@gmail.com",
                   "Contact No" : "9896589585", "Permanent Address" : "Gwalior",
                   "Education Qualification" : "Graduate", "Active" : "No"},

                  {"First Name" : "Aditya", "Last Name" : "Goyal", "E-mail" : "adityagoyal@gmail.com",
                   "Contact No" : "9090565632", "Permanent Address" : "Kailaras",
                   "Education Qualification" : "Post Graduate", "Active" : "Yes"}]

if "UserInformationRecord" not in DatabaseClient.list_database_names():
    InitialEntry = CollectionObject.insert_many(InitialEntries)

def GetInfo(FirstName, LastName):
    if not CollectionObject.count_documents({"First Name" : FirstName, "Last Name" : LastName} ):
        print("\nNo entry with First Name - {} and Last Name - {} exists.".format(FirstName,LastName))
        return
    UserDataObject  = CollectionObject.find({"First Name" : FirstName, "Last Name" : LastName},{"_id":0})
    print("\nDetails for {} {}".format(FirstName,LastName))
    for UserData in UserDataObject:
        pprint(UserData)

def SortByQualification():
    ToBeSortedData = CollectionObject.find({},{"_id" : 0, "First Name" : 1, "Last Name" : 1, "Education Qualification" : 1}).sort("Education Qualification")
    print("\nUsers sorted by Educational Qualification\n")
    for SortedData in ToBeSortedData:
        pprint(SortedData)

def GetActiveUsers():
    ActiveUserDataObject = CollectionObject.find({"Active" : "Yes"},{"_id": 0, "First Name" : 1, "Last Name" : 1})
    print("\nList of Active Users\n")
    for ActiveUserData in ActiveUserDataObject:
        print(ActiveUserData)

def UpdateAnEntry(FirstName, LastName, ToBeUpdatedData, UpdatedValues):
    if not CollectionObject.count_documents({"First Name" : FirstName, "Last Name" : LastName} ):
        print("No entry with First Name - {} and Last Name - {} exists.\n".format(FirstName,LastName))
        return
    UpdateThis = {"First Name" : FirstName, "Last Name" : LastName}
    for i in range(len(ToBeUpdatedData)):
        ToThis = {"$set": {ToBeUpdatedData[i] : UpdatedValues[i]}}
        CollectionObject.update_one(UpdateThis,ToThis)

def CreateNewEntry(FirstName, LastName, Email, ContactNo, PermanentAddress, EducationQualification, Active):
    if not CollectionObject.count_documents({"First Name" : FirstName, "Last Name" : LastName, "E-mail" : Email,"Contact No": ContactNo,
                                             "Permanent Address" : PermanentAddress, "Education Qualification" : EducationQualification, "Active" :Active}):
        CollectionObject.insert_one({"First Name" : FirstName, "Last Name" : LastName, "E-mail" : Email,"Contact No": ContactNo,
                                     "Permanent Address" : PermanentAddress, "Education Qualification" : EducationQualification, "Active" :Active})
    else:
        print("This entry already exists.\n")

def Menu():
    print("\nSelect from options below.\n")
    print("1. Get Information of a particular user.\n2. Get all user sort by educational qualification.\n"
          "3. Get list of active users.\n4. Update entry of a particular user.\n5. Create a new entry.\n6. Exit")
    choice = int(input("\nEnter your choice(1/2/3/4/5/6) : "))

    if choice == 1:
        print("Enter details of the user.")
        FirstName = input("Enter First Name : ").strip()
        LastName = input("Enter Last Name : ").strip()
        GetInfo(FirstName, LastName)
        Menu()

    elif choice == 2:
        SortByQualification()
        Menu()

    elif choice == 3:
        GetActiveUsers()
        Menu()

    elif choice == 4:
        print("Enter details of the user.")
        FirstName = input("Enter First Name: ").strip()
        LastName = input("Enter Last Name: ").strip()
        if not CollectionObject.count_documents({"First Name" : FirstName, "Last Name" : LastName} ):
            print("\nNo entry with First Name - {} and Last Name - {} exists.".format(FirstName,LastName))
            Menu()
        print("Select Details to be updated.")
        Items = ["First Name","Last Name","E-mail","Contact No", "Permanent Address", "Education Qualification", "Active"]
        for i in range(len(Items)):
            print("{}. {}".format(i + 1,Items[i]))
        IndxToBeUpdatedData = [int(data) - 1 for data in (input("Enter your choice(s)((1/2/3/4/5/6/7): "))]
        ToBeUpdatedData = []
        for Indx in IndxToBeUpdatedData:
            ToBeUpdatedData.append(Items[Indx])

        UpdatedValues = []
        for index in IndxToBeUpdatedData:
            if Items[index] != "Active":
                Update = input("Enter updated {} : ".format(Items[index]))
                UpdatedValues.append(Update)
            else:
                Update = input("Enter updated Active(Yes/No) : ")
                UpdatedValues.append(Update)

        UpdateAnEntry(FirstName.strip(), LastName.strip(), ToBeUpdatedData, UpdatedValues)
        Menu()

    elif choice == 5:
        print("Enter details of the user : ")
        FirstName = input("Enter First Name : ").strip()
        LastName = input("Enter Last Name : ").strip()
        Email = input("Enter E-Mail : ").strip()
        ContactNo = input("Enter Contact No : ").strip()
        PermanentAddress = input("Enter Permanent Address : ").strip()
        EducationQualification = input("Enter Eduational Qualification : ").strip()
        Active = input("Enter active status : ").strip()
        CreateNewEntry(FirstName, LastName, Email, ContactNo, PermanentAddress, EducationQualification, Active)
        Menu()

    else:
        return

Menu()



