#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int some_function(int device_id) {
	return 1;
}

int endless_loop(void) {
	while(1) {
		sleep(1);
		printf("endlesssss loooooop\n");
	}
}