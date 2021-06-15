package com.breakfast.main;
import java.awt.Font;
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
    /** Initializes the y coord. */
    private static int score;
    /** Initializes the size. */
    private AudioFilePlayer music = new AudioFilePlayer();
    /** Initializes the size. */
    private final int maxParam = 5;
    /** Initializes the size. */
    private final int x = 170;
    /** Initializes the size. */
    private final int x2 = 360;
    /** Initializes the size. */
    private final int x3 = 560;
    /** Initializes the size. */
    private final int y = 100;
    /** Initializes the size. */
    private final int y2 = 115;
    /** Initializes the size. */
    private final int y3 = 131;
    /** Initializes the size. */
    private final int scoreNum = 100;
    /** Initializes the size. */
    private final int font = 15;

    /**
     * Create the plates for the programe.
     *
     */
    public void createPlates() {
        if (RenderBacon.getBacon() && MoveFood.plate1()
                                            && baconCounter[0] != 0) {
            baconCounter[0]--;
            score += scoreNum;
        } else if (RenderPancakes.getPancakes() && MoveFood.plate1()
                                                    && panCounter[0] != 0) {
            panCounter[0]--;
            score += scoreNum;
        } else if (RenderEggs.getEggs() && MoveFood.plate1()
                                                     && eggCounter[0] != 0) {
            eggCounter[0]--;
            score += scoreNum;
        } else if (panCounter[0] == 0 && eggCounter[0]
                                            == 0 && baconCounter[0] == 0) {
            eggCounter[0] = (int) ((Math.random() * (maxParam - 1)) + 1);
            panCounter[0] = (int) ((Math.random() * (maxParam - 1)) + 1);
            baconCounter[0] = (int) ((Math.random() * (maxParam - 1)) + 1);
            score += scoreNum;
            music.load("C:\\Users\\super\\git\\ICS4U.2020-Final-Project\\Cam"
                    + "eronTeed\\Breakfast\\Music\\bell_small_001.wav");
        }

        if (RenderPancakes.getPancakes() && MoveFood.plate2()
                                                    && panCounter[1] != 0) {
            panCounter[1]--;
            score += scoreNum;
        } else if (RenderBacon.getBacon() && MoveFood.plate2()
                                                    && baconCounter[1] != 0) {
            baconCounter[1]--;
            score += scoreNum;
        } else if (RenderEggs.getEggs() && MoveFood.plate2()
                                                      && eggCounter[1] != 0) {
            eggCounter[1]--;
            score += scoreNum;
        } else if (panCounter[1] == 0 && eggCounter[1] == 0
                                                    && baconCounter[1] == 0) {
            eggCounter[1] = (int) ((Math.random() * (maxParam - 1)) + 1);
            panCounter[1] = (int) ((Math.random() * (maxParam - 1)) + 1);
            baconCounter[1] = (int) ((Math.random() * (maxParam - 1)) + 1);
            score += scoreNum;
            music.load("C:\\Users\\super\\git\\ICS4U.2020-Final-Project\\Cam"
                    + "eronTeed\\Breakfast\\Music\\bell_small_001.wav");
        }

        if (RenderPancakes.getPancakes() && MoveFood.plate3()
                                                    && panCounter[2] != 0) {
            panCounter[2]--;
            score += scoreNum;
        } else if (RenderEggs.getEggs() && MoveFood.plate3()
                                                    && eggCounter[2] != 0) {
            eggCounter[2]--;
            score += scoreNum;
        } else if (RenderBacon.getBacon() && MoveFood.plate3()
                                                    && baconCounter[2] != 0) {
            baconCounter[2]--;
            score += scoreNum;
        } else if (eggCounter[2] == 0 && baconCounter[2] == 0
                                                      && panCounter[2] == 0) {
            eggCounter[2] = (int) ((Math.random() * (maxParam - 1)) + 1);
            panCounter[2] = (int) ((Math.random() * (maxParam - 1)) + 1);
            baconCounter[2] = (int) ((Math.random() * (maxParam - 1)) + 1);
            score += scoreNum;
            music.load("C:\\Users\\super\\git\\ICS4U.2020-Final-Project\\Cam"
                    + "eronTeed\\Breakfast\\Music\\bell_small_001.wav");
        }
    }

    /**
     * Renders the plates.
     *
     * @param g2d
     */
    public void renderPlates(final Graphics g2d) {
        Font myFont = new Font ("Plain", 1, font);
        g2d.setFont(myFont);
        g2d.drawString("Pancakes: " + panCounter[0], x, y);
        g2d.drawString("Eggs: " + eggCounter[0], x, y2);
        g2d.drawString("Bacon: " + baconCounter[0], x, y3);

        g2d.drawString("Pancakes: " + panCounter[1], x2, y);
        g2d.drawString("Eggs: " + eggCounter[1], x2, y2);
        g2d.drawString("Bacon: " + baconCounter[1], x2, y3);

        g2d.drawString("Pancakes: " + panCounter[2], x3, y);
        g2d.drawString("Eggs: " + eggCounter[2], x3, y2);
        g2d.drawString("Bacon: " + baconCounter[2], x3, y3);
    }

    /**
     * returns the score.
     *
     * @return score
     */
    public static int getScore() {
        return score;
    }
}
