#include <iostream>
#include <cstdlib>

int main() {
  // Write code here 💖
  std::string a= "Don't pursue happiness – create it.";
  std::string b="All things are difficult before they are easy.";
  std::string c="The early bird gets the worm, but the second mouse gets the cheese.";
  std::string d="Someone in your life needs a letter from you.";
  std::string e="The fortune you search for is in another cookie.";
  std::string f="Help! I'm being held prisoner in a Chinese bakery!";
  srand(time(NULL));
  int cookie = std::rand() %6;
  if (cookie==1){
    std::cout << "🥠" << a;

  }
  else if (cookie==2){
    std::cout << "🥠" << b;
  }
  else if (cookie==3){
    std::cout << "🥠" << c;
  }
  else if (cookie==4){
    std::cout << "🥠" << d;
  }
  else if (cookie==5){
    std::cout << "🥠" << e;
  }
  else{
    std::cout << "🥠" << f;
  }
}
