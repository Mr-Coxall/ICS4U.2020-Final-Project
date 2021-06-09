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


    /**
     * 
     * @param x
     * @param y
     * @return
     */
    public boolean isClicked(double x, double y) {
        Rectangle eggBound = new Rectangle(param1, param2, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return(true);
      }
       // System.out.println(x + "," + y);
       return(false);
    }

    /**
     * 
     * @param x
     * @param y
     * @return
     */
    public boolean isClicked2(double x, double y) {
        Rectangle eggBound = new Rectangle(param1, param3, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return(true);
      }
        // System.out.println(x + "," + y);
       return(false);
    }

    /**
     * 
     * @param x
     * @param y
     * @return
     */
    public boolean isClicked3(double x, double y) {
        Rectangle eggBound = new Rectangle(param1, param4, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return(true);
      }
        // System.out.println(x + "," + y);
       return(false);
    }

    /**
     * 
     * @param x
     * @param y
     * @return
     */
    public boolean isClicked4(double x, double y) {
        Rectangle eggBound = new Rectangle(param1, param5, param6, param6);
        if (eggBound.contains(x, y) && MyMouseListener.getState2()) {
            // System.out.println("click");
            return(true);
      }
        // System.out.println(x + "," + y);
       return(false);
    }

}
