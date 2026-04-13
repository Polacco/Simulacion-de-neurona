from ursina import *
import random
import math

app = Ursina()

window.title = 'Bio-Molecular Neuron Simulator'
window.color = color.black
window.fps_counter.enabled = True

NA_COUNT = 150  # Sodio (Amarillo)
K_COUNT = 150   # Potasio (Azul)
particulas = []

membrana = Entity(model='sphere', color=color.rgba(255,255,255,40), scale=5, double_sided=True)

class Ion(Entity):
    def __init__(self, tipo='Na', **kwargs):
        super().__init__(
            model='sphere',
            scale=0.12,
            **kwargs
        )
        self.tipo = tipo
        if tipo == 'Na':
            self.color = color.yellow
            self.carga = 1
        else:
            self.color = color.cyan
            self.carga = 1
            
        self.velocity = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))

    def update(self):
        self.position += self.velocity * time.dt
        
        dist_al_centro = self.position.length()
        
        if self.tipo == 'Na' and dist_al_centro < 2.6:
            self.velocity = -self.position.normalized() * self.velocity.length()
        elif self.tipo == 'K' and dist_al_centro > 2.4:
            self.velocity = -self.position.normalized() * self.velocity.length()
            
        self.velocity += Vec3(random.uniform(-.1,.1), random.uniform(-.1,.1), random.uniform(-.1,.1))

for i in range(NA_COUNT):
    pos = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized() * random.uniform(3, 4.5)
    particulas.append(Ion(tipo='Na', position=pos))

for i in range(K_COUNT):
    pos = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized() * random.uniform(0, 2)
    particulas.append(Ion(tipo='K', position=pos))

EditorCamera()
light = PointLight(parent=camera, position=(0,0,0), color=color.white)

def update():
    membrana.scale = 5 + math.sin(time.time() * 2) * 0.05
    membrana.color = color.rgba(255, 255, 255, 30 + math.sin(time.time()) * 10)

app.run()