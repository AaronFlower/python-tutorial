from setuptools import setup, find_packages

setup(
    name='what-havefun',
    # packages=['src', 'mysecond']
    packages=find_packages(exclude=['src', 'mysecond'])
)
