#include <iostream>
#include <bitset>

#define MAX_SIZE  1024

using namespace std;

void bitMapSort(int * data, int size)
{
	bitset<MAX_SIZE> bitMap;
	for (int i = 0; i < size; ++i) {
		bitMap.set(data[i], 1);
	}
	int j = 0;
	for (int i = 0; i < MAX_SIZE; ++i) {
		if (bitMap[i]) {
			data[j++] = i;
		}
	}
}

void printData(int * data, int size)
{
	for (int i = 0; i < size; ++i) {
		cout << data[i] << "\t";
	}
}

int main ()
{
	int data[] = {79, 75, 85, 7, 45, 20, 81, 72, 6, 33, 53, 4, 19, 63, 26, 39, 27, 43, 22, 11, 24, 61, 60, 44, 25, 86, 66, 3, 92, 48};
	int size = sizeof(data) / sizeof(data[0]);
	cout << "Before sorting: ";
	printData(data, size);
	bitMapSort(data, size);
	cout << "\n After sorting: ";
	printData(data, size);
	return 0;
}