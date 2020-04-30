#!/usr/bin/env python3
# -*- coding: utf-8 -*-

radius = 42
pi = 3.1415926
print(round(pi * radius ** 2, 4))

point_1 = (23, 34)

distance = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5

print(radius > distance)

point_2 = (30, 30)

distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5

print(radius > distance_2)

# Зачёт!
