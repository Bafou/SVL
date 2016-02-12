PETIT Antoine & WISSOCQ Sarah

TP5 : Shut the box

Lancer_des : lancer le nombre de dés souhaités, afficher le score des dés, demander au joueur quelle(s) tuile(s) fermer puis fermer les tuiles demander.
Tour : Tant que le joueur n'a pas gagné, ou n'est pas bloqué, lance la fonction lancer_des. Puis à la fin affiche le score du tour.
Jeu : Quand un tour est fait, change de joueur, jusqu'à la fin de la partie. Puis affiche le score total.

Lance_des :
    - 2 dés sont bien lancés.
    - 1 dé est bien lancé.
    - Verifier qu'il est encore possible de jouer.
    - On demande bien une fois au joueur quelle tuile il voudrait abaisser
    - On demande bien au moins une fois au joueur quelle tuiles il voudrait abaisser
    - Si le joueur demande d'abaisser une tuile plus grande que le résultat des dés, c'est impossible.
    - Toutes les tuiles sont ouvertes au début.
    - Il est impossible de fermer une tuile déjà fermée.
    - On ferme bien la tuile que le joueur voulait abaisser.
    - Le joueur demande d'abaisser plusieurs tuiles, les tuiles choisit sont fermées.
    
Tour : 
    - Si le joueur a fermé toutes les tuiles, il a gagné, tour fini.
    - Si le joueur n'a plus de coup possible, il a terminé, tour fini.
    - On lance bien la fonction lancer_des.
    - Le score s'affiche bien à la fin du tour.
    
Jeu :
    - Si le tour est fini, passe bien au joueur suivant.
    - Effectue bien le nombre de tour demandé.
    - Affiche bien les 2 scores finaux à la fin de la partie.