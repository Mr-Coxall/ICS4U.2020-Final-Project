package com.breakfast.main;
/*
 * This class renders the creates the logic for the hitboxes.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Rectangle;

import com.breakfast.main.Game.STATE;

abstract class HitBoxes {
 // This is the HitBox Class.

    /** Initializes the size. */
    private AudioFilePlayer music = new AudioFilePlayer();
    /** Initializes the size. */
    private int clickCount = 0;

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
            if (clickCount == 0 && MyMouseListener.getState2()
                                && Game.getState() == STATE.GAME) {
                music.load2("C:\\Users\\super\\git\\ICS4U.2020-Final-Project\\"
                                        + "\\CameronTeed\\Breakfast\\Musi"
                                        + "c\\Sizzling-sound-effect.wav");
                clickCount++;
            }
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
    public boolean isClicked3(final double x, final double y, final int param1,
                        final int param2, final int param3, final int param4) {
        Rectangle eggBound = new Rectangle(param1, param2, param3, param4);
        if (eggBound.contains(x, y) && MyMouseListener.getState4()) {
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
    public boolean isClicked4(final double x, final double y, final int param1,
                        final int param2, final int param3, final int param4) {
        Rectangle eggBound = new Rectangle(param1, param2, param3, param4);
        if (eggBound.contains(x, y) && MyMouseListener.getState()) {
            if (clickCount == 0 && MyMouseListener.getState4()
                    && Game.getState() == STATE.GAME) {
                music.load2("C:\\Users\\super\\git\\ICS4U.2020-Final-Project\\"
                                    + "\\CameronTeed\\Breakfast\\Music"
                                    + "\\Sizzling-sound-effect.wav");
                clickCount++;
            }
            return true;
      }
       // System.out.println(x + "," + y);
       return false;
    }
}
