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

class myMouseListener implements MouseListener {

  private static boolean keyPressed = false;
  private static boolean keyPressed1 = false;
  private static boolean keyPressed2 = false;

  @Override
  public void mouseClicked(MouseEvent e) {
    Rectangle bounds = new Rectangle(8, 174, 100, 100);
    Rectangle bounds1 = new Rectangle(13, 284, 90, 90);
    Rectangle bounds2 = new Rectangle(13, 384, 100, 100);
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
  public void mouseEntered(MouseEvent e) {}

  @Override
  public void mouseExited(MouseEvent e) {
    // setKeyPressed(false);
  }

  @Override
  public void mousePressed(MouseEvent e) {}

  @Override
  public void mouseReleased(MouseEvent e) {
    // Rectangle bounds = new Rectangle(8, 174, 100, 100);
    // if (bounds.contains(e.getX(), e.getY())) {
    // setKeyPressed(true);
    // while((bounds.contains(e.getX(), e.getY()))) {
    // cursors.pancakeCursor(true);
    // }
    // System.out.println("click");
    // To realse it they will have to put down more batter, it will come when i do
    // the other function or statmenets.
    // }
    // Rectangle bounds1 = new Rectangle(13, 284, 90, 90);
    // if (bounds1.contains(e.getX(), e.getY())) {
    // cursors.pancakeCursor2(true);
    // System.out.println("click");
    // }
    // Rectangle bounds2 = new Rectangle(13, 384, 100, 100);
    // if (bounds2.contains(e.getX(), e.getY())) {
    // System.out.println("click");
    // }
  }

  public static boolean isKeyPressed() {
    return keyPressed;
  }

  public void setKeyPressed(boolean keyPressed) {
    myMouseListener.keyPressed = keyPressed;
  }

  public static boolean isKeyPressed1() {
    return keyPressed1;
  }

  public void setKeyPressed1(boolean keyPressed1) {
    myMouseListener.keyPressed1 = keyPressed1;
  }

  public static boolean isKeyPressed2() {
    return keyPressed2;
  }

  public void setKeyPressed2(boolean keyPressed) {
    myMouseListener.keyPressed2 = keyPressed;
  }
}
