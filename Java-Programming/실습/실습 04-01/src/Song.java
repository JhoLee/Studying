
/**
 * <pre>
 *  (default package)
 *    |_ Song.java
 * </pre>
 * 
 * @date : 2017. 3. 30. ���� 10:36:34
 * @version :
 * @author : jho36
 */
public class Song
{
    private String title;
    private String artist;
    private String album;
    private String[] composer;
    private int year;
    private int track;

    public Song()
    {
        title = null;
        artist = null;
        album = null;
        composer = null;
        year = 0;
        track = 0;

    }

    public Song(String title, String artist, String album, String[] composer,
            int year, int track)
    {
        this.title = title;
        this.artist = artist;
        this.album = album;
        this.composer = composer;
        this.year = year;
        this.track = track;

    }

    public void show()
    {
        System.out.println("�뷡�� : " + title);
        System.out.println("������ : " + artist);
        System.out.println("�ٹ��� : " + album);
        System.out.print("�۰�� : ");
        for (int i = 0; i < composer.length; i++)
        {
            System.out.print(composer[i]);

            if (i == 0) System.out.println();
            else System.out.print(", ");
        }
        System.out.println("�߸ſ��� : " + year);
        System.out.println("Ʈ�� : " + track);
    }

    public static void main(String args[])
    {

        Song ABBA = new Song("Dansing Queen", "ABBA", "", new String[] { "" },
                0, 0);
        ABBA.show();

    }

}