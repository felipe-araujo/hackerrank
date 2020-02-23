import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String delim = "[ !,?._'@]+";
        String[] tokens = s.replaceFirst("^" + delim, "").replaceFirst(delim+"$", "").split(delim);
        System.out.println(tokens.length);
        for(String t: tokens){
            System.out.println(t);
        }
        
        scan.close();
    }
}
