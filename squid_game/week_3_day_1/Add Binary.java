class Solution {
        public String addBinary(String a, String b) {
            StringBuilder output = new StringBuilder();
            int R = 0, sum = 0;
            int remain = 0, carry = 0;
            String[] subOne = a.split("");
            String[] subTwo = b.split("");

            if(subOne.length > subTwo.length) {
                remain = add(subTwo.length, sum, R, subOne, subTwo, output);
                carry = remaining(subOne.length-subTwo.length-1, sum, remain, subOne, output);
            }
            else if(subOne.length <= subTwo.length) {
                remain = add(subOne.length, sum, R, subTwo, subOne, output);
                carry = remaining(subTwo.length-subOne.length-1, sum, remain, subTwo, output);
            }
            if(carry == 1)
                output.append(1);
            return output.reverse().toString();
        }

        public int add(int length, int sum, int R, String[] large, String[]                               small, StringBuilder output){
            for(int i=length-1; i>=0 ; i--) {
                sum = Integer.parseInt(large[i + (large.length - small.length)]) +                          Integer.parseInt(small[i]) + R;
                if(sum == 1)
                    R = 0;
                else if(sum == 2){
                    sum = 0;
                    R = 1;
                }
                else if(sum == 3){
                    sum = 1;
                    R = 1;
                }
                else {sum = 0;}
                output.append(sum);
            }
        return R;
        }

    public int remaining(int length, int sum, int R, String[] one, StringBuilder                                output){
        for(int i=length; i>=0 ; i--) {
            sum = Integer.parseInt(one[i]) + R;
            if(sum == 1) R = 0;
            else if(sum == 2){
                sum = 0;
                R = 1;
            }
            output.append(sum);
        }
        return R;
    }
}