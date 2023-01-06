#include <stdio.h>

int main()
{
  int n;
  int i = 0;
  int sum = 0;
  scanf("%d", &n);
  while(sum < n){
    sum += i;
    i += 1;
  }
  printf("%d", sum);
  return 0;
}