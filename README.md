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
Working on adding an interactive browser interface, which's usage might be like:
```py
from consolehtml import encode, Interface
encoded = encode("<textarea></textarea>")
interface = Interface(encoded)
interface.moveMouseTo(1,1) # 1 is about equal to the size of "A"
interface.click() # or
interface.rightclick() # or
interface.middleclick()
interface.keyPress("shift pagedown")
```
