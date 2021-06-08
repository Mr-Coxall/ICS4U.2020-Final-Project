package com.breakfast.main;

/*
 * This class loads the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.image.BufferedImage;

/** */
public class SpriteLoader {

  /** */
  private BufferedImage sprite;
  /** */
  private final int top = 75;
  /** */
  private final int bot = 73;

  /** */
  public SpriteLoader(final BufferedImage ss) {
    this.sprite = ss;
  }

  /**
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
