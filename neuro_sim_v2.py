from ursina import *
import random
import math

app = Ursina()

window.title = 'Bio-Molecular Neuron - Anatomical Structure'
window.color = color.black
EditorCamera() 

class NeuronStructure(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # SOMA (Cuerpo Celular)
        self.soma = Entity(parent=self, model='sphere', color=color.rgba(255, 100, 100, 50), scale=6, double_sided=True)
        self.nucleus = Entity(parent=self, model='sphere', color=color.rgba(100, 0, 0, 150), scale=2.5)

        # DENDRITAS (Ramificaciones)
        for i in range(20): 
            random_dir = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized()
            d_pos = random_dir * 3 
            
            Entity(
                parent=self.soma, 
                model='cylinder', 
                color=color.rgba(255, 100, 100, 100), 
                scale=(.1, random.uniform(2,5), .1), 
                position=d_pos,
                look_at=self.soma.position + random_dir * 10
            )

        # AXON
        self.axon_shaft = Entity(parent=self, model='cylinder', color=color.rgba(255, 100, 100, 80), scale=(.2, 12, .2), rotation=(0,0,90), position=(6,0,0))

        # VAINA DE MIELINA
        for i in range(5):
            seg_pos = -0.4 + (i * 0.2)
            Entity(parent=self.axon_shaft, model='sphere', color=color.yellow, scale=(1.5, .1, 1.5), position=(0, seg_pos, 0))

class Ion(Entity):
    def __init__(self, tipo='Na', **kwargs):
        super().__init__(model='sphere', scale=0.15, **kwargs)
        self.tipo = tipo
        self.color = color.yellow if tipo == 'Na' else color.cyan
        self.velocity = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))

    def update(self):
        self.position += self.velocity * time.dt
        
        self.velocity += Vec3(random.uniform(-.1,.1), random.uniform(-.1,.1), random.uniform(-.1,.1))
        
        dist = self.position.length()
        if self.tipo == 'Na' and dist < 6.2:
            self.velocity = -self.position.normalized() * self.velocity.length()
        elif self.tipo == 'K' and dist > 5.8:
            self.velocity = -self.position.normalized() * self.velocity.length()

structure = NeuronStructure()

for i in range(100):
    pos = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized() * random.uniform(7, 10)
    Ion(tipo='Na', position=pos)

for i in range(100):
    pos = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized() * random.uniform(2, 5)
    Ion(tipo='K', position=pos)

def update():
    structure.nucleus.scale = 2.5 + math.sin(time.time() * 2) * 0.1

app.run()