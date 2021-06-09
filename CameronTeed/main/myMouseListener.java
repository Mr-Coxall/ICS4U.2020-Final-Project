package com.breakfast.main;
/*
 * This class listens to user input and creates the hit boxes.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */

// Imports the needed classes
import java.awt.Rectangle;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

/** */
final class MyMouseListener implements MouseListener {

  /** Initializes the variable that stores the key state. */
  private static boolean keyPressed;
  /** Initializes the variable that stores the key state. */
  private static boolean keyPressed1;
  /** Initializes the variable that stores the key state. */
  private static boolean keyPressed2;
  /** Initializes the x coordinent. */
  private final int param1 = 8;
  /** Initializes the x coordinent. */
  private final int param2 = 13;
  /** Initializes the y coordinent. */
  private final int param3 = 174;
  /** Initializes the y coordinent. */
  private final int param4 = 284;
  /** Initializes the y coordinent. */
  private final int param5 = 384;
  /** Initializes the size. */
  private final int param6 = 100;
  /** Initializes the size. */
  private final int param7 = 90;

  MyMouseListener() {
    this.keyPressed = false;
    this.keyPressed1 = false;
    this.keyPressed2 = false;
  }

  @Override
  public void mouseClicked(final MouseEvent e) {

    // Creates the hit boxes for the eggs, bacon, and pancake mix
    Rectangle bounds = new Rectangle(param1, param3, param6, param6);
    Rectangle bounds1 = new Rectangle(param2, param4, param7, param7);
    Rectangle bounds2 = new Rectangle(param2, param5, param6, param6);
    // Checks if the user clicked the hitboxes and returns true
    if (bounds.contains(e.getX(), e.getY())) {
      setKeyPressed(true);
      setKeyPressed2(false);
      setKeyPressed1(false);
    } else if (bounds1.contains(e.getX(), e.getY())) {
      setKeyPressed1(true);
      setKeyPressed(false);
      setKeyPressed2(false);
    } else if (bounds2.contains(e.getX(), e.getY())) {
      setKeyPressed2(true);
      setKeyPressed1(false);
      setKeyPressed(false);
    } else {
      setKeyPressed(false);
      setKeyPressed1(false);
      setKeyPressed2(false);
    }
  }

  @Override
  public void mouseEntered(final MouseEvent e) {

  }

  @Override
  public void mouseExited(final MouseEvent e) {

  }

  @Override
  public void mousePressed(final MouseEvent e) {

  }

  @Override
  public void mouseReleased(final MouseEvent e) {

  }

  /**
  * Getter.
  *
  * @return keyPressed1
  */
  public static boolean isKeyPressed() {
    return keyPressed;
  }

  /**
  * Setter.
  *
  * @param keyState
  */
  public void setKeyPressed(final boolean keyState) {
    keyPressed = keyState;
  }

  /**
  * Getter.
  *
  * @return keyPressed1
  */
  public static boolean isKeyPressed1() {
    return keyPressed1;
  }

  /**
   * Setter.
   *
   * @param keyState1
   */
  public void setKeyPressed1(final boolean keyState1) {
    keyPressed1 = keyState1;
  }

  /**
  * Getter.
  *
  * @return keyPressed2
  */
  public static boolean isKeyPressed2() {
    return keyPressed2;
  }

  /**
  * Setter.
  *
  * @param keyState2
  */
  public void setKeyPressed2(final boolean keyState2) {
    keyPressed2 = keyState2;
  }
}
