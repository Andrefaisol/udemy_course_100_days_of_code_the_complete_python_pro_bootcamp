import colorgram
color_in = colorgram.extract("20_001.jpg", 25)

color_tup = []

for i in color_in:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color_tup.append((r, g, b))


