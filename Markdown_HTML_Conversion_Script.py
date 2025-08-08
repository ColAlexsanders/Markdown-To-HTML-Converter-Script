import os
import markdown 

def convert_markdown_to_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
        
        html_content = markdown.markdown(markdown_content)

        base_dir = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        html_dir = os.path.join(base_dir, base_name + '.html')

        with open(html_dir, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        print(f"Successfully converted '{file_path}' to '{html_dir}'")

    except FileNotFoundError:
        print(f"Error: Markdown file not found at '{file_path}'")
    except Exception as e:
        print(f"An error has occurred during the conversion process: {e}")

markdown_file = input("Enter filepath to convert to HTML: ")

convert_markdown_to_html(markdown_file)