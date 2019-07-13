import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Print {
	String contents;

	public String getContents() {
		return contents;
	}

	public void setContents(String contents) {
		this.contents = contents;
	}

	public int getPriority() {
		return priority;
	}

	public void setPriority(int priority) {
		this.priority = priority;
	}

	int priority;

	Print(String contents, int priority) {
		this.priority = priority;
		this.contents = contents;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return contents + "" + priority;
	}

}

public class Main {

	public static void main(String[] args) {

		// 배열 생성
		Main main = new Main();
		char content = 65;
		List<Print> list = new ArrayList<Print>();
		for (int i = 0; i < 6; i++) {
			int nedan = (int)(Math.random()*6) + 1;
			Print print = new Print(String.valueOf(content),nedan);
			list.add(print);
			content++;
		}
		System.out.println(list.toString());
		System.out.println("=========================");
		System.out.println("result :" + main.printOrderByLocation(list, 2));
	}

	public int printOrderByLocation(List<Print> list, int location) {
		String index = list.get(location).contents;
		
		List<Print> l = new ArrayList<Print>();
		
		
		while(true) {
			int cnt = 0;
			int s = list.get(0).priority;
			int g = 0;
			Print p = null;
			
			for (int i = 1; i < list.size(); i++) {
				g = s - list.get(i).priority;
				if(g < 0) {
					p = list.get(0);
					list.remove(0);
					list.add(p);
					break;
				}
			}
			
			if(g >= 0) {
				l.add(list.get(0));
				list.remove(0);
			}
			if (list.
					size() == 0) {
				break;
			}
		}
		
		System.out.println(l.toString());
		
		for (int i = 0; i < l.size(); i++) {
			if(l.get(i).contents.equals(index)) {
				
				return i + 1;
			}
			
		}
		return 0;
	}

}
