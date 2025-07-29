from PIL import Image, ImageDraw
import random

TILE_SIZE = 128
TILES_PER_ROW = 4096 // TILE_SIZE
ATLAS_SIZE = 4096

img = Image.new("RGB", (ATLAS_SIZE, ATLAS_SIZE))

for y in range(TILES_PER_ROW):
    for x in range(TILES_PER_ROW):
        color = (
            random.randint(64, 255),
            random.randint(64, 255),
            random.randint(64, 255)
        )
        for i in range(TILE_SIZE):
            for j in range(TILE_SIZE):
                img.putpixel((x * TILE_SIZE + i, y * TILE_SIZE + j), color)

img.save("vt_test_atlas_4096.png")