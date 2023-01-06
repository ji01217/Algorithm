#include <stdio.h>

int main()
{
  int sum = 0;
  int i, n;
  scanf("%d", &n);
  for (i=0;i<=n;i+=2){
    sum += i;
  }
  printf("%d", sum);
  return 0;
}