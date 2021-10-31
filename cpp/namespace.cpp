#include<iostream>

// # is preprocessor directive

// g++ -E helloworld.cpp shows you the code after preprocessing directive

using namespace std;



namespace a{

void f(){
  cout << "hi in namespace a";
}

}

namespace b{

  void f(){
    cout << "hi in namespace b";
  }
}

int main(){
  //using namespace a;
  cout << "Hello World\n";
  //f(); // f was not declared in this scope if not used using namespace a;
  //f();
  // If we do not use using namespace, we use the scope resolution operator ::
  a::f();

  return 0;
}
