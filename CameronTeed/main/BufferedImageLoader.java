package com.breakfast.main;

/*
 * This class loads the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;

/** Buffered image loader class. */
public class BufferedImageLoader {

  /** Initializes the buffered image. */
  private BufferedImage image;

  /**
   * Loads the buffered image.
   *
   * @param path
   * @return image
   */
  public BufferedImage loadImage(final String path) {
    try {
      image = ImageIO.read(getClass().getResource(path));
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    return image;
  }
}
