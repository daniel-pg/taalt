#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Daniel Paulo Garcia © 2020

taalt.py

Descrição: Jogo de linha de comando, similar ao Tic-Tac-Toe, onde cada jogador deve tentar preencher uma sequencia de k
peças, em diagonal, vertical ou horizontal, em um tabuleiro de dimensões m,n.
"""

import random

import colorama
from colorama import Fore, Back, Style

__author__ = 'Daniel Paulo Garcia'
__copyright__ = 'Copyright 2020, Taalt!'
# __credits__ = ['{credit_list}']
# __license__ = '{license}'
__version__ = '0.0.1'
# __maintainer__ = '{maintainer}'
# __email__ = '{contact_email}'
# __status__ = '{dev_status}'


class TaaltGame:
    def __init__(self, m: int, n: int, k: int, /, has_gravity: bool = False, check_diagonals: bool = True):
        self.board = [[0 for _ in range(m)] for _ in range(n)]
        self.m = m
        self.n = n
        self.k = k
        self.has_gravity = has_gravity
        self.check_diagonals = check_diagonals
        # self.misere_mode = False
        # self.n_of_players = 2
        # self.n_of_bots = 0
        self.player_symbols = ['X', 'O', 'Y', '+']

    def draw_board(self):
        print(colorama.ansi.clear_screen())

        print(Fore.LIGHTCYAN_EX, end='')
        print(("Taalt! " + __version__).center(self.m))
        print()
        print(Style.RESET_ALL, end='')

        for row in self.board:
            print("+---" * self.m + "+")

            for column in row:
                if 0 < column <= 4:
                    print("| " + self.player_symbols[column], end=' ')
                else:
                    print("| - ", end='')

            print("|")

        print("+---" * self.m + "+")

    def check_for_winner(self) -> bool:
        return True

    def make_move(self):
        pass

    def play(self):
        print()

        while True:
            self.draw_board()
            self.make_move()
            if self.check_for_winner():
                break
            else:
                pass


def print_greet_message():
    print(Fore.RED, end='')
    print(r"  ______            ____  __")
    print(r" /_  __/___ _____ _/ / /_/ /")
    print(r"  / / / __ `/ __ `/ / __/ / ")
    print(r" / / / /_/ / /_/ / / /_/_/  ")
    print(r"/_/  \__,_/\__,_/_/\__(_)   ")
    print(Style.RESET_ALL, end='')
    print()


def print_info(msg, end: str = '\n'):
    print(Fore.YELLOW + Style.BRIGHT + msg + Style.RESET_ALL, end=end)


def configure_game_settings(parameters: dict):
    # TODO: Validar os valores de entrada
    print_info("Qual deve ser a altura do tabuleiro?")
    parameters['m'] = int(input("m: "))

    print_info("Qual deve ser a largura do tabuleiro?")
    parameters['n'] = int(input("n: "))

    print_info("Quantas casas devem ser ocupadas em sequencia no tabuleiro para ganhar o jogo?")
    parameters['k'] = int(input("k: "))


def main():
    colorama.init()

    parameters = dict()

    print_greet_message()
    configure_game_settings(parameters)

    # game = TaaltGame(**parameters)
    # game.play()

    colorama.deinit()


if __name__ == '__main__':
    main()
