from setuptools import setup, find_packages

# Function to read the requirements from the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name="dpfm_factory",
    version="0.1",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    package_dir={'': 'dpfm_model_runners'}
)
