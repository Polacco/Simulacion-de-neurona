#include <GLFW/glfw3.h>
#include <iostream>

int main() {
    if (!glfwInit()) {
        std::cerr << "Error crítico: Fallo al inicializar GLFW." << std::endl;
        return -1;
    }

    GLFWwindow* window = glfwCreateWindow(1024, 768, "Bio-Molecular Neuron - C++ Engine", NULL, NULL);
    if (!window) {
        std::cerr << "Error crítico: Fallo al crear la ventana." << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    while (!glfwWindowShouldClose(window)) {
        
        glClearColor(0.05f, 0.05f, 0.05f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glfwSwapBuffers(window);
        
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}