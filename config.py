import os
import subprocess

import gensim.downloader as api


def install_dependencies():
    print("Installing dependencies")
    subprocess.run('pip install -r requirements.txt'.split(' '))
    
    
def download_dataset():
    print("Downloading dataset from Kaggle")
    os.makedirs('datasets', exist_ok=True)
    subprocess.run(
        'kaggle datasets download -d rounakbanik/the-movies-dataset -p datasets --unzip'.split(" ")
    )
    
    
def import_word2vec():
    print("Downloading word2vec model")
    os.makedirs('model', exist_ok=True)
    os.chdir('model')
    # api.load('word2vec-google-news-300', return_path=True)
    
if __name__ == '__main__':
    install_dependencies()
    download_dataset()
    import_word2vec()