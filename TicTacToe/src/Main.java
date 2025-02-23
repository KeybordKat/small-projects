// imports:
import java.util.*;

@SuppressWarnings("rawtypes")
public class Main {

    // array lists to store player and cpu moves
    static ArrayList<Integer> playerPositions = new ArrayList<>();
    static ArrayList<Integer> cpuPositions = new ArrayList<>();

    public static void main(String[] args) {

        // 5 elements in each row in array, 3 for x and o's, 2 for separating lines
        char[][] gameBoard = {
                {' ', '|', ' ', '|', ' '},
                {'-', '+', '-', '+', '-'},
                {' ', '|', ' ', '|', ' '},
                {'-', '+', '-', '+', '-'},
                {' ', '|', ' ', '|', ' '}
        };

        char[][] boardInstructions = {
                {'1', '|', '2', '|', '3'},
                {'-', '+', '-', '+', '-'},
                {'4', '|', '5', '|', '6'},
                {'-', '+', '-', '+', '-'},
                {'7', '|', '8', '|', '9'}
        };
        // Game instructions
        System.out.println();
        System.out.println("Welcome to Tic Tac Toe!");
        printGameBoard(boardInstructions);
        System.out.println();
        System.out.println("""
                Select a number between 1 and 9 to determine your tile placement\s
                according to the chart above.
                """);
        printGameBoard(gameBoard);

        while(true) {
            Scanner sc = new Scanner(System.in);

            // places symbol based on player input
            System.out.println("Enter your placement: ");
            int playerPos = sc.nextInt();
            while(playerPositions.contains(playerPos) || cpuPositions.contains(playerPos)) {
                System.out.println("Position taken! Enter a correct position");
                playerPos = sc.nextInt();
            }
            placePiece(gameBoard, playerPos, "player");

            // if empty string returned, game is over
            String result = checkWinner();
            if(result.length() > 0) {
                System.out.println(result);
                break;
            }

            // places symbol for computer randomly
            Random rand = new Random();
            int cpuPos = rand.nextInt(9) + 1;
            while(playerPositions.contains(cpuPos) || cpuPositions.contains(cpuPos)) {
                cpuPos = rand.nextInt(9) + 1;
            }
            placePiece(gameBoard, cpuPos, "cpu");

            printGameBoard(gameBoard);

            // if empty string returned, game is over
            result = checkWinner();
            if(result.length() > 0) {
                System.out.println(result);
                break;
            }
        }
    }

    public static void printGameBoard(char [] [] gameBoard) {
        // print gameBoard character by character, row by row
        for (char[] row : gameBoard) {
            for (char cell : row) {
                System.out.print(cell);
            }
            System.out.println();
        }
    }

    public static void placePiece(char [] [] gameBoard, int pos, String user) {

        // Default character set to x, chooses correct symbol based on player type
        // Adds position played to array of played positions
        char symbol = 'x';
        if(user.equals("player")) {
            playerPositions.add(pos);
        } else if(user.equals("cpu")) {
            symbol = 'o';
            cpuPositions.add(pos);
        }
        // places x or o based on given position
        switch(pos) {
            case 1:
                gameBoard[0][0] = symbol;
                break;
            case 2:
                gameBoard[0][2] = symbol;
                break;
            case 3:
                gameBoard[0][4] = symbol;
                break;
            case 4:
                gameBoard[2][0] = symbol;
                break;
            case 5:
                gameBoard[2][2] = symbol;
                break;
            case 6:
                gameBoard[2][4] = symbol;
                break;
            case 7:
                gameBoard[4][0] = symbol;
                break;
            case 8:
                gameBoard[4][2] = symbol;
                break;
            case 9:
                gameBoard[4][4] = symbol;
                break;

                default:
                    break;
        }
    }

    @SuppressWarnings("SuspiciousMethodCalls")
    public static String checkWinner() {

        // List of all possible winning combinations for symbol positions
        List<List> winning = getLists();

        // Loops through to check if any winning condition is met
        for(List l : winning)
            if (playerPositions.containsAll(l)) {
                return "Congratulations you won!!!";
            } else if (cpuPositions.contains(l)) {
                return "CPU wins, sorry :(";
                // checks number of elements on board to see if board is full
            } else if (playerPositions.size() + cpuPositions.size() == 9) {
                return "It's a tie";
            }

        return "";
    }

    private static List<List> getLists() {
        // Lists of all winning position combinations
        List topRow = Arrays.asList(1, 2, 3);
        List midRow = Arrays.asList(4, 5, 6);
        List botRow = Arrays.asList(7, 8, 9);
        List leftCol = Arrays.asList(1, 4, 7);
        List midCol = Arrays.asList(2, 5, 8);
        List rightCol = Arrays.asList(3, 6, 9);
        List cross1 = Arrays.asList(1, 5, 9);
        List cross2 = Arrays.asList(7, 5, 3);

        // Creates a list of lists containing all winning conditions
        List<List> winning = new ArrayList<>();
        winning.add(topRow);
        winning.add(midRow);
        winning.add(botRow);
        winning.add(leftCol);
        winning.add(midCol);
        winning.add(rightCol);
        winning.add(cross1);
        winning.add(cross2);
        return winning;
    }
}