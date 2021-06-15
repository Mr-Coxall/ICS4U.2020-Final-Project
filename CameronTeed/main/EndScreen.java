package com.breakfast.main;
import java.awt.Font;
/*
 * This renders the end screen.
 *
 * @author Cameron Teed
 * @version 1.0
 * @since 2021-05-26
 */
import java.awt.Graphics;

/** */
public class EndScreen {

    /** Initializes height. */
    private final int x = 430;
    /** Initializes height. */
    private final int y = 182;
    /** Initializes height. */
    private final int font = 30;
    /** Initializes width the background. */
    private Backgrounds background = new Backgrounds();

    /**
     * Renders the end screen.
     *
     * @param g
     */
    public void render(final Graphics g) {
        background.loadBackground4(g);
        Font myFont = new Font("Plain", 1, font);
        g.setFont(myFont);
        g.drawString("" + RenderPlates.getScore(), x, y);
    }
}
