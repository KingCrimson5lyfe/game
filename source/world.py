import pygame
import sys
from sprite import Sprite
from sound import Sound, Music

# Note on the parralax: Its kind of hacky right now, that will be improved later,
# of course.  Notice how each scrolling layer has two sprites, this is simply
# because we don't want 1280px wide gaps between each rotation.
#
# Currently, there is a bug where after so many rotations, some of the slower
# layers get "lost", and don't repeat.  This will also be fixed.
#
# If this hurts your mind, try to visualize it.  Its pretty simple in concept.
# When the picture reaches the point where it is off screen, another takes its
# place, and the original is moved after that one.  Like stitching a quilt.
#
# -joshbeitler

class BackgroundLayer:
    def __init__(self, filename, pos, scroll_speed):
        self.s1 = Sprite(filename, pos)
        self.s2 = Sprite(filename, (1280, pos[1]))

        self.filename = filename
        self.position = pos
        self.speed    = scroll_speed

    def draw(self):
        self.s1.draw()
        self.s2.draw()

    def update(self):
        self.s1.rect.x -= self.speed
        self.s2.rect.x -= self.speed

        if (self.s1.rect.x + 1280) == 0:
            self.s1.rect.x = 1280
        if (self.s2.rect.x + 1280) == 0:
            self.s1.rect.x = 0
            self.s2.rect.x = 0

class World:
    """
    World: encapsulates everything related to the world: time, children,
    background, drawing, etc.
    """

    def __init__(self):
        # This constant represents the speed at which the world moves.  I find
        # that anything less than around 5ish causes it to appear uniform - this
        # is because of all the division to reduce speeds. I find around 10 is
        # a good starting point.
        self.scroll_factor = 9
        pass

    def load(self):
        """
        Load the required resources to display the world
        """

        # The order here matters! Back to front.
        self.layers = [
            BackgroundLayer("world/test_bg_3.png", (0, 0), 2.5),
            BackgroundLayer("world/test_bg_2.png", (0, 0), 5.5),
            BackgroundLayer("world/test_bg_1.png", (0, 0), 3)
        ]

        self.ground = Sprite("world/test_bg_4.png", (0, 0))

    def update(self):    
        """
        Update critical world information, such as background position, etc.
        """

        for layer in self.layers:
            layer.update()

    def draw(self):
        """
        Draw the world and everything in it
        """

        for layer in self.layers:
            layer.draw()

        # Ground
        self.ground.draw()