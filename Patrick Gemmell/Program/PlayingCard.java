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
  /**
  * the number three.
  */
  public static final int THREE = 3;
  /**
  * the number four.
  */
  public static final int FOUR = 4;
  /**
  * the number five.
  */
  public static final int FIVE = 5;
  /**
  * the number six.
  */
  public static final int SIX = 6;
  /**
  * the number seven.
  */
  public static final int SEVEN = 7;
   /**
  * the number eight.
  */
  public static final int EIGHT = 8;
  /**
  * the number nine.
  */
  public static final int NINE = 9;
  /**
  * the number ten.
  */
  public static final int TEN = 10;
  /**
  * the number eleven.
  */
  public static final int ELEVEN = 11;
  // Initializing fields
  /**
   * variable card face.
   */
  private String cardFace;
  /**
   * variable card suit.
   */
  private String cardSuit;
  /**
   * variable card value.
   */
  private int cardValue;

  /**
   * Setting field values with a constructor.
   * @param cardIdentity
   * @param handValue
   */
  public PlayingCard(final String cardIdentity, final int handValue) {
    // Checking if the card face passed in is valid
    if (!isCardValid(cardIdentity)) {
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
   * @param cardString
   * @return
   * retunrs values
   */
  private Boolean isCardValid(final String cardString) {
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
   * @param cardImage
   * @return
   * returns suit
   */
  private String setSuit(final String cardImage) {
    // Finding the suit of the card
    String suit = cardImage.substring(cardImage.length() - 1);

    // Setting the card's suit as the suit found
    return suit;
  }

  /**
   * This method finds the value of the card.
   * @param cardPicture
   * @param aceValue
   * @return
   * returns case
   */
  private int setValue(final String cardPicture, final int aceValue) {
    // Determining the first character to help with finding the value
    char cardNumber = cardPicture.charAt(0);

    // If statement that determines the value of the card
    if (cardNumber == '2') {
      // Returning the card value as 2
      return 2;

    } else if (cardNumber == '3') {
      // Returning the card value as 3
      return THREE;

    } else if (cardNumber == '4') {
      // Returning the card value as 4
      return FOUR;

    } else if (cardNumber == '5') {
      // Returning the card value as 5
      return FIVE;

    } else if (cardNumber == '6') {
      // Returning the card value as 6
      return SIX;

    } else if (cardNumber == '7') {
      // Returning the card value as 7
      return SEVEN;

    } else if (cardNumber == '8') {
      // Returning the card value as 8
      return EIGHT;

    } else if (cardNumber == '9') {
      // Returning the card value as 9
      return NINE;

    } else if (cardNumber == '1' || cardNumber == 'J' || cardNumber == 'Q'
               || cardNumber == 'K') {
      // Returning the value of 10 based on the 10 and face cards
      return TEN;

    } else if (cardNumber == 'A') {
      // Checking to see if the ace should be equal to 1 or 11
      if (aceValue >= ELEVEN) {
        // Returning the ace value as 1 based on a card hand more than 11
        return 1;
      } else {
        // Returning the ace value as 11 based on a card hand less than 11
        return ELEVEN;
      }

    } else {
      // Returning -1 to show that an error occurred
      return -1;
    }
  }

  /**
   * This getter shows the user the card face.
   * @return
   * returns card face
   */
  public String getCardFace() {
    // Returning the card face
    return this.cardFace;
  }

  /**
   * This getter shows the user the card value.
   * @return
   * returns card value
   */
  public int getCardValue() {
    // Returning the card value
    return this.cardValue;
  }

  /**
   * This getter shows the suit of the card.
   * @return
   * returns card suit
   */
  public String getCardSuit() {
    // Returning the card suit
    return this.cardSuit;
  }
}
