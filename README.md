Bio-Molecular Neuron Engine 🧠💻

Este es un motor físico y gráfico en C++ construido desde cero para simular la dinámica molecular y los gradientes electroquímicos de una neurona en tiempo real.


Sobre el Proyecto y mi Motivación

Siendo un Licenciado en Psicología y apasionado por las neurociencias, pasé mucho tiempo estudiando la anatomía del cerebro y cómo la información viaja a través de potenciales de acción. Hoy, trabajando como desarrollador de software, me propuse el desafío técnico de cruzar el puente entre la biología computacional y la programación de muy bajo nivel. Quería ver la teoría biológica funcionando en código, intente usar motores prefabricados (como Unity o Unreal) y lenguajes de alto nivel aunque llegué a enfrentarme a un desafío. En los primeros commits puede verse los intentos de usar Python y Ursina, aunque pronto logre llegar a los límites gráficos, razón por la que me propuse aprender C++ y llevar adelante esta tarea. Este proyecto es el resultado de dicha inquietud. Es un motor propio escrito en C++ puro que simula las leyes termodinámicas y electromagnéticas de miles de iones tanto de Potasio como de Sodio interactuando entre sí, renderizados nativamente por la tarjeta gráfica (GPU).


¿Qué simula exactamente?

En lugar de dibujar formas geométricas estáticas para representar la célula, la anatomía se genera dinámicamente a través de sistemas de partículas guiados por la física:

* Gradiente Electroquímico: Simulación en tiempo real de miles de iones de Potasio (K+, celeste) confinados en el soma, e iones de Sodio (Na+, amarillo) orbitando en el exterior.

* Bomba Sodio-Potasio: Algoritmos matemáticos de confinamiento y repulsión que mantienen a la célula en su estado de reposo.

* Potencial de Acción Interactivo: Al disparar un estímulo (al tocar la tecla Espacio), la permeabilidad de la membrana colapsa. El Sodio invade el núcleo violentamente, despolarizando la célula y generando una onda de energía que viaja a través del axón (creando el flujo direccional anatómico).


Arquitectura Técnica

Para lograr un rendimiento fluido (60 FPS estables) manipulando miles de partículas independientes, la arquitectura del motor se apoya en:

* El lenguaje: C++ (Data-Oriented Design con structs optimizados para la memoria caché).

* Gestor de Construcción: CMake para portabilidad y gestión de dependencias.

* Contexto Gráfico: GLFW para la creación de la ventana nativa y la captura de eventos (teclado/mouse) saltando las capas superficiales del SO.

* Renderizado Pipeline (OpenGL): Gestión directa de vértices y sincronización vertical (VSync).
  Additive Blending: Técnica óptica en la GPU donde el color de las partículas superpuestas se suma matemáticamente para crear núcleos incandescentes (Glow biológico) en lugar de píxeles sólidos.
  Motion Trails: Manipulación del buffer de color para generar estelas de movimiento en el flujo axónico, acentuando la transferencia de energía electromagnética.


Cómo ejecutarlo

Clonar el repositorio
git clone https://github.com/Polacco/Simulacion-de-neurona.git
cd Simulacion-de-neurona

Construir el proyecto con CMake
cmake -B build
cmake --build build

Ejecutar la simulación (en Windows)
.\build\Debug\NeuronSim.exe

Este proyecto nacio de la duda, la curiosidad, la inquietud y las ganas de empujar los límites de mis conocimientos y hasta donde podía llegar yo. No tenía ningún conocimiento acerca de C++ por lo que fue un reto ir aprendiendolo (además de haber sido ayudado por Claude) y estoy satisfecho con el resultado. 
Pido por favor que si alguien ve este repo y encuentra errores, bugs o cosas mal ejecutadas se comunique y me cuente por favor sobre esto así poder aprender más. Muchas gracias y bendiciones a todos!
