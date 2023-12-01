import pygame
import random
import sys

class Rammus:
    def __init__(self, position_x, position_y, size_x, size_y, rotation, acceleration, image_path, screen, background_image):
        self.position_x = position_x
        self.position_y = position_y
        self.size_x = size_x
        self.size_y = size_y
        self.rotation = rotation
        self.acceleration = acceleration
        self.image_path = image_path
        self.screen = screen
        self.background_image = background_image
        
        
    def dessiner(self):
        # Redimensionnement de l'image à 100x60
        target_dimensions = (self.size_x, self.size_y)
        
        original_image = pygame.image.load(self.image_path)
        resized_image = pygame.transform.scale(original_image, target_dimensions)
     
        self.avancer()
        # Dessiner l'image au centre
        self.screen.blit(resized_image,
                        # déplacement de rammu
                         (self.position_x,
                          self.position_y))
        
    def avancer(self):
        prex = self.position_x
        prey = self.position_y
        i = random.randint(1,4)
        if i == 1:
            self.position_x -= self.acceleration
        if i == 2:
            self.position_x += self.acceleration
        if i == 3:
            self.position_y -= self.acceleration
        if i == 4:
            self.position_y += self.acceleration
                    
        if(self.collision()):
            self.position_x = prex
            self.position_y = prey
            
        
    def collision(self):
        if (self.position_x < 0 or self.position_x + self.size_x > 1000 or
            self.position_y < 0 or self.position_y + self.size_y > 1000):
            return True
        else: 
            # Vérifier la couleur des coins du rectangle de la voiture
            top_left_color = self.background_image.get_at((int(self.position_x), int(self.position_y)))
            top_right_color = self.background_image.get_at((int(self.position_x + self.size_x), int(self.position_y)))
            bottom_left_color = self.background_image.get_at((int(self.position_x), int(self.position_y + self.size_y)))
            bottom_right_color = self.background_image.get_at((int(self.position_x + self.size_x), int(self.position_y + self.size_y)))

        # Si l'une des couleurs des coins est blanche, la voiture "meurt"
        if any(color == (255, 255, 255, 255) for color in [top_left_color, top_right_color, bottom_left_color, bottom_right_color]):
            return True
        return False

        
        
        

def main():
    # Initialisation de Pygame
    pygame.init()
    
    screen_width = 1500
    screen_height = 1000
    # Création de la fenêtre
    screen = pygame.display.set_mode((screen_width, screen_height))
    image_path = "Rammus_Render.webp"  # Remplacez par le chemin de votre image
    
    # Chargement de l'image de fond
    background_image_path = "maze.webp"  # Remplacez par le chemin de votre image de fond
    background_image = pygame.image.load(background_image_path)
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    
    # Temps initial en millisecondes
    start_time = pygame.time.get_ticks()
    # Police de caractères pour afficher le temps
    font = pygame.font.Font(None, 36)
    
    rammu = [ ]
    for i in range(0, 1):
        rammu.append( Rammus(position_x=520,
                   position_y=0,
                   size_x=20,
                   size_y=30,
                   rotation=0,
                   acceleration=7,
                   image_path=image_path,
                   screen=screen,
                   background_image=background_image))

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Effacement de l'écran
        screen.blit(background_image, (0,0))
        for i in rammu:
            i.dessiner()
         # Afficher le temps écoulé
         
        # Calculer le temps écoulé en millisecondes
        elapsed_time = pygame.time.get_ticks() - start_time

         # Convertir le temps en secondes
        elapsed_seconds = elapsed_time // 1000
        text_surface = font.render(f"Temps écoulé: {elapsed_seconds} secondes", True, (255,2,2))
        
        if elapsed_seconds > 300 : 
            running = False
        
        screen.blit(text_surface, (10, 10))

        # Mise à jour de l'affichage
        pygame.display.flip()



if __name__ == "__main__":
    main()

# Quitter Pygame
pygame.quit()
sys.exit()