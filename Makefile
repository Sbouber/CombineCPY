CC = gcc
NAME = cpy

all:
	$(CC) -c -Wall -Werror cpy.c

	$(CC) -shared -o $(NAME).so cpy.o

run:
	python cpy.py

clean:
	rm *.o *.so