from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a ist of requirements
    '''
    requirements=[]
    with open(file_path) as filr_obj:
        requirements=file.obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name='MY_1ST_ML_PROJECT',
version='0.0.1',
author='Dheeraj',
author_email='dheerajreddy5b7@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirents.txt')
)
