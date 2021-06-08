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

public class BufferedImageLoader {

  BufferedImage image;

  public BufferedImage loadImage(String path) {
    try {
      image = ImageIO.read(getClass().getResource(path));
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    return image;
  }
}
