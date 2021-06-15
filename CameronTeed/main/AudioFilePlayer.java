package com.breakfast.main;
/*
 * This class runs the game loop and renders the sprites.
 *
 * @author  Cameron Teed
 * @version 1.0
 * @since   2021-05-26
 */
import java.io.File;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

/** */
public class AudioFilePlayer {

  /**
   * Loads the first audio.
   *
   * @param s
   */
  public void load(String s) {
        try {           
           File musicPath = new File(s);
           
           AudioInputStream audioInput = AudioSystem.getAudioInputStream(musicPath);
           Clip clip = AudioSystem.getClip();
           clip.open(audioInput);
           clip.start();
           // clip.loop(Clip.LOOP_CONTINUOUSLY);
        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }

  /**
   * Loads the second audio.
   *
   * @param s
   */
  public void load2(String s) {
      try {           
         File musicPath = new File(s);
         
         AudioInputStream audioInput = AudioSystem.getAudioInputStream(musicPath);
         Clip clip = AudioSystem.getClip();
         clip.open(audioInput);
         clip.start();
         clip.loop(Clip.LOOP_CONTINUOUSLY);
      }
      catch(Exception e) {
          e.printStackTrace();
      }
  }
}