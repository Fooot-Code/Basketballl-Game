import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRAVITY = 0.1
BOUNCE_IMPACT = 0.6

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basketball Shooter")

# Ball properties
ball_radius = 20
ball_color = (255, 165, 0)  # Orange

# Class(es)
class Ball:
    def __init__(self):
        self.x = 0
        self.y = HEIGHT // 2
        self.startingX = 0
        self.startingY = HEIGHT //2 
        self.vel_x = 0
        self.vel_y = 0
        self.is_shot = False    

    def draw(self):
        pygame.draw.circle(screen, ball_color, (int(self.x), int(self.y)), ball_radius) 

    def shoot(self, power):
        angle = math.pi / 4  # Fixed launch angle (45 degrees)
        self.vel_x = power * math.cos(angle)
        self.vel_y = -power * math.sin(angle)
        self.is_shot = True 
        

    def update(self):
        if self.is_shot:
            self.x += self.vel_x
            self.y += self.vel_y
            self.vel_y += GRAVITY   

            # Check if ball hits the ground or the ceiling
            if self.y + ball_radius >= HEIGHT or self.y - ball_radius <= 0:
                self.y = min(self.y, HEIGHT - ball_radius)
                self.y = max(self.y, ball_radius)
                self.vel_y *= -BOUNCE_IMPACT

            # elif self.vel_x <= 0.001 and self.vel_y <= 0.001 and self.is_shot == True:
            #     self.x = self.startingX
            #     self.y = self.startingY
            #     self.is_shot = False

            # Check if ball hits the left or right wall
            if self.x + ball_radius >= WIDTH or self.x - ball_radius <= 0:
                self.x = min(self.x, WIDTH - ball_radius)
                self.x = max(self.x, ball_radius)
                self.vel_x *= -BOUNCE_IMPACT

            # elif self.vel_x <= 0.001 and self.vel_y <= 0.001 and self.is_shot == True:
            #     self.x = self.startingX
            #     self.y = self.startingY
            #     self.is_shot = False


# Functions

        
       
    

def main():
    clock = pygame.time.Clock()
    ball = Ball()
    power = 0

    while True:


        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    power = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    ball.shoot(power)
                    power = 0

        # Calculate power based on how long space bar is held
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            power += 0.1

        # Draw ball
        ball.draw()

        # Update ball position
        ball.update()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
