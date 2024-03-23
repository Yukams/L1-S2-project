# -*- coding: utf-8 -*-
import copy
import time

#                                    *************************************
#                                                  IMPORTANT
#                                               ---------------
#                                Ce projet est un très long projet (+ 1300 lignes)
#                              Afin de faciliter la lecture et la compréhension, voici
#                            un guide simplifié qui vous donnera toutes les informations
#                           nécessaire pour perdre le moins de temps possible à l'évaluation
#
#                                         https://pastebin.com/BSmH2sDS
#
#                                    *************************************
#
# ********************************************************************************************************** #
# ****** OUTILS POUR L'AFFICHAGE GRAPHIQUE DES GRILLES ****** #

def print_grid(grid):
    horizontal_numbers()
    double_dash()
    # permet d'afficher les 8 lignes de la matrice
    for indice in range(8):
        line(indice, grid)

        # permet de changer le simple_dash en double_dash au milieu du tableau pour signifier le changement de camp
        # et en bas du tableau pour la forme
        if indice != 3 and indice != 7:
            simple_dash()
        else:
            double_dash()
    print("\n\n")


# AFFICHE LA LIGNE DES INDICES DE COLONNES
def horizontal_numbers():
    print("      1", "    2", "    3", "    4", "    5", "    6", "    7", "    8")


# AFFICHE UNE LIGNE SIMPLE
def simple_dash():
    print('   -------------------------------------------------')


# AFFICHE UNE LIGNE DOUBLE
def double_dash():
    print("   =================================================")


# AFFICHE LES LIGNES SUCCESSIVES DU TABLEAU ET LEUR INDICE
def line(indice, grid):
    # Liste des lettres des lignes
    letter_list = ["A  | ", "B  | ", "C  | ", "D  | ", "E  | ", "F  | ", "G  | ", "H  | "]
    print(letter_list[indice], end=" ")

    # Affiche les éléments présents sur la ligne
    for column in range(8):
        print(grid[indice][column], " | ", end=" ")
    print("")


# ********************************************************************************************************** #
# ****** OUTILS POUR LA CREATION DES GRILLES ****** #

# Crée la grille initiale
def create_grid():
    grid = [" "] * 8
    for i in range(8):
        grid[i] = [" "] * 8
    return grid


# FONCTION DE CREATION D'UNE NOUVELLE GRILLE
def set_grid(grid, i_black, i_white):

    indices_grid_black = i_black
    indices_grid_white = i_white
    indices_grids = [indices_grid_black, indices_grid_white]

    for indice_list in indices_grids:
        for indice in range(len(indice_list)):
            if len(indice_list[0]) > 0:
                x = indice_list[indice][0]
                y = indice_list[indice][1]
                if indice_list == indices_grid_black:
                    grid[x][y] = "•"
                else:
                    grid[x][y] = "o"

    return grid


# FONCTION D'APPEL DE LA FONCTION DE CREATION DES NOUVELLES GRILLES
def set_all_grids(grid, i_b_start, i_w_start, i_b_mid, i_w_mid, i_b_end, i_w_end):
    # copy.deepcopy permet simplement de faire une copie d'une liste de liste
    grid_debut = set_grid(copy.deepcopy(grid), i_b_start, i_w_start)
    grid_mid = set_grid(copy.deepcopy(grid), i_b_mid, i_w_mid)
    grid_fin = set_grid(copy.deepcopy(grid), i_b_end, i_w_end)

    return grid_debut, grid_mid, grid_fin


# POSITIONS DES PIONS EN LISTE PAR COULEUR SOUS LE FORMAT (x, y) : X = ligne, Y = colonne
# MODIFIABLE POUR CREER DE NOUVELLES SITUATIONS
def init_all_indices():
    # Start :
    indices_grid_black_start = [(1, 0), (2, 1), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6), (2, 7)]
    indices_grid_white_start = [(5, 0), (6, 1), (5, 2), (6, 3), (5, 4), (6, 5), (5, 6), (6, 7)]
    # Mid :
    indices_grid_black_mid = [(1, 0), (1, 4), (1, 6), (2, 1), (3, 5), (4, 3), (4, 6), (5, 5)]
    indices_grid_white_mid = [(0, 2), (1, 2), (3, 3), (4, 7), (5, 2), (5, 4), (5, 6), (6, 5)]
    # End :
    indices_grid_black_end = [(1, 0), (1, 2), (2, 1), (2, 7), (3, 5), (4, 5), (5, 4), (6, 3)]
    indices_grid_white_end = [(1, 3), (3, 2), (4, 3), (4, 1), (5, 0), (5, 6), (6, 5), (6, 7)]

    return indices_grid_black_start, indices_grid_white_start, indices_grid_black_mid, indices_grid_white_mid,\
        indices_grid_black_end, indices_grid_white_end


# FONCTION MERE AFFICHAGE

def show_all_grids(init_grid):
    # Appel de fonction d'initialisation des listes d'indices des pions blancs et noirs
    # Format des variables : i = indice, b = black, w = white
    i_b_start, i_w_start, i_b_mid, i_w_mid, i_b_end, i_w_end = init_all_indices()

    # Appel de fonction d'initialisation de : grille de départ, grille du milieu, grille de fin
    start_grid, mid_grid, end_grid = set_all_grids(init_grid, i_b_start, i_w_start,
                                                         i_b_mid, i_w_mid, i_b_end, i_w_end)

    # Appel de la fonction d'affichage des 3 grilles
    print("Grille début :\n")
    print_grid(start_grid)
    time.sleep(1.5)

    print("Grille milieu :\n")
    print_grid(mid_grid)
    time.sleep(1.5)

    print("Grille fin :\n")
    print_grid(end_grid)
    time.sleep(1.5)

    return start_grid, mid_grid, end_grid


# Initialise les grilles de jeu, demande à l'utilisateur d'en choisir une et la renvoie
def init_jeu(initial_grid):
    start_grid, mid_grid, end_grid = show_all_grids(initial_grid)
    chosen_grid = grid_choice_confirmation(start_grid, mid_grid, end_grid)
    return chosen_grid


# Initialise la grille pour la partie "Tests"
def init_test(initial_grid, i_black, i_white):
    grid = set_grid(copy.deepcopy(initial_grid), i_black, i_white)
    return grid


# ********************************************************************************************************** #
# ****** OUTILS POUR LA SAISIE ET LA VERIFICATION DES SAISIES DE COORDONNEES ****** #
# Teste si les coordonnées saisies sont dans la matrice
def est_dans_grille(line, column):
    if line < 8 and line >= 0 and column < 8 and column >= 0:
        return True
    else:
        return False


# Demande à l'utilisateur de saisir une ligne jusqu'à ce qu'elle soit dans la grille
# Et convertit la lettre donnée en nombre pour la vérification dans la liste du programme
def get_line():
    list_accepted_str = ["A", "B", "C", "D", "E", "F", "G", "H", "a", "b", "c", "d", "e", "f", "g", "h"]

    while True:
        print("Saisissez la ligne (lettre) : ", end="")
        line = input()

        if list_accepted_str.count(line) != 1:
            print("Ligne saisie invalide ! Recommencez\n")
        else:
            if line == "A" or line == "a":
                line = 0
            elif line == "B" or line == "b":
                line = 1
            elif line == "C" or line == "c":
                line = 2
            elif line == "D" or line == "d":
                line = 3
            elif line == "E" or line == "e":
                line = 4
            elif line == "F" or line == "f":
                line = 5
            elif line == "G" or line == "g":
                line = 6
            elif line == "H" or line == "h":
                line = 7
            return line


# Demande à l'utilisateur de saisir une colonne jusqu'à ce qu'elle soit dans la grille
def get_column():
    # L'affichage des colonnes étant de 1 à 8, nous considérerons les coordonnées (0,0) de Python comme (A,1) de la
    #                                                                                                       grille
    list_accepted_str = ["1", "2", "3", "4", "5", "6", "7", "8"]

    while True:
        print("Saisissez la colonne (chiffre) : ", end="")
        column = input()

        if list_accepted_str.count(column) != 1:
            print("Colonne saisie invalide ! Recommencez\n")
        else:
            column = int(column)
            return column - 1


# ********************************************************************************************************** #
# ****** OUTILS POUR CHOISIR LA GRILLE DE JEU ****** #

# Demande à l'utilisateur de choisir une des trois grilles de jeu disponible
def grid_choice():
    while True:
        print("Choisissez sur quelle grille jouer :\n1 - Grille du début\n2 - Grille du milieu\n3 - Grille de fin\n\n"
              "Saisie : ", end="")
        choice_str = str(input())

        if choice_str == "1" or choice_str == "2" or choice_str == "3":
            print("\n")
            return choice_str

        else:
            print("\n\nChoix invalide, recommencez\n")


# Demande à l'utilisateur de confirmer son choix de grille
def grid_choice_confirmation(start_grid, mid_grid, end_grid):
    chosen_grid = None
    while True:
        choice_str = grid_choice()
        validation_str = ""

        if choice_str == "1":
            print("Êtes vous sûr de vouloir jouer sur cette grille ?\n\nGrille début :\n")
            time.sleep(0.75)
            chosen_grid = start_grid

        elif choice_str == "2":
            print("Êtes vous sûr de vouloir jouer sur cette grille ?\n\nGrille mid :\n")
            time.sleep(0.75)
            chosen_grid = mid_grid

        elif choice_str == "3":
            print("Êtes vous sûr de vouloir jouer sur cette grille ?\n\nGrille fin :\n")
            time.sleep(0.75)
            chosen_grid = end_grid

        else:
            print("Choix invalide, recommencez\n")

        print_grid(chosen_grid)

        while validation_str != ("1" and "2"):
            print("Confirmez :\n1 - Oui\n2 - Non\n")
            validation_str = str(input())

            if validation_str == "1":
                return chosen_grid

            elif validation_str == "2":
                print("Retour au choix des grilles...\n")
                time.sleep(1)

            else:
                print("Saisie invalide, recommencez !\n")
                time.sleep(1)


# ********************************************************************************************************** #
# ****** OUTILS POUR JOUER UNE PARTIE ****** #

# FONCTION PRINCIPALE POUR UN TOUR DE JEU
def game_turn(grid):
    pawn_x, pawn_y, chosen_team = pawn_choice(grid)
    x, y = turn(chosen_team, pawn_x, pawn_y, grid)

    if not end_game_test(x, y):
        print("\nLancement du prochain tour...\n")
        print("(À venir...)")
        time.sleep(2)
    else:
        replace_cross(chosen_team, x, y, grid), print("\n\n\n")
        print_grid(grid)
        print("L'équipe", chosen_team, "remporte la victoire !\n")
        time.sleep(2)


# Demande au joueur si il veut rejouer (si il peut)
def play_again(grid, old_x, old_y, x, y, team):
    if not end_game_test(x, y) and can_jump(grid, x, y, team, old_x, old_y):

        while True:
            print("Vous pouvez encore jouer, souhaitez vous continuer ?\n1 - Oui\n2 - Non\n")
            str_validation = str(input())

            if str_validation == "1":
                return True

            elif str_validation == "2":
                print("Fin du tour...\n")
                time.sleep(1)
                return False

            else:
                print("Saisie invalide, recommencez !\n")
                time.sleep(1)
    return False


# Remplace la croix de selection par le pion d'origine
def replace_cross(team, x, y, grid):
    if team == "blanche":
        grid[x][y] = "o"
    else:
        grid[x][y] = "•"


# Vérifie si le tour effectué signe la fin de la partie
def end_game_test(x, y):
    if (x == 7 and y == (3 or 4)) or (x == 0 and y == (3 or 4)):
        return True
    return False


# Vérifie si le pion peut jouer
def can_play(grid, x, y):
    color = pawn_color(x, y, grid)

    if can_move(grid, x, y, color) or can_jump(grid, x, y, color):
        return True

    return False


# Vérifie si le pion peut bouger orthogonalement
def can_move(grid, x, y, team):
    can = False
    move_list = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    i = 0
    while not can and i < 4:
        if move_tests(grid, x, y, move_list[i][0], move_list[i][1], team):
            can = True
        i += 1

    return can


# Vérifie si le pion peut sauter
def can_jump(grid, x, y, team, old_x=-1, old_y=-1):
    # old_x et old_y sont optionnels, ils permettent d'éviter de proposer à nouveau un tour
    # si le seul saut disponible est la case d'où provient le joueur

    # Lance une batterie de test pour vérifier s'il existe au moins un déplacement possible
    move_list = [[x+2, y], [x-2, y], [x, y+2], [x, y-2], [x+2, y+2], [x-2, y+2], [x+2, y-2], [x-2, y-2]]
    i = 0

    while i < 8:
        test_x = move_list[i][0]
        test_y = move_list[i][1]

        # Vérifie que le saut ne sort pas de la grille
        if test_x >= 0 and test_y >=0 and test_x < 8 and test_y < 8:

            # Que l'endroit souhaité est une case vide
            if grid[test_x][test_y] == " ":

                # Que le saut n'est pas une position antérieure immédiate
                if not (test_x == old_x and test_y == old_y):

                    # Que le saut s'effectue par dessus un pion allié uniquement
                    if jump(x, y, test_x, test_y, team, grid):
                        return True
        i += 1

    return False


# Vérifie si le mouvement dans son camps est possible
def move_tests(grid, x, y, new_x, new_y, team):
    if grid[new_x][new_y] == " ":

        if not forbidden_cases(new_x, new_y, team):

            if not forbidden_move(new_x, team):

                if new_x == x or new_y == y:
                    return True

    return False


# Vérifie si le déplacement est un saut et si il est possible
def jump(x, y, new_x, new_y, team, grid):

    if grid[new_x][new_y] != " " or forbidden_cases(new_x, new_y, team):
        return False

    # Teste les cases de saut orthogonales
    if (new_x == x or new_y == y) and ((abs(new_y - y) + abs(new_x - x)) == 2):
        if new_x-x == -2:
            if team == pawn_color(new_x+1, new_y, grid):
                return True
        elif new_x-x == 2:
            if team == pawn_color(new_x-1, new_y, grid):
                return True
        elif new_y-y == -2:
            if team == pawn_color(new_x, new_y+1, grid):
                return True
        elif new_y-y == 2:
            if team == pawn_color(new_x, new_y-1, grid):
                return True

    # Teste les cases de saut en diagonale
    elif (abs(new_y-y) == abs(new_x-x)) and ((abs(new_y-y)+abs(new_x-x)) == 4):
        if new_x-x == -2 and new_y-y == -2:
            if team == pawn_color(new_x+1, new_y+1, grid):
                return True
        elif new_x-x == 2 and new_y-y == -2:
            if team == pawn_color(new_x-1, new_y+1, grid):
                return True
        elif new_x-x == -2 and new_y-y == 2:
            if team == pawn_color(new_x+1, new_y-1, grid):
                return True
        elif new_x-x == 2 and new_y-y == 2:
            if team == pawn_color(new_x-1, new_y-1, grid):
                return True

    return False


# Vérifie si le déplacement s'effectue sur les buts de son propre camps
def forbidden_cases(x, y, team):
    if team == "noire" and (x == 0 and (y == 3 or y == 4)):
        return True

    elif team == "blanche" and (x == 7 and (y == 3 or y == 4)):
        return True

    return False


# Vérifie si le déplacement orthogonal s'effectue sur le camps adverse
def forbidden_move(x, team):
    if team == "noire" and x > 3:
        return True

    elif team == "blanche" and x < 4:
        return True

    return False


# Effectue un tour en saisissant les coordonnées et vérifie si le mouvement est correct
def turn(team, x, y, grid):
    print_grid(grid)
    print("Equipe", team, "...\n")
    print("À vous de jouer\n\n")
    time.sleep(0.5)
    only_jump = False  # Si le joueur a déjà joué un saut, empêche de jouer autre chose qu'un saut

    while True:
        print("Entrez des coordonnées pour déplacer votre pion :\n")
        if only_jump:
            print("Vous pouvez annuler le mouvement en vous déplaçant sur la case actuelle\n")

        new_x = get_line()
        new_y = get_column()
        print("\n")

        if x == new_x and y == new_y:
            print("Vous ne vous êtes pas déplacé...\n")
            # Si le joueur s'est déjà déplacé par saut, permet d'annuler la prise d'un nouveau coup
            if only_jump:
                if give_up_move():
                    return new_x, new_y

        # Si le joueur peut et veut se déplacer orthogonalement...
        elif move_tests(grid, x, y, new_x, new_y, team) and not only_jump:
            grid[new_x][new_y] = "X"
            grid[x][y] = " "
            return new_x, new_y

        # Si le joueur peut et veut sauter...
        elif jump(x, y, new_x, new_y, team, grid):
            grid[new_x][new_y] = "X"
            grid[x][y] = " "
            print_grid(grid)

            # Si le joueur peut et veut jouer à nouveau...
            if not play_again(grid, x, y, new_x, new_y, team):
                return new_x, new_y

            else:
                only_jump = True
                x = new_x
                y = new_y

        else:
            print("Mouvement impossible, recommencez\n\n")


# Permet au joueur d'abandonner un déplacement s'il a saisit la poursuite de son tour par erreur
def give_up_move():
    print("\nSouhaitez vous abandonner le déplacement ?\n1 - Oui\n2 - Non\n")
    str_validation = str(input())

    if str_validation == "1":
        print("Abandon de la saisie du déplacement...\n")
        time.sleep(1)
        return True

    elif str_validation == "2":
        print("Retour à la saisie du déplacement...\n")
        time.sleep(1)
        return False

    else:
        print("Saisie invalide, recommencez !\n")
        time.sleep(0.5)


# Attribue la couleur de l'équipe du pion que le joueur a choisi
def pawn_color(x, y, grid):
    if grid[x][y] == "•":
        color = "noire"
    elif grid[x][y] == "o":
        color = "blanche"
    else:
        color = ""

    time.sleep(0.5)
    return color


# Permet au joueur de changer de pion
def pawn_choice_confirmation(x, y, grid):
    copy_grid_value = grid[x][y]  # utile si le joueur change de choix de selection de pion
    color = pawn_color(x, y, grid)
    grid[x][y] = "X"

    time.sleep(0.5)
    print("\n\n")
    print_grid(grid)
    while True:
        print("Vous avez sélectionné le pion marqué d'une croix, c'est un pion de l'équipe", color)
        print("\nSouhaitez vous jouer ce pion ?\n1 - Oui\n2 - Non")
        validation_str = str(input())

        if validation_str == "1":
            print("\n\nVous jouez maintenant l'équipe", color, "!\n\n")
            time.sleep(1)
            return color

        elif validation_str == "2":
            print("Retour à la sélection du pion...\n")
            grid[x][y] = copy_grid_value
            time.sleep(1)

            print("\n\n")
            print_grid(grid)
            return " "

        else:
            print("Saisie invalide, recommencez !\n")
            time.sleep(1)


# Fonction de choix du pion à jouer
def pawn_choice(grid):
    while True:
        print("Donnez les coordonnées du pion que vous souhaitez jouer :\n")
        pawn_x = get_line()
        pawn_y = get_column()

        if not est_dans_grille(pawn_x, pawn_y):
            print("Coordonnées saisies invalides, recommencez.\n")

        elif grid[pawn_x][pawn_y] == " ":
            print("Vous n'avez pas choisi un pion... Recommencez.\n")

        elif not can_play(grid, pawn_x, pawn_y):
            print("Ce pion ne peut pas se déplacer... Choisissez-en un autre\n")

        else:
            color = pawn_choice_confirmation(pawn_x, pawn_y, grid)
            if color != " ":
                return pawn_x, pawn_y, color


# FONCTION PRINCIPALE POUR UNE PARTIE
def game():
    initial_grid = create_grid()  # Creation de la grille initiale
    grille_jeu = init_jeu(initial_grid)  # Propose au joueur de choisir une des 3 grilles pour commencer à jouer
    game_turn(grille_jeu)  # Lance un tour de jeu


# ********************************************************************************************************** #
# ****** OUTILS DU MENU PRINCIPAL ET AFFICHAGE DES MENUS ****** #

# FONCTION PRINCIPALE MENU
def game_menu():
    while True:
        print_menu()
        while True:
            print("Saisie : ", end="")
            choice = str(input())

            if choice == "1":
                launch_game_menu()
                break

            elif choice == "2":
                tests_menu()
                break

            elif choice == "3":
                print_doc()
                time.sleep(5)
                break

            elif choice == "4":
                return False


# Menu "jeu"
def launch_game_menu():
    while True:
        print_game_menu()
        while True:
            print("Saisie : ", end="")
            choice = str(input())

            if choice == "1":
                game()
                return 0

            elif choice == "2":
                break

            elif choice == "3":
                break

            elif choice == "4":
                print_rules()
                time.sleep(5)
                break

            elif choice == "5":
                return False


# Affcihe le menu du jeu
def print_menu():
    print(
        '''
               __   __         ___       ______      ___      ______       ___         __   __   
              /  \_/  \       / _ \     /  ____|    / _ \    |   _  \     / _ \       /  \_/  \ 
             / __   __ \     / |_| \   |  /        / |_| \   |  | |  \   / |_| \     / __   __ \  
            / /  \_/  \ \   / /___\ \  |  \____   / /___\ \  |  |_|  /  / /___\ \   / /  \_/  \ \ 
           /_/         \_\ /_/     \_\  \______| /_/     \_\ |______/  /_/     \_\ /_/         \_\ 
        
        _____________________________________________________________________________________________
        
        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        
                                                Bienvenue !
                                            -------------------
                                                
                                            Choisissez un mode :
                                            
                                                1 - Jeu
                                                2 - Tests
                                                
                                                3 - Documentation
                                                4 - Quitter le jeu
                                                
        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Affiche le menu "jeu"
def print_game_menu():
    print(
        '''  

        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Menu de jeu 
                                        ---------------------------------

                                            Que souhaitez vous faire ?

                                            1 - Lancer un tour de jeu
                                            2 - Partie J vs J (bientôt...)
                                            3 - Partie J vs IA (bientôt...)
                                            4 - Règles du jeu
                                            5 - Retour au menu principal

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Affiche le menu des Tests
def print_test_menu():
    print(
        '''  

        _____________________________________________________________________________________________
        
        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Menu des Tests 
                                        ---------------------------------

                                            Choisissez un sous-menu :
                                            
                                            1 - Lancer tous les tests
                                            2 - Déplacement orthogonal
                                            3 - Déplacement par saut
                                            4 - Créer son propre test
                                            5 - Retour au menu principal

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Affiche le menu des tests orthogonaux
def print_test_move_menu():
    print(
        '''  

        _____________________________________________________________________________________________
        
        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                Tests orthogonaux
                                            ------------------------- 

                                        Choisissez une batterie de tests :
                                        
                                            1 - Avec visuel (long)
                                            2 - Sans visuel
                                            3 - Retour au Menu des Tests

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Affiche le menu de "lancer tous les tests"
def print_test_all_menu():
    print(
        '''  

        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Tous les tests
                                            ------------------------- 

                                        Choisissez une batterie de tests :
                                        
                                            1 - Avec visuel (long)
                                            2 - Sans visuel
                                            3 - Retour au Menu des Tests

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Affiche le menu des tests des sauts
def print_test_jump_menu():
    print(
        '''  

        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                Tests des sauts
                                            ------------------------- 

                                        Choisissez une batterie de tests :
                                        
                                            1 - Avec visuel (long)
                                            2 - Sans visuel
                                            3 - Retour au Menu des Tests

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Affiche le menu de création personnalisée de tests
def print_test_create_menu():
    print(
        '''  

        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                Création de tests
                                            ------------------------- 
                                            
                                Envie de jouer un tour sur une grille personnalisée ?
                                            
                                            1 - Créer un test
                                            2 - Retour au Menu des Tests

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


def print_rules():
    print(
        '''  

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                Règles du jeu
                                            ------------------------- 

                                            Disponibles à l'adresse :

        https://moodle.univ-tlse3.fr/pluginfile.php/376187/mod_resource/content/4/reglesDemeterRev1.pdf

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

        '''
    )


def print_doc():
    print(
        '''  

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Documentation
                                            ------------------------- 

                                            Disponibles à l'adresse :

                                           https://pastebin.com/Cx7MQR0f

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

        '''
    )


# ********************************************************************************************************** #
# ****** OUTILS POUR LES MENUS DE TESTS ****** #

# FONCTION PRINCIPALE MENUS DE TESTS
def tests_menu():
    initial_grid = create_grid()
    while True:
        print_test_menu()

        while True:
            print("\nChoisissez un test à effectuer : ")
            str_choice = str(input())

            if str_choice == "1":  # Lancer tous les tests
                test_all_menu(initial_grid)
                break

            elif str_choice == "2":  # Déplacement orthogonal
                test_move_menu(initial_grid)
                break

            elif str_choice == "3":  # Déplacement par saut
                test_jump_menu(initial_grid)
                break

            elif str_choice == "4":  # Créer son propre test
                test_create_menu(initial_grid)
                break

            elif str_choice == "5":  # Retour au menu de jeu
                return 0


# Menu de "lancer tous les tests"
def test_all_menu(grid):
    while True:
        print_test_all_menu()

        while True:
            print("\nSaisie : ")
            str_choice = str(input())

            if str_choice == "1":  # Avec visuel
                launch_all_tests(grid, True)
                return 0

            elif str_choice == "2":  # Sans visuel
                launch_all_tests(grid)
                return 0

            elif str_choice == "3":  # Retour au menu des tests
                return 0


# Menu de création personnalisée de tests
def test_create_menu(initial_grid):
    while True:
        print_test_create_menu()

        while True:
            print("\nSaisie : ")
            str_choice = str(input())

            if str_choice == "1":  # Avec visuel
                launch_test_create(initial_grid)
                print("Retour au menu précédent...")
                time.sleep(2)
                return 0

            elif str_choice == "2":  # Retour au menu des tests
                return 0


# Menu des tests orthogonaux
def test_move_menu(grid):
    while True:
        print_test_move_menu()

        while True:
            print("\nSaisie : ")
            str_choice = str(input())

            if str_choice == "1":  # Avec visuel
                launch_test_move(grid, True)
                print("Retour au menu précédent...")
                time.sleep(2)
                return 0

            elif str_choice == "2":  # Sans visuel
                launch_test_move(grid)
                return 0

            elif str_choice == "3":  # Retour au menu des tests
                return 0


# Menu des tests diagonaux
def test_jump_menu(grid):
    while True:
        print_test_jump_menu()

        while True:
            print("\nSaisie : ")
            str_choice = str(input())

            if str_choice == "1":  # Avec visuel
                launch_test_jump(grid, True)
                print("Retour au menu précédent...")
                time.sleep(2)
                return 0

            elif str_choice == "2":  # Sans visuel
                launch_test_jump(grid)
                return 0

            elif str_choice == "3":  # Retour au menu des tests
                return 0


# Affiche des informations quand aux informations visuelles présentes dans les tests
def visual_info():
    print(
        '''
                                    *******************
                                    *** Information ***

        ***     Le signe "*" marque l'ancienne position du pion                 ***
        ***     S'il n'est pas visible, aucun déplacement n'a été effectué      ***

                                    *******************
        ''')


# Affiche les informations relatives à la création personnalisée de tests
def test_create_info():
    print(
        '''
                                    *******************
                                    *** Information ***

        ***     La création de grille nécessite une entière coopération de      ***
        ***     l'utilisateur, si vous saisissez de manière incorrecte les      ***
        ***     listes d'indices, le programme s'arrêtera à cause d'une erreur  ***
        ***                                                                     ***
        ***     Il est beaucoup plus aisé pour vous de n'avoir à saisir que     ***
        ***     deux listes de tuples plutôt que de passer par des              ***
        ***     vérifications qui rendraient l'utilisation de                   ***
        ***     cette fonctionnalité fastidieuse                                ***
        ***                                                                     ***
        ***     Voici le format à respecter :                                   ***
        ***     [(x, y), (x, y), (x, y), ... , (x, y)]                          ***
        ***                                                                     ***
        ***     Exemple :                                                       ***
        ***     [(1, 0), (2, 1), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6)]        ***
        ***                                                                     ***
        ***     Note :                                                          ***
        ***     - La case "A1" se note (0, 0) et "H8" se note (7,7)             ***
        ***     - Si vous saisissez deux fois la même coordonnée, le premier    ***
        ***         pion sera écrasé                                            ***

                                    *******************
        ''')

# ********************************************************************************************************** #
# ****** OUTILS POUR LES TESTS ****** #

    # Format des test :
    # (grille, indice_pions_noirs, indice_pions_blancs, deplacement_x, deplacement_y, nom_test, visual, [optionnel])
    # Le statut [optionnel] indique si le test doit réussir les assert ou non (pour détecter les mouvements impossible)
    # Le pion testé est toujours le premier pion de la liste noire

    # Chaque test effectué passe par une assertion
    # La notion "visual" permet de savoir si l'on va afficher ou non le visuel d'un test


# Lance tous les tests
def launch_all_tests(grid, visual=False):
    launch_test_move(grid, visual)
    launch_test_jump(grid, visual)

    print("\n\n\n\n*** Tous les tests ont été validés ***\n")
    print("Retour au Menu des Tests...\n\n\n\n")
    time.sleep(2)

    return False


# Fonction de tests des mouvements diagonauc
def launch_test_jump(grid, visual=False):
    print("\n****** TESTS DEPLACEMENTS PAR SAUT ******\n\n")
    time.sleep(2)

    if visual:
        visual_info()
        time.sleep(5)

    # ## Tests valides
    # Test 1
    print("--- Test 1 : saut valide par dessus un allié à domicile (diagonale), C5 à A3 ---")
    if test_jump(grid, [(2, 4), (1, 3)], [()], 0, 2, "Test 1", visual):
        print("*** Test 1 : OK\n\n")

        # Test 2
        print("--- Test 2 : saut valide par dessus un allié à domicile (orthogonal), C5 à C3 ---")
        if test_jump(grid, [(2, 4), (2, 3)], [()], 2, 2, "Test 2", visual):
            print("*** Test 2 : OK\n\n")

            # Test 3
            print("--- Test 3 : saut valide par dessus un allié sur territoire adverse, E5 à E3 ---")
            if test_jump(grid, [(4, 4), (4, 3)], [()], 4, 2, "Test 3", visual):
                print("*** Test 3 : OK\n\n")

                # Test 4
                print("--- Test 4 : saut valide par dessus un allié changement de camps, D5 à F5 ---")
                if test_jump(grid, [(3, 4), (4, 4)], [()], 5, 4, "Test 4", visual):
                    print("*** Test 4 : OK\n\n")

                    # Test 5
                    print("--- Test 5 : saut valide goals adverse, H2 à H4 ---")
                    if test_jump(grid, [(7, 1), (7, 2)], [()], 7, 3, "Test 5", visual):
                        print("*** Test 5 : OK\n\n")

    # ## Tests invalides
    # Test 5
    print("--- Test 6 : saut invalide par dessus un ennemi, C5 à C3 ---")
    if test_jump(grid, [(2, 4)], [(2, 3)], 2, 2, "Test 6", visual, False):
        print("*** Test 6 : OK\n\n")
        # Test 6
        print("--- Test 7 : saut invalide sur un pion, C5 à C3 ---")
        if test_jump(grid, [(2, 4), (2, 3)], [(2, 2)], 2, 2, "Test 7", visual, False):
            print("*** Test 7 : OK\n\n")
            # Test 7
            print("--- Test 8 : saut invalide goals propre camps, A2 à A5 ---")
            if test_jump(grid, [(0, 1), (0, 2)], [()], 0, 3, "Test 8", visual, False):
                print("*** Test 8 : OK\n\n")
                # Test 8
                print("--- Test 9 : saut invalide sortie de plateau, B2 à ?? ---")
                if test_jump(grid, [(1, 1), (0, 0)], [()], -1, -1, "Test 9", visual, False):
                    print("*** Test 9 : OK\n\n")

    time.sleep(2)
    print("\n*** Tests des sauts terminés... ***\n\n")
    time.sleep(2)


# Fonction de tests des mouvements orthogonaux
def launch_test_move(grid, visual=False):
    print("\n****** TESTS DEPLACEMENTS ORTHOGONAUX ******\n\n")
    time.sleep(2)

    if visual:
        visual_info()
        time.sleep(5)

    # ## Tests valides
    # Test 1
    print("--- Test 1 : déplacement valide d'une case en x, C5 à C6 ---")
    if test_move(grid, [(2, 4)], [()], 2, 5, "Test 1", visual):
        print("*** Test 1 : OK\n\n")

        # Test 2
        print("--- Test 2 : déplacement valide d'une case en y, C5 à D5 / B1 à A1 / B8 à A8 ---")
        if test_move(grid, [(2, 4)], [()], 3, 4, "Test 2.1", visual)\
                and test_move(grid, [(1, 0)], [()], 0, 0, "Test 2.2", visual)\
                and test_move(grid, [(1, 7)], [()], 0, 7, "Test 2.3", visual):
            print("*** Test 2 : OK\n\n")

            # Test 3
            print("--- Test 3 : déplacement valide de plusieurs cases en x, C5 à C1 ---")
            if test_move(grid, [(2, 4)], [()], 2, 0, "Test 3", visual):
                print("*** Test 3 : OK\n\n")

                # Test 4
                print("--- Test 4 : déplacement valide de plusieurs cases en y, C6 à A6 ---")
                if test_move(grid, [(2, 5)], [()], 0, 5, "Test 4", visual):
                    print("*** Test 4 : OK\n\n")

    # ## Test invalides (avec l'option "test_status" en False)
    # Test 5
    print("--- Test 5 : déplacement invalide sur une case avec un pion ennemi, C5 à C6 ---")
    if test_move(grid, [(2, 4)], [(2, 5)], 2, 5, "Test 5", visual, False):
        print("*** Test 5 : OK\n\n")

        # Test 6
        print("--- Test 6 : déplacement invalide sur une case avec un pion allié, C5 à C6 ---")
        if test_move(grid, [(2, 4), (2, 5)], [()], 2, 5, "Test 6", visual, False):
            print("*** Test 6 : OK\n\n")

            # Test 7
            print("--- Test 7 : déplacement invalide sur territoire adverse, C5 à E5 ---")
            if test_move(grid, [(2, 4)], [()], 4, 5, "Test 7", visual, False):
                print("*** Test 7 : OK\n\n")

                # Test 8
                print("--- Test 8 : déplacement invalide sur ses propres goals, C5 à A5 ---")
                if test_move(grid, [(2, 4)], [()], 0, 4, "Test 8", visual, False):
                    print("*** Test 8 : OK\n\n")

                    # Test 9
                    print("--- Test 9 : déplacement invalide diagonal, C5 à A5 ---")
                    if test_move(grid, [(2, 4)], [()], 3, 2, "Test 9", visual, False):
                        print("*** Test 9 : OK\n\n")

                        # Test 10
                        print("--- Test 10 : déplacement invalide sortie de plateau, C5 à C? ---")
                        if test_move(grid, [(2, 4)], [()], 2, -1, "Test 10", visual, False):
                            print("*** Test 10 : OK\n\n")

    time.sleep(2)
    print("\n*** Tests orthogonaux terminés... ***\n\n")
    time.sleep(2)


# Test mouvement orthogonal
def test_move(grid, i_black, i_white, x_move, y_move, test_name, visual, test_status=True):
    x_pos = i_black[0][0]
    y_pos = i_black[0][1]

    test_grid = init_test(copy.deepcopy(grid), i_black, i_white)  # Initialise la grille de test

    if visual:
        time.sleep(2)
        print("\nSituation initiale :\n\n")
        print_grid(test_grid)
        time.sleep(3)

    if test_status:
        assert (move_tests(test_grid, x_pos, y_pos, x_move, y_move, "noire")
                and (can_move(test_grid, x_pos, y_pos, "noire"))
                and est_dans_grille(x_move, y_move)),\
            "!!! Erreur !!! Test orthogonal valide échoué : " + test_name
    else:
        assert not (move_tests(test_grid, x_pos, y_pos, x_move, y_move, "noire")
                    and (can_move(test_grid, x_pos, y_pos, "noire"))
                    and est_dans_grille(x_move, y_move)),\
            "!!! Erreur !!! Test orthogonal invalide échoué : " + test_name

    if visual:
        print("\nDéplacement du pion 'X'\n\n")
        time.sleep(1.5)
        test_grid[x_pos][y_pos] = "X"  # Remplace le pion par une croix
        print_grid(test_grid)
        time.sleep(2)
        print("\nSituation post déplacement (si effectué)\n\n")

        # Si le déplacement s'effecute...
        if test_status:
            # Change la position du pion
            test_grid[x_pos][y_pos] = "*"
            test_grid[x_move][y_move] = "X"

        print_grid(test_grid)
        time.sleep(4)

    return True


# Test saut
def test_jump(grid, i_black, i_white, x_move, y_move, test_name, visual, test_status=True):
    x_pos = i_black[0][0]
    y_pos = i_black[0][1]

    test_grid = init_test(copy.deepcopy(grid), i_black, i_white)  # Initialise la grille de test

    if visual:
        time.sleep(2)
        print("\nSituation initiale :\n\n")
        print_grid(test_grid)
        time.sleep(3)

    if test_status:
        assert (jump(x_pos, y_pos, x_move, y_move, "noire", test_grid)
            and est_dans_grille(x_move, y_move)),\
            "!!! Erreur !!! Test saut valide échoué : " + test_name
    else:
        assert not (jump(x_pos, y_pos, x_move, y_move, "noire", test_grid)
            and est_dans_grille(x_move, y_move)),\
            "!!! Erreur !!! Test saut invalide échoué : " + test_name

    if visual:
        print("\nDéplacement du pion 'X'\n\n")
        time.sleep(1.5)
        test_grid[x_pos][y_pos] = "X"  # Remplace le pion par une croix
        print_grid(test_grid)
        time.sleep(2)
        print("\nSituation post déplacement (si effectué)\n\n")

        # Si le déplacement s'effecute...
        if test_status:
            # Change la position du pion
            test_grid[x_pos][y_pos] = "*"
            test_grid[x_move][y_move] = "X"

        print_grid(test_grid)
        time.sleep(4)

    return True


# ********************************************************************************************************** #
# ****** OUTILS POUR LE TEST PERSONNALISÉ ****** #

# Fonction principale de création de tests personnalisés
def launch_test_create(grid):
    test_create_info()
    time.sleep(5)

    i_black = eval(input("Saisissez la liste des pions noirs : "))
    i_white = eval(input("Saisissez la liste des pions blancs : "))
    print("\n\n")

    test_grid = init_test(copy.deepcopy(grid), i_black, i_white)  # Initialise la grille de test

    print_grid(test_grid)
    game_turn(test_grid)  # Lance un tour de jeu


# PROGRAMME PRINCIPAL :
status = True
while status:
    status = game_menu()
