/**
 * @date : 2017. 5. 25.
 */
/**
 * <pre>
 *  
 *    |_ HV.java
 * 
 * </pre>
 * @date : 2017. 5. 25. ���� 11:25:48
 * @version : 
 * @author : Jho
 */

/*
 * <������>
 * 119
 * 112
 * 114
 * 
 */
import java.util.*;

public class HV {
    public static Vector<String> hashToVector(HashMap<String, String> h) {
        // �ۼ� �κ�
        Vector<String> vTmp = new Vector<String>();
        vTmp.addAll(h.values());
        return vTmp;
    }

    public static void main(String[] args) {
        HashMap<String, String> h = new HashMap<String, String>();
        h.put("����", "112");
        h.put("ȭ��", "119");
        h.put("��ȭ��ȣ", "114");
        Vector<String> v = HV.hashToVector(h);
        for (int n = 0; n < v.size(); n++)
            System.out.println(v.get(n));
    }
}
