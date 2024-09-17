def write_to_file(filename, content):
  try:
    with open(filename, 'w') as file:
      file.write(content)
  except Exception as e:
    print(f"Error writing to {filename}: {e}")

def read_from_file(filename):
  try:
    with open(filename, 'r') as file:
      print(file.read())
  except Exception as e:
    print(f"Error reading from {filename}: {e}")

def append_to_file(filename, content):
  try:
    with open(filename, 'a') as file:
      file.write(content)
  except Exception as e:
    print(f"Error appending to {filename}: {e}")

# Usage example:

filename = "my_file.txt"
write_to_file(filename, "Line 1\nLine 2\nLine 3")
read_from_file(filename)
append_to_file(filename, "\nLine 4\nLine 5")
read_from_file(filename)