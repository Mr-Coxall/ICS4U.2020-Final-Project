package com.breakfast.main;

/*
 * This class renders the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.image.BufferedImage;

final class Assets {
  // This is the Asset Class.

  /**
   * Initializing variable.
   */
  private static BufferedImage spatula;
  /**
   * Initializing variable.
   */
  private static BufferedImage spoon;
  /**
   * Initializing variable.
   */
  private static BufferedImage egg;
  /**
   * Initializing variable.
   */
  private static BufferedImage bacon;
  /**
   * Initializing variable.
   */
  private final int imageW = 70;
  /**
   * Initializing variable.
   */
  private final int imageH = 70;
  /**
   * Initializing variable.
   */
  private final int col = 3;
  /**
   * Initializing variable.
   */
  private final int row1 = 2;
  /**
   * Initializing variable.
   */
  private final int row2 = 1;
  /**
   * Initializing variable.
   */
  private final int row3 = 3;
  /**
   * Initializing variable.
   */
  private final int imageBacon = 73;
  /**
   * Initializing variable.
   */
  private final int imageEgg = 75;

  Assets() {

  }

  /**
   * This method initializes the sprites.
   */
  public void init() {
    // This loads the sprites using the buffered image loader
    BufferedImageLoader loader = new BufferedImageLoader();
    SpriteLoader ss = new SpriteLoader(loader.loadImage("/pancakes.png"));
    SpriteLoader bs = new SpriteLoader(loader.loadImage("/eggs.png"));

    // This gets the specific image from the sprite sheet
    spatula = ss.grabImage(col, row1, imageW, imageH);
    spoon = ss.grabImage(col, row2, imageW, imageH);
    bacon = ss.grabImage(col, row3, imageBacon, imageBacon);
    egg = bs.grabImage(col, row1, imageW, imageEgg);
  }

  /**
   * Getter for a sprite.
   * @return spatula
   */
  public BufferedImage getImage() {
      return spatula;
  }

  /**
   * Getter for a sprite.
   * @return spoon
   */
  public BufferedImage getImage2() {
      return spoon;
  }

  /**
   * Getter for a sprite.
   * @return bacon
   */
  public BufferedImage getImage3() {
      return bacon;
  }

  /**
   * Getter for a sprite.
   * @return egg
   */
  public BufferedImage getImage4() {
      return egg;
  }
}