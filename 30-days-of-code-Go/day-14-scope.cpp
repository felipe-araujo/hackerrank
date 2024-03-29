#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
        vector<int> elements;
  
  	public:
  	    int maximumDifference;

        Difference(vector<int> elements){
            this->elements = elements;
        }
        void computeDifference(){
            int delta = 0;
            for(unsigned i = 0; i < this->elements.size()-1; i++){
                for(unsigned j = i+1; j < this->elements.size(); j++){                    
                    int diff = abs(this->elements[i] - this->elements[j]);
                    if(diff > delta){
                        delta = diff;
                    }
                }
            }
            this->maximumDifference = delta;
        }

	// Add your code here

}; // End of Difference class

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }
    
    Difference d(a);
    
    d.computeDifference();
    
    cout << d.maximumDifference;
    
    return 0;
}