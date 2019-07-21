from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
      requires = [requirement.strip() for requirement in requirements_file]

setup(name='wisp',
      version='0.1',
      description='Weather Station running on Raspberry pi Zero!',
      url='https://github.com/FosterFromGloucester/wisp',
      author='FosterFromGloucester',
      author_email='',
      license='MIT',
      include_package_data=True,
      packages=find_packages(),
      package_dir={"wisp-api": "wisp-api","wisp-daemon": "wisp-daemon"},
      install_requires=requires,
      zip_safe=False)
