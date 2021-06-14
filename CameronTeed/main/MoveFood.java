package com.breakfast.main;
/*
 * This class renders the eggs.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Graphics;
import java.awt.image.BufferedImage;

/** */
public class MoveFood {

    /** Initializes the size. */
    private final Spatula spatula = new Spatula();
    /** Initializes the size. */
    private final Plates plates = new Plates();
    /** Initializes the size. */
    private final int offsetCursory = 200;
    /** Initializes the y coord. */
    private final int offsetCursorx = 440;
    /** Initializes the y coord. */
    private boolean move;
    /** Initializes the y coord. */
    private static boolean plate1;
    /** Initializes the y coord. */
    private static boolean plate2;
    /** Initializes the y coord. */
    private static boolean plate3;

    /**
     * Constructor.
     */
    MoveFood() {
        plate1 = false;
        plate2 = false;
        plate3 = false;
        this.move = false;
        
    }

    /**
     * Moves the sprites.
     *
     * @param image
     * @param x
     * @param y
     * @param g
     */
    void moveSprites(BufferedImage image, final int x, final int y, Graphics g) {
        if (!spatula.getSpatula() && plates.isHit(x,y)) {
            plate3 = false;
            plate2 = false;
            plate1 = true;
        } else if (!spatula.getSpatula() && plates.isHit2(x,y)) {
            plate3 = false;
            plate2 = true;
            plate1 = false;
        } else if (!spatula.getSpatula() && plates.isHit3(x,y)) {
            plate3 = true;
            plate2 = false;
            plate1 = false;
        } else {
            plate3 = false;
            plate2 = false;
            plate1 = false;
        }
        if (!spatula.getSpatula() && plates.isHit(x,y) || plates.isHit2(x,y) || plates.isHit3(x,y)) {
            this.move = true;
        } else if (!spatula.getSpatula() && !plates.isHit(x,y) || !plates.isHit2(x,y) || !plates.isHit3(x,y)) {
            g.drawImage(image, x - offsetCursorx, y - offsetCursory, null);
            this.move = false;
        }
    }

    /**
     * Gets if it moved.
     *
     * @return move
     */
    public boolean getMove() {
        return move;
    }

    /**
     * Gets if it touched the plate.
     *
     * @return plate1
     */
    public static boolean plate1() {
        return plate1;
    }

    /**
     * Gets if it touched the plate.
     *
     * @return plate2
     */
    public static boolean plate2() {
        return plate2;
    }

    /**
     * Gets if it touched the plate.
     *
     * @return plate3
     */
    public static boolean plate3() {
        return plate3;
    }
}
