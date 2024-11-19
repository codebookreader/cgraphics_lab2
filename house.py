import cairo
import math

# Canvas dimensions
WIDTH, HEIGHT = 800, 600

# Create surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background color (light green ground)
context.set_source_rgb(0.8, 0.9, 0.6)
context.paint()
