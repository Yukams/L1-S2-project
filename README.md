Bonjour,

Bienvenue sur mon projet Déméter.

Tout d'abord, avant de commencer la documentation, je vous recommande de lancer le programme, afin de vous familiariser avec l'interface.
Le nombre de lignes peut s'avérer intimidant, mais je suis là pour vous guider afin de comprendre rapidement et aisément le code.

Si vous rencontrez un quelconque bug ou si vous avez des suggestions, n'hésitez surtout pas à les écrire lors de l'évaluation.

==============================================================================================================
Chapitre I : L'interface
L'interface se décompose en 3 parties, le menu du jeu, le menu des tests et la présente documentation.
Elle a pour but de vous faciliter la naviguation et rendre agréable l'utilisation du programme
Toute la partie du code de l'interface vous est inutile à corriger ou à vérifier puisqu'il ne s'agit en rien du jeu.
Ce code se situe entre les LIGNES : 608 et 1041

==============================================================================================================
Chapitre II : Les tests
Les tests fonctionnent avec des assertions et utilisent les fonctions : move_tests(), can_move(), est_dans_grille() et jump()
Les outils relatifs aux tests vous intéresseront sûrement et sont disponibles de la LIGNES 1042 à 1295

Le menu des tests vous permet de choisir plusieurs types de tests, attention les tests visuels sont volontairement lents.
En effet, le code est parsemé de l'instruction "time.sleep()" qui, je l'espère, vous rendra la lecture sur le Terminal bien plus aisée. J'ai indexé cette attente sur ma vitesse de lecture, il se peut alors que vous ayez à attendre ou à remonter sur le Terminal pour pouvoir lire.

Vous pouvez créer vous même des tests si ceux que je propose ne vous conviennent pas dans le menu de tests

==============================================================================================================
Chapitre III : Le jeu
Voici comment se décompose le code du jeu :
- LIGNES 17 à LIGNES 62 : Outils pour l'affichage graphique des grilles
- LIGNES 62 à LIGNES 160 : Outils de création des grilles
- LIGNES 161 à LIGNES 218 : Outils pour la saisie et la vérification des coordonnées
- LIGNES 219 à LIGNES 279 : Outils de choix de la grille de jeu
- LIGNES 280 à LIGNES 607 : Outils pour jouer une partie

======================
Contexte :
Les ressources qui vous intéressent le plus sont dans cette dernière catégorie, c'est le codage des règles du jeu et des règles du programme.
400 lignes ??? Pourquoi est ce aussi long ?
Le programme comporte de nombreuses vérifications afin d'empêcher que le joueur ne puisse se bloquer dans la partie.
Ainsi, il peut aussi la plupart du temps changer d'avis après une saisie, il lui sera quasiment systématiquement demandé de confirmer son choix. Pourquoi celà ? Je me suis rendu compte en jouant qu'il était facile de se tromper entre deux coordonnées et que se retrouver bloqué était affreusement frustrant, je n'aimerais pas que celà m'arrive en plein milieu d'une partie. J'ai donc fait le choix d'ajouter beaucoup de barrières de protections pour libérer les joueurs des mauvaises surprises.

======================
Fonctions :
- Les fonctions (pawn_choice_confirmation [LIGNE 547], give_up_move [LIGNE 514], pawn_choice [LIGNE 580],
  play_again [LIGNE 300], game_turn [LIGNE 283], turn [LIGNE 465]) sont des fonctions principalement textuelles et permettent au joueur de communiquer avec le jeu
- Les fonctions (pawn_color [LIGNE 533], replace_cross [LIGNE 547]) sont des fonctions utiles pour le fonctionnement du jeu
- Les fonctions (forbidden_move [LIGNE 454], forbidden_cases [LIGNE 443], jump [LIGNE 404], move_tests [LIGNE 390],
  can_jump [LIGNE 360], can_move [LIGNE 347], can_play [LIGNE 337], end_game_test [LIGNE 330]) sont toutes des fonctions de vérifications, elles peuvent être très fastidieuses à lire, je vous recommande de vous cantonner aux commentaires
- Les fonctions (game_turn [LIGNE 284], turn [LIGNE 465]) sont par ailleurs les fonctions "mères", celles qui sont à la racine du système de jeu


======================
Exemple :
Afin de vous aider à mieux cerner les rouages du jeu, voici le détail d'un tour de jeu:
!!! Certains tests sont redondants, c'est parce que les fonctions sont pensées pour être utilisées indépendamment les une des autres !!!


*** Après le choix de la grille et son affichage ***
game_turn ([LIGNE 284])
=> pawn_choice ([LIGNE 580])

# Choix du pion
- Le joueur saisit une ligne
  => Le programme vérifie si cette ligne existe dans la grille (get_line [LIGNE 173]), sinon demande de ressaisir
- Le joueur saisit une colonne
  => Le programme vérifie si cette colonne existe dans la grille (get_column [LIGNE 203]), sinon demande de ressaisir

{
=> Le programme vérifie que les coordonnées sont bien dans la grille (utile pour d'autres cas)
(est_dans_grille ([LIGNE 164])
=> Le programme vérifie que les coordonnées correspondent à un pion
=> Le programme vérifie que le pion sélectionné peut se déplacer (can_play [LIGNE 337])
=> can_play
{
=> Reconnait la couleur du pion
=> Teste si le pion peut se mouvoir (can_move [LIGNE 347], can_jump [LIGNE 360])
=> can_move
{
=> move_test (LIGNE [390]) # Effectue des essais de mouvements (orthogonaux)
{
=> Le programme vérifie que la case d'arrivée est vide
=> forbidden_cases (LIGNE [443])
{
=> Verifie en fonction de la couleur du pion qu'il ne va pas dans ses buts
}
=> forbidden_move (LIGNE [454])
{
=> Vérifie que le pion ne se déplace pas dans le camps adverse en fonction de sa couleur
}
=> Vérifie que le pion se déplace orthogonalement
}
}
=> can_jump # Effectue des essais de mouvements (sauts)
{
=> Vérifie que le saut ne sort pas de la grille
=> Vérifie que les coordonnées correspondent à un pion
=> Vérifie que la case d'arrivée est vide
=> Vérifie que le saut n'est pas une position antérieure immédiate
=> Effectue des tests de sauts (jump [LIGNE 404])
{
=> Vérifie que la case d'arrivée est vide
=> forbidden_cases
=> Teste les 4 sauts orthogonaux
=> Teste les 4 sauts en diagonale
}
}
}

=> Le programme demande au joueur si il veut vraiment jouer ce pion (pawn_choice_confirmation [LIGNE 547])
{
=> Reconnait la couleur du pion selectionné (pawn_color [LIGNE 534])
=> Signale la couleur du pion choisi
=> Remplace visuellement le pion sur la grille par une croix

	=> Le joueur peut alors choisir d'accepter son choix de pion ou de retourner à la saisie de coordonnées pour en changer
		=> Si le joueur accepte, renvoie la couleur à pawn_choice
		=> Si il refuse, renvoie une couleur vide " " à pawn_choice
	}
=> Si le pion possède une couleur autre que " "
=> pawn_choice renvoie à game_turn la position en x et en y ainsi que la couleur du pion
=> Sinon recommence la boucle
}

=============
(suite...)
game_turn ([LIGNE 284])
=> pawn_choice ([LIGNE 580])
=> turn ([LIGNE 465])

# Déplacement du pion
- Le joueur saisit une ligne
  => Le programme vérifie si cette ligne existe dans la grille (get_line [LIGNE 173]), sinon demande de ressaisir
- Le joueur saisit une colonne
  => Le programme vérifie si cette colonne existe dans la grille (get_column [LIGNE 203]), sinon demande de ressaisir

{
=> Vérifie que le joueur n'a pas saisi les coordonnées actuelles du pion
=> Si le joueur a déjà effectué un saut, demande s'il veut abandonner sa remise de tour
=> Si oui, envoie les nouvelles coordonnées du pion

	=> Si le joueur veut se déplacer orthogonalement et qu'il n'a pas déjà sauté
		=> move_test (LIGNE [390]) # Effectue des essais de mouvements (orthogonaux)
			{
			=> Le programme vérifie que la case d'arrivée est vide 
			=> forbidden_cases (LIGNE [443])
				{
				=> Verifie en fonction de la couleur du pion qu'il ne va pas dans ses buts
				}
			=> forbidden_move (LIGNE [454])
				{
				=> Vérifie que le pion ne se déplace pas dans le camps adverse en fonction de sa couleur
				}
			=> Vérifie que le pion se déplace orthogonalement
			}
			=> Change la position du pion par sur la grille et renvoie ses nouvelles coordonnées

	=> Si le joueur veut sauter
		=> Effectue des tests de sauts (jump [LIGNE 404])
			{
			=> Vérifie que la case d'arrivée est vide
			=> forbidden_cases
			=> Teste les 4 sauts orthogonaux
			=> Teste les 4 sauts en diagonale	
			}
			=> Change la croix position du pion sur la grille
				=> Vérifie si il veut jouer à nouveau (play_again [LIGNE 300])
					=> Verifie que le jeu n'est pas terminé (end_game_test [LIGNE 330])
						{
						=> Vérifie en fonction de la couleur du pion, si il est sur les goals adverses ou non
						}

					=> can_jump # Effectue des essais de mouvements (sauts)
						{
						=> Vérifie que le saut ne sort pas de la grille
						=> Vérifie que les coordonnées correspondent à un pion
						=> Vérifie que la case d'arrivée est vide
						=> Vérifie que le saut n'est pas une position antérieure immédiate
						=> Effectue des tests de sauts (jump [LIGNE 404])
							{
							=> Vérifie que la case d'arrivée est vide
							=> forbidden_cases
							=> Teste les 4 sauts orthogonaux
							=> Teste les 4 sauts en diagonale
							}
						}
				- Demande au joueur si il veut jouer à nouveau
					=> Si oui, relance la boucle et garde en mémoire que le joueur a sauté
						=> Change la position actuelle du pion en mémoire
					=> Si non, renvoie les nouvelles coordonnées du pion
			}
}

=============
(suite...)
game_turn ([LIGNE 284])
=> pawn_choice ([LIGNE 580])
=> turn ([LIGNE 465])
=> end_game_test

=> Si oui, remplace la croix de selection par le pion de la bonne couleur, affiche le message de victoire
=> Si non, passe au prochain tour

FIN DU TOUR DE JEU