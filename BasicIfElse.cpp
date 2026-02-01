#include <iostream>

int main() {
  // Write code here 💖
  int level;
  std::cout << "enter ur level";
  std::cin >> level;
  if(level<=5){
    std::cout << "Bronze";
  }
  else if(level>5 && level <=10){
    std::cout << "Silver";
  }
  else if(level>10 && level<=15){
    std::cout << "Gold";
  }
  else if(level>15 && level<=20){
    std::cout << "Platinum";
  }
  else{
    std::cout << "Diamond";
  }

}
