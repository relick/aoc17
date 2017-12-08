#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>
typedef std::chrono::high_resolution_clock Clock;

void solution(std::vector<int>& input) {
    int totalsteps = 0;    
    int currentpos = 0;
    auto t1 = Clock::now();
    while(0 <= currentpos && currentpos < input.size()) {
        int k = 1;
        if(input[currentpos] >= 3) {
            k = -1;
            input[currentpos] += k;
        } else {
            input[currentpos] += k;
        }
        currentpos += input[currentpos]-k;
        totalsteps += 1;
    }
    auto t2 = Clock::now();
    std::cout << totalsteps << std::endl << std::chrono::duration_cast<std::chrono::milliseconds>(t2-t1).count() << "ms" << std::endl;
}

int main(int argc, char** argv) {
    std::ifstream file;
    file.open(argv[1]);
    std::vector<int> input;
    int rd;
    while(file >> rd) {
        input.push_back(rd);
    }
    solution(input);
}
