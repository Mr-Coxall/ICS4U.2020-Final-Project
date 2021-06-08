package com.breakfast.main;

import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Backgrounds extends Canvas {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	BufferedImage image, image2, image3 = null;
	private int HEIGHT;
	private int WIDTH;

	public Backgrounds(int WIDTH, int HEIGHT) {
		try {
			image = ImageIO.read(new File("C:/Users/super/eclipse-workspace/Breakfast/Background/background.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void loadBackground(Graphics g) {
		g.drawImage(image, 0, 0, this.WIDTH, this.HEIGHT, null);
		g.drawImage(image, 0, 0, null);

	}
}
