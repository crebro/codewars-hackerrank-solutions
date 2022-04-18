// it is to be noted that no inbuilt function for the conversion is used
String numberToHexa(int n) {
  if (n >= 255) {
    return "FF";
  } else if (n <= 0) {
    return "00";
  }
  List<int> totalValue = [];
  while (n > 16) {
    totalValue.add(n % 16);
    n = (n / 16).floor();
  }
  totalValue.add(n);

  String out = "";
  for (int i = totalValue.length - 1; i >= 0; i--) {
    int val = totalValue[i];
    out =
        out + (val <= 9 ? val.toString() : String.fromCharCode(64 + (val - 9)));
  }
  return out.length == 1 ? "0" + out : out;
}

String rgb(int r, int g, int b) {
  return numberToHexa(r) +
      numberToHexa(g) +
      numberToHexa(b); // replace with your solution
}
