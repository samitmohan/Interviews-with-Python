#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    pid_t pid = fork();
    pid = fork();
    pid = fork();
    if (pid==0) {
	fork();
    }
    fork();
    return 0;
}

