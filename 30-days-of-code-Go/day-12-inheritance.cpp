#include <iostream>
#include <vector>

using namespace std;


class Person{
	protected:
		string firstName;
		string lastName;
		int id;
	public:
		Person(string firstName, string lastName, int identification){
			this->firstName = firstName;
			this->lastName = lastName;
			this->id = identification;
		}
		void printPerson(){
			cout<< "Name: "<< lastName << ", "<< firstName <<"\nID: "<< id << "\n"; 
		}
	
};

class Student :  public Person{
	private:
		vector<int> testScores;  
	public:
        /*	
        *   Class Constructor
        *   
        *   Parameters:
        *   firstName - A string denoting the Person's first name.
        *   lastName - A string denoting the Person's last name.
        *   id - An integer denoting the Person's ID number.
        *   scores - An array of integers denoting the Person's test scores.
        */
        // Write your constructor here
        Student(string firstName, string lastName, int identification, vector<int> scores)
        : Person(firstName, lastName, identification)
        {
            this->testScores = scores;
        }

        /*	
        *   Function Name: calculate
        *   Return: A character denoting the grade.
        */
        // Write your function here
        char calculate(){
            int sum;
            int n;
            for(int n = 0; n < this->testScores.size(); n++){
                sum += this->testScores[n];
            }
            float mean = sum / (this->testScores.size());
            if(mean < 40){
                return 'T';
            }else if(mean >= 40  && mean < 55){
                return 'D';
            }else if(mean >=55 && mean < 70){
                return 'P';
            }else if(mean >= 70 && mean < 80){
                return 'A';
            }else if(mean >= 80 && mean < 90){
                return 'E';
            }else {
                return 'O';
            }


        }
};

// <ALERT>
// There was no option to do this in Go...
// </ALERT>

int main() {
	string firstName;
  	string lastName;
	int id;
  	int numScores;
	cin >> firstName >> lastName >> id >> numScores;
  	vector<int> scores;
  	for(int i = 0; i < numScores; i++){
	  	int tmpScore;
	  	cin >> tmpScore;
		scores.push_back(tmpScore);
	}
	Student* s = new Student(firstName, lastName, id, scores);
	s->printPerson();
	cout << "Grade: " << s->calculate() << "\n";
	return 0;
}