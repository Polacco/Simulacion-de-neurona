#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <random>
#include <cmath>

struct Ion {
    float x, y;       
    float vx, vy;     
    float r, g, b;    
    int tipo;         
};

int main() {
    if (!glfwInit()) return -1;
    GLFWwindow* window = glfwCreateWindow(1024, 768, "Bio-Molecular Neuron - Fase 2: Axon Activo", NULL, NULL);
    if (!window) { glfwTerminate(); return -1; }
    glfwMakeContextCurrent(window);
    glfwSwapInterval(1); // maximo de 60 FPS

    std::vector<Ion> iones;
    int cantidad_na = 2500; 
    int cantidad_k = 1500;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> angle_dist(0.0f, 3.14159f * 2.0f);
    std::uniform_real_distribution<float> pos_dist(0.0f, 1.0f);
    std::uniform_real_distribution<float> brownian(-0.002f, 0.002f);

    float soma_cx = -0.5f;
    float soma_cy = 0.0f;

    // generar poblacion
    for (int i = 0; i < cantidad_na; ++i) {
        float angle = angle_dist(gen); float radius = pos_dist(gen);
        iones.push_back({ soma_cx + cos(angle)*radius, soma_cy + sin(angle)*radius, 0, 0, 1.0f, 0.8f, 0.0f, 0 });
    }
    for (int i = 0; i < cantidad_k; ++i) {
        float angle = angle_dist(gen); float radius = pos_dist(gen);
        iones.push_back({ soma_cx + cos(angle)*radius, soma_cy + sin(angle)*radius, 0, 0, 0.0f, 0.8f, 1.0f, 1 });
    }

    while (!glfwWindowShouldClose(window)) {
        glClearColor(0.02f, 0.02f, 0.04f, 1.0f); 
        glClear(GL_COLOR_BUFFER_BIT);

        bool is_firing = (glfwGetKey(window, GLFW_KEY_SPACE) == GLFW_PRESS);

        glPointSize(3.0f); 
        glBegin(GL_POINTS);

        for (auto& ion : iones) {
            float dx = ion.x - soma_cx;
            float dy = ion.y - soma_cy;
            float dist = std::sqrt(dx * dx + dy * dy);
            if (dist == 0.0f) dist = 0.001f;

            float dir_x = dx / dist;
            float dir_y = dy / dist;

            // logica del axon
            bool en_axon = (ion.x > soma_cx && std::abs(ion.y) < 0.15f);
            bool adentro = (dist < 0.4f || en_axon);

            if (is_firing) {
                if (ion.tipo == 0) { // sodio
                    if (!adentro) {
                        if (ion.x > soma_cx) ion.vy += (0.0f - ion.y) * 0.01f; 
                        else { ion.vx -= dir_x * 0.005f; ion.vy -= dir_y * 0.005f; }
                    } else {
                        ion.vx += 0.012f; 
                    }
                } else if (ion.tipo == 1) { // potasio
                    ion.vx += dir_x * 0.001f; ion.vy += dir_y * 0.001f;
                }
            } else { // estado de reposo neuronal
                if (ion.tipo == 0) { // sodio entra para despolarizar
                    if (adentro) {
                        if (en_axon) ion.vy += (ion.y > 0 ? 0.006f : -0.006f);
                        else { ion.vx += dir_x * 0.004f; ion.vy += dir_y * 0.004f; }
                    } else if (dist > 0.9f && !en_axon) { 
                        ion.vx -= dir_x * 0.001f; ion.vy -= dir_y * 0.001f;
                    }
                } else if (ion.tipo == 1) { // potasio sale para repolarizar
                    if (!adentro) {
                        if (ion.x > soma_cx) ion.vy += (0.0f - ion.y) * 0.006f; // movimiento a axon
                        else { ion.vx -= dir_x * 0.004f; ion.vy -= dir_y * 0.004f; }
                    }
                }
            }

            if (ion.x > 1.2f) ion.x = -1.2f;

            ion.vx *= 0.88f; 
            ion.vy *= 0.88f;

            ion.vx += brownian(gen);
            ion.vy += brownian(gen);

            ion.x += ion.vx;
            ion.y += ion.vy;

            glColor3f(ion.r, ion.g, ion.b);
            glVertex2f(ion.x, ion.y);
        }

        glEnd();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}