#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <random>
#include <cmath>

struct Ion {
    float x, y; // posicion
    float vx, vy; // velocidad
    float r, g, b; // color
    int tipo;
};

int main() {
    if (!glfwInit()) return -1;
    GLFWwindow* window = glfwCreateWindow(1024, 768, "Bio-Molecular Neuron - Laboratorio C++", NULL, NULL);
    if (!window) { glfwTerminate(); return -1; }
    glfwMakeContextCurrent(window);

    std::vector<Ion> iones;
    int cantidad_na = 1000;
    int cantidad_k = 1000;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> angle_dist(0.0f, 3.14159f * 2.0f);
    std::uniform_real_distribution<float> vel_dist(-0.005f, 0.005f);

    // sodio
    for (int i = 0; i < cantidad_na; ++i) {
        float angle = angle_dist(gen);
        float radius = 0.6f + std::abs(vel_dist(gen) * 60.0f); 
        iones.push_back({
            cos(angle) * radius, sin(angle) * radius,
            vel_dist(gen), vel_dist(gen),
            1.0f, 1.0f, 0.0f,
            0
        });
    }

    // potasio
    for (int i = 0; i < cantidad_k; ++i) {
        float angle = angle_dist(gen);
        float radius = std::abs(vel_dist(gen) * 80.0f); 
        iones.push_back({
            cos(angle) * radius, sin(angle) * radius, 
            vel_dist(gen), vel_dist(gen),             
            0.0f, 1.0f, 1.0f,
            1                                         
        });
    }

    while (!glfwWindowShouldClose(window)) {
        glClearColor(0.02f, 0.02f, 0.04f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glPointSize(3.0f); 
        glBegin(GL_POINTS);

        for (auto& ion : iones) {
            ion.x += ion.vx;
            ion.y += ion.vy;

            float dist = std::sqrt(ion.x * ion.x + ion.y * ion.y);
            
            if (ion.tipo == 0 && dist < 0.5f) {
                ion.vx *= -1; 
                ion.vy *= -1;
            }
            else if (ion.tipo == 1 && dist > 0.45f) {
                ion.vx *= -1; 
                ion.vy *= -1;
            }

            if (std::abs(ion.x) > 1.0f) ion.vx *= -1;
            if (std::abs(ion.y) > 1.0f) ion.vy *= -1;

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