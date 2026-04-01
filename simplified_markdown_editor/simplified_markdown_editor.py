FORMATTERS = [
    "plain", "bold", "italic", "header",
    "link", "inline-code",
    "ordered-list", "unordered-list", "new-line"
]

def print_help():
    """Display available formatters and special commands.

    Parameters:
    None

    Returns:
    None
    """
    print(f"Available formatters: {' '.join(FORMATTERS)}")
    print("Special commands: !help !done")

def format_plain():
    """Get plain text from user.

    Parameters:
    None

    Returns:
    str: plain text entered by user
    """
    return input("Text: ")

def format_bold():
    """Format text as bold.

    Parameters:
    None

    Returns:
    str: text wrapped in bold markdown syntax
    """
    return f"**{input('Text: ')}**"

def format_italic():
    """Format text as italic.

    Parameters:
    None

    Returns:
    str: text wrapped in italic markdown syntax
    """
    return f"*{input('Text: ')}*"

def format_inline_code():
    """Format text as inline code.

    Parameters:
    None

    Returns:
    str: text wrapped in inline code markdown syntax
    """
    return f"`{input('Text: ')}`"

def format_header():
    """Format text as a Markdown header.

    Parameters:
    None

    Returns:
    str: formatted header with level from 1 to 6
    """
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            break
        print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    return f"{'#' * level} {text}\n"

def format_link():
    """Format text as a Markdown link.

    Parameters:
    None

    Returns:
    str: formatted markdown link
    """
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def format_list(ordered=True):
    """Format text as a Markdown list.

    Parameters:
    ordered (bool): determines if list is ordered or unordered

    Returns:
    str: formatted list with given number of rows
    """
    while True:
        rows = int(input("Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")

    result = ""
    for i in range(1, rows + 1):
        text = input(f"Row #{i}: ")
        if ordered:
            result += f"{i}. {text}\n"
        else:
            result += f"* {text}\n"

    return result

def save_to_file(text):
    """Save Markdown text to file.

    Parameters:
    text (str): markdown content to save

    Returns:
    None
    """
    with open("output.md", "w", encoding="utf-8") as file:
        file.write(text)

def main():
    """Run the main program loop.

    Parameters:
    None

    Returns:
    None
    """
    result = ""

    while True:
        user_input = input("Choose a formatter: ")

        if user_input == "!help":
            print_help()

        elif user_input == "!done":
            save_to_file(result)
            break

        elif user_input == "plain":
            result += format_plain()

        elif user_input == "bold":
            result += format_bold()

        elif user_input == "italic":
            result += format_italic()

        elif user_input == "inline-code":
            result += format_inline_code()

        elif user_input == "header":
            result += format_header()

        elif user_input == "link":
            result += format_link()

        elif user_input == "new-line":
            result += "\n"

        elif user_input == "ordered-list":
            result += format_list(ordered=True)

        elif user_input == "unordered-list":
            result += format_list(ordered=False)

        else:
            print("Unknown formatting type or command")
            continue

        print(result)

if __name__ == "__main__":
    main()