/*
* This program is a game of Black Jack.
*
* @author  Patrick Gemmell
* @version 1.1
* @since   2021-06-13
*/

import java.util.Scanner;  // Import the Scanner class

/**
 * This class makes use of objects to create a game of black jack.
 */
public class Main {
  /**
   * This function clears the screen.
   */
  static void clearScreen() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
  }

  /**
   * This function figures out if a player has gone bust.
   */
  static Boolean isBust(CardHand bustHand) {
    // Checking if the player's hand amount is over 21
    if (bustHand.getHandValue() > 21) {
      // Returning the player's hand is valid
      return true;
    } else {
      // Returning the player's hand is valid
      return false;
    }
  }

  /**
   * This function figures out a winner between the player and the dealer.
   */
  static int findWinner(CardHand playerSet, CardHand dealerSet) {
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
   */
  static int stand(CardHand userSet, CardHand cpuSet, DeckOfCards standDeck,
                   int money) {
    // Drawing cards for the dealer
    while (cpuSet.getHandValue() < 17) {
      cpuSet = hit(cpuSet, standDeck, cpuSet.amountOfCards());
    }

   
     
      // Catching any errors that occurred
    } catch (InterruptedException e) {
      System.out.println("ERROR: Unable to complete stand");
    }

    // Returning the player's new amount of money
    return money;
  }

  /**
   * This function allows a player to draw a card.
   */
  static CardHand hit(CardHand drawHand, DeckOfCards drawDeck, int handSize) {
    // Checking if the hand size is too large to draw a card
    if (handSize > 6) {
      // Returning the current hand
      return drawHand;

    } else {
      // Drawing a new card
      PlayingCard newCard = new PlayingCard(drawDeck.drawCard(),
                                            drawHand.getHandValue());

      // Adding the new card to the hand
      drawHand.addCard(newCard);

      // Returning the card hand
      return drawHand;
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


  public static void main(String[] args) {
    try {
      // Creating scanners to accept the starting user input
      final Scanner beginInput = new Scanner(System.in);
      final Scanner gameInput = new Scanner(System.in);

      // Printing title text
      System.out.println("Gemmell Casinos BlackJack");
      System.out.println("");

      // Input that starts the game
      System.out.print("Press 'ENTER' to Play: ");
      String startInput = beginInput.nextLine();
      System.out.println("");
      System.out.println("");

      // Instantiating a deck of cards
      DeckOfCards deck = new DeckOfCards();

      // Dealing each player a hand of cards
      CardHand[] handInfo = dealCards(deck);
      CardHand playerHand = handInfo[0];
      CardHand dealerHand = handInfo[1];

      // Clearing the screen
      clearScreen();

      // Setting up the player's initial monetary amount
      int playerMoney = 50;

      // Setting up the variable containing the number of rounds played
      int roundsPlayed = 0;

      // Game loop
      while (true) {
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

        // Checking to see if the player went bust
        if (isBust(playerHand)) {
          // Printing that the player went bust and removing appropriate money
          System.out.println("\u001B[31m" + "You Went Bust! You lose $10"
                             + "\u001B[0m");
          playerMoney = playerMoney - 10;
          Thread.sleep(3000);

          // Reshuffling the deck
          deck.recallDeck();

          // Dealing each player a new hand
          CardHand[] newHands = dealCards(deck);

          // Giving the players their new hands
          playerHand = newHands[0];
          dealerHand = newHands[1];

          // Printing that the computer is reshuffling the cards
          System.out.println("");
          System.out.println("Reshuffling...");
          Thread.sleep(1000);

          // Increasing the number of rounds played
          roundsPlayed += 1;

          // Clearing the screen
          clearScreen();

          // Checking if the player went bankrupt
        } else if (playerMoney == 0) {
          // Variable for finding if the player would like to play again
          Boolean bankrupt = gameOver(playerMoney, roundsPlayed);

          // Figuring out whether or not the user wants the game to end
          if (bankrupt == true) {
            // Printing that the program will start a new game
            System.out.println("");
            System.out.println("Please wait while we shuffle a new deck...");
            Thread.sleep(3000);

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
            playerMoney = 50;

            // Clearing the screen
            clearScreen();

          } else if (bankrupt == false) {
            // Printing a farewell message to the user
            System.out.println("");
            System.out.println("♠♥♦♣ Thanks for Playing! ♣♦♥♠");
            Thread.sleep(3000);
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
            if (playerHand.amountOfCards() > 5) {
              // Printing that the user cannot draw anymore cards
              System.out.println("");
              System.out.println("You cannot draw anymore cards");
              Thread.sleep(3000);
            } else {
              // Drawing a card
              playerHand = hit(playerHand, deck, playerHand.amountOfCards());
              clearScreen();
            }

          } else if (userInput.equals("STAND")) {
            // Calling the stand function to find a winner
            clearScreen();
            playerMoney = stand(playerHand, dealerHand, deck, playerMoney);

            // Printing that the computer is reshuffling the cards
            System.out.println("");
            System.out.println("Reshuffling...");
            Thread.sleep(1000);

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
            if (endGame == true) {
              // Printing that the program will start a new game
              System.out.println("");
              System.out.println("Please wait while we shuffle a new deck...");
              Thread.sleep(3000);

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
              playerMoney = 50;

            } else if (endGame == false) {
              // Printing a farewell message to the user
              System.out.println("");
              System.out.println("♠♥♦♣ Thanks for Playing! ♣♦♥♠");
              Thread.sleep(3000);
              break;

            } else {
              // Printing that an error occurred in determining the choice made
              System.out.println("ERROR: Unable to determine continuation");
              break;
            }

          } else {
            // Printing that the user entered an invalid input
            System.out.println("");
            System.out.println("Your input is not valid. Try again!");
            Thread.sleep(3000);
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