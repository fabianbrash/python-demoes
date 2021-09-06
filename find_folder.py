
folders = [{
    "folder": "group-v1017",
    "name": "templates"
},
{
    "folder": "group-v1772",
    "name": "APPLIANCES"
},
{
    "folder": "group-v2000",
    "name": "VMs"
}
]

#print(data[0]["name"])

for folder in folders:
    print(f"Folder:{folder['folder']}({folder['name']})")

def getFolderName():
    theFolder = "group-v1772"

    for f in folders:
        if f['folder'] == theFolder:
            print(f"Folder Name is: {f['name']}")
            return
    print("Error folder not found...")


getFolderName()
