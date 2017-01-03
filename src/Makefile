
CC = i686-pc-toaru-gcc
CFLAGS = -I${TOOLCHAIN}/python/include/python3.6m $(shell pkg-config --cflags cairo) -DVERSION='"1.10.1"' -DPYCAIRO_VERSION_MAJOR=1 -DPYCAIRO_VERSION_MINOR=10 -DPYCAIRO_VERSION_MICRO=1


OBJS = cairomodule.o  context.o  font.o  matrix.o  path.o  pattern.o  region.o  surface.o

.PHONY: all install

all: _cairo.so

install: _cairo.so
	echo "from _cairo import *" > ${TOOLCHAIN}/python/lib/python3.6/cairo.py
	cp _cairo.so ${TOOLCHAIN}/python/lib/python3.6/_cairo.so

$(OBJS):

_cairo.so: $(OBJS)
	$(CC) -shared -o _cairo.so $(OBJS) -lpython3.6m -lcairo -lc
