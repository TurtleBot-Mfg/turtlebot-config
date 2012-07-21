from distutils.core import setup
import os
import subprocess

if os.path.exists("debian/changelog"):
    output=subprocess.check_output("parsechangelog | grep Version", shell=True)
    version = output.split(":")[1].strip()

setup(name = "turtlebot-config",
    version = version,
    description = "TurtleBot Autoconfiguration Tool",
    author = "I Heart Engineering",
    author_email = "code@iheartengineering.com",
    url = "http://www.iheartengineering.com",
    license = "BSD-3-clause",
    scripts = ["turtlebot-config"],
    long_description = """This tool automatically generates launch files and udev rules for TurtleBot robots.""" 
    #classifiers = []     
) 
