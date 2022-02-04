#ifndef SLIDELINE_H
#define SLIDELINE_H

#include <stdio.h>
#include <stdlib.h>

#define SLIDE_LEFT 0
#define SLIDE_RIGHT 1

int slide_line(int *line, size_t size, int direction);
void slide_l(int *line, size_t size);
void slide_r(int *line, size_t size);
void combine(int *line, size_t size, int direction);

#endif /* SLIDELINE_H */
