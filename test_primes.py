from main import Sieve
import pytest


MySieve = Sieve()
class TestPrimesTrue:
    def test_should_right_number_of_primes(self):
        assert len(MySieve.primes) == 11078936

    def test_should_last_prime_is_right(self):
        assert MySieve.primes[-1] == 199999991

    def test_random_file_numbers_are_prime(self):
        assert MySieve.random_test_one_file(1,100) == True

