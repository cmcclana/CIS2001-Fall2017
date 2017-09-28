import os



def print_contents(path):

    #print("Your path exists %s" % os.path.exists(path))
    #print("Your path is a directory: %s" % os.path.isdir(path))
    #print("Your path is a file: %s" % os.path.isfile(path))

    if os.path.isdir(path):
        children = os.listdir(path)
        for item in children:
            if os.path.isfile(os.path.join( path, item )):
                print(os.path.join(path, item))
            else:
                print_contents(os.path.join(path, item))

path = input("enter a path:\n")
print_contents(path)


for root, dirs, files in os.walk(path):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))