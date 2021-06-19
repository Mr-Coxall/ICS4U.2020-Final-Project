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

/** Main class. */
public class Main extends Canvas implements Runnable {

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
      HELP,
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
  /** Initializes the spatula. */
  private final Spatula spatula = new Spatula();
  /** Initializes the plates. */
  private final RenderPlates render = new RenderPlates();
  /** Initializes the end screen. */
  private EndScreen end = new EndScreen();
  /** Initializes the audio. */
  private AudioFilePlayer music = new AudioFilePlayer();
  /** Initializes the help screen. */
  private Help help = new Help();

  /** Constructor. */
  public Main() {
    this.addMouseListener(new MyMouseListener());
    new Window(WIDTH, HEIGHT, "Breakfast: The Main", this);
  }

  /** initializing. */
  public void init() {
    assets.init();
    music.load("C:\\Users\\super\\git\\ICS4U.2020-Final-Proj"
            + "ect\\CameronTeed\\Breakfast\\Music\\bell_small_001.wav");
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

  /**
   * This method pains some graphics.
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

    // Renders all the sprites.
    render.renderPlates(g2d);
    render.createPlates();
    renderEggs.eggLogic(x, y, g2d);
    renderEggs.flipTime(g2d, x, y);
    renderPancake.pancakeLogic(x, y, g2d);
    renderPancake.flipTime(g2d, x, y);
    renderBacon.flipTime(g2d, x, y);
    renderBacon.baconLogic(x, y, g2d);
    spatula.getSpatula(g2d, x, y);
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

    // Checks if the game state is equal to the end menu
    if (getState() == STATE.END) {
        end.render(g);
     // Checks if the game state is equal to the game
    } else if (getState() == STATE.GAME) {
        // Renders the background
        scenes.loadBackground(g);
        // Renders the cursors
        renderEggs.putEgg(g, x, y);
        renderPancake.putPancakes(g, x, y);
        renderBacon.putBacon(g, x, y);
        renderBacon.getBurnt();
        renderEggs.getBurnt();
        renderPancake.getBurnt();
        rePaint(g);
        // Checks if the game state is equal to the help screen
    } else if (getState() == STATE.HELP) {
        help.render(g, x, y);
     // Checks if the game state is equal to the menu
    } else if (getState() == STATE.MENU) {
        menu.render(g, x, y);
     // Checks if the game state is equal to the splash
    } else if (getState() == STATE.SPLASH) {
        splash.render(g);
        // Loads the splash for a certain amount of time.
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
     Main.state = state1;
 }

/**
   * Main function.
   *
   * @param args
   */
  public static void main(final String[] args) {
    new Main();
  }
}
