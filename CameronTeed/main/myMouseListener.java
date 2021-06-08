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
final class myMouseListener implements MouseListener {

  /** */
  private static boolean keyPressed = false;
  /** */
  private static boolean keyPressed1 = false;
  /** */
  private static boolean keyPressed2 = false;
  /** */
  private final int param1 = 8;
  /** */
  private final int param2 = 13;
  /** */
  private final int param3 = 174;
  /** */
  private final int param4 = 284;
  /** */
  private final int param5 = 384;
  /** */
  private final int param6 = 100;
  /** */
  private final int param7 = 90;

  @Override
  public void mouseClicked(final MouseEvent e) {

    Rectangle bounds = new Rectangle(param1, param3, param6, param6);
    Rectangle bounds1 = new Rectangle(param2, param4, param7, param7);
    Rectangle bounds2 = new Rectangle(param2, param5, param6, param6);
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
  *
  * @return keyPressed1
  */
  public static boolean isKeyPressed() {
    return keyPressed;
  }

  /**
  *
  * @param keyPressed
  */
  public void setKeyPressed(final boolean keyPressed1) {
    myMouseListener.keyPressed = keyPressed1;
  }

  /**
  *
  * @return keyPressed1
  */
  public static boolean isKeyPressed1() {
    return keyPressed1;
  }

  /**
   *
   * @param keyPressed1
   */
  public void setKeyPressed1(final boolean keyPressed) {
    myMouseListener.keyPressed1 = keyPressed;
  }

  /**
  *
  * @return keyPressed2
  */
  public static boolean isKeyPressed2() {
    return keyPressed2;
  }

  /**
  *
  * @param keyPressed2
  */
  public void setKeyPressed2(final boolean keyPressed) {
    myMouseListener.keyPressed2 = keyPressed;
  }
}
