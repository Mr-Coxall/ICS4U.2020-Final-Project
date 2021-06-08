package com.breakfast.main;

/*
* This class loads the sprites.
*
* @author  Cameron Teed
* @version 1.0
* @since   2021-05-26
*/
import java.awt.image.BufferedImage;

public class SpriteLoader {

	private BufferedImage sprite;

	public SpriteLoader(BufferedImage ss) {
		this.sprite = ss;
	}

	public BufferedImage grabImage(int col, int row, int width, int height) {
		BufferedImage img = sprite.getSubimage((row * 75) - 73, (col * 75) - 73, width, height);
		return img;
	}

}
