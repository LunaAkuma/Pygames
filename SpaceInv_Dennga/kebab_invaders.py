import pygame
import sys

# Pygame initialisieren
pygame.init()

# Fenster und Titel erstellen
fenster_breite = 800
fenster_hoehe = 600
fenster = pygame.display.set_mode((fenster_breite, fenster_hoehe))
pygame.display.set_caption("Kebab Invaders")

class Spieler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Schiff png laden
        original_bild = pygame.image.load('SpaceInv_Dennga/assets/spaceship.png').convert_alpha()
        
        # Größe des Schiffs png halbieren
        original_breite = original_bild.get_width()
        original_hoehe = original_bild.get_height()
        neue_groesse = (original_breite // 2, original_hoehe // 2)
        
        # Schiff auf Hintergrund skalieren
        self.image = pygame.transform.scale(original_bild, neue_groesse)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = fenster_breite // 2
        self.rect.bottom = fenster_hoehe + 150
        self.geschwindigkeit = 20

# Klasse für das Projektil
class Kugel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Kugel PNG laden
        original_bild_kugel = pygame.image.load('SpaceInv_Dennga/assets/bullet.png').convert_alpha()
        
        # Kugel PNG skalieren
        neue_groesse_kugel = (60, 60)  
        self.image = pygame.transform.scale(original_bild_kugel, neue_groesse_kugel)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.geschwindigkeit = -1  # Negativer Wert, um sich nach oben zu bewegen

    def update(self):
        self.rect.y += self.geschwindigkeit
        # Entfernt den Schuss, wenn er den oberen Bildschirmrand verlässt
        if self.rect.bottom < 0:
            self.kill()

# --- Sprite Gruppe (Pygame feature) ---
alle_sprites = pygame.sprite.Group()
kugeln = pygame.sprite.Group()
spieler = Spieler()
alle_sprites.add(spieler)

# Spielschleife (Game Loop)
laeuft = True
while laeuft:
    # Event-Handling (Eingaben)
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.QUIT:
            laeuft = False

        # Tastenabfrage im Event-Loop
        if ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_LEFT:
                spieler.rect.x -= spieler.geschwindigkeit
            if ereignis.key == pygame.K_RIGHT:
                spieler.rect.x += spieler.geschwindigkeit
            if ereignis.key == pygame.K_SPACE:
                # KORREKTUR: Feste Y-Position für die Kugel, wie gewünscht.
                # Du kannst den Wert 700 anpassen, um die Kugel nach oben (+) oder unten (-) zu verschieben.
                neue_kugel = Kugel(spieler.rect.centerx, 700) 
                alle_sprites.add(neue_kugel)
                kugeln.add(neue_kugel)

    # Spiel-Logik und Zeichnen
    fenster.fill((0, 0, 0))
    alle_sprites.update()  
    alle_sprites.draw(fenster)  

    # Fenster aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()
sys.exit()