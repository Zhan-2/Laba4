def get_file_content(filename):
    """Read content from a specified file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def save_to_file(content, output_filename):
    """Save content to a specified output file."""
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content successfully saved to '{output_filename}'")
    except IOError as e:
        print(f"Failed to write to file '{output_filename}': {e}")

def main():
    filename = input("Enter the name of the text file to format and print: ")
    content = get_file_content(filename)
    if content is None:
        return

    print("Choose output option:")
    print("1. Print to screen")
    print("2. Save to another file")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nDisplaying content on screen:\n")
        print(content)
    elif choice == '2':
        output_filename = input("Enter the name of the output file: ")
        save_to_file(content, output_filename)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
