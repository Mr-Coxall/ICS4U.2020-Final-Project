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

  /** Creates serial id. */
  private static final long serialVersionUID = 1L;
  /** Initializing the buffered image. */
  private BufferedImage image = null;
  /** Initializing the buffered image. */
  private BufferedImage image2 = null;
  /** Initializing the buffered image. */
  private BufferedImage image3 = null;
  /** Initializing the buffered image. */
  private BufferedImage image4 = null;
  /** Initializing the buffered image. */
  private BufferedImage image5 = null;

  /**
   * This method loads the background.
   *
   */
  public Backgrounds() {
    try {
      image = ImageIO.read(new File("C:/Users/super/git/ICS4U.2020-Final"
              + "-Project/CameronTeed/Breakfast/Background/background.png"));
      image2 = ImageIO.read(new File("C:/Users/super/git/ICS4U.2020-Final-Pro"
              + "ject/CameronTeed/Breakfast/Background/brunch.jpg"));
      image3 = ImageIO.read(new File("C:/Users/super/git/ICS4U.2020-Final-"
              + "Project/CameronTeed/Breakfast/Background/donut.jpg"));
      image4 = ImageIO.read(new File("C:/Users/super/git/ICS4U.2020-Final-"
              + "Project/CameronTeed/Breakfast/Background/endScreen.jpg"));
      image5 = ImageIO.read(new File("C:/Users/super/git/ICS4U.2020-Final-Pro"
                  + "ject/CameronTeed/Breakfast/Background/HelpScreen.jpg"));
    } catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }

  /**
   * This method renders the background.
   *
   * @param g
   */
  public void loadBackground(final Graphics g) {
    g.drawImage(image, 0, 0, null);
  }

  /**
   * This method renders the background.
   *
   * @param g
   */
  public void loadBackground2(final Graphics g) {
    g.drawImage(image2, 0, 0, null);
  }

  /**
   * This method renders the background.
   *
   * @param g
   */
  public void loadBackground3(final Graphics g) {
    g.drawImage(image3, 0, 0, null);
  }

  /**
   * This method renders the background.
   *
   * @param g
   */
  public void loadBackground4(final Graphics g) {
    g.drawImage(image4, 0, 0, null);
  }

  /**
   * This method renders the background.
   *
   * @param g
   */
  public void loadBackground5(final Graphics g) {
    g.drawImage(image5, 0, 0, null);
  }
}
