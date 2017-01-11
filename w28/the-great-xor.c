#include <stdio.h>
#include <limits.h>

int main(){
  int q, i;
  unsigned long x, xx, y;
  scanf("%d",&q);
  for(int a0 = 0; a0 < q; a0++){
    scanf("%lu", &x);
    xx = x;
    i = 1;
    while (xx >>= 1) ++i;
    y = (1lu << i) - 1 - x;
    printf("%lu\n", y);
  }
  return 0;
}
