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

/** */
public class SpriteSheet {

  /**
   * Loads the sprite sheet.
   *
   * @param path
   */
  public SpriteSheet(final String path) {
    BufferedImage image = null;
    try {
      image = ImageIO.read(SpriteSheet.class.getResourceAsStream(path));
    } catch (IOException e) {
      e.printStackTrace();
    }

    if (image == null) {
      return;
    }
  }
}
