#include <stdio.h>

int main()
{
  int h, b, c, s;
  double storage;
  scanf("%d %d %d %d", &h, &b, &c, &s);
  storage = (double)h * b * c * s / 8 / 1024 / 1024 ;
  printf("%.1lf MB", storage);
  return 0;
}