package com.breakfast.main;
/*
 * This class renders the help menu.
 *
 * @author Cameron Teed
 * @version 1.0
 * @since 2021-05-26
 */
import java.awt.Graphics;

/** */
public class Help extends HitBoxes {

    /** Initializes the x. */
    private final int param1 = 400;
    /** Initializes the y. */
    private final int param2 = 150;
    /** Initializes the width. */
    private final int param3 = 155;
    /** Initializes the height. */
    private final int param4 = 75;
    /** Initializes the width. */
    private final int width = 740;
    /** Initializes the height. */
    private final int height = 550;
    /** Initializes the background. */
    private Backgrounds background = new Backgrounds();

    /**
     * Renders the help menu.
     *
     * @param g
     * @param x
     * @param y
     */
    public void render(final Graphics g, final int x, final int y) {
        background.loadBackground5(g);
        if (isClicked(x, y, param1, param2, param3, param4)) {
            g.clearRect(0, 0, width, height);
            Main.setState(Main.STATE.MENU);
        }
    }
}
