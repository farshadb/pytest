from pathlib import Path


# path = Path("ecommerce")
# print(path.exists())
#
# # path = Path("emails")
# # print(path.rmdir())
# #path.mkdir() will create a new path in our project folder
# path = Path("scripts")
# print(path.mkdir())
# print(path.glob("*.* or *.xml or ....))

path = Path("")
print(path)
for file in path.glob("*"):
    print(file)