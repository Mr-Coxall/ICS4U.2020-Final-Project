package com.breakfast.main;

/*
* This class creates the Jframe needed to output HelloWorld.
*
* @author  Cameron Teed
* @version 1.0
* @since   2021-05-21
*/
import java.awt.Canvas;
import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.WindowConstants;

public class Window extends Canvas {

	/**
	 * SerialVersion UID (Will need for later).
	 */
	private static final long serialVersionUID = 7115408214738794472L;

	/**
	 * Constructor for Window class.
	 *
	 * @param width
	 * @param height
	 * @param title
	 * @param game
	 */
	public Window(int width, int height, String title, Game game) {
		JFrame frame = new JFrame(title);

		frame.setPreferredSize(new Dimension(width, height));
		frame.setMaximumSize(new Dimension(width, height));
		frame.setMinimumSize(new Dimension(width, height));

		frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		frame.setResizable(false);
		frame.setLocationRelativeTo(null);
		frame.add(game);
		frame.setVisible(true);
		game.start();
	}
}
