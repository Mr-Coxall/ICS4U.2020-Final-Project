package com.breakfast.main;
/*
 * This class renders the creates the logic for the hitboxes.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Rectangle;

abstract class HitBoxes {
 // This is the HitBox Class.

    /**
     * Checks if the user clicked the egg hitbox.
     *
     * @param x
     * @param y
     * @param param1
     * @param param2
     * @param param3
     * @param param4
     * @return boolean
     */
    public boolean isClicked(final double x, final double y, final int param1,
                        final int param2, final int param3, final int param4) {
        Rectangle eggBound = new Rectangle(param1, param2, param3, param4);
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
     * @param param1
     * @param param2
     * @param param3
     * @param param4
     * @return boolean
     */
    public boolean isClicked2(final double x, final double y, final int param1,
                        final int param2, final int param3, final int param4) {
        Rectangle eggBound = new Rectangle(param1, param2, param3, param4);
        if (eggBound.contains(x, y)) {
            return true;
      }
       // System.out.println(x + "," + y);
       return false;
    }
}
