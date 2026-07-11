class DynamicArray {
private:
    int* arr;      
    int cap;       
    int size;

public:

    DynamicArray(int capacity) {
        cap = capacity;
        arr = new int[capacity];
        size = 0;
    }

    ~DynamicArray() {
        delete[] arr; // Automatically cleans up memory when the object is destroyed
    }
    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == cap) {
            resize();
        }
        arr[size++] = n;
    }

    int popback() {
        size--;
        return arr[size];
        //need to pop arr[size]
    }

    void resize() {
        cap *= 2;
        int* new_arr = new int[cap];

        for (int i = 0; i < size; i++) {
            new_arr[i] = arr[i];
        }

        delete[] arr;
        arr = new_arr;

        //need to get new memory that is double cap, copy old arr to it, and then delete olld arr?

    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return cap;
    }
};
