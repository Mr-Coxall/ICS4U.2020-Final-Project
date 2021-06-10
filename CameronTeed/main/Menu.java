package com.breakfast.main;
/*
 * This class renders the menu.
 *
 * @author Cameron Teed
 * @version 1.0
 * @since 2021-05-26
 */
import java.awt.Graphics;

/** */
public class Menu extends HitBoxes {

    /** Initializes the x. */
    private final int param1 = 685;
    /** Initializes the y. */
    private final int param2 = 322;
    /** Initializes the width. */
    private final int param3 = 180;
    /** Initializes the height. */
    private final int param4 = 50;
    /** Initializes the width. */
    private final int width = 740;
    /** Initializes the height. */
    private final int height = 550;
    /** Initializes the background. */
    private Backgrounds background = new Backgrounds();

    /**
     * Renders the main menu.
     *
     * @param g
     * @param x
     * @param y
     */
    public void render(final Graphics g, final int x, final int y) {
        background.loadBackground2(g);
        if (isClicked(x, y, param1, param2, param3, param4)) {
            System.out.println("Click");
            g.clearRect(0, 0, width, height);
            Game.State = Game.STATE.GAME;
        }
    }
}
