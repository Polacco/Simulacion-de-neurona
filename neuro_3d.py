from ursina import *
import random

app = Ursina()

window.title = 'Simulación de Partículas - Entorno Físico'
window.borderless = False
window.color = color.black

NUM_PARTICULAS = 500
particulas = []

membrana = Entity(model='sphere', color=color.rgba(255,255,255,20), scale=10, double_sided=True)

for i in range(NUM_PARTICULAS):
    p = Entity(
        model='sphere',
        color=color.hsv(random.uniform(280, 320), 1, 1), 
        scale=0.15,
        position=(random.uniform(-4, 4), random.uniform(-4, 4), random.uniform(-4, 4)),
        velocity=Vec3(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)) * 2
    )
    particulas.append(p)

def update():
    for p in particulas:
        p.position += p.velocity * time.dt
        
        if p.position.length() > 4.8:
            p.velocity = -p.position.normalized() * p.velocity.length()

EditorCamera()

app.run()