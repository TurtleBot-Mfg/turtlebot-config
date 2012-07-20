from distutils.core import setup

setup(name = "turtlebot-config",
    version = "0.0.2",
    description = "TurtleBot Autoconfiguration Tool",
    author = "I Heart Engineering",
    author_email = "code@iheartengineering.com",
    url = "http://www.iheartengineering.com",
    license = "BSD-3-clause",
    scripts = ["turtlebot-config"],
    long_description = """This tool automatically generates launch files and udev rules for TurtleBot robots.""" 
    #classifiers = []     
) 
