public class Main
{
    public static int power(int n, int m)
    {
        if (m == 1) {
            return n;
        } else {
            return n*(power(n, m-1));
        }
    }
    public static float getFloat(String number) {
        float result = 0.0f;
        int dotPosition = 0;
        for(int i=0; i < number.length(); i++) {
            if (number.charAt(i) == '.') {
                dotPosition = number.length() - i - 1;
            } else {
                result = result*10 + number.charAt(i) -'0';
            }
        }
        result /= power(10, dotPosition);
        
        return result;
    }
	public static void main(String[] args) {
	    System.out.println(getFloat("100.23"));
	}
}
