package com.breakfast.main;

/*
 * This class runs the game loop and renders the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.MouseInfo;
import java.awt.Point;
import java.awt.PointerInfo;
import java.awt.image.BufferStrategy;

/** Game class. */
public class Game extends Canvas implements Runnable {

  /** SerialVersion UID (Will need for later). */
  private static final long serialVersionUID = 5102725995743094780L;
  /** The size of the GUI. */
  private static final int WIDTH = 740;
  /** Initializes the height. */
  private static final int HEIGHT = 580;
  /** Initializes the threads. */
  private Thread thread;
  /** Tells the programs its not yet running. */
  private boolean running = false;
  /** Initializes the background. */
  private Backgrounds scenes = new Backgrounds();
  /** Initializes the background. */
  private Assets assets = new Assets();
  /** Initializes the tick speed. */
  private final long tickSpeed = 100000;
  /** Initializes the frames. */
  private final double frames2 = 60.0;
  /** Initializes the timer. */
  private final double timerCalc = 1000;
  /** Initializes the x coord. */
  private final int offsetCursory = 200;
  /** Initializes the y coord. */
  private final int offsetCursorx = 440;
  /** Initializes the amount of threads. */
  private final int threads = 3;
  /** Initializes the amount of threads. */
  private HitBoxes boxes = new HitBoxes();
  /** Initializes the egg. */
  private boolean renderEgg = false;
  /** Initializes the egg. */
  private boolean renderEgg2 = false;
  /** Initializes the egg. */
  private boolean renderEgg3 = false;
  /** Initializes the egg. */
  private boolean renderEgg4 = false;
  /** Initializes the X. */
  private final int eggX = 140;
  /** Initializes the Y. */
  private final int eggY = 190;
  /** Initializes the Y. */
  private final int eggY2 = 265;
  /** Initializes the Y. */
  private final int eggY3 = 340;
  /** Initializes the Y. */
  private final int eggY4 = 415;

  /** Constructor. */
  public Game() {
    this.addMouseListener(new MyMouseListener());
    new Window(WIDTH, HEIGHT, "Breakfast: The Game", this);
  }

  /** initializing. */
  public void init() {
    assets.init();
  }

  /** Starts the GUI. */
  public synchronized void start() {
    thread = new Thread(this);
    thread.start();
    running = true;
  }

  /** Stops the GUI. */
  public synchronized void stop() {
    try {
      thread.join();
      running = false;
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  /** This method creates a loop that can run the graphics. */
  @Override
  public void run() {
    long lastTime = System.nanoTime();
    double amountOfTicks = frames2;
    double ns = tickSpeed / amountOfTicks;
    double delta = 0;
    long timer = System.currentTimeMillis();
    int frames = 0;
    // Calls the init function to load the sprites
    init();
    while (running) {
      render();
      long now = System.nanoTime();
      delta += (now - lastTime) / ns;
      lastTime = now;
      while (delta >= 1) {
        tick();
        delta--;
      }
      if (running) {
        render();
        frames++;
      }
      if (System.currentTimeMillis() - timer > timerCalc) {
        timer += timerCalc;
        System.out.println("FPS: " + frames);
      }
    }
    stop();
  }

  /** This method will set the tick speed. */
  public void tick() {

  }

  /** This method pains some graphics.
  *
  * @param g
  */
  public void renderEgg(final Graphics g) {
      if (renderEgg) {
          g.drawImage(assets.getImage5(), eggX, eggY, null);
      }
      if (renderEgg2) {
          g.drawImage(assets.getImage5(), eggX, eggY2, null);
      }
      if (renderEgg3) {
          g.drawImage(assets.getImage5(), eggX, eggY3, null);
      }
      if (renderEgg4) {
          g.drawImage(assets.getImage5(), eggX, eggY4, null);
      }
  }

  /** This method pains some graphics.
   *
   * @param g
   */
  public void rePaint(final Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    // Gets the location of the users cursor to render the following sprites
    PointerInfo a = MouseInfo.getPointerInfo();
    Point b = a.getLocation();
    int y = (int) b.getY();
    int x = (int) b.getX();

    // Checks if user clicked on the hitbox for the egg and loads it
    if (MyMouseListener.isKeyPressed()) {
      g2d.drawImage(assets.getImage2(), x - offsetCursorx,
              y - offsetCursory, null);
    } else if (MyMouseListener.isKeyPressed1()) {
      // Checks if user clicked on the hitbox for the spoon and loads it
      g2d.drawImage(assets.getImage4(), x - offsetCursorx,
              y - offsetCursory, null);
      if (boxes.isClicked(x, y)) {
        renderEgg = true;
      } else if (boxes.isClicked2(x, y)) {
        renderEgg2 = true;
      } else if (boxes.isClicked3(x, y)) {
        renderEgg3 = true;
      } else if (boxes.isClicked4(x, y)) {
        renderEgg4 = true;
      }
    } else if (MyMouseListener.isKeyPressed2()) {
      // Checks if user clicked on the hitbox for the bacon and loads it
      g2d.drawImage(assets.getImage3(), x - offsetCursorx,
              y - offsetCursory, null);
    } else {
      // Checks if user clicked on the hitbox for the spatula and loads it
      g2d.drawImage(assets.getImage(), x - offsetCursorx,
              y - offsetCursory, null);
    }

  }

  /** This method renders the graphics. */
  public void render() {
    BufferStrategy bs = this.getBufferStrategy();
    if (bs == null) {
      this.createBufferStrategy(threads);
      return;
    }

    Graphics g = bs.getDrawGraphics();
    // Renders the background
    scenes.loadBackground(g);
    // Renders the cursors
    rePaint(g);
    renderEgg(g);
    g.dispose();
    bs.show();
  }

  /**
   * Main function.
   *
   * @param args
   */
  public static void main(final String[] args) {
    new Game();
  }
}
