import os
def rename_files():
    # get file
    filelist = os.listdir(r"/Users/danielholliday/Downloads/msg")
    #rename file
    saved_path = os.getcwd() #get current working dir
    os.chdir(r"/Users/danielholliday/Downloads/msg")
    for file_name in filelist:
        print("Old name - "+ file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()

#emergency code C7BRcXNT/bj4Vyz3aFxTINiURQy8IvefbmpZuZtM
