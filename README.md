# ConsoleHTML
Run HTML in your Console Python apps!
## Usage
```py
from consolehtml import encode, Snapshot
encoded = encode("<p>Hello, world!</p>") # Encode only works with one line.
snapshot = Snapshot(encoded) # Creates a non-interactive browser interface
print("The output of the code you put in is:")
snapshot.view(lambda x: print("Image: "+x)) # Display the image with the text 'Image: ' in front.
```
