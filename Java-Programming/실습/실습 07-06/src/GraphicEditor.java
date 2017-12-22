/**
 * @date : 2017. 5. 24.
 */
/**
 * <pre>
 *  
 *    |_ GraphicEditor.java
 * 
 * </pre>
 * 
 * @date : 2017. 5. 24. 오후 11:37:26
 * @version :
 * @author : Jho
 */

import java.util.*;

abstract class GraphicObject {
    int x, y, w, h;

    GraphicObject(int x, int y, int w, int h) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
    }

    public abstract void view();
}

public class GraphicEditor {
    Vector<GraphicObject> v = new Vector<GraphicObject>();

    void add(GraphicObject ob) {
        v.add(ob);
    }

    void draw() {
        for (int i = 0; i < v.size(); i++) {
            v.get(i).view();
        }
    }

    public static void main(String args[]) {
        GraphicEditor g = new GraphicEditor();
        g.add(new Rect(2, 2, 3, 4)); // (2,2)에서 3x4짜리 사각형
        g.add(new Line(3, 3, 8, 8)); // (3,3)에서 8x8의 사각형 내의 대각선 직선
        g.add(new Line(2, 5, 6, 6)); // (2,5)에서 6x6의 사각형 내의 대각선 직선
        g.draw();

    }

}

class Rect extends GraphicObject {
    public Rect(int x, int y, int w, int h) {
        super(x, y, w, h);
    }

    @Override
    public void view() {
        System.out.println(x + "," + y + " -> " + w + "," + h + "의 사각형");

    }
}

class Line extends GraphicObject {
    public Line(int x, int y, int w, int h) {
        super(x, y, w, h);
    }

    @Override
    public void view() {
        System.out.println(x + "," + y + " -> " + w + "," + h + "의 선");

    }
}