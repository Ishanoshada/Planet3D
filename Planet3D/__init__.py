import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_planet_center(x, y, z):
    glColor3f(0.0, 0.0, 0.0)  # Black color
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex3f(x, y, z)
    glEnd()

class Planet:
    def __init__(self, name, radius, orbit_radius, rotation_speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.rotation_speed = rotation_speed
        self.color = color
        self.angle = 0.0
        self.rings = None
        self.moons = []

    def draw(self):
        try:
            glEnable(GL_TEXTURE_2D)

            glPushMatrix()
            glRotatef(self.rotation_speed, 0, 1, 0)

            x = self.orbit_radius * math.cos(math.radians(self.angle))
            z = self.orbit_radius * math.sin(math.radians(self.angle))

            glTranslatef(x, 0, z)

            glColor3f(*self.color)
            gluSphere(gluNewQuadric(), self.radius, 50, 50)

            self.draw_rings()
            self.draw_moons()

            glPopMatrix()
            glDisable(GL_TEXTURE_2D)

            self.angle += self.rotation_speed

        except Exception as e:
            print(f"Error drawing planet {self.name}: {e}")

    def draw_rings(self):
        if self.rings:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

            glColor4f(*self.rings["color"], self.rings["transparency"])

            glBegin(GL_QUADS)
            glVertex3f(-self.rings["width"], 0, -self.rings["radius"])
            glVertex3f(self.rings["width"], 0, -self.rings["radius"])
            glVertex3f(self.rings["width"], 0, self.rings["radius"])
            glVertex3f(-self.rings["width"], 0, self.rings["radius"])
            glEnd()

            glDisable(GL_BLEND)

    def draw_moons(self):
        for moon in self.moons:
            moon.draw()

    def draw_orbit(self):
        glColor3f(0.0, 0.0, 1.0)  # Blue color for orbit
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            angle = math.radians(i)
            x = self.orbit_radius * math.cos(angle)
            z = self.orbit_radius * math.sin(angle)
            glVertex3f(x, 0, z)
        glEnd()

    def add_ring(self, radius, width, color, transparency):
        self.rings = {"radius": radius, "width": width, "color": color, "transparency": transparency}

    def add_moon(self, name, radius, orbit_radius, rotation_speed, color):
        moon = Moon(name, radius, orbit_radius, rotation_speed, color)
        self.moons.append(moon)

class Moon:
    def __init__(self, name, radius, orbit_radius, rotation_speed, color):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.rotation_speed = rotation_speed
        self.color = color

    def draw(self):
        try:
            glEnable(GL_TEXTURE_2D)

            glPushMatrix()
            glRotatef(self.rotation_speed, 0, 1, 0)
            glTranslatef(self.orbit_radius, 0, 0)

            glColor3f(*self.color)
            gluSphere(gluNewQuadric(), self.radius, 50, 50)

            glPopMatrix()
            glDisable(GL_TEXTURE_2D)

        except Exception as e:
            print(f"Error drawing moon {self.name}: {e}")

def generate_solar_system(planets, display=(1200, 800), fullscreen=False):
    try:
        pygame.init()

        if fullscreen:
            display = pygame.display.list_modes()[0]
        
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL | FULLSCREEN if fullscreen else OPENGL)

        gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
        glTranslatef(0.0, 0.0, -50)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)

        light_position = [1, 1, 1, 0]
        light_ambient = [0.2, 0.2, 0.2, 1]
        light_diffuse = [1, 1, 1, 1]
        light_specular = [1, 1, 1, 1]

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                glTranslatef(0.1, 0, 0)
            if keys[pygame.K_RIGHT]:
                glTranslatef(-0.1, 0, 0)
            if keys[pygame.K_UP]:
                glTranslatef(0, -0.5, 0)
            if keys[pygame.K_DOWN]:
                glTranslatef(0, 0.5, 0)
            if keys[pygame.K_w]:
                glTranslatef(0, 0, 0.5)
            if keys[pygame.K_s]:
                glTranslatef(0, 0, -0.5)
            if keys[pygame.K_z]:
                glTranslatef(0, 0, 2.0)
            if keys[pygame.K_x]:
                glTranslatef(0, 0, -2.0)

            glRotatef(1, 0, 1, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for planet in planets:
                glPushMatrix()
                planet.draw_orbit()
                planet.draw()
                planet.draw_moons()
                draw_planet_center(0, 0, 0)
                glPopMatrix()

            pygame.display.flip()
            clock.tick(30)

    except Exception as e:
        print(f"Error in generating solar system: {e}")

