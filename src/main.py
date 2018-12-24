from pathlib import Path
import pygame
import sys

WATER = 1
DIRT = 2

tile_textures = {
    WATER: pygame.image.load(
        str(Path(sys.argv[0]).parent / "resources/images/water.png")),
    DIRT: pygame.image.load(
        str(Path(sys.argv[0]).parent / "./resources/images/dirt.png")),
}

tile_map = [
    [WATER, WATER, DIRT, DIRT, DIRT, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, DIRT, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, DIRT, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, WATER, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, WATER, WATER, WATER],
    [WATER, DIRT, DIRT, WATER, WATER, WATER, WATER],
    [WATER, DIRT, DIRT, WATER, WATER, WATER, WATER],
]

TILE_SIZE = 40


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (len(tile_map)*TILE_SIZE, len(tile_map[0])*TILE_SIZE))
    pygame.display.set_caption("Pygame Test")

    while(True):
        # screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        for row, row_tiles in enumerate(tile_map):
            for column, tile in enumerate(row_tiles):
                screen.blit(
                    pygame.transform.scale(
                        tile_textures[tile_map[row][column]],
                        (TILE_SIZE, TILE_SIZE)),
                    (column*TILE_SIZE, row*TILE_SIZE))

        pygame.display.update()


if __name__ == "__main__":
    main()
