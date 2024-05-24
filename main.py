import pygame
import tabla
import plocica
import constants
import upis_u_fajl

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

tabla = tabla.Tabla()
matrica = tabla.getMatrica()
plocica = plocica.Plocica()

def prikazi_pozadinu(matrica):
    global text_button_rect
    """Inicijalizacija ekrana"""

    screen.fill(color=constants.BEIGE)
    font = pygame.font.SysFont("Serif", 25)
    pygame.draw.rect(screen, constants.BEIGE, (0, 0, constants.WIDTH, 50), 0)

    """Labele za score-ove"""
    score_text = font.render(f"Score: {tabla.getScore()}", True, constants.TRADITIONAL_BROWN)
    best_text = font.render(f"Best: {upis_u_fajl.citanje_najveceg_scorea()}", True, constants.TRADITIONAL_BROWN)
    screen.blit(score_text, (70, 20))
    screen.blit(best_text, (200, 20))

    """Dugme za opciju New Game"""
    new_game_button = pygame.Rect(350, 18, 120, 30)
    pygame.draw.rect(screen, constants.TRADITIONAL_BROWN, new_game_button)
    new_game_text = font.render("New Game", True, constants.WHITE)
    text_button_rect = new_game_text.get_rect(center=new_game_button.center)
    screen.blit(new_game_text, text_button_rect)

    """Iscrtavanje matrice"""
    sirina_celije = constants.WIDTH // constants.GRID_SIZE
    visina_celije = (constants.HEIGHT - 50) // constants.GRID_SIZE
    font_matrice_size = 40
    for red in range(constants.GRID_SIZE):
        for kolona in range(constants.GRID_SIZE):
            x = kolona * sirina_celije
            if red == 0:
                y = 50
            else:
                y = (red * visina_celije) + 50

            boja_celije = constants.TRADITIONAL_BROWN
            pygame.draw.rect(screen, constants.BROWN, (x, y, sirina_celije, visina_celije), 25)
            if matrica[red][kolona] in ["2", "4", "8"]:
                font_matrice_size = 40
            elif matrica[red][kolona] in ["16", "32", "64"]:
                font_matrice_size = 35
                boja_celije = constants.DEEP_SEA_CORAL
            elif matrica[red][kolona] in ["128", "256", "512"]:
                font_matrice_size = 30
                boja_celije = constants.SALMON
            elif matrica[red][kolona] in ["1024", "2048"]:
                font_matrice_size = 25
                boja_celije = constants.UA_RED

            font_matrice = pygame.font.SysFont("Serif", font_matrice_size)
            tekst = font_matrice.render(matrica[red][kolona], True, boja_celije)
            tekst_rect = tekst.get_rect(center=(x + sirina_celije // 2, y + visina_celije // 2))

            screen.blit(tekst, tekst_rect)

    """Prikazivanje ishoda kraja igre"""

    if tabla.getIshod() != constants.PLAYING:
        pozadina = pygame.Surface((constants.WIDTH, constants.HEIGHT))
        pozadina.blit(screen, (0, 0))
        ishod_pozadina = pygame.transform.smoothscale(pozadina, (constants.WIDTH, constants.HEIGHT))

        screen.fill((0, 0, 0))
        screen.blit(ishod_pozadina, (0, 0))
        font_pozadina = pygame.font.SysFont("Serif", font_matrice_size)
        text_ishod = font_pozadina.render(tabla.getIshod(), True, constants.TRADITIONAL_BROWN)
        text_ishod_rect = text_ishod.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2))
        screen.blit(text_ishod, text_ishod_rect)

    pygame.display.flip()


def main():
    tabla.prokazi_prve_dve_plocice()
    prikazi_pozadinu(matrica)

    while True:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if plocica.ima_li_poteza_nagore(matrica):
                        plocica.pomeri_nagore(matrica, tabla)
                        tabla.prikazi_random_plocicu()

                if event.key == pygame.K_DOWN:
                    if plocica.ima_li_poteza_nadole(matrica):
                        plocica.pomeri_nadole(matrica, tabla)
                        tabla.prikazi_random_plocicu()

                if event.key == pygame.K_LEFT:
                    if plocica.ima_li_poteza_ulevo(matrica):
                        plocica.pomeri_ulevo(matrica, tabla)
                        tabla.prikazi_random_plocicu()

                if event.key == pygame.K_RIGHT:
                    if plocica.ima_li_poteza_udesno(matrica):
                        plocica.pomeri_udesno(matrica, tabla)
                        tabla.prikazi_random_plocicu()

                tabla.kraj_igre(plocica)
                prikazi_pozadinu(matrica)

                if tabla.getIshod() == constants.PLAYING:
                    continue
                elif tabla.getIshod() != constants.PLAYING:
                    upis_u_fajl.upis_scorea_u_fajl(tabla.getScore())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_button_rect.collidepoint(event.pos):
                    tabla.nova_igra()
                    nova_matrica = tabla.getMatrica()
                    tabla.prokazi_prve_dve_plocice()
                    prikazi_pozadinu(nova_matrica)

            if event.type == pygame.QUIT:
                upis_u_fajl.upis_scorea_u_fajl(tabla.getScore())
                pygame.quit()
                return


if __name__ == '__main__':
    main()
