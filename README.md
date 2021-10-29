# PythonPackageChecker

## Purpose:
This simple Python3 library exists to aid in the process of checking whether or not specific pip packages are installed.

## Prerequisites:
- Python3
- pip3

## How to use it:
Below is a sample driver program:
```python3
from PythonPackageChecker import PythonPackageChecker

package_checker = PythonPackageChecker() # initialize the package checker
print(package_checker.packages) # get a list of currently installed packages and their versions

packages_to_check = ["virtualenv", "wheel", "requests"] # populate this list depending on what you need
missing_packages = package_checker.get_missing_packages(packages_to_check)
if len(missing_packages) != 0:
    print(f"The following packages are missing: {missing_packages}")
```
