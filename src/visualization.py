import pygame
import time

class Visualization:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Self-Awareness Visualization")
        self.clock = pygame.time.Clock()

    def draw(self, awareness_level, emotion, goals):
        self.screen.fill((0, 0, 0))  # Black background
        
        # Draw a circle representing awareness level
        radius = int(awareness_level * 5)  # Scale the radius with awareness level
        pygame.draw.circle(self.screen, (0, 255, 0), (400, 300), radius)
        
        # Display the awareness level
        font = pygame.font.Font(None, 36)
        text = font.render(f"Awareness Level: {awareness_level}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        
        # Display current emotion
        emotion_text = font.render(f"Emotion: {emotion}", True, (255, 255, 255))
        self.screen.blit(emotion_text, (10, 50))
        
        # Display goals
        goals_text = font.render("Goals:", True, (255, 255, 255))
        self.screen.blit(goals_text, (10, 90))
        y_pos = 130
        for goal in goals:
            goal_text = font.render(goal, True, (255, 255, 255))
            self.screen.blit(goal_text, (10, y_pos))
            y_pos += 30
        
        pygame.display.flip()
        self.clock.tick(60)  # Limit to 60 frames per second

    def run(self, awareness, emotion, goals):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            awareness.increase_awareness()
            awareness.reflect()
            self.draw(awareness.awareness_level, emotion.current_emotion, [goal for goal in goals.goals])
            time.sleep(1)
        pygame.quit()

if __name__ == "__main__":
    from main import SelfAwareness
    from emotion import Emotion
    from goal_setting import GoalSetting
    awareness = SelfAwareness()
    emotion = Emotion()
    goals = GoalSetting()
    viz = Visualization()
    viz.run(awareness, emotion, goals)