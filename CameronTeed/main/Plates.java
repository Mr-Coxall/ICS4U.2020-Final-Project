package com.breakfast.main;
/*
 * This class renders the eggs.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */

public class Plates extends HitBoxes {

    /** */
    private final int param1 = 514;
    /** */
    private final int param2 = 190;
    /** */
    private final int param3 = 175;
    /** */
    private final int param4 = 150;
    /** */
    private final int param5 = 689;
    /** */
    private final int param6 = 864;

    /**
     * Checks if hit.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isHit(final int x, final int y) {
        return (isClicked(x, y, param1, param2, param3, param4));
    }

    /**
     * Checks if hit.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isHit2(final int x, final int y) {
        return (isClicked(x, y, param5, param2, param3, param4));
    }

    /**
     * Checks if hit.
     *
     * @param x
     * @param y
     * @return boolean
     */
    public boolean isHit3(final int x, final int y) {
        return (isClicked(x, y, param6, param2, param3, param4));
    }
}
