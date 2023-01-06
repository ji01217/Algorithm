#include <stdio.h>

int main()
{
  int a, r, n;
  scanf("%d %d %d", &a, &r, &n);
  long long int ans = a;
  for (int i=1; i<n; i++){
    ans *= r;
  }
  printf("%lld", ans);
  return 0;
}