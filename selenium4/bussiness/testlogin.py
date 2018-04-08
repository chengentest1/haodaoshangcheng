import yaml,os
# path=os.getcwd()
# path1=os.path.dirname(__file__)
# print(path)
# print(path1)
file=open(r'C:\Users\cheng\PycharmProjects\selenium4\data\page_data.yaml', "r",encoding= "utf-8")
f=yaml.load(file)
print(f)