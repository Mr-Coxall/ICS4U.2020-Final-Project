package com.breakfast.main;
/*
 * This class renders the creates the logic for the hitboxes.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Rectangle;

final class HitBoxes {
 // This is the HitBox Class.

    /** Initializes the x coordinent. */
    private final int param1 = 550;
    /** Initializes the x coordinent. */
    private final int param2 = 360;
    /** Initializes the y coordinent. */
    private final int param3 = 435;
    /** Initializes the y coordinent. */
    private final int param4 = 510;
    /** Initializes the y coordinent. */
    private final int param5 = 585;
    /** Initializes the size. */
    private final int param6 = 75;
    /** Initializes the size. */
    private final int param7 = 625;

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param1, param2, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
       // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked2(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param1, param3, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
        // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked3(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param1, param4, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
        // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked4(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param1, param5, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
        // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked5(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param7, param2, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
       // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked6(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param7, param3, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
        // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked7(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param7, param4, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
        // System.out.println(x + "," + y);
       return false;
    }

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isClicked8(final double x, final double y) {
        Rectangle eggBound = new Rectangle(param7, param5, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return true;
      }
        // System.out.println(x + "," + y);
       return false;
    }

}
