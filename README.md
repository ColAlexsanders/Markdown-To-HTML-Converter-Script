# Markdown-To-HTML-Converter-Script
Converting markdown files to html for further editing and to print the document as a PDF through the print functionality found in most browsers

This is a very simple python script I wrote at work which is mainly used to write documents in markdown in environments where you don't want to use word but you're unable to install programs like Pandoc, Latex, etc. The HTML file that is generated after the script is ran would be used to format images, text, etc. 

# Usage
First off, you're going to want to have python installed. Then, you're going to want to use pip through your terminal of choice to install the markdown library:

```
pip install markdown
```

Then you're going to want to clone this repository, or download the zip file and extract that into one of your directories. After that, change your directory to the one where the script is stored and run the script with this command if you're on windows:

```
python .\Markdown_HTML_Conversion_Script.py
```

The script will ask you what file you want to convert to HTML. **Make sure to use the absolute file path**, which would look like this: `C:\Users\<USERNAME>\path\to\file.md`. After that, just open the new HTML file and make any edits you need and print to PDF!
