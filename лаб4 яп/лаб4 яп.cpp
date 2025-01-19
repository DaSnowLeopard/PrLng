#include <iostream>
#include <string> // для работы со строками
#include <vector> //для динамических массивов
#include <sstream> //для работы со строковыми потоками (ввод, ввывод)
#include <algorithm> // для использование reverse
#include <map> // для хранения пар
#include <fstream>
using namespace std;

class FindPalindrome {
public:
	FindPalindrome() = default; //конструктор по умолчанию

	void read_file(const string& filename) {
		ifstream inputFile(filename); // Открываем файл для чтения
		if (!inputFile.is_open()) {
			cerr << "File error: " << filename << endl;
			return; // Если файл не открылся, завершаем метод
		}

		string line;
		for (int i = 0; i < 10; i++) {
			if (!getline(inputFile, line)) {
				break; // Если достигнут конец файла раньше, чем считано 10 строк, прерываем цикл
			}
			stringstream ss(line);
			string word;
			while (ss >> word) { // разбиваем строку на слова
				words_.push_back(word); // сохраняем слова в вектор
			}
		}
		inputFile.close(); // Закрываем файл после чтения
	}

	void findPalindrome() {
		for (const string& word : words_) { // перебор слов в векторе
			if (isPalindrome(word)) {
				palindromeCnt_[word]++; // если подходит, счетчик +1
			}
		}
	}

	void printPalindrome(const string& filename) const {
		ofstream outputFile(filename); // Открываем файл для записи
		if (!outputFile.is_open()) {
			cerr << "File error: " << filename << endl;
			return; // Если файл для записи не открылся, завершаем метод
		}

		for (const auto& pair : palindromeCnt_) {
			outputFile << pair.first << " " << pair.second << endl; // Записываем в файл
		}
		outputFile.close(); // Закрываем файл после записи
		cout << "data saved to 2.txt";
	}

private:
	bool isPalindrome(const string& word) const {
		string reversedWord = word; 
		reverse(reversedWord.begin(), reversedWord.end()); //разворот строки
		return word == reversedWord; //сравниваем исходную и перевернутую
	}
	vector<string> words_; // вектор для всех слов
	map<string, int> palindromeCnt_; // хранение палиндромов и их кол
};

int main() {
	FindPalindrome finder; // создаем объект класса
	finder.read_file("1.txt"); // считываем данные
	finder.findPalindrome(); // находим палиндромы
	finder.printPalindrome("2.txt"); // вывод результата
	return 0;
}