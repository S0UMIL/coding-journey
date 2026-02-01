#include <iostream>

int main() {
  int hAge;
  int cAge;
  
  std::cout << "Welcome to the Cat Years program! This only works for cats older than 2years old.\n";
  std::cout << "Enter your cat's age:\n";
  std::cin >> cAge;
  hAge=(cAge-2) * 4 + 24;
  std::cout << "Your cat is" << hAge << " years old in human years";

  
}
