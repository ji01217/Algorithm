#include <stdio.h>

int main()
{
  int n;
  int sum = 0;
  int i = 0;
  scanf("%d", &n);
  while(sum < n) {
    i += 1;
    sum += i;
  }
  printf("%d", i);
  return 0;
}