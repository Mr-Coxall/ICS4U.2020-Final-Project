package com.breakfast.main;

/*
 * This class loads the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.image.BufferedImage;

/** Method loads the sprite sheet. */
public class SpriteLoader {

  /** Initializing the sprite. */
  private BufferedImage sprite;
  /** Initializing the size of the sprites. */
  private final int top = 75;
  /** Initializing the size of the sprites. */
  private final int bot = 73;

  /**
   * Constructor.
   *
   * @param ss
   */
  public SpriteLoader(final BufferedImage ss) {
    this.sprite = ss;
  }

  /**
   * Grabs the image from the sprite sheet.
   *
   * @param col
   * @param row
   * @param width
   * @param height
   * @return img
   */
  public BufferedImage grabImage(final int col, final int row,
	  			 final int width, final int height) {
    BufferedImage img = sprite.getSubimage((row * top) - bot,
	    				   (col * top) - bot, width, height);
    return img;
  }
}
