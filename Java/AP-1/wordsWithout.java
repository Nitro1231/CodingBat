/*
Given an array of strings, return a new array without the strings that are equal to the target string. One approach is to count the occurrences of the target string, make a new array of the correct length, and then copy over the correct strings.

wordsWithout(["a", "b", "c", "a"], "a") → ["b", "c"]
wordsWithout(["a", "b", "c", "a"], "b") → ["a", "c", "a"]
wordsWithout(["a", "b", "c", "a"], "c") → ["a", "b", "a"]
*/

public String[] wordsWithout(String[] words, String target) {
  String[] get = new String[words.length];
  int c = 0;
  for (int i = 0; i < words.length; i++)
    if (!words[i].equals(target))
      get[c++] = words[i];
      
  String[] arr = new String[c];
  for (int i = 0; i < c; i++)
    arr[i] = get[i];
  
  return arr;
}

