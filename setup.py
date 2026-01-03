#build ml applications as package and deploy on python pipi
from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT="-e ."# to ignore -e . reded by this function -
def get_requirements(file_path:str)->List[str]:
    ''' this function will return list of requirements'''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        # CHANGE: Use .strip() instead of .replace().
        requirements = [req.strip() for req in requirements] #replacing \n\r both as in windows include both , with blank as when we read requrements .txt it also read \n
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements;       



setup(
    name='mlproject',
    version='0.0.1',
    author='Abhinav',
    author_email='abhinavishu0311@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') #have to create this function so that all upcoming packages get installed dynimic
)