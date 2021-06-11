package com.breakfast.main;
/*
 * This class renders the eggs.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Graphics;

/** */
public class RenderBacon extends HitBoxes {

    /** Initializes the background. */
    private Assets assets = new Assets();
    /** Initializes the x coord. */
    private final int offsetCursory = 200;
    /** Initializes the y coord. */
    private final int offsetCursorx = 440;
    /** Initializes the egg. */
    private boolean renderEgg = false;
    /** Initializes the egg. */
    private boolean renderEgg2 = false;
    /** Initializes the egg. */
    private boolean renderEgg3 = false;
    /** Initializes the egg. */
    private boolean renderEgg4 = false;
    /** Initializes the egg. */
    private boolean renderEgg5 = false;
    /** Initializes the egg. */
    private boolean renderEgg6 = false;
    /** Initializes the egg. */
    private boolean renderEgg7 = false;
    /** Initializes the egg. */
    private boolean renderEgg8 = false;
    /** Initializes the X. */
    private final int eggX = 320;
    /** Initializes the Y. */
    private final int eggY = 190;
    /** Initializes the Y. */
    private final int eggY2 = 225;
    /** Initializes the Y. */
    private final int eggY3 = 260;
    /** Initializes the Y. */
    private final int eggY4 = 295;
    /** Initializes the Y. */
    private final int eggY6 = 330;
    /** Initializes the Y. */
    private final int eggY7 = 365;
    /** Initializes the Y. */
    private final int eggY8 = 400;
    /** Initializes the Y. */
    private final int eggY9 = 435;
    /** Initializes the x coordinent. */
    private final int param1 = 720;
    /** Initializes the x coordinent. */
    private final int param2 = 360;
    /** Initializes the y coordinent. */
    private final int param3 = 395;
    /** Initializes the y coordinent. */
    private final int param4 = 430;
    /** Initializes the y coordinent. */
    private final int param5 = 465;
    /** Initializes the y coordinent. */
    private final int param6 = 500;
    /** Initializes the y coordinent. */
    private final int param7 = 535;
    /** Initializes the y coordinent. */
    private final int param8 = 565;
    /** Initializes the y coordinent. */
    private final int param9 = 600;
    /** Initializes the size. */
    private final int param10 = 100;
    /** Initializes the size. */
    private final int param11 = 45;
    /** Initializes the size. */
    private final int cookTime = 12000;
    /** Initializes the size. */
    private final int array3 = 3;
    /** Initializes the size. */
    private final int array4 = 4;
    /** Initializes the size. */
    private final int array5 = 5;
    /** Initializes the size. */
    private final int array6 = 6;
    /** Initializes the size. */
    private final int array7 = 7;
    /** Initializes the size. */
    private final int array8 = 8;
    /** Initializes the size. */
    private final long[] timer = new long[array8];
    /** Initializes the size. */
    private boolean spatula = false;

    /**
     * Creates the logic to render the bacon.
     *
     * @param x
     * @param y
     * @param g2d
     */
    public void baconLogic(final int x, final int y, final Graphics g2d) {
        if (MyMouseListener.isKeyPressed2()) {
          // Checks if user clicked on the hitbox for the spoon and loads it
          g2d.drawImage(assets.getImage3(), x - offsetCursorx,
                  y - offsetCursory, null);
          System.out.println(x + ", " + y);
          if (isClicked(x, y, param1, param2, param10, param11)) {
            renderEgg = true;
            timer[0] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param3, param10, param11)) {
            renderEgg2 = true;
            timer[1] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param4, param10, param11)) {
            renderEgg3 = true;
            timer[2] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param5, param10, param11)) {
            renderEgg4 = true;
            timer[array3] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param6, param10, param11)) {
            renderEgg5 = true;
            timer[array4] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param7, param10, param11)) {
            renderEgg6 = true;
            timer[array5] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param8, param10, param11)) {
            renderEgg7 = true;
            timer[array6] = System.currentTimeMillis();
          } else if (isClicked(x, y, param1, param9, param10, param11)) {
            renderEgg8 = true;
            timer[array7] = System.currentTimeMillis();
          }
        } else if (!MyMouseListener.isKeyPressed2()
                && !MyMouseListener.isKeyPressed1()
                && !MyMouseListener.isKeyPressed()) {
            // Checks if user clicked on the hitbox for the spatula and loads it
            g2d.drawImage(assets.getImage(), x - offsetCursorx,
                    y - offsetCursory, null);
            spatula = true;
          }
    }

    /**
    * This method pains some graphics.
    *
    * @param g
    */
    public void putBacon(final Graphics g) {

        if (renderEgg && System.currentTimeMillis() - timer[0] >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY, null);
        } else if (renderEgg) {
            g.drawImage(assets.getImage6(), eggX, eggY, null);
        }
        if (renderEgg2 && System.currentTimeMillis() - timer[1] >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY2, null);
        } else if (renderEgg2) {
            g.drawImage(assets.getImage6(), eggX, eggY2, null);
        }
        if (renderEgg3 && System.currentTimeMillis() - timer[2] >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY3, null);
        } else if (renderEgg3) {
            g.drawImage(assets.getImage6(), eggX, eggY3, null);
        }
        if (renderEgg4 && System.currentTimeMillis() - timer[array3]
                                                        >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY4, null);
        } else if (renderEgg4) {
            g.drawImage(assets.getImage6(), eggX, eggY4, null);
        }
        if (renderEgg5 && System.currentTimeMillis() - timer[array4]
                                                        >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY6, null);
        } else if (renderEgg5) {
            g.drawImage(assets.getImage6(), eggX, eggY6, null);
        }
        if (renderEgg6 && System.currentTimeMillis() - timer[array5]
                                                        >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY7, null);
        } else if (renderEgg6) {
            g.drawImage(assets.getImage6(), eggX, eggY7, null);
        }
        if (renderEgg7 && System.currentTimeMillis() - timer[array6]
                                                        >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY8, null);
        } else if (renderEgg7) {
            g.drawImage(assets.getImage6(), eggX, eggY8, null);
        }
        if (renderEgg8 && System.currentTimeMillis() - timer[array7]
                                                        >= cookTime) {
            g.drawImage(assets.getImage9(), eggX, eggY9, null);
        } else if (renderEgg8) {
            g.drawImage(assets.getImage6(), eggX, eggY9, null);
        }
    }

    /**
     * This returns the state of the spatula.
     *
     * @return spatula
     */
    boolean getSpatula() {
        return spatula;
    }
}
