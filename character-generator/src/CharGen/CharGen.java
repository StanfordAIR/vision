package CharGen;

import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.AffineTransform;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.util.concurrent.ThreadLocalRandom;

public class CharGen {

	public static void main(String[] args) throws IOException {
		String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		char[] charArray = chars.toCharArray();
		int ratio = 4;
		int howManyInstances = 4000;
		// Replace with your own
		String newDirPath = "/Users/joshpayne1/desktop/chars/";
		File trainDir = new File(newDirPath+"train");
		File validateDir = new File(newDirPath+"validate");
		if (!trainDir.exists()) {
			trainDir.mkdir();
		}
		if (!validateDir.exists()) {
			validateDir.mkdir();
		}
		for (char ch : charArray) {
			String text = Character.toString(ch);
			for (int m = 0; m <= howManyInstances; m+=0) {
				BufferedImage img = new BufferedImage(1, 1, BufferedImage.TYPE_INT_ARGB);
				Graphics2D g2d = img.createGraphics();
				Font font;
				int bold = ThreadLocalRandom.current().nextInt(0,2);
				int size = ThreadLocalRandom.current().nextInt(8,17);
				if (bold == 0) {
					font = new Font("Arial", Font.BOLD, size);
				} else font = new Font("Arial", Font.PLAIN, size);
				g2d.setFont(font);
				FontMetrics fm = g2d.getFontMetrics();
				int width = fm.stringWidth(text);
				int height = fm.getHeight();

				g2d.dispose();

				img = new BufferedImage(width+32, height+32, BufferedImage.TYPE_INT_ARGB);
				g2d = img.createGraphics();
				g2d.setRenderingHint(RenderingHints.KEY_ALPHA_INTERPOLATION, RenderingHints.VALUE_ALPHA_INTERPOLATION_QUALITY);
				g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
				g2d.setRenderingHint(RenderingHints.KEY_COLOR_RENDERING, RenderingHints.VALUE_COLOR_RENDER_QUALITY);
				g2d.setRenderingHint(RenderingHints.KEY_DITHERING, RenderingHints.VALUE_DITHER_ENABLE);
				g2d.setRenderingHint(RenderingHints.KEY_FRACTIONALMETRICS, RenderingHints.VALUE_FRACTIONALMETRICS_ON);
				g2d.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BILINEAR);
				g2d.setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
				g2d.setRenderingHint(RenderingHints.KEY_STROKE_CONTROL, RenderingHints.VALUE_STROKE_PURE);
				g2d.setFont(font);
				fm = g2d.getFontMetrics();
				g2d.setColor(Color.BLACK);
				g2d.drawString(text, 0, fm.getAscent());
				g2d.dispose();

				// Rotation information
				int randomNumR = 0;
				if (text.equals("W")||text.equals("M")||text.equals("6")||text.equals("9")) {
					randomNumR = ThreadLocalRandom.current().nextInt(-90, 91);
				} else {
					randomNumR = ThreadLocalRandom.current().nextInt(0, 360);
				}
				double rotationRequired = Math.toRadians(randomNumR);
				double locationX = img.getWidth() / 2;
				double locationY = img.getHeight() / 2;
				//        
				AffineTransform tl = new AffineTransform();
				int randomNumW = ThreadLocalRandom.current().nextInt(8, 17);
				int randomNumH = ThreadLocalRandom.current().nextInt(8, 17);
				tl.setToTranslation(randomNumW, randomNumH);
				AffineTransformOp optl = new AffineTransformOp(tl, AffineTransformOp.TYPE_BILINEAR);

				img = optl.filter(img, null);
				//        

				AffineTransform rt = AffineTransform.getRotateInstance(rotationRequired, locationX, locationY);
				AffineTransformOp oprt = new AffineTransformOp(rt, AffineTransformOp.TYPE_BILINEAR);

				img = oprt.filter(img, null);

				if (img.getWidth() >= 48 && img.getHeight() >= 48) {
					BufferedImage dest = img.getSubimage(0, 0, 48, 48);
					m++;
					if (m % ratio == 1) {
						File charDir = new File(newDirPath+"validate/"+ch);
						if (!charDir.exists()) {
							charDir.mkdir();
							try {
								ImageIO.write(dest, "png", new File(newDirPath+"validate/"+text+"/"+m+".png"));
							} catch (IOException ex) {
								ex.printStackTrace();
							}
						} else {
							ImageIO.write(dest, "png", new File(newDirPath+"validate/"+text+"/"+m+".png"));
						}

					} else {
						File charDir = new File(newDirPath+"train/"+ch);
						if (!charDir.exists()) {
							charDir.mkdir();
							try {
								ImageIO.write(dest, "png", new File(newDirPath+"train/"+text+"/"+m+".png"));
							} catch (IOException ex) {
								ex.printStackTrace();
							}
						} else {
							ImageIO.write(dest, "png", new File(newDirPath+"train/"+text+"/"+m+".png"));
						}
					}
				}
			}
		}
	}
}