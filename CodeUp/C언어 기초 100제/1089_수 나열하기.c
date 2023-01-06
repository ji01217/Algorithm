#include <stdio.h>

int main()
{
  int a, d, n;
  scanf("%d %d %d", &a, &d, &n);
  int ans = a;
  for (int i=1; i<n; i++){
    ans += d;
  }
  printf("%d", ans);
  return 0;
}