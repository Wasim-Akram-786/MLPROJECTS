from setuptools import find_packages ,setup 
from typing import List  


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirments
    '''
    requirements=[]   
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] 
    return requirements

setup(
    name="ML_Projects",
    version="0.01",
    author="Wasim Akram",
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt')
)