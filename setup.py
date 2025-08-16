from setuptools import setup, find_packages,setup 
from typing import List

def get_requirments(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')

setup(
name='Student_Prediction',
version='0.0.1',
author='Saurabh',
author_email='saurabhsingh.93011@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirements.txt'),
)