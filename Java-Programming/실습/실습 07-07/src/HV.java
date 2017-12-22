/**
 * @date : 2017. 5. 25.
 */
/**
 * <pre>
 *  
 *    |_ HV.java
 * 
 * </pre>
 * @date : 2017. 5. 25. 오전 11:25:48
 * @version : 
 * @author : Jho
 */

/*
 * <실행결과>
 * 119
 * 112
 * 114
 * 
 */
import java.util.*;

public class HV {
    public static Vector<String> hashToVector(HashMap<String, String> h) {
        // 작성 부분
        Vector<String> vTmp = new Vector<String>();
        vTmp.addAll(h.values());
        return vTmp;
    }

    public static void main(String[] args) {
        HashMap<String, String> h = new HashMap<String, String>();
        h.put("범죄", "112");
        h.put("화재", "119");
        h.put("전화번호", "114");
        Vector<String> v = HV.hashToVector(h);
        for (int n = 0; n < v.size(); n++)
            System.out.println(v.get(n));
    }
}
