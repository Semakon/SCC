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
        pass

    def eval(self, pk, P, c):
        pass

    def dec(self, sk, c):
        pass

    def __D__(self, p):
        q = random.randrange(0, int((2**self.gamma) / p))
        r = random.randrange(-(2**self.rho) + 1, 2**self.rho)
        return (p * q) + r


test = VanDijk(100, 1000, 10, 10)
print(test.key_gen())
