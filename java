package kasper;

public class Kasper {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// kommentaar
		/*
		 * a
		 * a
		 * a
		 */
		int minuArv = 3;
		System.out.println(minuArv);
		System.out.println("Karl-Kasper Ots it-20");
		double sportlane1 = kiirusvahe(10,1);
		double sportlane2 = kiirusvahe(10,1);
		//t2isarv
		//int arv = 40;
		//double pikkus = 20.3;
		
		double x,y;
		x = 10;
		y = x * 0.0254;
		System.out.println("Tollid meetrites " + y + "m");
		
		//ellips
		double xx,yy,z,v;
		xx = 20;
		yy = 50;
		z = Math.PI;
		v = z*xx*yy;
		v = Math.round(v*100.0)/100.0;
		System.out.println("Ellipsi pindala " + v);
		
		//minutid
		teisendus();
		
		//sportlased
		
		System.out.println(kiirusvahe(sportlane1, sportlane2));
		}
		static void teisendus(){
			 double j,k;
			 j = 30;
			 k = j/60;
			 System.out.println("Minutid tundides: " + k);
			 
		
		}
		static double kiirusvahe(double sportlane1, double sportlane2){
			double k= sportlane1/sportlane2;
			return k;
		}
		static double arvutus(double a1, double a2){	
			double vahe = (a1-a2);
			return vahe;
	}

}
