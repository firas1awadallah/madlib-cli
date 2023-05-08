
import re

pattern = re.compile(r"{\s*[A-Za-z0-9\-',\. ]+\s*}")

def read_template(file_path):
    """
    Read the contents of the template file and return the text as a string.
    """
    with open(file_path, "r") as file:
        template = file.read()
    return template

def parse_template(template):
    """
    Given a template string, return a tuple containing the stripped version of the
    string and a tuple of the placeholders.
    """
    parts = re.findall(r"\{([^{}]+)\}", template)
    stripped = re.sub(r"\{([^{}]+)\}", "{}", template)
    return stripped, tuple(parts)

def merge(template, user_inputs):
    """
    Replace the placeholders in the template with the user inputs and return the completed madlib.
    """
    return template.format(*user_inputs)

if __name__ == "__main__":
    print("Welcome to Madlib game!")
    print("Madlib is a game where you provide different words to fill in the blanks in a story.")
    print("Please enter the required words when prompted, and the final story will be generated.")

    template = read_template("madlib_cli/template.txt")
    stripped_template, placeholders = parse_template(template)

    user_inputs = []
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder}: ")
        user_inputs.append(user_input)

    madlib = merge(stripped_template, user_inputs)
    print(madlib)

    with open("madlib_cli/completed_madlib.txt", "w") as file:
        file.write(madlib)
