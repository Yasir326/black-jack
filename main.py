'''
1. Computer Dealer
    Dealer starts with 1 card face up and 1 card face down
2. Player starts with 2 cards face up 
    Player goes first in the gameplay

## PLAYER GOALS
    Get close to a total value of 21 than the dealer does
    * Possible Actions:
        HIT(Receive another card)
        STAY(Stop receiving cards)

## Computer
    Dealer HIT for more cards from DECK
    * After player turn:
        If player is under 21, dealer then hits until they either beat the player or the dealer busts

## After Player Turn
    if player keeps hitting goes over 21, they bust and lost the bet
    the game is then over and dealer collects the money

## Computer sum higher than player sum and still under 21 
    if player is under 21, dealer then hits until they either beat the player or the dealer busts

## Player Wins
    if player is under 21 then hits until they either beat the player or the dealer busts


### SPECIAL RULE
* Face Cards (Jack, Queen, King) count as a value of 10
* Aces can as either 1 or 11 (which ever value is preferable to the player)
'''