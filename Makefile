exec = bin/termachat.exe
src = $(wildcard src/*.cpp)
cc = g++
flags = -Wall -Wextra -Werror -std=c++17 -g
libs = 

all: $(exec)

$(exec): $(src)
	$(cc) $(flags) -o $(exec) $(src) $(libs)
	./$(exec)

clean:
	rm -f $(exec)