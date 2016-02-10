Petit Antoine & Wissocq Sarah


Actuellement les tests du transformateur de log ont été fait, nous avons fait le choix que les logs seraient lu d'un bloc et donc qu'on obtiendrait une liste de Message suite à la lecture d'un log.

Les tests et le programme du lecteur de message ont été intégralement écrit (nous pensons avoir géré la majorité des erreurs possibles lors de la lecture de logs).
Lors de l'implémentation de ce lecteur nous avons fait le choix qu'il lisait d'un bloc les logs et que la méthode principale ne renvoyé pas d'exception si un des logs étaient mal formé.
A la réception des exceptions on pourrait envoyé les lignes vers un fichier .bad si on le souhaitait ou afficher que nous avons reçu une exception.
