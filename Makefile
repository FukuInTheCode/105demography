##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## Makefile for 105demography
##

NAME = 105demography

CC = gcc

FLAGS =  -Wall -Wextra -Wno-unused-value -Wno-sign-compare 				-Wno-unused-parameter -I./include

SRC = $(shell find ./ -type f -name "*.c")

OBJ = $(SRC:./%.c=./obj/%.o)

all: $(NAME)

$(NAME):	$(OBJ)
			 $(CC) $(FLAGS) -o $(NAME) $(OBJ)

./obj/%.o: ./%.c
		@mkdir -p $(dir $@)
		@$(CC) -c -o $@ $< $(FLAGS)

clean:
		@rm -rf obj

fclean: clean
		@rm -f $(NAME)

re: fclean all

