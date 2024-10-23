#include <cstddef>
#include <memory>
#include <stdexcept>
#include <utility>
#include<vector>
#include<cassert>

// task 1
// no comparison operator => less operations (automatic cast to bool)
auto is_even = [](int num) { return !(num % 2); };


// task 2
// queue based on std::vector.
// advantages: (1) easy to implement & understand
//             (2) automatic memory management
// disadvantages: (1) bulky reallocation when the vector capacity is exceeded
//                (2) array-based structure
template <typename T>
class VectorQueue
{
    std::vector<T> data;

public:

    VectorQueue() = default;
    VectorQueue(std::initializer_list<T> list) : data(list) { }

    auto size() const { return data.size(); }
    void put(T val) { data.push_back(val); }
    T pop() {
        if (data.empty()) throw std::out_of_range("Queue is empty");

        auto val = data.front();
        data.erase(data.begin());
        return val;
    }
};


// queue based on linked list.
// advantages: (1) dynamic memory allocation
//             (2) no shifting when popping an elem 
// disadvantages: (1) semi-manual memory management (since unique_ptr)
//                (2) a little bit more complicated to implement & support (than vector queue)
template <typename T>
struct Node
{
    T val;
    std::unique_ptr<Node> next = nullptr;
    Node(T val) : val(val) { }
};


template <typename T>
class ListQueue
{
    std::unique_ptr<Node<T>> head = nullptr; // owns the memory
    Node<T>* tail = nullptr; // observes the last elem
    size_t s = 0;

public:

    ListQueue(std::initializer_list<T> list) {
        for (auto val : list) {
            put(val);
        }
    }

    auto size() const { return s; }

    void put(T val) {
        auto new_node = std::make_unique<Node<T>>(val);

        if (!head) {
            head = std::make_unique<Node<T>>(val);
            tail = head.get();
        } else {
            tail->next = std::make_unique<Node<T>>(val);
            tail = tail->next.get();
        }
      
        ++s;
    }

    T pop() {
        if (head == nullptr) throw std::out_of_range("Queue is empty");
        auto val = std::move(head->val);
        head = std::move(head->next);
        if (!head) tail = nullptr;
        --s;
        return val;
    }

    const T& peek() const {
        if (!head) throw std::out_of_range("Queue is empty");
        return head->val;
    }
};

// task 3
// iterative quick sort.
// average time complexity: O(nlogn), no recursive calls (recuresion slows down code exec)
 
template <typename T>
int partition(T* arr, unsigned int first, unsigned int last)
{
    T pivot = arr[last];
    int i = first;
    for (int j = first; j<last; ++j) {
        if (arr[j] <= pivot) {
            std::swap(arr[i], arr[j]);      
            ++i;
        }
    }
    std::swap(arr[i], arr[last]);
    return (i);
}

template <typename T>
void quick_sort_iterative(T* arr, unsigned int first, unsigned int last)
{
    int stack[last - first + 1];
    auto top = -1;
    stack[++top] = first;
    stack[++top] = last;
    while (top >= 0) {
        last = stack[top--];
        first = stack[top--];
        int pivot_pos = partition(arr, first, last);

        // left side of the pivot
        if (pivot_pos - 1 > first) {
            stack[++top] = first;
            stack[++top] = pivot_pos - 1;
        }

        // right side of the pivot
        if (pivot_pos + 1 < last) {
            stack[++top] = pivot_pos + 1;
            stack[++top] = last;
        }
    }
}


int main(int argc, char const *argv[])
{
    // task 1
    assert(is_even(4) == true);
    assert(is_even(9) == false);


    // task 2
    auto vq = VectorQueue({1, 2, 3, 4, 5});
    assert(vq.size() == 5);
    vq.put(6);
    assert(vq.size() == 6);
    assert(vq.pop() == 1);
    assert(vq.pop() == 2);
    assert(vq.pop() == 3);
    assert(vq.pop() == 4);
    assert(vq.pop() == 5);
    assert(vq.pop() == 6);

    auto lq = ListQueue({1, 2, 3, 4, 5});
    assert(lq.size() == 5);
    lq.put(6);
    assert(lq.size() == 6);
    assert(lq.pop() == 1);
    assert(lq.pop() == 2);
    assert(lq.pop() == 3);
    assert(lq.pop() == 4);
    assert(lq.pop() == 5);
    assert(lq.pop() == 6);

    // task 3
    int* arr = new int[10] {13, 1, 5, 12, 4, 7, 8, 9, 10, 1};
    quick_sort_iterative(arr, 0, 9);
    assert(arr[0] == 1);
    assert(arr[1] == 1);
    assert(arr[2] == 4);
    assert(arr[3] == 5);
    assert(arr[4] == 7);
    assert(arr[5] == 8);

    delete[] arr;

    return 0;
}
