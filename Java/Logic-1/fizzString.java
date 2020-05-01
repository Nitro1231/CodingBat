/*
Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz". If both the "f" and "b" conditions are true, return "FizzBuzz". In all other cases, return the string unchanged. (See also: FizzBuzz Code)

fizzString("fig") → "Fizz"
fizzString("dib") → "Buzz"
fizzString("fib") → "FizzBuzz"
*/

public String fizzString(String str) {
  String out = "";
  if (str.startsWith("f"))
    out += "Fizz";
  if (str.endsWith("b"))
    out += "Buzz";
    
  if (out.equals(""))
    return str;
  else
    return out;
}
