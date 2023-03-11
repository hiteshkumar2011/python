## Extract colors from image using module colorgram

import colorgram
rgb_colors = []
colors = colorgram.extract('image1.jpg', 6)
print(colors)

for color in colors:
    #rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
