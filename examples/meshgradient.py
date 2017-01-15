#!/usr/bin/env python

import math
import cairo

WIDTH, HEIGHT  = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale (WIDTH/1.0, HEIGHT/1.0)

pat = cairo.MeshGradient ()
pat.begin_patch ()
pat.move_to (0, 0)
pat.line_to (0.5, 0)
pat.line_to (0.5, 1)
pat.line_to (0, 1)
pat.set_corner_color_rgb (0, 1, 0, 0)
pat.set_corner_color_rgb (1, 0, 1, 0)
pat.set_corner_color_rgb (2, 0, 0, 1)
pat.set_corner_color_rgb (3, 1, 1, 0)
pat.end_patch ()

pat.begin_patch ()
pat.move_to (0.5, 0)
pat.curve_to (0.75, 0.5, 0.75, 0.5, 1, 0)
pat.line_to (1, 1)
pat.curve_to (0.75, 0.5, 0.75, 0.5, 0.5, 1)
pat.set_corner_color_rgb (0, 0, 1, 0)
pat.set_corner_color_rgb (1, 0, 1, 1)
pat.set_corner_color_rgb (2, 1, 0, 1)
pat.set_corner_color_rgb (3, 0, 0, 1)
pat.end_patch ()

ctx.rectangle (0,0,1,1)
ctx.set_source (pat)
ctx.fill ()

surface.write_to_png('meshgradient.png')
