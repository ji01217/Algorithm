#include <stdio.h>

int main()
{
  int w, h, b;
  double ans;
  scanf("%d %d %d", &w, &h, &b);
  ans = (double)w * h * b / 8 / 1024 / 1024;
  printf("%.2f MB", ans);
  return 0;
}