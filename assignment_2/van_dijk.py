import random


class VanDijk:

    def __init__(self, eta, gamma, rho, tau):
        self.eta = eta
        self.gamma = gamma
        self.rho = rho
        self.tau = tau

    def key_gen(self):
        # Generate secret key as eta-bit odd integer
        p = random.randint(2**(self.eta - 1), (2**self.eta) - 1)
        while p % 2 == 0:
            p = random.randint(2**(self.eta - 1), (2**self.eta) - 1)

        # Generate public key
        q0 = random.randrange(0, int((2**self.gamma) / p))
        x0 = p * q0
        pk = [x0]
        for i in range(1, self.tau + 1):
            xi = self.__D__(p)
            while x0 <= xi:
                # xi must be strictly smaller than x0
                xi = self.__D__(p)
            pk.append(xi)
        assert len(pk) == self.tau + 1

        return p, pk

    def enc(self, pk, m):
        # Sample a random subset S \in [1, tau]
        s = random.sample(range(1, self.tau + 1), random.randint(1, self.tau))

        # Sample a random int r <- (-2^(2_p), 2^(2_p))
        r = random.randint((-(2 ** (2 * self.rho))) + 1, (2 ** (2 * self.rho)) - 1)

        # Output c = (m + 2r + 2 \sum_{i \in S}(x_i))
        sum_x_i = 0

        for i in s:
            sum_x_i += pk[i]

        return mod(m + 2 * r + 2 * sum_x_i, pk[0])

    def eval(self, pk, P, *c):
        c_prime = P(*c)
        return mod(c_prime, pk[0])

    def dec(self, sk, c):
        return mod(mod(c, sk), 2)

    def __D__(self, p):
        q = random.randrange(0, int((2**self.gamma) / p))
        r = random.randrange(-(2**self.rho) + 1, 2**self.rho)
        return (p * q) + r


def quot(z, p):
    q, r = divmod(z, p)
    return q + round(r / p)


def mod(z, p):
    return z - quot(z, p) * p
