import sys

expected_html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Learning Git</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Learning Git</h1>
  </body>
</html>
"""

def normalize_html(html_content):
    # Remove extra whitespaces and newlines
    return ' '.join(html_content.split())

def check_html_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        normalized_file_content = normalize_html(file_content)
        normalized_expected_content = normalize_html(expected_html_content)
        
        if normalized_file_content == normalized_expected_content:
            print(f"The content in {file_path} matches the expected HTML.")
        else:
            print(f"The content in {file_path} does not match the expected HTML.")
            sys.exit(1)  # Exit with a non-zero status code to indicate failure

if __name__ == "__main__":
    file_name = "index.html"
    check_html_content(file_name)
