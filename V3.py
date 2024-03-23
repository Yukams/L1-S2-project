# coding utf8
import copy
import time
import random


# ================================================================================
# OUTILS POUR LA SAISIE ET L'AFFICHAGE DES GRILLES

# Crée une liste vide
def create_grid():
    grid = ["   "] * 8
    for i in range(8):
        grid[i] = ["   "] * 8
    # Les buts de chaque equipe
    grid[0][3] = grid[0][4] = grid[7][3] = grid[7][4] = "▓▓▓"
    return grid


# Permet de saisir les coordonnées des pions des grilles début/milieu/fin
def set_grid_start():
    black_coordinates = [(5, 0), (6, 1), (5, 2), (6, 3), (5, 4), (6, 5), (5, 6), (6, 7)]
    white_coordinates = [(1, 0), (2, 1), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6), (2, 7)]
    return [black_coordinates, white_coordinates]


def set_grid_mid():
    black_coordinates = [(0, 2), (1, 2), (3, 3), (4, 7), (5, 2), (5, 4), (5, 6), (6, 5)]
    white_coordinates = [(1, 0), (1, 4), (1, 6), (2, 1), (3, 5), (4, 3), (4, 6), (5, 5)]
    return [black_coordinates, white_coordinates]


def set_grid_end():
    black_coordinates = [(1, 3), (3, 2), (4, 3), (4, 1), (5, 0), (5, 6), (6, 5), (6, 7)]
    white_coordinates = [(1, 0), (1, 2), (2, 1), (2, 7), (3, 5), (4, 5), (5, 4), (6, 3)]
    return [black_coordinates, white_coordinates]


# Construit la grille avec les indices
def build_grid(grid, coordinates):
    for indices_list in coordinates[0]:
        if len(indices_list) > 0:
            x = indices_list[0]
            y = indices_list[1]
            grid[x][y] = " ○ "
    for indices_list in coordinates[1]:
        if len(indices_list) > 0:
            x = indices_list[0]
            y = indices_list[1]
            grid[x][y] = " ♦ "

    return grid


# Affichage d'une grille
def print_grid(grid):
    print('''
     1     2     3     4     5     6     7     8
  ╔═════╤═════╤═════╦═════╦═════╦═════╤═════╤═════╗
''', end="")
    line(0, grid)
    print("  ╟─────┼─────┼─────╚═───═╩═───═╝─────┼─────┼─────╢")
    for indice in range(5):
        line(indice+1, grid)
        if indice == 2:
            print("  ╟═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╢")
        else:
            print("  ╟─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────╢")
    line(6, grid)
    print("  ╟─────┼─────┼─────╔═───═╦═───═╗─────┼─────┼─────╢")
    line(7, grid)
    print("  ╚═════╧═════╧═════╩═════╩═════╩═════╧═════╧═════╝")


# Affiche les lignes successives du tableau
def line(indice, grid):
    # Liste des lettres des lignes
    letter_list = ["A ║", "B ║", "C ║", "D ║", "E ║", "F ║", "G ║", "H ║"]
    print(letter_list[indice], end=" ")

    # Affiche les éléments présents sur la ligne
    for column in range(7):
        print(grid[indice][column], "| ", end="")
    print(grid[indice][7], "║ ", end="")
    print('')


# Montre les trois grilles à l'écran
def print_all_grid():
    grid = create_grid()

    print("Grille du début :\n\n")
    print_grid(build_grid(copy.deepcopy(grid), set_grid_start()))
    print("\n\nGrille du milieu :\n\n")
    print_grid(build_grid(copy.deepcopy(grid), set_grid_mid()))
    print("\n\nGrille de fin :\n\n")
    print_grid(build_grid(copy.deepcopy(grid), set_grid_end()))


# ================================================================================
# OUTILS POUR LA SAISIE ET LA VERIFICATION DES COORDONNEES

# Vérifie si la ligne entrée est correcte, puis renvoie son indice
def check_line(line):
    accepted_line = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for i in range(len(accepted_line)):

        if accepted_line[i] == line:
            return i

    return -1


# Vérifie si la colonne entrée est correcte, puis renvoie son indice
def check_column(column):
    accepted_column = ["1", "2", "3", "4", "5", "6", "7", "8"]

    for i in range(len(accepted_column)):

        if accepted_column[i] == column:
            return i

    return -1


# Demande la saisie de coordonnées jusqu'à ce qu'elles soient correctes
def enter_coordinates():
    while True:
        user_input = str(input("Saisissez une coordonnée (ex : B1): ")).upper()
        user_input = [user_input[i:i+1] for i in range(0, len(user_input), 1)]  # Splits in two separated string

        if len(user_input) == 2:  # Si la saisie utilisateur fait deux caractères
            line = check_line(user_input[0])

            if line != -1:
                column = check_column(user_input[1])

                if column != -1:
                    return line, column

        print("\n/!/ Saisie incorrecte /!/\n")


# ================================================================================
# OUTILS DE TESTS

# FONCTION PRINCIPALE DE TEST : Lance tous les tests
def launch_all_tests():
    test_check_line()
    test_check_column()

    # Après ces fonctions, on ne vérifie plus les cas où l'on sélectionne une case hors du plateau car impossible

    grid = create_grid()
    grid_start = build_grid(copy.deepcopy(grid), set_grid_start())

    test_is_a_pawn(grid_start)
    test_is_same_team(grid_start)
    test_is_home()
    test_is_own_goal()
    test_is_different()

    test_is_orthogonal(grid_start)
    test_is_diagonal_jump(grid_start)
    test_is_orthogonal_jump(grid_start)
    test_is_jump()
    test_is_able_to_play()
    test_is_the_end()
    test_is_on_grid()

    test_ia_choose_team()
    test_ia_find_pawn(grid_start)
    test_ia_test_move(grid_start)
    test_ia_movepool(grid)

    print("\n*** Tous les tests ont été effectués avec succès ***\n")
    time.sleep(2)


# Lance les vérifications pour la fonction check_line
def test_check_line():
    assert check_line("A") == 0, "ERROR : check_line (1) process failed"
    assert check_line("H") == 7, "ERROR : check_line (2) process failed"
    assert check_line("1") == -1, "ERROR : check_line (3) process failed"
    assert check_line("J") == -1, "ERROR : check_line (4) process failed"
    assert check_line("zzz") == -1, "ERROR : check_line (5) process failed"
    print("test_check_line : OK")


# Lance les vérifications pour la fonction check_column
def test_check_column():
    assert check_column("A") == -1, "ERROR : check_column (1) process failed"
    assert check_column("1") == 0, "ERROR : check_column (2) process failed"
    assert check_column("5") == 4, "ERROR : check_column (3) process failed"
    assert check_column("9") == -1, "ERROR : check_column (4) process failed"
    assert check_column("uuz") == -1, "ERROR : check_column (5) process failed"
    print("test_check_column : OK")


def test_is_a_pawn(grid):
    assert not is_a_pawn(check_line("A"), check_column("3"), grid), "ERROR : is_a_pawn (1) process failed"
    assert is_a_pawn(check_line("B"), check_column("1"), grid), "ERROR : is_a_pawn (2) process failed"
    assert not is_a_pawn(check_line("A"), check_column("4"), grid), "ERROR : is_a_pawn (3) process failed"
    assert not is_a_pawn(check_line("H"), check_column("8"), grid), "ERROR : is_a_pawn (4) process failed"
    print("test_is_a_pawn : OK")


def test_is_same_team(grid):
    assert not is_same_team(check_line("A"), check_column("1"), "blanche", grid), \
        "ERROR : is_same_team (1) process failed"
    assert not is_same_team(check_line("A"), check_column("1"), "noire", grid), \
        "ERROR : is_same_team (2) process failed"
    assert is_same_team(check_line("B"), check_column("1"), "blanche", grid), \
        "ERROR : is_same_team (3) process failed"
    assert not is_same_team(check_line("B"), check_column("1"), "noire", grid), \
        "ERROR : is_same_team (4) process failed"
    assert not is_same_team(check_line("A"), check_column("4"), "blanche", grid), \
        "ERROR : is_same_team (5) process failed"
    assert not is_same_team(check_line("B"), check_column("5"), "", grid), \
        "ERROR : is_same_team (6) process failed"
    assert is_same_team(check_line("F"), check_column("1"), "noire", grid), \
        "ERROR : is_same_team (7) process failed"
    print("test_is_same_team : OK")


def test_is_home():
    assert is_home(check_line("A"), "blanche"), "ERROR : is_home (1) process failed"
    assert not is_home(check_line("E"), "blanche"), "ERROR : is_home (2) process failed"
    assert is_home(check_line("E"), "noire"), "ERROR : is_home (3) process failed"
    assert not is_home(check_line("A"), "noire"), "ERROR : is_home (4) process failed"
    print("test_is_home : OK")


def test_is_own_goal():
    assert is_own_goal(check_line("A"), check_column("4"), "blanche"), "ERRROR : is_own_goal (1) process failed"
    assert is_own_goal(check_line("A"), check_column("5"), "blanche"), "ERRROR : is_own_goal (2) process failed"
    assert is_own_goal(check_line("H"), check_column("4"), "noire"), "ERRROR : is_own_goal (3) process failed"
    assert is_own_goal(check_line("H"), check_column("5"), "noire"), "ERRROR : is_own_goal (4) process failed"
    assert not is_own_goal(check_line("H"), check_column("4"), ""), "ERRROR : is_own_goal (5) process failed"
    assert not is_own_goal(check_line("A"), check_column("4"), "noire"), "ERRROR : is_own_goal (6) process failed"
    print("test_is_own_goal : OK")


def test_is_different():
    assert not is_different(check_line("A"), check_column("4"), check_line("A"), check_column("4")), \
        "ERRROR : is_different (1) process failed"
    assert is_different(check_line("A"), check_column("4"), check_line("B"), check_column("4")), \
        "ERRROR : is_different (2) process failed"
    assert is_different(check_line("A"), check_column("4"), check_line("A"), check_column("5")), \
        "ERRROR : is_different (3) process failed"
    print("test_is_different : OK")


def test_is_orthogonal(grid):
    assert is_orthogonal(check_line("B"), check_column("1"), check_line("A"), check_column("1"), grid, "blanche"), \
        "ERRROR : is_orthogonal (1) process failed"
    assert not is_orthogonal(check_line("C"), check_column("4"), check_line("D"), check_column("5"), grid, "blanche"), \
        "ERRROR : is_orthogonal (2) process failed"
    assert is_orthogonal(check_line("B"), check_column("1"), check_line("B"), check_column("2"), grid, "blanche"), \
        "ERRROR : is_orthogonal (3) process failed"
    assert not is_orthogonal(check_line("B"), check_column("1"), check_line("B"), check_column("4"), grid, "blanche"), \
        "ERRROR : is_orthogonal (4) process failed"
    assert not is_orthogonal(check_line("B"), check_column("1"), check_line("E"), check_column("1"), grid, "blanche"), \
        "ERRROR : is_orthogonal (5) process failed"
    print("test_is_orthogonal : OK")


def test_is_diagonal_jump(grid):
    assert is_diagonal_jump(check_line("B"), check_column("1"), check_line("D"), check_column("3"),
                            "blanche", grid), "ERROR : is_diagonal_jump (1) process failed"
    assert is_diagonal_jump(check_line("F"), check_column("1"), check_line("H"), check_column("3"),
                            "noire", grid), "ERROR : is_diagonal_jump (2) process failed"
    assert not is_diagonal_jump(check_line("B"), check_column("1"), check_line("C"), check_column("1"),
                            "blanche", grid), "ERROR : is_diagonal_jump (3) process failed"
    assert not is_diagonal_jump(check_line("C"), check_column("2"), check_line("E"), check_column("2"),
                            "blanche", grid), "ERROR : is_diagonal_jump (4) process failed"

    grid = build_grid(copy.deepcopy(grid), set_grid_mid())

    assert not is_diagonal_jump(check_line("E"), check_column("4"), check_line("G"), check_column("2"),
                                "blanche", grid), "ERROR : is_diagonal_jump (5) process failed"
    assert not is_diagonal_jump(check_line("G"), check_column("6"), check_line("E"), check_column("7"),
                                "noire", grid), "ERROR : is_diagonal_jump (5) process failed"
    print("test_is_diagonal_jump : OK")


def test_is_orthogonal_jump(grid):
    grid = build_grid(copy.deepcopy(grid), set_grid_mid())

    assert is_orthogonal_jump(check_line("A"), check_column("3"), check_line("C"), check_column("3"), "noire",
                              grid), "ERROR : is_orthogonal_jump (1) process failed"
    assert not is_orthogonal_jump(check_line("D"), check_column("4"), check_line("F"), check_column("4"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (2) process failed"
    assert not is_orthogonal_jump(check_line("E"), check_column("8"), check_line("E"), check_column("6"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (3) process failed"
    assert not is_orthogonal_jump(check_line("F"), check_column("7"), check_line("F"), check_column("5"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (4) process failed"
    assert not is_orthogonal_jump(check_line("D"), check_column("4"), check_line("F"), check_column("4"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (5) process failed"
    assert not is_orthogonal_jump(check_line("F"), check_column("3"), check_line("D"), check_column("5"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (6) process failed"
    assert not is_orthogonal_jump(check_line("D"), check_column("4"), check_line("F"), check_column("4"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (7) process failed"
    assert not is_orthogonal_jump(check_line("B"), check_column("3"), check_line("C"), check_column("4"), "noire",
                                  grid), "ERROR : is_orthogonal_jump (2) process failed"
    print("test_is_orthogonal_jump : OK")


def test_is_jump():
    # Utilise orthogonal_jump et diagonal_jump
    print("test_is_jump : OK")


def test_is_able_to_play():
    grid_test = create_grid()
    grid = build_grid(copy.deepcopy(grid_test), [[], [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (3, 1), (3, 2), (3, 4),
                                                  (3, 5)]])

    assert not is_able_to_play(check_line("D"),check_column("4"), "blanche", grid), \
        "ERROR : is_able_to_play (1) process failed"

    grid = build_grid(copy.deepcopy(grid_test), [[], [(1, 3), (3, 3), (4, 3), (5, 3), (3, 1), (3, 2), (3, 4), (3, 5)]])

    assert is_able_to_play(check_line("D"), check_column("4"), "blanche", grid), \
        "ERROR : is_able_to_play (2) process failed"

    grid = build_grid(copy.deepcopy(grid_test), [[], [(1, 3), (2, 3), (3, 3), (5, 3), (3, 1), (3, 2), (3, 4), (3, 5)]])

    assert not is_able_to_play(check_line("D"), check_column("4"), "blanche", grid), \
        "ERROR : is_able_to_play (3) process failed"

    grid = build_grid(copy.deepcopy(grid_test), [[], [(4, 3)]])

    assert not is_able_to_play(check_line("E"), check_column("4"), "blanche", grid), \
        "ERROR : is_able_to_play (4) process failed"

    grid = build_grid(copy.deepcopy(grid_test), [[], [(3, 2), (2, 1), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6), (2, 7)]])
    assert is_able_to_play(check_line("D"), check_column("3"), "blanche", grid), \
        "ERROR : is_able_to_play (5) process failed"

    print("test_is_able_to_play : OK")


def test_is_the_end():
    assert not is_the_end(check_line("A"), check_column("4"), "blanche"), "ERROR : is_the_end (1) process failed"
    assert is_the_end(check_line("A"), check_column("4"), "noire"), "ERROR : is_the_end (2) process failed"
    assert not is_the_end(check_line("H"), check_column("4"), "noire"), "ERROR : is_the_end (3) process failed"
    assert is_the_end(check_line("H"), check_column("4"), "blanche"), "ERROR : is_the_end (4) process failed"
    print("test_is_the_end : OK")


def test_is_on_grid():
    assert not is_on_grid(1, -1), "ERROR : is_on_grid (1) process failed"
    assert not is_on_grid(-1, 1), "ERROR : is_on_grid (2) process failed"
    assert not is_on_grid(0, 8), "ERROR : is_on_grid (3) process failed"
    assert is_on_grid(0, 7), "ERROR : is_on_grid (4) process failed"
    assert is_on_grid(7, 0), "ERROR : is_on_grid (5) process failed"
    print("test_is_on_grid : OK")


def test_ia_choose_team():
    assert ia_choose_team("blanche") == "noire", "ERROR : ia_choose_team (1) process failed"
    assert ia_choose_team("noire") == "blanche", "ERROR : ia_choose_team (2) process failed"
    assert not ia_choose_team("blanche") == "blanche", "ERROR : ia_choose_team (3) process failed"
    print("test_ia_choose_team : OK")


def test_ia_find_pawn(grid):
    assert ia_find_pawn("noire", grid) == [[5, 0], [5, 2], [5, 4], [5, 6], [6, 1], [6, 3], [6, 5], [6, 7]], \
        "ERROR : ia_find_pawn (1) process failed"
    print("test_ia_find_pawn : OK")


def test_ia_test_move(grid):
    assert ia_test_move([1, 0], "blanche", grid) == [[2, 0], [3, 0], [0, 0], [1, 1], [3, 2]], \
        "ERROR : ia_test_move (1) process failed"

    grid_test = create_grid()
    grid = build_grid(copy.deepcopy(grid_test), [[], [(3, 2), (2, 1), (1, 2), (2, 3), (1, 4), (2, 5), (1, 6), (2, 7)]])

    assert ia_test_move([3, 2], "blanche", grid, jumped=True) == [[1, 0]], \
        "ERROR : ia_test_move (2) process failed"
    print("test_ia_test_move : OK")


def test_ia_movepool(grid_test):
    grid = build_grid(copy.deepcopy(grid_test), [[(1, 3), (4, 3), (5, 3), (3, 1), (3, 2), (3, 4), (3, 5)], [(3, 3)]])

    assert ia_movepool("blanche", grid) == [[3, 3, [[2, 3]]]], "ERROR : ia_movepool (1) process failed"
    print("test_ia_movepool : OK")


# ================================================================================
# OUTILS DE SET UP DU JEU

# FONCTION PRINCIPALE DE PRE-JEU
def game_set():
    grid = grid_select()
    player_team = team_select()
    print("Vous avez choisi l'équipe", player_team, "\n\n")
    time.sleep(1)
    return grid, player_team


# Permet de choisir sa grille de jeu
def grid_choice():
    print_all_grid()
    grid = create_grid()

    while True:
        print("\n\nSur quelle grille souhaitez vous jouer ?\n1 - Grille début\n2 - Grille milieu\n3 - Grille fin\n")
        answer = str(input())

        if answer == "1":
            return build_grid(copy.deepcopy(grid), set_grid_start())
        elif answer == "2":
            return build_grid(copy.deepcopy(grid), set_grid_mid())
        elif answer == "3":
            return build_grid(copy.deepcopy(grid), set_grid_end())
        else:
            print("\n/!/ Saisie invalide... Recommencez /!/\n")
            time.sleep(1)


# Demande la grille sur laquelle l'utilisateur veut jouer et l'affiche
def grid_select():
    grid = grid_choice()
    print("Vous avez choisi cette grille :\n")
    time.sleep(1)
    print_grid(grid)
    return grid


# Permet de choisir son équipe
def team_select():
    while True:
        print("\n\nChoisissez votre équipe :\n1 - Blancs (♦)\n2 - Noirs (○)\n")
        answer = str(input())

        if answer == "1":
            return "blanche"
        elif answer == "2":
            return "noire"
        else:
            print("\n/!/ Saisie invalide... Recommencez /!/\n")


# Affiche la grille de jeu avec des informations complétementaires
def show_game_grid(grid, selected_pawn=False, old_position=False):
    print("\n      Pions blancs : ♦         Pions noirs : ○")
    if selected_pawn and not old_position:
        print("               Pion sélectionné : ▲")
    elif selected_pawn and old_position:
        print("   Pion sélectionné : ▲     Ancienne position : █")
    print("   –––––––––––––––––––––––––––––––––––––––––––––––", end="")
    print_grid(grid)


# ================================================================================
# OUTILS DE TOUR DE JEU

# FONCTION PRINCIPALE D'UN TOUR
def turn(grid, player_team):
    announce(player_team)
    time.sleep(1)
    play_again = False

    while True:
        # Le joueur choisit le pion qu'il veut jouer
        if not play_again:
            show_game_grid(grid)
            line, column = pawn_select(player_team, grid)
            highlight_pawn(line, column, grid)
        show_game_grid(grid, selected_pawn=True)

        # Le joueur déplace son pion
        new_line, new_column = turn_move(line, column, player_team, grid, play_again)
        if new_line is not None and new_column is not None:
            if not is_jump(line, column, new_line, new_column, player_team, grid) or not is_able_to_play(
                    new_line, new_column, player_team, grid) or is_the_end(new_line, new_column, player_team):
                unhighlight_pawn(new_line, new_column, grid, player_team)
                break
            else:
                print("\n*** Vous pouvez jouer à nouveau ***\n")
                play_again = True
                line, column = new_line, new_column
        elif not play_again:
            unhighlight_pawn(line, column, grid, player_team)
        if play_again:
            print("\n*** Voulez vous passer votre tour ? (o pour passer) ***")
            choice = str(input()).lower()
            if choice == "o":
                unhighlight_pawn(line, column, grid, player_team)
                break

    if is_the_end(new_line, new_column, player_team):
        print("\n\n*** Fin du jeu ***\n\n*** Gagnant : équipe", player_team, "***\n")
        return True
    else:
        print("\n\n*** Tour suivant ***\n\n")
        return False


# Enlève le marquage du pion
def unhighlight_pawn(line, column, grid, team):
    if team == "blanche":
        grid[line][column] = " ♦ "
    elif team == "noire":
        grid[line][column] = " ○ "


# Appelle les fonctions permettant au joueur de faire bouger son pion
def turn_move(line, column, player_team, grid, play_again):
    while True:
        new_line, new_column = player_move(line, column, player_team, grid, play_again)
        if new_line is not None and new_column is not None:
            change_grid(new_line, new_column, line, column, grid)
            show_game_grid(grid, selected_pawn=True, old_position=True)
            change_grid(new_line, new_column, line, column, grid, reset=True)
            return new_line, new_column
        else:
            return None, None


# Vérifie si la partie doit se terminer ou non
def is_the_end(line, column, team):
    if team == "noire" and (line == 0 and (column == 3 or column == 4)):
        return True
    if team == "blanche" and (line == 7 and (column == 3 or column == 4)):
        return True
    return False


# Fonction de mouvement d'un pion
def player_move(selected_x, selected_y, selected_team, grid, play_again):
    while True:
        print("\n*** Déplacez votre pion (déplacez vous sur vous même pour annuler) ***\n")
        destination_line, destination_column = enter_coordinates()
        if check_move(selected_x, selected_y, selected_team, grid, destination_line, destination_column, play_again):
            return destination_line, destination_column
        else:
            print("\n*** Voulez vous effectuer une autre saisie ? (n pour quitter) ***\n")
            choice = str(input()).lower()
            if choice == "n":
                return None, None


# Effectue les changements post-mouvement sur la grille de jeu
def change_grid(new_line, new_column, line, column, grid, reset=False):
    if not reset:
        grid[new_line][new_column] = grid[line][column]
        grid[line][column] = " █ "
    else:
        grid[line][column] = "   "


# Vérifie si le mouvement est possible
def check_move(selected_x, selected_y, selected_team, grid, destination_line, destination_column, play_again=False,
               bot=False):
    if is_different(selected_x, selected_y, destination_line, destination_column):
        if check_destination(destination_line, destination_column, grid, selected_team):
            if is_jump(selected_x, selected_y, destination_line, destination_column, selected_team, grid):
                return True
            elif is_orthogonal(selected_x, selected_y, destination_line, destination_column, grid, selected_team)\
                    and not play_again:
                return True
            elif not bot:
                print("\n/!/ Mouvement interdit /!/\n")
        elif not bot:
            print("\n/!/ Vous ne pouvez pas vous déplacer sur un pion ou dans vos goals /!/\n")
    elif not bot:
        print("\n/!/ Vous ne pouvez pas vous déplacer sur vous même/!/\n")
    return False


# Vérifie s'il s'agit d'un saut
def is_jump(x, y, new_x, new_y, team, grid):
    if is_orthogonal_jump(x, y, new_x, new_y, team, grid) or is_diagonal_jump(x, y, new_x, new_y, team, grid):
        return True
    return False


# Vérifie s'il s'agit d'un saut orthogonal
def is_orthogonal_jump(x, y, new_x, new_y, team, grid):
    if abs(x-new_x)+abs(y-new_y) == 2:
        if x == new_x or y == new_y:
            if is_same_team(int((x+new_x)/2), int((y+new_y)/2), team, grid):
                return True
    return False


# Vérifie s'il s'agit d'un saut diagonal
def is_diagonal_jump(x, y, new_x, new_y, team, grid):
    if abs(x-new_x)+abs(y-new_y) == 4:
        if abs(x-new_x) == abs(y-new_y):
            if is_same_team(int((x+new_x)/2), int((y+new_y)/2), team, grid):
                return True
    return False


# Vérifie si le mouvement est orthogonal
def is_orthogonal(x, y, new_x, new_y, grid, team):
    if new_x == x or new_y == y:
        if can_go_to(x, y, new_x, new_y, grid, team):
            if is_home(x, team):
                return True
    return False


# Vérifie s'il n'y a aucun obstacle sur le chemin du pion (mouvement orthogonal)
def can_go_to(x, y, new_x, new_y, grid, team):
    if not is_home(new_x, team):
        return False
    if y == new_y:
        for i in range(1, abs(x-new_x)):
            if x > new_x:
                if not grid[x-i][y] == "   ":
                    return False
            elif new_x > x:
                if not grid[x+i][y] == "   ":
                    return False
    if x == new_x:
        for i in range(1, abs(y-new_y)):
            if y > new_y:
                if not grid[x][y-i] == "   ":
                    return False
            elif new_y > y:
                if not grid[x][y+i] == "   ":
                    return False
    return True


# Vérifie si le mouvement du pion est possible
def check_destination(line, column, grid, team):
    if not is_a_pawn(line, column, grid):
        if not is_own_goal(line, column, team):
            return True


# Vérifie si la case est le goal de l'équipe du joueur selectionné
def is_own_goal(line, column, team):
    if team == "blanche" and (line == 0 and (column == 3 or column == 4)):
        return True
    if team == "noire" and (line == 7 and (column == 3 or column == 4)):
        return True
    return False


# Permet de montrer le pion selectionné par le joueur
def highlight_pawn(line, column, grid):
    grid[line][column] = " ▲ "


# Fonction de choix de pion
def pawn_select(team, grid):
    print("*** Choix d'un pion ***\n")
    while True:
        line, column = pawn_coordinates()
        if pawn_verify(line, column, team, grid):
            return line, column
        else:
            print("\n/!/ Recommencez /!/\n")
            time.sleep(1)


# Série de tests pour vérifier la saisie des coordonnées d'un pion
def pawn_verify(line, column, team, grid):
    if is_a_pawn(line, column, grid):
        if is_same_team(line, column, team, grid):
            if is_able_to_play(line, column, team, grid):
                return True
            else:
                print("\n/!/ Ce pion ne peut pas se déplacer /!/ \n")
        else:
            print("\n/!/ Le pion n'est pas de la bonne équipe /!/")
    else:
        print("\n/!/ Vous n'avez pas choisi un pion /!/")
    return False


# Vérifie si le pion peut-être joué
def is_able_to_play(line, column, team, grid):
    move_list = [[line+1, column], [line-1, column], [line, column-1], [line, column+1], [line+2, column+2],
                 [line+2, column-2], [line-2, column-2], [line-2, column+2], [line-2, column], [line, column-2],
                 [line+2, column], [line, column+2]]
    for move in move_list:
        move_line = move[0]
        move_column = move[1]
        if is_on_grid(move_line, move_column):
            if check_move(line, column, team, grid, move_line, move_column, bot=True):
                return True
    return False


# Vérifie si les coordonnées sont celles d'un pion
def is_a_pawn(line, column, grid):
    if grid[line][column] == " ♦ " or grid[line][column] == " ○ ":
        return True
    return False


# Vérifie si le pion est de l'équipe du joueur
def is_same_team(line, column, team, grid):
    if team == "blanche" and grid[line][column] == " ♦ ":
        return True
    if team == "noire" and grid[line][column] == " ○ ":
        return True
    return False


# Vérifie si les coordonnées sont dans la grille
def is_on_grid(line, column):
    if line >= 0 and line < 8 and column >= 0 and column < 8:
        return True
    return False


# Vérifie si les coordonnées saisies sont du côté du plateau de l'équipe choisie
def is_home(line, team):
    if team == "blanche" and line >= 0 and line < 4:
        return True
    if team == "noire" and line >= 4 and line < 8:
        return True
    return False


# Demande à l'utilisateur de saisir les coordonnées du pion qu'il veut sélectionner
def pawn_coordinates():

    line, column = enter_coordinates()
    return line, column


# Annonce quelle équipe joue
def announce(team):
    print("********************************")
    print("  Au tour de l'équipe", team, "!")
    print("********************************\n\n")


# Vérifie que la coordonnée saisie est différente du pion selectionné
def is_different(x, y, new_x, new_y):
    if x != new_x or y != new_y:
        return True
    return False


# ================================================================================
# OUTILS DE L'IA

# FONCTION PRINCIPALE TOUR JOUEUR VS IA
def player_versus_ia(difficulty=0):
    grid, player_team = game_set()
    ia_team = ia_choose_team(player_team)
    if player_team == "blanche":
        switch_turn = True
    else:
        switch_turn = False

    while True:
        if switch_turn:
            if turn(grid, player_team):
                break
            else:
                switch_turn = False
        elif not switch_turn:
            if difficulty == 0:
                if turn_ia(grid, ia_team, player=True):
                    break
                else:
                    switch_turn = True
            elif difficulty == 1:
                if turn_advanced_ia(grid, ia_team, player=True):
                    break
                else:
                    switch_turn = True

        time.sleep(1.5)


# Trouve tous les mouvements possibles pour l'IA
def ia_movepool(team, grid, jumped=False):
    movepool = []
    ia_pawn_list = ia_find_pawn(team, grid)

    for pawn_coord in ia_pawn_list:
        ia_pawn_list_move = ia_test_move(pawn_coord, team, grid, jumped)
        if ia_pawn_list_move != []:
            movepool.append([pawn_coord[0], pawn_coord[1], ia_pawn_list_move])

    return movepool


# Teste toutes les possibilités de mouvement pour un pion
def ia_test_move(pawn_coord, team, grid, jumped=False):
    x = pawn_coord[0]
    y = pawn_coord[1]
    ia_pawn_move_list = []
    if is_the_end(x, y, team):
        return []

    if not jumped:
        possible_movement = [[x+1, y], [x+2, y], [x+3, y], [x+4, y],
                             [x-1, y], [x-2, y], [x-3, y], [x-4, y],
                             [x, y+1], [x, y+2], [x, y+3], [x, y+4], [x, y+5], [x, y+6], [x, y+7],
                             [x, y-1], [x, y-2], [x, y-3], [x, y-4], [x, y-5], [x, y-6], [x, y-7],
                             [x+2, y+2], [x-2, y+2], [x-2, y-2], [x+2, y-2]]
    else:
        possible_movement = [[x+2, y+2], [x-2, y+2], [x-2, y-2], [x+2, y-2], [x+2, y], [x-2, y], [x, y-2], [x, y+2]]

    for movement in possible_movement:
        new_x = movement[0]
        new_y = movement[1]
        if is_on_grid(new_x, new_y):
            if not jumped:
                if check_move(x, y, team, grid, new_x, new_y, bot=True):
                    ia_pawn_move_list.append(movement)
            else:
                if is_jump(x, y, new_x, new_y, team, grid):
                    if check_move(x, y, team, grid, new_x, new_y, bot=True):
                        ia_pawn_move_list.append(movement)

    return ia_pawn_move_list


# Trouve les pions de l'IA sur la grille et retourne leurs positions
def ia_find_pawn(team, grid):
    ia_pawn_list = []
    for line in range(len(grid)):
        for column in range(len(grid[0])):
            if team == "blanche" and grid[line][column] == " ♦ ":
                ia_pawn_list.append([line, column])
            if team == "noire" and grid[line][column] == " ○ ":
                ia_pawn_list.append([line, column])
    return ia_pawn_list


#
def turn_ia_select_pawn(movepool, grid):
    random_num = random.randint(0, len(movepool) - 1)
    ia_pawn_choice = movepool[random_num]
    ia_pawn_line = ia_pawn_choice[0]
    ia_pawn_column = ia_pawn_choice[1]
    highlight_pawn(ia_pawn_line, ia_pawn_column, grid)

    return ia_pawn_choice, ia_pawn_line, ia_pawn_column


#
def turn_ia_select_move(ia_pawn_choice):
    random_num = random.randint(0, len(ia_pawn_choice[2]) - 1)
    ia_move_choice = ia_pawn_choice[2][random_num]
    ia_move_line = ia_move_choice[0]
    ia_move_column = ia_move_choice[1]

    return ia_move_line, ia_move_column


#
def turn_ia_change_grid(ia_move_line, ia_move_column, ia_pawn_line, ia_pawn_column, grid, team):
    change_grid(ia_move_line, ia_move_column, ia_pawn_line, ia_pawn_column, grid)
    show_game_grid(grid, selected_pawn=True, old_position=True)
    change_grid(ia_move_line, ia_move_column, ia_pawn_line, ia_pawn_column, grid, reset=True)
    unhighlight_pawn(ia_move_line, ia_move_column, grid, team)


#
def turn_ia_remove_last_move(next_move_list, ia_pawn_line, ia_pawn_column):
    i = 0
    while i < len(next_move_list):
        if next_move_list[i][0] == ia_pawn_line and next_move_list[i][1] == ia_pawn_column:
            del next_move_list[i]
            break
        i += 1


#
def check_is_the_end(ia_move_line, ia_move_column, team):
    if is_the_end(ia_move_line, ia_move_column, team):
        print("\n\n*** Fin du jeu ***\n\n*** Gagnant : équipe", team, "***\n")
        return True
    else:
        print("\n\n*** Tour suivant ***\n\n")
        return False


#
def turn_ia_jump_again(ia_move_line, ia_move_column, next_move_list):
    if next_move_list != []:
        will_jump_again = random.randint(0, 100)
        if will_jump_again >= 50:
            return True
        else:
            return False
    else:
        return False


#
def turn_ia_random(movepool, grid, team):
    #
    ia_pawn_choice, ia_pawn_line, ia_pawn_column = turn_ia_select_pawn(movepool, grid)

    #
    ia_move_line, ia_move_column = turn_ia_select_move(ia_pawn_choice)

    #
    turn_ia_change_grid(ia_move_line, ia_move_column, ia_pawn_line, ia_pawn_column, grid, team)

    return ia_pawn_line, ia_pawn_column, ia_move_line, ia_move_column


# Execute un tour pour l'IA
def turn_ia(grid, team, player=False):
    jumped = False
    announce(team)
    ia_move_line = ia_move_column = 0
    while True:
        if not jumped:
            movepool = ia_movepool(team, grid, jumped)
            # movepool sous la forme :
            # [[pawn, [mouvement 1, mouvement 2, etc..]]]
            # plus précisément : [[line, column,[[line, column], [line, column], etc...]]]
            if movepool == []:
                break

        #
        ia_pawn_line, ia_pawn_column, ia_move_line, ia_move_column = turn_ia_random(movepool, grid, team)

        #
        if is_jump(ia_pawn_line, ia_pawn_column, ia_move_line, ia_move_column, team, grid) and not \
                is_the_end(ia_move_line, ia_move_column, team):
            jumped = True

            next_move_list = ia_test_move((ia_move_line, ia_move_column), team, grid, jumped)
            turn_ia_remove_last_move(next_move_list, ia_pawn_line, ia_pawn_column)

            #
            if not turn_ia_jump_again(ia_move_line, ia_move_column, next_move_list):
                break
            else:
                movepool = [[ia_move_line, ia_move_column, next_move_list]]
                print("\n*** L'IA va resauter ***\n")
        else:
            break

        # Si l'IA joue contre un joueur, ajoute un temps d'attente à la fin du tour
        if player:
            time.sleep(2)

    return check_is_the_end(ia_move_line, ia_move_column, team)


#
def turn_advanced_ia(grid, team, player=False):
    jumped = False
    announce(team)
    ia_move_line = ia_move_column = 0
    while True:
        if not jumped:
            movepool = ia_movepool(team, grid, jumped)
            # movepool sous la forme :
            # [[pawn, [mouvement 1, mouvement 2, etc..]]]
            # plus précisément : [[line, column,[[line, column], [line, column], etc...]]]
            if movepool == []:
                break

        #
        best_move = ia_find_best_move(movepool, team)
        if jumped and not best_move:
            break
        elif not jumped and not best_move:
            turn_ia_random(ia_movepool(team, grid, jumped), grid, team)
            break
        elif jumped and best_move:
            print("\n*** L'IA va resauter ***\n")

        #
        if jumped and ia_give_score(best_move[2][0], best_move[2][1], ia_find_goals(team)) >= \
                ia_give_score(ia_pawn_line, ia_pawn_column, ia_find_goals(team)):
            break

        ia_pawn_line, ia_pawn_column, ia_move_line, ia_move_column = best_move[0], best_move[1], best_move[2][0]\
            , best_move[2][1]

        #
        highlight_pawn(ia_pawn_line, ia_pawn_column, grid)
        turn_ia_change_grid(ia_move_line, ia_move_column, ia_pawn_line, ia_pawn_column, grid, team)

        #
        if is_jump(ia_pawn_line, ia_pawn_column, ia_move_line, ia_move_column, team, grid) and not \
                is_the_end(ia_move_line, ia_move_column, team):
            jumped = True

            #
            next_move_list = ia_test_move((ia_move_line, ia_move_column), team, grid, jumped)
            turn_ia_remove_last_move(next_move_list, ia_pawn_line, ia_pawn_column)

            if next_move_list != []:
                movepool = [[ia_move_line, ia_move_column, next_move_list]]
            else:
                break

        else:
            break

        # Si l'IA joue contre un joueur, ajoute un temps d'attente à la fin du tour
        if player:
            time.sleep(2)

    return check_is_the_end(ia_move_line, ia_move_column, team)


# Renvoie les positions des buts adverses
def ia_find_goals(team):
    if team == "blanche":
        return [(7, 3), (7, 4)]
    elif team == "noire":
        return [(0, 3), (0, 4)]


#
def ia_find_best_move(movepool, team):
    goals_position = ia_find_goals(team)
    move_score_list = []

    for i in range(len(movepool)):
        pawn_info = movepool[i]
        move_list = pawn_info[2]
        pawn_x, pawn_y = pawn_info[0], pawn_info[1]

        score = ia_find_score(move_list, goals_position, pawn_x, pawn_y)
        if score:
            move_score_list.append([pawn_x, pawn_y, score])

    for i in range(len(move_score_list)):
        for j in range(len(move_score_list)):
            if move_score_list[i][2][2] < move_score_list[j][2][2]:
                move_score_list[j], move_score_list[i] = move_score_list[i], move_score_list[j]

    if move_score_list != []:
        return [move_score_list[0][0], move_score_list[0][1], [move_score_list[0][2][0], move_score_list[0][2][1]]]


#
def ia_find_score(move_list, goals_position, pawn_x, pawn_y):
    move_score_list = []
    i_move = 0
    pawn_score = ia_give_score(pawn_x, pawn_y, goals_position)

    while len(move_list) > len(move_score_list):
        move_x = move_list[i_move][0]
        move_y = move_list[i_move][1]
        move_score = ia_give_score(move_x, move_y, goals_position)

        if not move_score >= pawn_score:
            move_score_list.append(move_score)
            i_move += 1
        else:
            del move_list[i_move]

    if move_score_list != []:
        return ia_find_best_score(move_list, move_score_list)


#
def ia_give_score(x, y, goals_position):
    goal1_x = goals_position[0][0]
    goal1_y = goals_position[0][1]  # 3
    goal2_x = goals_position[1][0]
    goal2_y = goals_position[1][1]  # 4

    if y >= 0 and y < 4:
        return abs(goal1_x - x) + abs(goal1_y - y)
    else:
        return abs(goal2_x - x) + abs(goal2_y - y)


#
def ia_find_best_score(move_list, move_score_list):
    for i in range(len(move_list)):
        for j in range(len(move_list)):
            if move_score_list[i] < move_score_list[j]:
                move_score_list[j], move_score_list[i] = move_score_list[i], move_score_list[j]
                move_list[j], move_list[i] = move_list[i], move_list[j]

    return [move_list[0][0], move_list[0][1], move_score_list[0]]


# Donne l'autre équipe à l'IA (Joueur vs IA)
def ia_choose_team(player_team):
    if player_team == "blanche":
        return "noire"
    else:
        return "blanche"


# ================================================================================
# OUTILS DEBUG (IA VS IA)
def ia_versus_ia(difficulty=0):
    ia_team = "blanche"
    grid_setup = create_grid()
    grid = build_grid(copy.deepcopy(grid_setup), set_grid_start())
    nb_turn = 0

    while True:
        nb_turn += 1

        # IA naïve vs IA naïve
        if difficulty == 0:
            if turn_ia(grid, ia_team):
                break
            else:
                if ia_team == "blanche":
                    ia_team = "noire"
                else:
                    ia_team = "blanche"

        # IA avancée vs IA naïve
        elif difficulty == 1:
            if ia_team == "blanche" and not turn_advanced_ia(grid, ia_team):
                ia_team = "noire"
            elif ia_team == "noire" and not turn_ia(grid, ia_team):
                ia_team = "blanche"
            else:
                break

        # IA avancée vs IA avancée
        elif difficulty == 2:
            if turn_advanced_ia(grid, ia_team):
                break
            else:
                if ia_team == "blanche":
                    ia_team = "noire"
                else:
                    ia_team = "blanche"

        # time.sleep(1.5)

    print("\n\n\n*** La partie a duré", nb_turn, "tours ***\n\n\n")


# ================================================================================
# OUTILS DES MENUS

# FONCTION PRINCIPALE DES MENUS
def main_menu():
    while True:
        print_main_menu()
        choice = str(input())
        if choice == "1":
            game_menu()
        elif choice == "2":
            launch_all_tests()
        elif choice == "3":
            print_doc()
        elif choice == "4":
            break


# Affiche le menu principal
def print_main_menu():
    print(
        '''
                        ____  U _____ u  __  __  U _____ u  _____  U _____ u   ____     
                       |  _"\ \| ___"|/U|' \/ '|u\| ___"|/ |_ " _| \| ___"|/U |  _"\ u  
                      /| | | | |  _|"  \| |\/| |/ |  _|"     | |    |  _|"   \| |_) |/  
                      U| |_| |\| |___   | |  | |  | |___    /| |\   | |___    |  _ <    
                       |____/ u|_____|  |_|  |_|  |_____|  u |_|U   |_____|   |_| \_\   
                        |||_   <<   >> <<,-,,-.   <<   >>  / / \ \  <<   >>   //   \ \  
                       (__)_) (__) (__) (./  \.) (__) (__)(__) (__)(__) (__) (__)  (__)
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


# Menu de jeu
def game_menu():
    while True:
        print_game_menu()
        choice = str(input())
        if choice == "1":
            grid, player_team = game_set()
            turn(grid, player_team)
            break
        elif choice == "2":
            player_versus_player()
            break
        elif choice == "3":
            menu_player_versus_ia()
        elif choice == "4":
            print_rules()
        elif choice == "5":
            break
        elif choice == "6":
            menu_ia_versus_ia()


#
def menu_player_versus_ia():
    while True:
        print_menu_player_versus_ia()
        choice = str(input())
        if choice == "1":
            player_versus_ia()
        elif choice == "2":
            player_versus_ia(difficulty=1)
        elif choice == "3":
            break


#
def print_menu_player_versus_ia():
    print(
        '''  
        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                              Menu Joueur versus IA
                                            ------------------------- 

                                            Choisissez votre mode :
                                            
                                            1 - Joueur vs IA naïve
                                            2 - Joueur vs IA avancée
                                            
                                            3 - Retour au menu de jeu

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________

        '''
    )


#
def menu_ia_versus_ia():
    while True:
        print_menu_ia_versus_ia()
        choice = str(input())
        if choice == "1":
            ia_versus_ia()
        elif choice == "2":
            ia_versus_ia(difficulty=1)
        elif choice == "3":
            ia_versus_ia(difficulty=2)
        elif choice == "4":
            break


#
def print_menu_ia_versus_ia():
    print(
        '''  
        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                Menu IA versus IA
                                            ------------------------- 

                                            Choisissez votre mode :
                                            
                                            1 - IA naïve vs IA naïve
                                            2 - IA avancée vs IA naïve
                                            3 - IA avancée vs IA avancée
                                            
                                            4 - Retour au menu de jeu

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )

# Affiche les règles du jeu
def print_rules():
    print(
        '''  
        _____________________________________________________________________________________________
        
        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Règles du jeu
                                            ------------------------- 

                                            Disponibles à l'adresse :

        https://moodle.univ-tlse3.fr/pluginfile.php/376187/mod_resource/content/4/reglesDemeterRev1.pdf

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________

        '''
    )
    time.sleep(1)


# Affiche le menu de jeu
def print_game_menu():
    print(
        '''  

        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Menu de jeu 
                                        ---------------------------------

                                            Que souhaitez vous faire ?

                                            1 - Lancer un tour de jeu
                                            2 - Partie J vs J
                                            3 - Partie J vs IA
                                            4 - Règles du jeu
                                            
                                            5 - Retour au menu principal
                                            
                                            6 - IA vs IA (debug)

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________
        '''
    )


# Le jeu en joueur contre joueur
def player_versus_player():
    grid = grid_select()
    # Le mode JcJ étant local, inutile de définir un "joueur 1" et "joueur 2", chacun joue l'équipe qu'il souhaite
    print("\n*** Le joueur souhaitant jouer l'équipe blanche commence en premier ***\n")
    player_team = "blanche"
    while True:
        if not turn(grid, player_team):
            if player_team == "blanche":
                player_team = "noire"
            else:
                player_team = "blanche"
        else:
            break


# Affiche la documentation
def print_doc():
    print(
        '''  
        _____________________________________________________________________________________________

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                                  Documentation
                                            ------------------------- 

                                            Disponibles à l'adresse :

                                           https://pastebin.com/00YTCZG1

        *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        _____________________________________________________________________________________________

        '''
    )


# ================================================================================
# FONCTION PRINCIPALE DE JEU
def game():
    main_menu()


# ================================================================================
# PROGRAMME PRINCIPAL
game()
