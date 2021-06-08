package com.breakfast.main;

/*
 * This class loads the sprites.
 *
 * @author Cameron Teed
 * @version 1.0
 * @since 2021-05-26
 */
import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

/** */
public class Backgrounds extends Canvas {

  /** */
  private static final long serialVersionUID = 1L;
  /** */
  private BufferedImage image = null;
  /** */
  private BufferedImage image2 = null;
  /** */
  private BufferedImage image3 = null;
  /** */
  private final int height;
  /** */
  private final int width;

  /**
   *
   * @param width
   * @param height
   */
  public Backgrounds(final int width, final int height) {
    try {
	image = ImageIO.read( new File(
                "C:/Users/super/git/ICS4U.2020-Final-Project/CameronTeed/"
                	  	 + "Breakfast/Background/background.png"));
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    this.width = width;
    this.height = height;
  }

  /**
   *
   * @param g
   */
  public void loadBackground(final Graphics g) {
    g.drawImage(image, 0, 0, this.width, this.height, null);
    g.drawImage(image, 0, 0, null);
  }
}
