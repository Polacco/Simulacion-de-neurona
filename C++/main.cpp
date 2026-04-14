#include <GLFW/glfw3.h>
#include <iostream>

int main() {
    if (!glfwInit()) return -1;

    GLFWwindow* window = glfwCreateWindow(1024, 768, "Bio-Molecular Neuron - C++ Engine", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    // BUCLE PRINCIPAL
    while (!glfwWindowShouldClose(window)) {
        
        glClearColor(0.05f, 0.05f, 0.05f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        
        glPointSize(15.0f); 

        glBegin(GL_POINTS);
            
            glColor3f(1.0f, 1.0f, 0.0f); 
            
            glVertex2f(0.0f, 0.0f); 

        glEnd();
        
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}