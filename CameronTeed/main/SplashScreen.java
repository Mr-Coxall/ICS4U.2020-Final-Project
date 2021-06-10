package com.breakfast.main;
/*
 * This renders the splash screen.
 *
 * @author Cameron Teed
 * @version 1.0
 * @since 2021-05-26
 */
import java.awt.Graphics;

/** */
public class SplashScreen {

    /** Initializes width. */
    private final int width = 740;
    /** Initializes height. */
    private final int height = 550;
    /** Initializes width the background. */
    private Backgrounds background = new Backgrounds();

    /**
     * Renders the splash screen
     *
     * @param g
     */
    public void render(final Graphics g) {
        background.loadBackground3(g);
    }

    /**
     * Clears the splash screen and sets the game state to the menu.
     *
     * @param g
     */
    public void clearSplash(final Graphics g) {
        g.clearRect(0, 0, width, height);
        Game.State = Game.STATE.MENU;
    }
}
