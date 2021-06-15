package com.breakfast.main;

import java.awt.Graphics;

public class Spatula {

    /** Initializes the background. */
    private Assets assets = new Assets();
    /** Initializes the x coord. */
    private final int offsetCursory = 200;
    /** Initializes the y coord. */
    private final int offsetCursorx = 440;
    /** Initializes the size. */
    private boolean spatula = false;

    /**
     * Gets what state the spatla is in.
     *
     * @param g2d
     * @param x
     * @param y
     */
    public void getSpatula(final Graphics g2d, final int x, final int y) {
        if (!MyMouseListener.isKeyPressed2()
                && !MyMouseListener.isKeyPressed1()
                && !MyMouseListener.isKeyPressed()) {
            // Checks if user clicked on the hitbox for the spatula and loads it
            g2d.drawImage(assets.getImage(), x - offsetCursorx,
                    y - offsetCursory, null);
            this.spatula = true;
          } else {
              this.spatula = false;
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
