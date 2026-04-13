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
        
        self.soma = Entity(parent=self, model='sphere', color=color.rgba(255, 120, 150, 80), scale=6)
        
        self.nucleus = Entity(parent=self, model='sphere', color=color.rgba(255, 50, 50, 200), scale=2)

        for _ in range(15): 
            r_dir = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized()
            
            if r_dir.x > 0.3: 
                r_dir.x *= -1
                
            d_length = random.uniform(2, 5)
            
            dendrite = Entity(parent=self, model='cylinder', color=color.rgba(255, 120, 150, 150), scale=(0.15, d_length, 0.15), position=r_dir * 3)
            
            dendrite.look_at(dendrite.position + r_dir)
            dendrite.rotation_x += 90 

        self.axon = Entity(parent=self, model='cylinder', color=color.rgba(255, 120, 150, 150), scale=(0.3, 15, 0.3), position=(9, 0, 0), rotation=(0, 0, 90))

        for i in range(5):
            x_pos = 4.5 + (i * 2.5)
            Entity(parent=self, model='cylinder', color=color.rgba(255, 220, 50, 200), scale=(0.6, 1.8, 0.6), position=(x_pos, 0, 0), rotation=(0, 0, 90))

class Ion(Entity):
    def __init__(self, tipo='Na', **kwargs):
        super().__init__(model='sphere', scale=0.12, **kwargs)
        self.tipo = tipo
        self.color = color.yellow if tipo == 'Na' else color.cyan
        self.velocity = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))

    def update(self):
        self.position += self.velocity * time.dt
        self.velocity += Vec3(random.uniform(-.1,.1), random.uniform(-.1,.1), random.uniform(-.1,.1))
        
        dist = self.position.length()
        if self.tipo == 'Na' and dist < 6.5: # Sodio choca por fuera
            self.velocity = -self.position.normalized() * self.velocity.length()
        elif self.tipo == 'K' and dist > 5.5: # Potasio choca por dentro
            self.velocity = -self.position.normalized() * self.velocity.length()

structure = NeuronStructure()

for _ in range(120):
    pos = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized() * random.uniform(7, 10)
    Ion(tipo='Na', position=pos)

for _ in range(120):
    pos = Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)).normalized() * random.uniform(1.5, 4)
    Ion(tipo='K', position=pos)

def update():
    structure.nucleus.scale = 2 + math.sin(time.time() * 3) * 0.1

app.run()