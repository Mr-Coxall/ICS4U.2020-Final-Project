/*
* This class is a playing card.
*
* @author  Patrick Gemmell
* @version 1.7
* @since   2021-06-17
*/

/**
 * This class creates an object that acts like a playing card.
 */
public class PlayingCard {
  // Initializing fields
  private String cardFace;
  private String cardSuit;
  private int cardValue;

  /**
   * Setting field values with a constructor.
   */
  public PlayingCard(String cardIdentity, int handValue) {
    // Checking if the card face passed in is valid
    if (isCardValid(cardIdentity) == false) {
      // Throwing an error that the card could not be created
      throw null;
    } else {
      // Setting the properties of the fields
      this.cardFace = cardIdentity;
      this.cardSuit = setSuit(cardFace);
      this.cardValue = setValue(cardFace, handValue);
    }
  }

  /**
   * This method figures out if a card can exist according to the face value the
   * user passed in.
   */
  private Boolean isCardValid(String cardString) {
    // Initializing a list of possible card faces
    String[] possibleValues = {"2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥",
                               "10♥", "J♥", "Q♥", "K♥", "A♥", "2♦", "3♦", "4♦",
                               "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦",
                               "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣",
                               "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♠",
                               "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠",
                               "J♠", "Q♠", "K♠", "A♠"};

    // Checking if the card passed in is one of the possible values
    for (int checkCounter = 0; checkCounter < possibleValues.length;
         checkCounter++) {
      if (possibleValues[checkCounter] == cardString) {
        return true;
      } else {
        continue;
      }
    }

    // Returning false should no value be found
    return false;
  }

  /**
   * This method finds the suit of the card.
   */
  private String setSuit(String cardImage) {
    // Finding the suit of the card
    String suit = cardImage.substring(cardImage.length() - 1);

    // Setting the card's suit as the suit found
    return suit;
  }

  /**
   * This method finds the value of the card.
   */
  private int setValue(String cardPicture, int aceValue) {
    // Determining the first character to help with finding the value
    char cardNumber = cardPicture.charAt(0);

    // If statement that determines the value of the card
    if (cardNumber == '2') {
      // Returning the card value as 2
      return 2;

    } else if (cardNumber == '3') {
      // Returning the card value as 3
      return 3;

    } else if (cardNumber == '4') {
      // Returning the card value as 4
      return 4;

    } else if (cardNumber == '5') {
      // Returning the card value as 5
      return 5;

    } else if (cardNumber == '6') {
      // Returning the card value as 6
      return 6;

    } else if (cardNumber == '7') {
      // Returning the card value as 7
      return 7;

    } else if (cardNumber == '8') {
      // Returning the card value as 8
      return 8;

    } else if (cardNumber == '9') {
      // Returning the card value as 9
      return 9;

    } else if (cardNumber == '1' || cardNumber == 'J' || cardNumber == 'Q'
               || cardNumber == 'K') {
      // Returning the value of 10 based on the 10 and face cards
      return 10;

    } else if (cardNumber == 'A') {
      // Checking to see if the ace should be equal to 1 or 11
      if (aceValue >= 11) {
        // Returning the ace value as 1 based on a card hand more than 11
        return 1;
      } else {
        // Returning the ace value as 11 based on a card hand less than 11
        return 11;
      }

    } else {
      // Returning -1 to show that an error occurred
      return -1;
    }
  }

  /**
   * This getter shows the user the card face.
   */
  public String getCardFace() {
    // Returning the card face
    return this.cardFace;
  }

  /**
   * This getter shows the user the card value.
   */
  public int getCardValue() {
    // Returning the card value
    return this.cardValue;
  }

  /**
   * This getter shows the suit of the card.
   */
  public String getCardSuit() {
    // Returning the card suit
    return this.cardSuit;
  }
}