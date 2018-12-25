from pathlib import Path
import pygame
import sys

resources_dir = Path(sys.argv[0]).parent / "resources/"

WATER = 1
DIRT = 2

tile_textures = {
    WATER: pygame.image.load(
        str(resources_dir / "images/water.png")),
    DIRT: pygame.image.load(
        str(resources_dir / "images/dirt.png")),
}

tile_map = [
    [DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, DIRT, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, DIRT, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, WATER, WATER, WATER],
    [WATER, WATER, DIRT, DIRT, WATER, WATER, WATER],
    [WATER, DIRT, DIRT, WATER, WATER, WATER, WATER],
    [WATER, DIRT, DIRT, WATER, WATER, WATER, WATER],
]

TILE_SIZE = 20


class Player:

    def __init__(self):
        self.image = pygame.image.load(
            str(resources_dir / "images/boy_r.png"))
        self.pos = [0, 0]


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (len(tile_map)*TILE_SIZE, len(tile_map[0])*TILE_SIZE))
    pygame.display.set_caption("Pygame Test")
    player = Player()
    map_size = [len(tile_map[0])-1, len(tile_map)-1]

    while(True):
        # screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and player.pos[0] < map_size[0]:
                    player.pos[0] += 1
                if event.key == pygame.K_LEFT and player.pos[0] > 0:
                    player.pos[0] -= 1
                if event.key == pygame.K_DOWN and player.pos[1] < map_size[1]:
                    player.pos[1] += 1
                if event.key == pygame.K_UP and player.pos[1] > 0:
                    player.pos[1] -= 1

        for row, row_tiles in enumerate(tile_map):
            for column, tile in enumerate(row_tiles):
                screen.blit(
                    pygame.transform.scale(
                        tile_textures[tile_map[row][column]],
                        (TILE_SIZE, TILE_SIZE)),
                    (column*TILE_SIZE, row*TILE_SIZE))

        screen.blit(
            player.image, (player.pos[0]*TILE_SIZE, player.pos[1]*TILE_SIZE))

        pygame.display.update()


if __name__ == "__main__":
    main()
