package com.breakfast.main;

import java.awt.Graphics;
import java.awt.image.BufferedImage;

public class MoveFood {

    /** Initializes the size. */
    private final RenderBacon spatula = new RenderBacon();
    /** Initializes the size. */
    private final Plates plates = new Plates();
    private final int offsetCursory = 200;
    /** Initializes the y coord. */
    private final int offsetCursorx = 440;
    /** Initializes the y coord. */
    private boolean move;

    public void moveSprites(BufferedImage image, final int x, final int y, Graphics g) {
        // System.out.println(x + "," + y);
        if (!spatula.getSpatula() && plates.isHit(x,y)) {
            this.move = true;
        } else if (!spatula.getSpatula() && !plates.isHit(x,y)) {
            g.drawImage(image, x - offsetCursorx, y - offsetCursory, null);
            System.out.println("clicked111113");
            this.move = false;
        }
    }

    public boolean getMove() {
        return move;
    }
}
