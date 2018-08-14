#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

class FibNaive final {
    public:
        static int get(int n) {
            assert(n>=0);
            if (n == 0 || n == 1) {
                return n;
            }
            return get(n - 2) + get(n - 1);
        }
};

class FibRecursiveWithCache final {
    public:
        static int get(int n) {
            assert(n>=0);
            if (n == 0 || n == 1) {
                return n;
            }
            static std::unordered_map<int, int> cache;
            auto &result = cache[n];
            if (result == 0) {
                result = get(n - 2) + get(n - 1);
            }

            return result;
        }
};


class FibIterative final {
    public:
        static int get(int n) {
            assert(n>=0);
            static std::vector<int> cache;
            cache.resize(n+1);
            cache[0] = 0;
            cache[1] = 1;
            for (int i = 2; i <=n; i++) {
                cache[i] = cache[i - 2] + cache[i - 1];
            }
            return cache[n];
        }
};

class FibFinal final {
    public:
        static int get(int n) {
            assert(n>=0);
            if (n <= 1) {
                return n;
            }
            int a = 0;
            int b = 1;
            for (int i = 2; i <=n; i++) {
                int c = a + b;
                a = b;
                b = c;
            }
            return b;
        }
};

int main(void) {
    int n;
    std::cin >> n;
    /*std::cout << FibNaive::get(n) << std::endl;*/
    std::cout << FibFinal::get(n) << std::endl;
    return 0;
}
