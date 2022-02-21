# Yukoo - Notes

## Ordre des coups `coups prioritaires`

1. Echec et mat
2. Echecs (tri par avantage matériel après coup >)
3. Prises (tri par valeur >)
4. Découverte sur deux pièces non protégées ou sur pièce de valeur supérieure
   > :warning: Temps de calcul
5. Clouage
6. Fourchette

## Coups à couper

- Mettre une pièce en prise par une pièce de valeur plus faible et si prise pas de cases supplémentaires accessible à un fou, une dame, une tour ou un cavalier.
- Bouger une pièce dèjà développée dans l'ouverture alors que d'autres pièces ne sont pas développées et que ce n'est pas un coup prioritaire.
- Avancée d'un pion situé situé devant le roi après roque sauf pour contrôler une case de destination d'une pièce adverse.
- Mettre une pièce sur une case menaçable par un pion (protégé si la pièce est une dame ou un fou) en 1 coup.
