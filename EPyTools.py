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
import sys
import utils
import os

from selenium import webdriver

module_name = "EPyTools: Automation task for emispendis Kemenag"
__version__ = "0.0.1"


def main():

    print("Path at terminal when executing this file")
    print(os.getcwd() + "\n")

    print("This file path, relative to os.getcwd()")
    print(__file__ + "\n")

    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path + "\n")

    print("This file directory and name")
    path, filename = os.path.split(full_path)
    print(path + ' --> ' + filename + "\n")

    print("This file directory only")
    print(os.path.dirname(full_path))


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

    parser.add_argument("--username", "-u", metavar="USERNAME",
                        action="store",
                        help="Username or email for login to emispendis Kemenag")

    parser.add_argument("--password", "-p", metavar="PASSWORD",
                        action="store",
                        help="Password for login to emispendis Kemenag")
    
    parser.add_argument("--browser", "-b",
                        action="store", #default="Chrome",
                        help="Browser to use for EPyTools")
    
    parser.add_argument("--path",
                        action="store", help="test path")


    args = parser.parse_args()

    if args.username and args.password is None:
        print("Username or password can't empty")
        sys.exit(1)
    else:
        print("ok")
    if args.browser is not None:
        print("Use optional browser")
        utils.browser.chromeBrowser(args.browser)
    if args.path is not None:
        path_stat = os.path
        print (path_stat)

if __name__ == "__main__":
    main()
    # Notify caller that all queries are finished.
