import java.time.LocalTime;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class WPMProgram {

    static String[] words = {
            "apple", "nimbus", "quartz", "zephyr", "echo",
            "velvet", "ember", "sprout", "horizon", "solace",
            "aurora", "bliss", "cobalt", "dusk", "eclipse",
            "flare", "glint", "harbor", "icicle", "jade",
            "lunar", "meadow", "nova", "oasis", "petal",
            "quiver", "ripple", "stellar", "thistle", "wander"
    };


    public static void main(String[] args) throws InterruptedException {

        // Countdown to start
        System.out.println("3");
        TimeUnit.SECONDS.sleep(1);

        System.out.println("2");
        TimeUnit.SECONDS.sleep(1);

        System.out.println("1");
        TimeUnit.SECONDS.sleep(1);

        System.out.println("Go!");

        // Generates 10 random words from list
        Random rand = new Random();
        StringBuilder sentence = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            String word = words[rand.nextInt(29)];
            System.out.print(word + " ");
            sentence.append(word).append(" ");
        }
        String finalSentence = sentence.toString();
        System.out.println();

        // Grabs exact nanoseconds of start
        double start = LocalTime.now().toNanoOfDay();

        Scanner sc = new Scanner(System.in);
        String typedWords = sc.nextLine();

        // Grabs exact nanoseconds of end
        double end = LocalTime.now().toNanoOfDay();
        double timeElapsed = end - start;
        double seconds = timeElapsed / 1000000000.0;
        int numChars = typedWords.length();
        // Calculation to get words per minute
        int wmp = (int) ((((double) numChars / 5) / seconds) * 60);

        System.out.println("You typed " + numChars + " characters in " + seconds + " seconds, or " + wmp + " words per minute.");

        // Compare typed sentence to original
        char[] first = typedWords.toCharArray();
        char[] second = finalSentence.toCharArray();
        // Test code to compare sentences
        // System.out.println("Your sentence was: " + finalSentence);
        // System.out.println("Your sentence was: " + typedWords);

        int minLength = Math.min(first.length, second.length);

        int counter = 0;
        for (int i = 0; i < minLength; i++) {
            if (first[i] != second[i]) {
                counter++;
            }
        }
        System.out.println("You typed " + counter + " characters wrong.");
    }
}
