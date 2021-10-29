from subprocess import Popen, PIPE

class PythonPackageChecker:
    def __init__(self):
        self.packages = {}
        self.get_packages()

    def get_packages(self):
        """
        Gets packages from pip3 using subprocess

        Returns a dictionary of packages currently installed where the key is the package name, and the value is the version number
        """
        shell_command = "pip3 list"
        capture = Popen(shell_command, stdout=PIPE, stderr=PIPE, shell=True)
        std_out, std_err = capture.communicate()
        if isinstance(std_err, bytes):
            std_err = std_err.decode()
        if isinstance(std_out, bytes):
            std_out = std_out.decode()
        return_code = capture.returncode
        if return_code != 0:
            raise Exception(f"The command '{shell_command}' exited with a return_code of '{return_code}' and an exit message of '{std_err}'")

        for line in std_out.split("\n"):
            if " " not in line: # skip lines without spaces because we can't use .split() on them
                continue
            line_list = line.split()
            package_name = line_list[0].lower() # pip packages are case insensitive, so always make them lowercase for easy comparison
            if package_name == "package" or (package_name.count("-") == len(package_name)): # skip packages where the package name is only hyphens because this indicates a header
                print(f"Skipping the package '{package_name}' because it is a header.")
                continue
            package_version = line_list[1]
            self.packages[package_name] = package_version
        return self.packages

    def get_missing_packages(self, list_of_packages_to_check):
        """
        Checks each package in list_of_packages_to_check against the list of currently installed packages (self.packages)

        Returns a list of missing packages, which has length 0 if there are no missing packages
        """
        list_of_packages_to_check_type = type(list_of_packages_to_check)
        if list_of_packages_to_check_type != list:
            raise TypeError(f"get_missing_packages() expects a list, but instead received '{list_of_packages_to_check_type}'")
        if len(self.packages) == 0:
            raise ValueError(f"Unable to run check_packages() because self.packages is empty")

        missing_packages = []
        for package in list_of_packages_to_check:
            package = package.lower() # pip packages are case insensitive, so always make them lowercase for easy comparison
            if package not in self.packages:
                missing_packages.append(package)
        return missing_packages
