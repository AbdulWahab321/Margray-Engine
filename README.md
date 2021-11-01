# Margray Game Engine
Margray game engine is a library based on Pygame and very easy to learn
## Margray game engine basics
#### Creating a window
```python
from margray_2d import *

engine = Margray()

window = engine.create_screen("1000x500") # Create the window with the resolution 1000x500

while True:
	for ev in engine.run(): # engine.run() returns events passed to the window
		event = EventHandler(ev)
		event.enableAutoQuit(engine) # Automatically Quites if the user clickes the "X" button
	engine.update() # Make sure to update the game All the time
```
**OR**
```python
from margray_2d import *

 
engine = Margray()

window = engine.create_screen((1000,500)) # Create the window with the resolution 1000x500

while True:
	for ev in engine.run(): # engine.run() returns events passed to the window
		event = EventHandler(ev)
		event.enableAutoQuit(engine) # Automatically Quites if the user clickes the "X" button
	engine.update() # Make sure to update the game All the time
```

#### Creating a Sprite
```python
from margray_2d import *

 
engine = Margray()

window = engine.create_screen("1000x500") # Create the window with the resolution 1000x500

# The 1st parameter is the Color and 2nd is the Position and 3rd is the Size

sprite = engine.sprite((255,255,255),(100,100),(75,75)) # Creating the sprite

while True:
	for ev in engine.run(): # engine.run() returns events passed to the window
		event = EventHandler(ev)
		event.enableAutoQuit(engine) # Automatically Quites if the user clickes the "X" button
	sprite.draw() # Drawing the sprite
	engine.update()
```
#### Creating a Sprite with Image
```python
from margray_2d import *


IMAGE_PATH = ""  # Your image path

engine = Margray()

window = engine.create_screen("1000x500") # Create the window with the resolution 1000x500

# The 1st parameter is the Image path and 2nd is X position and 3rd is Y position and 4th is Size

sprite = engine.image_sprite(IMAGE_PATH,100,100,(50,50)) # Creating the image sprite

while True:
	for ev in engine.run(): # engine.run() returns events passed to the window
		event = EventHandler(ev)
		event.enableAutoQuit(engine) # Automatically Quites if the user clickes the "X" button
		
	sprite.draw() # Drawing the image sprite

	engine.update()
```
#### Creating an Animated sprite
```python
from margray_2d import *

  

IMAGES = ["image1","image2","image3","image4","image5","image6","image7"] # Your image path

engine = Margray()

window = engine.create_screen("1000x500") # Create the window with the resolution 1000x500

# The 1st parameter is the images and 2nd is the X position and 3rd is the Y position and 4th is size and the startingIndex (in which index should the image start)

animated_sprite = engine.animated_sprite(IMAGES,50,50,(25,25),0)
while True:
	for ev in engine.run(): # engine.run() returns events passed to the window
		event = EventHandler(ev)
		event.enableAutoQuit(engine) # Automatically Quites if the user clickes the "X" button
		
	animated_sprite.draw() # Drawing the Sprite
	animated_sprite.animate(185) # Animating the Sprite the parameter is the duration between the animation frames
	engine.update()
	```
