package com.breakfast.main;

/*
 * This class renders the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.image.BufferedImage;

public class Assets {
  public static BufferedImage spriteSheet;
  public static BufferedImage spatula, spoon, egg, bacon;

  public static void init() {
    BufferedImageLoader loader = new BufferedImageLoader();
    SpriteLoader ss = new SpriteLoader(loader.loadImage("/pancakes.png"));
    SpriteLoader bs = new SpriteLoader(loader.loadImage("/eggs.png"));

    spatula = ss.grabImage(3, 2, 70, 70);
    spoon = ss.grabImage(3, 1, 70, 70);
    bacon = ss.grabImage(3, 3, 73, 73);
    egg = bs.grabImage(3, 2, 70, 75);
  }
}
