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

public class CharGen {

	public static void main(String[] args) throws IOException {
		String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		char[] charArray = chars.toCharArray();
		int ratio = 2;
		int sz = 15;
		int howManyInstances = 3;
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
			int bold = 0;
			for (int m = 0; m <= howManyInstances; m+=0) {
				BufferedImage img = new BufferedImage(1, 1, BufferedImage.TYPE_INT_ARGB);
				Graphics2D g2d = img.createGraphics();
				Font font;

				if (bold >= 2) {
					font = new Font("Arial", Font.BOLD, sz);
				} else font = new Font("Arial", Font.PLAIN, sz);
				bold++;
				g2d.setFont(font);
				FontMetrics fm = g2d.getFontMetrics();
				int width = fm.stringWidth(text);
				int height = fm.getHeight();


				img = new BufferedImage(width+200, height+200, BufferedImage.TYPE_INT_ARGB);
				
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
				g2d.setBackground(Color.WHITE);
				g2d.drawString(text, 0, fm.getAscent());
				g2d.dispose();

				AffineTransform tl = new AffineTransform();
				int x = (28 - width)/2;
				int y = (28-height) / 2;
				tl.setToTranslation(x, y);
				
				AffineTransformOp optl = new AffineTransformOp(tl, AffineTransformOp.TYPE_BILINEAR); //centers character
				
				img = optl.filter(img, null);
				System.out.println("width: " + img.getWidth() + ", height: " + img.getHeight());
				if (img.getWidth() >= 4 && img.getHeight() >= 4) {
					BufferedImage dest = img.getSubimage(0, 0, 28, 28);
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