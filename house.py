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


# Main house body (front face)
draw_polygon(
    context,
    [(150, 360), (150, 560), (300, 560), (300, 360)],  # Aligned with ground
    fill_color=(0.8, 0.8, 0.8),  # Light gray
    stroke_color=(0, 0, 0)
)

# Main house body (side face)
draw_polygon(
    context,
    [(300, 360), (450, 320), (450, 520), (300, 560)],  # Aligned with ground
    fill_color=(0.7, 0.7, 0.7),  # Slightly darker gray
    stroke_color=(0, 0, 0)
)

# Roof (front face)
draw_polygon(
    context,
    [(150, 360), (300, 360), (225, 260)],
    fill_color=(0.3, 0.3, 0.3),  # Dark gray
    stroke_color=(0, 0, 0)
)

# Roof (side face)
draw_polygon(
    context,
    [(300, 360), (450, 320), (375, 220), (225, 260)],
    fill_color=(0.2, 0.2, 0.2),  # Even darker gray
    stroke_color=(0, 0, 0)
)
# Windows (on the front face)
for i in range(2):  # Two windows vertically
    context.rectangle(160 + i * 70, 400, 40, 50)  # x, y, width, height
    context.set_source_rgb(0.5, 0.7, 1)  # Light blue glass
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)
    context.stroke()

# Two new windows directly below the existing ones
for i in range(2):  # Two windows horizontally
    context.rectangle(160 + i * 70, 490, 40, 50)  # x, y, width, height
    context.set_source_rgb(0.5, 0.7, 1)  # Light blue glass
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black outline
    context.stroke()

# Windows (on the side face)
for i in range(2):  # Two windows stacked vertically
    draw_polygon(
        context,
        [
            (320, 410 + i * 80),  # Top-left
            (360, 400 + i * 80),  # Top-right
            (360, 440 + i * 80),  # Bottom-right
            (320, 450 + i * 80),  # Bottom-left
        ],
        fill_color=(0.5, 0.7, 1),  # Light blue glass
        stroke_color=(0, 0, 0)
    )

# Door (on the side face)
draw_polygon(
    context,
    [
        (380, 460),  # Top-left corner of the door
        (420, 450),  # Top-right corner of the door
        (420, 520),  # Bottom-right corner of the door
        (380, 530),  # Bottom-left corner of the door
    ],
    fill_color=(0.2, 0.2, 0.5),  # Dark blue
    stroke_color=(0, 0, 0)       # Black outline
)

# Chimney (on the roof)
draw_polygon(
    context,
    [(375, 230), (400, 220), (400, 300), (375, 310)],
    fill_color=(0.8, 0.8, 0.8),  # Same as the house
    stroke_color=(0, 0, 0)
)

# Save the drawing
surface.write_to_png("3d_house.png")
print("3D house saved as '3d_house.png'")