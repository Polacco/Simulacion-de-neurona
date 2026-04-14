#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <random>
#include <cmath>

struct Ion {
    float x, y; // posicion
    float vx, vy; //velocidad
    float r, g, b; //color
    int tipo;
};

int main() {
    if (!glfwInit()) return -1;
    GLFWwindow* window = glfwCreateWindow(1024, 768, "Bio-Molecular Neuron - Potencial de Accion", NULL, NULL);
    if (!window) { glfwTerminate(); return -1; }
    glfwMakeContextCurrent(window);
    glfwSwapInterval(1);

    std::vector<Ion> iones;
    int cantidad_na = 1500;
    int cantidad_k = 1500;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> angle_dist(0.0f, 3.14159f * 2.0f);
    std::uniform_real_distribution<float> pos_dist(0.0f, 1.0f);
    std::uniform_real_distribution<float> brownian(-0.002f, 0.002f);

    // sodio
    for (int i = 0; i < cantidad_na; ++i) {
        float angle = angle_dist(gen); float radius = pos_dist(gen);
        iones.push_back({ cos(angle)*radius, sin(angle)*radius, 0, 0, 1.0f, 0.8f, 0.0f, 0 }); // amarillo
    } // potasio
    for (int i = 0; i < cantidad_k; ++i) {
        float angle = angle_dist(gen); float radius = pos_dist(gen);
        iones.push_back({ cos(angle)*radius, sin(angle)*radius, 0, 0, 0.0f, 0.8f, 1.0f, 1 }); // celeste
    }

    while (!glfwWindowShouldClose(window)) {
        glClearColor(0.02f, 0.02f, 0.04f, 1.0f); 
        glClear(GL_COLOR_BUFFER_BIT);

        bool is_firing = (glfwGetKey(window, GLFW_KEY_SPACE) == GLFW_PRESS);

        glPointSize(3.0f); 
        glBegin(GL_POINTS);

        for (auto& ion : iones) {
            float dist = std::sqrt(ion.x * ion.x + ion.y * ion.y);
            if (dist == 0.0f) dist = 0.001f;

            float dir_x = ion.x / dist;
            float dir_y = ion.y / dist;

            if (is_firing) {
                if (ion.tipo == 0) {
                    ion.vx -= dir_x * 0.005f;
                    ion.vy -= dir_y * 0.005f;
                } else if (ion.tipo == 1) {
                    ion.vx += dir_x * 0.001f;
                    ion.vy += dir_y * 0.001f;
                }
            } else {
                if (ion.tipo == 0) {
                    if (dist < 0.6f) {
                        ion.vx += dir_x * 0.002f;
                        ion.vy += dir_y * 0.002f;
                    } else if (dist > 0.8f) {
                        ion.vx -= dir_x * 0.001f;
                        ion.vy -= dir_y * 0.001f;
                    }
                } else if (ion.tipo == 1) {
                    if (dist > 0.4f) {
                        ion.vx -= dir_x * 0.003f;
                        ion.vy -= dir_y * 0.003f;
                    }
                }
            }

            ion.vx *= 0.92f;
            ion.vy *= 0.92f;

            // movimiento browniano
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