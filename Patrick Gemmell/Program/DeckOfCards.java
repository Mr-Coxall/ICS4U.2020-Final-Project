/*
* This class is a deck of cards.
*
* @author  Patrick Gemmell
* @version 1.3
* @since   2021-06-15
*/

import java.util.ArrayList; // Import the ArrayList class
import java.util.Collections; // Import the collections class
import java.util.Random;  // Import the Random class

/**
 * This class creates an object that acts like a deck of cards.
 */
public class DeckOfCards {
  /**
  * the number fifty two.
  */
  public static final int FIFTYTWO = 52;

  // Initializing fields
  /**
   * Setting the array of cards.
   */
  private static String[] possibleCards = {"2♥", "3♥", "4♥", "5♥", "6♥", "7♥",
                                           "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
                                           "A♥", "2♦", "3♦", "4♦", "5♦", "6♦",
                                           "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦",
                                           "K♦", "A♦", "2♣", "3♣", "4♣", "5♣",
                                           "6♣", "7♣", "8♣", "9♣", "10♣", "J♣",
                                           "Q♣", "K♣", "A♣", "2♠", "3♠", "4♠",
                                           "5♠", "6♠", "7♠", "8♠", "9♠", "10♠",
                                           "J♠", "Q♠", "K♠", "A♠"};

  /**
   * Setting field values with a constructor.
   */
  public DeckOfCards() {
    // Setting up the initial deck of cards
    this.possibleCards = shuffleDeck(this.possibleCards);
  }

  /**
   * This getter finds the number of cards in the deck.
   * @return
   * returns possible cards
   */
  public int numberOfCards() {
    // Returning the current size of the deck
    return this.possibleCards.length;
  }

  /**
   * This method shuffles the cards in the deck.
   * @param initialDeck
   * @return
   * returns deck
   */
  private String[] shuffleDeck(final String[] initialDeck) {
    // Setting up a random number generator
    Random randomNumber = new Random();

    // Adding all the card values to an ArrayList
    ArrayList<String> tempList = new ArrayList<String>();
    for (int listCounter = 0; listCounter < this.possibleCards.length - 1;
         listCounter++) {
      tempList.add(this.possibleCards[listCounter]);
    }

    // Shuffling the array
    Collections.shuffle(tempList, randomNumber);

    // Placing the shuffled card list elements back into an array
    for (int shuffle = 0; shuffle < initialDeck.length - 1; shuffle++) {
      initialDeck[shuffle] = tempList.get(shuffle);
    }

    // Shuffling in the final card
    String tempValue = initialDeck[initialDeck.length - 1];
    int randomIndex = randomNumber.nextInt(FIFTYTWO);
    String topCard = initialDeck[randomIndex];
    initialDeck[initialDeck.length - 1] = topCard;
    initialDeck[randomIndex] = tempValue;

    // Returning the shuffled deck of cards
    return initialDeck;
  }

  /**
   * This method draws a card from the deck.
   * @return
   * returns card drawn
   */
  public String drawCard() {
    // Drawing a card from the deck and assigning it a value
    String cardDrawn = this.possibleCards[this.possibleCards.length - 1];

    // Removing the card from the top of the deck
    String[] newDeck = new String[this.possibleCards.length - 1];
    for (int newCounter = 0; newCounter < newDeck.length; newCounter++) {
      newDeck[newCounter] = this.possibleCards[newCounter];
    }
    this.possibleCards = newDeck;

    // Returning the value of the card that was drawn
    return cardDrawn;
  }

  /**
   * This method draws a card from the deck.
   */
  public void recallDeck() {
    // Setting up a brand new full deck of cards
    String[] recalledValues = {"2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥",
                               "10♥", "J♥", "Q♥", "K♥", "A♥", "2♦", "3♦", "4♦",
                               "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦",
                               "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣",
                               "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♠",
                               "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠",
                               "J♠", "Q♠", "K♠", "A♠"};

    // Setting the current deck to be the deck with all its cards
    this.possibleCards = recalledValues;

    // Shuffling the newly recalled deck
    this.possibleCards = shuffleDeck(this.possibleCards);
  }
}
