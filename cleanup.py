import os
import shutil

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

def delete_model():
    print("Deleting model directory")
    shutil.rmtree(BASE_PATH + '/model')
    
    
def delete_datasets():
    print("Deleting datasets")
    shutil.rmtree(BASE_PATH + '/datasets')
    

if __name__ == '__main__':
    delete_model()
    delete_datasets()