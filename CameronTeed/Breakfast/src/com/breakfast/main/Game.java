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
import java.awt.image.BufferedImage;

public class Game extends Canvas implements Runnable {

	/**
	 * SerialVersion UID (Will need for later).
	 */
	private static final long serialVersionUID = 5102725995743094780L;
	/**
	 * The size of the GUI.
	 */
	public static final int WIDTH = 740;
	/**
	 * Initializes the height.
	 */
	public static final int HEIGHT = 580;
	/**
	 * Initializes the sprites.
	 */
	public static BufferedImage spriteSheet;
	/**
	 * Initializes the threads.
	 */
	private Thread thread;
	/**
	 * Tells the programs its not yet running.
	 */
	private boolean running = false;
	/**
	 * Initializes the background.
	 */
	private Backgrounds scenes = new Backgrounds(WIDTH, HEIGHT);

	/**
	 * Constructor.
	 */
	public Game() {
		this.addMouseListener(new myMouseListener());
		new Window(WIDTH, HEIGHT, "Hello, World!", this);
	}

	public void init() {
		Assets.init();
	}

	/**
	 * Starts the GUI.
	 */
	public synchronized void start() {
		thread = new Thread(this);
		thread.start();
		running = true;
	}

	/**
	 * Stops the GUI.
	 */
	public synchronized void stop() {
		try {
			thread.join();
			running = false;
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * This method creates a loop that can run the graphics.
	 */
	@Override
	public void run() {
		long lastTime = System.nanoTime();
		double amountOfTicks = 60.0;
		double ns = 100000 / amountOfTicks;
		double delta = 0;
		long timer = System.currentTimeMillis();
		int frames = 0;
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
			if (running)
				render();
			frames++;

			if (System.currentTimeMillis() - timer > 1000) {
				timer += 1000;
				System.out.println("FPS: " + frames);
			}
		}
		stop();
	}

	/**
	 * This method will set the tick speed.
	 */
	public void tick() {
	}

	public void rePaint(Graphics g) {
		Graphics2D g2d = (Graphics2D) g;
		PointerInfo a = MouseInfo.getPointerInfo();
		Point b = a.getLocation();
		int y = (int) b.getY();
		int x = (int) b.getX();

		if (myMouseListener.isKeyPressed()) {
			g2d.drawImage(Assets.spoon, x - 440, y - 200, null);
		} else if (myMouseListener.isKeyPressed1()) {
			g2d.drawImage(Assets.egg, x - 440, y - 200, null);
		} else if (myMouseListener.isKeyPressed2()) {
			g2d.drawImage(Assets.bacon, x - 440, y - 200, null);
		} else {
			g2d.drawImage(Assets.spatula, x - 440, y - 200, null);
		}
	}

	/**
	 * This method renders the graphics.
	 */
	public void render() {

		BufferStrategy bs = this.getBufferStrategy();
		if (bs == null) {
			this.createBufferStrategy(3);
			return;
		}

		Graphics g = bs.getDrawGraphics();
		// scenes.splashScreen(g);
		// scenes.mainMenu(g);
		scenes.loadBackground(g);
		rePaint(g);
		g.dispose();
		bs.show();
	}

	/**
	 * Main function.
	 *
	 * @param args
	 */
	public static void main(String args[]) {
		new Game();
	}
}
