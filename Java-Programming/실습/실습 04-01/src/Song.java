
/**
 * <pre>
 *  (default package)
 *    |_ Song.java
 * </pre>
 * 
 * @date : 2017. 3. 30. 오후 10:36:34
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
        System.out.println("노래명 : " + title);
        System.out.println("가수명 : " + artist);
        System.out.println("앨범명 : " + album);
        System.out.print("작곡가명 : ");
        for (int i = 0; i < composer.length; i++)
        {
            System.out.print(composer[i]);

            if (i == 0) System.out.println();
            else System.out.print(", ");
        }
        System.out.println("발매연도 : " + year);
        System.out.println("트랙 : " + track);
    }

    public static void main(String args[])
    {

        Song ABBA = new Song("Dansing Queen", "ABBA", "", new String[] { "" },
                0, 0);
        ABBA.show();

    }

}