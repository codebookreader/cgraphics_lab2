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

# Helper function to draw polygons
def draw_polygon(ctx, points, fill_color, stroke_color=None, stroke_width=2):
    ctx.move_to(*points[0])
    for point in points[1:]:
        ctx.line_to(*point)
    ctx.close_path()
    ctx.set_source_rgb(*fill_color)
    ctx.fill_preserve()
    if stroke_color:
        ctx.set_line_width(stroke_width)
        ctx.set_source_rgb(*stroke_color)
        ctx.stroke()

# Ground rectangle
context.set_source_rgb(0.6, 0.8, 0.4)  # Darker green ground
context.rectangle(100, 560, 600, 20)
context.fill()
