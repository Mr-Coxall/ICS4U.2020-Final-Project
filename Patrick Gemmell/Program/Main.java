/*
* This program is a game of Black Jack for the Java console on AWS Cloud9.
*
* @author  Patrick Gemmell
* @version 2.2
* @since   2021-06-16
*/

import java.util.Scanner;  // Import the Scanner class

/**
 * This class makes use of objects to create a game of black jack.
 */
public final class Main {
  private Main() {
  }
  /**
  * the number five.
  */
  public static final int FIVE = 5;
  /**
  * the number six.
  */
  public static final int SIX = 6;
  /**
  * the number ten.
  */
  public static final int TEN = 10;
  /**
  * the number twenty one.
  */
  public static final int TWENTYONE = 21;
  /**
  * the number seventeen.
  */
  public static final int SEVENTEEN = 17;
  /**
  * the number fifty.
  */
  public static final int FIFTY = 50;
  /**
  * the number one thousand.
  */
  public static final int THOUSAND = 1000;
  /**
  * the number three thousand.
  */
  public static final int THREETHOUSAND = 3000;
  /**
   * This function clears the screen.
   */
  static void clearScreen() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
  }

  /**
   * This function figures out if a player has gone bust.
   * @param bustHand
   * @return
   * returns if bust.
   */
  static Boolean isBust(final CardHand bustHand) {
    // Checking if the player's hand amount is over 21
    if (bustHand.getHandValue() > TWENTYONE) {
      // Returning the player's hand is valid
      return true;
    }
      // Returning the player's hand is valid
      return false;
  }

  /**
   * This function figures out a winner between the player and the dealer.
   * @param playerSet
   * @param dealerSet
   * @return
   * returns the winner.
   */
  static int findWinner(final CardHand playerSet, final CardHand dealerSet) {
    // Checking if the player's hand is higher than the dealer's hand
    if (playerSet.getHandValue() > dealerSet.getHandValue()) {
      return 0;

      // Checking if the dealer's hand is greater than the player's hand
    } else if (playerSet.getHandValue() < dealerSet.getHandValue()) {
      return 1;

      // Returning that there was a tie
    } else {
      return 2;
    }
  }

  /**
   * This function pits the player's hand against the dealer's hand.
   * @param userSet
   * @param cpuSet
   * @param standDeck
   * @param money
   * @return
   * returns money
   */
  static int stand(final CardHand userSet, final CardHand cpuSet,
                   final DeckOfCards standDeck, final int money) {
    int newMoney = 0;
    // Drawing cards for the dealer
    while (cpuSet.getHandValue() < SEVENTEEN) {
      hit(cpuSet, standDeck, cpuSet.amountOfCards());
    }

    try {
      // Printing info about the dealer's hand and the card deck
      System.out.print("\u001B[35m" + "Dealer's Hand" + "\u001B[0m");
      System.out.print("\u001B[35m" + "       Total: "
                       + cpuSet.getHandValue() + "\u001B[0m");
      System.out.println("\u001B[35m" + "       Cards in Deck: "
                         + standDeck.numberOfCards() + "\u001B[0m");

      // Printing out the dealer's final hand
      for (int cpuCounter = 0; cpuCounter < cpuSet.amountOfCards();
           cpuCounter++) {
        System.out.print(cpuSet.showCardFace(cpuCounter));
        if (cpuCounter == cpuSet.amountOfCards() - 1) {
          continue;
        } else {
          System.out.print(" | ");
        }
      }
      System.out.println("");
      System.out.println("");

      // Printing info about the player's hand and how much money they have
      System.out.print("\u001B[36m" + "Player's Hand" + "\u001B[0m");
      System.out.print("\u001B[36m" + "       Total: "
                       + userSet.getHandValue() + "\u001B[0m");
      System.out.println("\u001B[36m" + "       Money: $"
                         + money + "\u001B[0m");

      // Printing out the player's final hand
      for (int userCounter = 0; userCounter < userSet.amountOfCards();
           userCounter++) {
        System.out.print(userSet.showCardFace(userCounter));
        if (userCounter == userSet.amountOfCards() - 1) {
          continue;
        } else {
          System.out.print(" | ");
        }
      }

      // Waiting for two seconds before doing anything else
      Thread.sleep(THREETHOUSAND);

      // Checking to see if the dealer went bust
      if (isBust(cpuSet)) {
        // Returning that the dealer went bust and awarding money accordingly
        System.out.println("");
        System.out.println("");
        System.out.println("\u001B[32m"
                           + "Dealer Went Bust. You Won! You gained $10."
                           + "\u001B[0m");
        Thread.sleep(THREETHOUSAND);
        newMoney = money + TEN;
        return newMoney;
      } else {
        // Figuring out which player won the game
        int winValue = findWinner(userSet, cpuSet);

        // Printing out the outcome of the round and awarding money accordingly
        switch (winValue) {
          case 0:
            // Case when the player wins
            System.out.println("");
            System.out.println("");
            System.out.println("\u001B[32m" + "You Won! You gained $10."
                               + "\u001B[0m");
            newMoney = money + TEN;
            break;

          case 1:
            // Case when the dealer wins
            System.out.println("");
            System.out.println("");
            System.out.println("\u001B[31m" + "You Lost! You lost $10."
                               + "\u001B[0m");
            newMoney = money - TEN;
            break;

          case 2:
            // Case when a tie occurs
            System.out.println("");
            System.out.println("");
            System.out.println("\u001B[33m"
                               + "You Tied! You keep your current money."
                               + "\u001B[0m");
            break;

          default:
            // No winner was determined
            System.out.println("");
            System.out.println("");
            System.out.println("Unable to determine winner.");
            break;
        }
      }

      // Waiting for three seconds before doing anything else
      Thread.sleep(THREETHOUSAND);

      // Catching any errors that occurred
    } catch (InterruptedException e) {
      System.out.println("ERROR: Unable to complete stand");
    }

    // Returning the player's new amount of money
    return money;
  }

  /**
   * This function allows a player to draw a card.
   * @param drawHand
   * @param drawDeck
   * @param handSize
   */
  static void hit(final CardHand drawHand,
                      final DeckOfCards drawDeck, final int handSize) {
    // Checking if the hand size is too large to draw a card
    if (handSize > SIX) {
      // Returning the current hand
      return;

    } else {
      // Drawing a new card
      PlayingCard newCard = new PlayingCard(drawDeck.drawCard(),
                                            drawHand.getHandValue());

      // Adding the new card to the hand
      drawHand.addCard(newCard);

      // Returning the card hand
      return;
    }
  }

  /**
   * This function prints a help screen for the user.
   */
  static void helpScreen() {
    // Creating a scanner to receive the input to end the help screen
    final Scanner helpInput = new Scanner(System.in);

    // Clearing the screen
    clearScreen();

    // Printing text that helps the player understand how the game works
    System.out.println("Rules:");
    System.out.println("-Your goal: get more points than the dealer without "
                       + "going over 21!");
    System.out.println("-Maximum 6 cards each");
    System.out.println("-Type 'Hit' for another card");
    System.out.println("-Type 'Stand' to end your turn and put your hand "
                       + "against the dealer's");
    System.out.println("-Type 'CashOut' to quit early with the money you have");
    System.out.println("-Aces can be worth 1 or 11 depending on when they are "
                       + "dealt");
    System.out.println("-Face cards are all worth 10");
    System.out.println("-You start with $50 and play until you have $0 or cash "
                       + "out");
    System.out.println("-You gain $10 for a win and lose $10 for a loss");
    System.out.println("-Good luck, have fun!");
    System.out.println("");
    System.out.flush();

    // Receiving user input about ending help screen
    System.out.print("Press ‘ENTER’ when you wish to continue playing: ");
    String endHelpInput = helpInput.nextLine();
  }

  /**
   * This function deals cards to the two players.
   * @param cardDeck
   * @return
   * returns hand list.
   */
  static CardHand[] dealCards(final DeckOfCards cardDeck) {
    // Instantiating card hands for each player
    CardHand userCardHand = new CardHand();
    CardHand cpuCardHand = new CardHand();

    // Drawing the first two cards for the player's and dealer's hand
    PlayingCard userCard1 = new PlayingCard(cardDeck.drawCard(), 0);
    userCardHand.addCard(userCard1);
    PlayingCard cpuCard1 = new PlayingCard(cardDeck.drawCard(), 0);
    cpuCardHand.addCard(cpuCard1);

    // Drawing the second two cards for the player's and dealer's hand
    PlayingCard userCard2 = new PlayingCard(cardDeck.drawCard(),
                                            userCardHand.getHandValue());
    userCardHand.addCard(userCard2);
    PlayingCard cpuCard2 = new PlayingCard(cardDeck.drawCard(),
                                           cpuCardHand.getHandValue());
    cpuCardHand.addCard(cpuCard2);

    // Creating a list to return each hand from the function
    CardHand[] handList = new CardHand[2];

    // Adding the hands to an array to pass out of this function
    handList[0] = userCardHand;
    handList[1] = cpuCardHand;

    // Returning the list with the hands
    return handList;
  }

  /**
   * This function shows the user their stats after the game ends.
   * @param finalMoney
   * @param matchesPlayed
   * @return
   * returns answer
   */
  static Boolean gameOver(final int finalMoney, final int matchesPlayed) {
    // Creating a scanner that accepts input regarding the end of the game
    final Scanner endInput = new Scanner(System.in);

    // Initializing end input string
    String endAnswer = "";

    // Initializing the variable that will be returned
    Boolean mainAnswer = null;

    try {
      // This loop will stay active until a correct input is entered
      while (!endAnswer.equals("YES") || !endAnswer.equals("NO")) {
        // Clearing the screen
        clearScreen();

        // Determining whether the user cashed out or went bankrupt
        if (finalMoney == 0) {
          // Printing that the player went bankrupt
          System.out.println("You Went Bankrupt. Game Over!");
        } else {
          // Printing that the player cashed out
          System.out.println("You Cashed Out. Game Over!");
        }

        // Printing the player's final amount of money
        System.out.println("");
        System.out.println("\u001B[33m" + "Final Money: $" + finalMoney
                           + "\u001B[0m");

        // Printing the amount of rounds played by the player
        System.out.println("");
        System.out.println("\u001B[33m" + "Rounds Played: " + matchesPlayed
                           + "\u001B[0m");

        // Receiving input for the move the player would like to make
        System.out.println("");
        System.out.print("Would you like to play again (Yes/No): ");
        String endAnswerLowerCase = endInput.nextLine();
        endAnswer = endAnswerLowerCase.toUpperCase();

        // Checking to see what input was entered
        if (endAnswer.equals("YES")) {
          // Returning that the user wants to play again
          mainAnswer = true;
          break;

        } else if (endAnswer.equals("NO")) {
          // Returning that the user does not want to play again
          mainAnswer = false;
          break;

        } else {
          // Printing that the input entered was invalid
          System.out.println("");
          System.out.println("Your input is not valid. Try again!");
          Thread.sleep(THREETHOUSAND);
        }
      }

      // Catching any errors that occur
    } catch (InterruptedException e) {
      System.out.println("");
      System.out.println("ERROR: Unable to pause program");
    }

    // Returning the user's answer
    return mainAnswer;
  }
  /**
   * this functions print message.
   * @param msg
   */
  public static void printMessage(final String msg)
                     throws InterruptedException {
    System.out.println("");
    System.out.println(msg);
    Thread.sleep(THREETHOUSAND);
  }
  /**
   * printhands.
   * @param dealerHand
   * @param deck
   * @param playerHand
   * @param playerMoney
   */
  public static void printHands(final CardHand dealerHand,
                                final DeckOfCards deck,
                                final CardHand playerHand,
                                final int playerMoney) {
            // Printing info about the dealer's hand and the card deck
        System.out.print("\u001B[35m" + "Dealer's Hand" + "\u001B[0m");
        System.out.print("\u001B[35m" + "       Total: " + "\u001B[0m");
        // Checking to see if the card displayed is an ace
        if (dealerHand.showCardFace(1).equals("A♥")
            || dealerHand.showCardFace(1).equals("A♦")
            || dealerHand.showCardFace(1).equals("A♣")
            || dealerHand.showCardFace(1).equals("A♠")) {
          System.out.print("\u001B[35m" + "11" + "\u001B[0m");
        } else {
          // Displaying the card face
          System.out.print("\u001B[35m" + dealerHand.showCardValue(1)
                           + "\u001B[0m");
        }
        // Printing the number of cards currently in the deck
        System.out.println("\u001B[35m" + "       Cards in Deck: "
                           + deck.numberOfCards() + "\u001B[0m");
        // Printing the hand of the dealer
        System.out.println("?? | " + dealerHand.showCardFace(1));
        System.out.println("");
        // Printing info about the player's hand and how much money they have
        System.out.print("\u001B[36m" + "Player's Hand" + "\u001B[0m");
        System.out.print("\u001B[36m" + "       Total: "
                         + playerHand.getHandValue() + "\u001B[0m");
        System.out.println("\u001B[36m" + "       Money: $" + playerMoney
                           + "\u001B[0m");
        // Printing the hand of the player
        for (int playerCounter = 0; playerCounter < playerHand.amountOfCards();
             playerCounter++) {
          System.out.print(playerHand.showCardFace(playerCounter));
          if (playerCounter == playerHand.amountOfCards() - 1) {
            continue;
          } else {
            System.out.print(" | ");
          }
        }
        System.out.println("");
        System.out.println("");
  }
  /**
   * This function runs a game of black jack.
   * @param args
   */
  public static void main(final String[] args) {
    try {
      // Creating scanners to accept the starting user input
      final Scanner beginInput = new Scanner(System.in);
      final Scanner gameInput = new Scanner(System.in);
      // Printing title text and input to start the game
      System.out.println("Gemmell's Casino Black Jack!");
      System.out.println("");
      System.out.print("Press 'ENTER' to Play: ");
      String startInput = beginInput.nextLine();
      System.out.println("\n\n");
      // Instantiating a deck of cards
      DeckOfCards deck = new DeckOfCards();
      // Dealing each player a hand of cards
      CardHand[] handInfo = dealCards(deck);
      CardHand playerHand = handInfo[0];
      CardHand dealerHand = handInfo[1];
      // Clearing the screen
      clearScreen();
      // Setting up the player's initial monetary amount
      int playerMoney = FIFTY;
      // Setting up the variable containing the number of rounds played
      int roundsPlayed = 0;
      // Game loop
      while (true) {
        printHands(dealerHand, deck, playerHand, playerMoney);
        // Checking to see if the player went bust
        if (isBust(playerHand)) {
          // Printing that the player went bust and removing appropriate money
          printMessage("\u001B[31m" + "You Went Bust! You lose $10"
                             + "\u001B[0m");
          playerMoney = playerMoney - TEN;
          // Reshuffling the deck
          deck.recallDeck();
          // Dealing each player a new hand
          CardHand[] newHands = dealCards(deck);
          // Giving the players their new hands
          playerHand = newHands[0];
          dealerHand = newHands[1];
          // Printing that the computer is reshuffling the cards
          printMessage("Reshuffling...");
          // Increasing the number of rounds played
          roundsPlayed += 1;
          // Clearing the screen
          clearScreen();
          // Checking if the player went bankrupt
        } else if (playerMoney == 0) {
          // Variable for finding if the player would like to play again
          Boolean bankrupt = gameOver(playerMoney, roundsPlayed);
          // Figuring out whether or not the user wants the game to end
          if (bankrupt) {
            // Printing that the program will start a new game
            printMessage("Please wait while we shuffle a new deck...");
            // Reshuffling the deck
            deck.recallDeck();
            // Dealing each player a new hand
            CardHand[] redealHands = dealCards(deck);
            // Giving the players their new hands
            playerHand = redealHands[0];
            dealerHand = redealHands[1];
            // Setting the rounds played to 0
            roundsPlayed = 0;
            // Setting player money to $50
            playerMoney = FIFTY;
            // Clearing the screen
            clearScreen();
          } else if (!bankrupt) {
            // Printing a farewell message to the user
            printMessage("♠♥♦♣ Thanks for Playing! ♣♦♥♠");
            break;
          }
        } else {
          // Receiving input for the move the player would like to make
          System.out.print("What would you like to do "
                           + "(Hit/Stand/Help/CashOut): ");
          String userInputLowerCase = gameInput.nextLine();
          String userInput = userInputLowerCase.toUpperCase();
          // Checking to see which input was entered
          if (userInput.equals("HELP")) {
            // Calling the help screen function
            helpScreen();
          } else if (userInput.equals("HIT")) {
            // Checking to see if the player can draw another card
            if (playerHand.amountOfCards() > FIVE) {
              // Printing that the user cannot draw anymore cards
              printMessage("You cannot draw anymore cards");
            } else {
              // Drawing a card
              hit(playerHand, deck, playerHand.amountOfCards());
              clearScreen();
            }
          } else if (userInput.equals("STAND")) {
            // Calling the stand function to find a winner
            clearScreen();
            playerMoney = stand(playerHand, dealerHand, deck, playerMoney);
            // Printing that the computer is reshuffling the cards
            printMessage("Reshuffling...");
            // Reshuffling the deck
            deck.recallDeck();
            // Dealing each player a new hand
            CardHand[] newHands = dealCards(deck);
            // Giving the players their new hands
            playerHand = newHands[0];
            dealerHand = newHands[1];
            // Increasing the number of rounds played
            roundsPlayed += 1;
          } else if (userInput.equals("CASHOUT")) {
            // Calling the function that ends the game
            Boolean endGame = gameOver(playerMoney, roundsPlayed);
            // Figuring out whether or not the user wants the game to end
            if (endGame) {
              // Printing that the program will start a new game
              printMessage("Please wait while we shuffle a new deck...");
              // Reshuffling the deck
              deck.recallDeck();
              // Dealing each player a new hand
              CardHand[] redealHands = dealCards(deck);
              // Giving the players their new hands
              playerHand = redealHands[0];
              dealerHand = redealHands[1];
              // Setting the rounds played to 0
              roundsPlayed = 0;
              // Setting player money to $50
              playerMoney = FIFTY;
            } else if (!endGame) {
              // Printing a farewell message to the user
              printMessage("♠♥♦♣ Thanks for Playing! ♣♦♥♠");
              break;
            } else {
              // Printing that an error occurred in determining the choice made
              System.out.println("ERROR: Unable to determine continuation");
              break;
            }
          } else {
            // Printing that the user entered an invalid input
            printMessage("Your input is not valid. Try again!");
          }
          // Clearing the screen again
          clearScreen();
        }
      }
      // Catches and tells the user what error occured
    } catch (NullPointerException e) {
      System.out.println("");
      System.out.println("ERROR: Card could not be created");
    } catch (Exception e) {
      System.out.println("");
      System.out.println("ERROR: Invalid Input");
    }
  }
}
