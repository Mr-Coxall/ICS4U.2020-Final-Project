package com.breakfast.main;
import java.awt.Font;
/*
 * This renders the splash screen.
 *
 * @author Cameron Teed
 * @version 1.0
 * @since 2021-05-26
 */
import java.awt.Graphics;

/** */
public class EndScreen {

    /** Initializes width. */
    private final int width = 740;
    /** Initializes height. */
    private final int height = 550;
    /** Initializes height. */
    private final int x = 430;
    /** Initializes height. */
    private final int y = 182;
    /** Initializes height. */
    private final int font = 30;
    /** Initializes width the background. */
    private Backgrounds background = new Backgrounds();

    /**
     * Renders the splash screen.
     *
     * @param g
     */
    public void render(final Graphics g) {
        background.loadBackground4(g);
        Font myFont = new Font ("Plain", 1, font);
        g.setFont(myFont);
        g.drawString("" + RenderPlates.getScore(), x, y);
    }

    /**
     * Clears the splash screen and sets the game state to the menu.
     *
     * @param g
     */
    public void clearSplash(final Graphics g) {
        g.clearRect(0, 0, width, height);
        Game.setState(Game.STATE.MENU);
    }
}
