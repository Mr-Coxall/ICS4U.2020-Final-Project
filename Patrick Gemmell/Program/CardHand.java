/*
* This class is a hand of playing cards.
*
* @author  Patrick Gemmell
* @version 1.3
* @since   2021-06-16
*/

/**
 * This class creates an object that acts like a hand of playing card.
 */
public class CardHand {
  // Initializing fields
  private PlayingCard[] cardsInHand;

  /**
   * Setting field values with a constructor.
   */
  public CardHand() {
    this.cardsInHand = new PlayingCard[6];
  }

  /**
   * This method adds a card to the hand.
   */
  public void addCard(PlayingCard newCard) {
    // Adding the new card to the end of the hand
    for (int addCounter = 0; addCounter < this.cardsInHand.length;
         addCounter++) {
      if (this.cardsInHand[addCounter] == null) {
        this.cardsInHand[addCounter] = newCard;
        break;
      } else {
        continue;
      }
    }
  }

  /**
   * This getter finds and returns the value of a specific card in the hand.
   */
  public int showCardValue(int cardValueIndex) {
    // Returning the value of the card at the index passed in
    return this.cardsInHand[cardValueIndex].getCardValue();
  }

  /**
   * This getter finds and returns the card face of a specific card in the hand.
   */
  public String showCardFace(int cardFaceIndex) {
    // Returning the face of the card at the index passed in
    return this.cardsInHand[cardFaceIndex].getCardFace();
  }

  /**
   * This getter finds and returns the card suit of a specific card in the hand.
   */
  public String showCardSuit(int cardSuitIndex) {
    // Returning the suit of the card at the index passed in
    return this.cardsInHand[cardSuitIndex].getCardSuit();
  }

  /**
   * This method empties the hand of all its cards.
   */
  public void emptyHand() {
    // Setting the player's hand to a new array to clear cards
    this.cardsInHand = new PlayingCard[6];
  }

  /**
   * This method finds and returns the value of the hand.
   */
  public int getHandValue() {
    // Setting up the hand amount variable
    int handValue = 0;

    // Checking the value of each card in the hand
    for (int valueCounter = 0; valueCounter < this.cardsInHand.length;
         valueCounter++) {
      // Checking to see if there is a card in the specified array index
      if (this.cardsInHand[valueCounter] != null) {
        handValue = handValue + this.cardsInHand[valueCounter].getCardValue();
      } else {
        continue;
      }
    }

    // Returning the value of the entire hand
    return handValue;
  }

  /**
   * This method finds and returns the number of cards in the hand.
   */
  public int amountOfCards() {
    // Searching for the amount of cards in a hand
    int handLength = 0;
    for (int cardCounter = 0; cardCounter < this.cardsInHand.length;
         cardCounter++) {
      if (this.cardsInHand[cardCounter] != null) {
        handLength += 1;
      } else {
        continue;
      }
    }

    // Returning the number of cards in the hand
    return handLength;
  }
}