
# Requirements:
- A command line interface 
- Python
- Internet Archive's command line tool

For Linux:
`sudo apt update` to update the existing packages. 
`sudo apt install pythonpy python3-pip internetarchive` to install python, pip, and the ia cli tool


# Running the Program
The program expects the unique identifier for the colelction to defined in the `collection_identifier` variable. This can be found from the Internet Archive website by clicking the "About" tab and scrolling down to the "Identifier" field under "Collection Info". 

Run the program with `python3 export.py`


# Resources
- [Documentation](https://archive.org/developers/index.html) for helpful definitions for Internet Archive terms
- [Documentation](https://archive.org/developers/internetarchive/internetarchive.html?highlight=search#internetarchive) for the Internet Archive Python library