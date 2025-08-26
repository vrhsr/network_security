''' setup py '''

from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    '''
    thsi function will return list of requirements
    '''

    requirement_lst :List[str] = []
    try:
        with open('requirements.txt','r') as file:
            ## read lines from the file

            lines = file.readlines()
            ## process each line 
            for line in lines:

                requirement = line.strip()

                ## ignore setup lines and -e. 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

## print(get_requirements())

setup (name="network security",
       version = "0.0.1",
       author="venkate",
       author_email="mvrhsr@gmail.com",
       packages=find_packages(),
       install_requires = get_requirements()


       )