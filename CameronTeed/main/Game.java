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
  /** Initializes the amount of threads. */
  private final int threads = 3;
  /** Initializes the render eggs. */
  private RenderEggs renderEggs = new RenderEggs();
  /** Initializes the render bacon. */
  private RenderBacon renderBacon = new RenderBacon();
  /** Initializes the render bacon. */
  private RenderPancakes renderPancake = new RenderPancakes();
  /** Initializes enum for the game state. */
  public enum STATE {
      /** Initializes splash screen. */
      SPLASH,
      /** Initializes menu. */
      MENU,
      /** Initializes the game. */
      GAME,
      /** Initializes the end menu. */
      END,
  }
  /** Initializes game state. */
  private static STATE state = STATE.SPLASH;
  /** Initializes the menu. */
  private Menu menu = new Menu();
  /** Initializes the splash screen. */
  private SplashScreen splash = new SplashScreen();
  /** Initializes the timer. */
  private long timer2;
  /** Initializes the timer the splash screen. */
  private final int splashTime = 1800;

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
    timer2 = System.currentTimeMillis();
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
  public void rePaint(final Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    // Gets the location of the users cursor to render the following sprites
    PointerInfo a = MouseInfo.getPointerInfo();
    Point b = a.getLocation();
    int y = (int) b.getY();
    int x = (int) b.getX();

    renderEggs.eggLogic(x, y, g2d);
    renderBacon.baconLogic(x, y, g2d);
    renderPancake.pancakeLogic(x, y, g2d);
  }

  /** This method renders the graphics. */
  public void render() {
    BufferStrategy bs = this.getBufferStrategy();
    if (bs == null) {
      this.createBufferStrategy(threads);
      return;
    }

    Graphics g = bs.getDrawGraphics();
    PointerInfo a = MouseInfo.getPointerInfo();
    Point b = a.getLocation();
    int y = (int) b.getY();
    int x = (int) b.getX();

    if (getState() == STATE.GAME) {
        // Renders the background
        scenes.loadBackground(g);
        // Renders the cursors
        renderEggs.putEgg(g, x ,y);
        renderBacon.putBacon(g);
        renderPancake.putPancake(g);
        rePaint(g);
    } else if (getState() == STATE.MENU) {
        menu.render(g, x, y);
    } else if (getState() == STATE.SPLASH) {
        splash.render(g);
        if ((System.currentTimeMillis() - timer2) >= splashTime) {
            splash.clearSplash(g);
        }
    }
    g.dispose();
    bs.show();
  }

 /**
  * Getter for the State.
  *
  * @return state
  */
 public static STATE getState() {
      return state;
 }

 /**
  * Setter for the state.
  *
  * @param state1
  */
 public static void setState(final STATE state1) {
     Game.state = state1;
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
