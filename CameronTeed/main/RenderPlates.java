package com.breakfast.main;
/*
 * This class renders the eggs.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Graphics;

/** */
public class RenderPlates {
 
    /** Initializes the y coord. */
    private int[] panCounter = new int[3];
    /** Initializes the y coord. */
    private int[] baconCounter = new int[3];
    /** Initializes the y coord. */
    private int[] eggCounter = new int[3];   

    /**
     * Create the plates for the programe.
     *
     */
    public void createPlates() {
        if (RenderBacon.getBacon() && MoveFood.plate1() && baconCounter[0] != 0 ) {
            baconCounter[0]--;
        } else if (RenderPancakes.getPancakes() && MoveFood.plate1() && panCounter[0] != 0) {
            panCounter[0]--;
        } else if (RenderEggs.getEggs() && MoveFood.plate1() && eggCounter[0] != 0) {
            eggCounter[0]--;
        } else if (panCounter[0] == 0 && eggCounter[0] == 0 && baconCounter[0] == 0) {
            eggCounter[0] = (int) ((Math.random() * (5 - 1)) + 1);
            panCounter[0] = (int) ((Math.random() * (5 - 1)) + 1);
            baconCounter[0] = (int) ((Math.random() * (5 - 1)) + 1);
        }

        if (RenderPancakes.getPancakes() && MoveFood.plate2() && panCounter[1] != 0) {
            panCounter[1]--;
        } else if (RenderBacon.getBacon() && MoveFood.plate2() && baconCounter[1] != 0) {
            baconCounter[1]--;
        } else if (RenderEggs.getEggs() && MoveFood.plate2() && eggCounter[1] != 0) {
            eggCounter[1]--;
        } else if (panCounter[1] == 0 && eggCounter[1] == 0 && baconCounter[1] == 0) {
            eggCounter[1] = (int) ((Math.random() * (5 - 1)) + 1);
            panCounter[1] = (int) ((Math.random() * (5 - 1)) + 1);
            baconCounter[1] = (int) ((Math.random() * (5 - 1)) + 1);
        }

        if (RenderPancakes.getPancakes() && MoveFood.plate3() && panCounter[2] != 0) {
            panCounter[2]--;
        } else if (RenderEggs.getEggs() && MoveFood.plate3() && eggCounter[2] != 0) {
            eggCounter[2]--;
        } else if (RenderBacon.getBacon() && MoveFood.plate3() && baconCounter[2] != 0) {
            baconCounter[2]--;
        } else if (eggCounter[2] == 0 && baconCounter[2] == 0 && panCounter[2] == 0) {
            eggCounter[2] = (int) ((Math.random() * (5 - 1)) + 1);
            panCounter[2] = (int) ((Math.random() * (5 - 1)) + 1);
            baconCounter[2] = (int) ((Math.random() * (5 - 1)) + 1);
        }

    }

    /** 
     * Renders the plates.
     *
     * @param g2d
     */
    public void renderPlates(Graphics g2d) {
        g2d.drawString("Pancakes: " + panCounter[0], 180, 100);
        g2d.drawString("Eggs: " + eggCounter[0], 180, 115);
        g2d.drawString("Bacon: " + baconCounter[0], 180, 131);

        g2d.drawString("Pancakes: " + panCounter[1], 370, 100);
        g2d.drawString("Eggs: " + eggCounter[1], 370, 115);
        g2d.drawString("Bacon: " + baconCounter[1], 370, 131);

        g2d.drawString("Pancakes: " + panCounter[2], 570, 100);
        g2d.drawString("Eggs: " + eggCounter[2], 570, 115);
        g2d.drawString("Bacon: " + baconCounter[2], 570, 131);
        
    }
}
