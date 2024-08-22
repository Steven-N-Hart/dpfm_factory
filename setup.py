from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if not line.startswith("git+")]

def parse_dependency_links(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.startswith("git+")]

setup(
    name="dpfm_factory",
    version="0.1",
    author="Steven N. Hart",
    author_email="Hart.Steven@Mayo.edu",
    description="Helper scripts for digital pathology foundation models",
    long_description=open('README.md').read(),  # Make sure you have a README.md file
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    dependency_links=parse_dependency_links('requirements.txt'),
)
