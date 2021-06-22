#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - zasdasd
 *
 * Description: asdasda
 * Return: asdasd
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - zasdasd
 *
 * Description: asdasda
 * Return: asdasd
 */

int main(void)
{
	int horda_zombies;
	pid_t zombie;

	for (horda_zombies = 0; horda_zombies < 5; horda_zombies++)
	{
		zombie = fork();
		if (!zombie)
			exit(0);
		printf("Zombie process created, PID: %i\n", zombie);
	}
	infinite_while();
	return (0);
}
