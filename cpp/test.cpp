//#include<iostream>
#include "hello.h" // "" used for user defined header file

using namespace std;
int main(){
  std::cout << "hi";
  hello();
}

// If we have using namespace std before line 2 after line 1,
// then we can have cout rather than std :: cout in the header file

// Furthermore, we could also have include iostream and using namespace in the header file

// If we do not require iostream in test.cpp we can remove it assuming the header file has include iostream 
