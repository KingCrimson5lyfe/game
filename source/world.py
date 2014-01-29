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

class World:
    """
    World: encapsulates everything related to the world: time, children,
    background, drawing, etc.
    """

    def __init__(self):
        self.scroll_factor = 9
        pass

    def load(self):
        self.bg1 = Sprite("world/test_bg_1.png", (0, 0))
        self.bg2 = Sprite("world/test_bg_1.png", (1280, 0))
        
        self.bg3 = Sprite("world/test_bg_2.png", (0, 0))
        self.bg4 = Sprite("world/test_bg_2.png", (1280, 0))

        self.bg5 = Sprite("world/test_bg_3.png", (0, 0))
        self.bg6 = Sprite("world/test_bg_3.png", (1280, 0))

        self.ground1 = Sprite("world/test_bg_4.png", (0, 0))

    def update(self):     
        # Background layer 1 (light mountains)
        self.bg1.rect.x -= (self.scroll_factor / 3)
        self.bg2.rect.x -= (self.scroll_factor / 3)

        if (self.bg1.rect.x + 1280) == 0:
            self.bg1.rect.x = 1280

        if (self.bg2.rect.x + 1280) == 0:
            self.bg1.rect.x = 0
            self.bg2.rect.x = 1280

        # Background layer 2 (clouds)
        self.bg3.rect.x -= (self.scroll_factor / 2)
        self.bg4.rect.x -= (self.scroll_factor / 2)

        if (self.bg3.rect.x + 1280) == 0:
            self.bg3.rect.x = 1280

        if (self.bg4.rect.x + 1280) == 0:
            self.bg3.rect.x = 0
            self.bg4.rect.x = 1280

        # Background layer 3 (dark mountains)
        self.bg5.rect.x -= (self.scroll_factor / 4)
        self.bg6.rect.x -= (self.scroll_factor / 4)

        if (self.bg5.rect.x + 1280) == 0:
            self.bg5.rect.x = 1280

        if (self.bg6.rect.x + 1280) == 0:
            self.bg5.rect.x = 0
            self.bg6.rect.x = 1280

    def draw(self):
        self.bg5.draw()
        self.bg6.draw()

        self.bg1.draw()
        self.bg2.draw()
        
        self.bg3.draw()
        self.bg4.draw()

        self.ground1.draw()