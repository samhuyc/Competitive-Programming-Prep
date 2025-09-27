#include <iostream>
#include <vector>

const int MOD = 1e9 + 7;

long long power(long long base, int exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return result;
}

long long xchoosey(int x, int y) {
    int diff = std::min(x - y, y);
    long long top = 1;
    long long bot = 1;
    for (int i = 0; i < diff; ++i) {
        top = (top * (x - i)) % MOD;
    }
    for (int j = 0; j < diff; ++j) {
        bot = (bot * (1 + j)) % MOD;
    }
    long long bot_inv = power(bot, MOD - 2); 
    return (top * bot_inv) % MOD;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        int n, k;
        std::cin >> n >> k;
        int new_n = n;
        for (int i = 0; i < k; ++i) {
            int a, b;
            std::cin >> a >> b;
            if (a == b) {
                new_n -= 1;
            } else {
                new_n -= 2;
            }
        }

        long long ans = 0;
        if (new_n % 2 == 0) {
            for (int diagonal = 0; diagonal <= new_n; diagonal += 2) {
                long long curr = 1;
                curr = (curr * xchoosey(new_n, diagonal)) % MOD;
                curr = (curr * power(2, (new_n - diagonal) / 2)) % MOD;

                for (int mult = 1; mult < new_n - diagonal; mult += 2) {
                    curr = (curr * mult) % MOD;
                }
                ans = (ans + curr) % MOD;
            }
        } else {
            for (int diagonal = 1; diagonal <= new_n; diagonal += 2) {
                long long curr = 1;
                curr = (curr * xchoosey(new_n, diagonal)) % MOD;
                curr = (curr * power(2, (new_n - diagonal) / 2)) % MOD;

                for (int mult = 1; mult < new_n - diagonal; mult += 2) {
                    curr = (curr * mult) % MOD;
                }
                ans = (ans + curr) % MOD;
            }
        }
        std::cout << ans << std::endl;
    }
    return 0;
}
