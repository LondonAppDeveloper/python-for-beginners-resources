
def read_contents(path, start, num_chars):
    """Opens the file and returns sub string based on start and num_chars."""
    # Write your code here

    with open(path) as f:
        f.seek(start)
        return f.read(num_chars)
