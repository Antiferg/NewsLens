from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    REM="-e ."

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if REM in requirements:
            requirements.remove(REM)
    return requirements
setup(
    name='NewsLens',
    version='0.0.1',
    author='Antiferg',
    author_email='samyarajghosh1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)