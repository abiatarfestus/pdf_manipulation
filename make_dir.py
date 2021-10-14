import os


parent_dir = "C:\\Users\Fessy\Desktop\\" # Parent Directory path
directory = input('Enter the pay month in word: ').capitalize()
path = os.path.join(parent_dir, directory) # Path to where new payslip files will be saved


def create_dir():
    '''Creates a salary month directory'''
    if not os.path.isdir(path):
        try: 
            os.mkdir(path) 
        except OSError as error: 
            print(error)
    return
    # print(os.listdir(path))