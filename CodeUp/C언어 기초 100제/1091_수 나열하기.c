#include <stdio.h>

int main()
{
  int a, m, d, n;
  scanf("%d %d %d %d", &a, &m, &d, &n);
  long long int ans = a;
  for (int i=1; i<n; i++){
    ans = ans * m + d;
  }
  printf("%lld", ans);
  return 0;
}