/*
Given three ints, a b c, return true if it is possible to add two of the ints to get the third.

twoAsOne(1, 2, 3) → true
twoAsOne(3, 1, 2) → true
twoAsOne(3, 2, 2) → false
*/

public boolean twoAsOne(int a, int b, int c) {
  int n[] = {Math.abs(a), Math.abs(b), Math.abs(c)};
  Arrays.sort(n);
  return (n[0] + n[1] == n[2]);
}

