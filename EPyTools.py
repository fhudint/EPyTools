#! /usr/bin/env python3

"""
EPyTools: This is an acronym for "EmisPendis Python Automation Tools Engine" 
which is a cool name for a project using Python Selenium to automate tasks 
that are typically done manually on the e-mispendis Ministry of Religion 
application using the Python engine, 
such as filling out forms or clicking buttons.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import requests
import platform

from selenium import webdriver

module_name = "EPyTools: Automation task for emispendis Kemenag"
__version__ = "0.0.1"


def main():
    version_string = f"%(prog)s {__version__}\n" + \
        f"{requests.__description__}:  {requests.__version__}\n" + \
        f"Python:  {platform.python_version()}"

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=f"{module_name} (Version {__version__})"
                            )

    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Displays information and dependencies"
                        )

    # parser.add_argument("path",
    #                     action="path", path="xlsutils",
    #                     help="Read and display data from \"xlsx\" file")

    args = parser.parse_args()

    # path = xlsutils.readData(
    #     "/home/jarvis/Sources/emi_selen/dd.xlsx", "TP", 1, 1)
    import utils
    read = utils.xlsutils.readData(
        "/home/jarvis/Sources/emi_selen/dd.xlsx", "TP", 2, 2)
    value = read
    print(value)


if __name__ == "__main__":
    main()
    # Notify caller that all queries are finished.
