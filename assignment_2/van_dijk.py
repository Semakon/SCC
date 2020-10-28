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
        print("s", s)
        # Sample a random int r <- (-2^(2_p), 2^(2_p))
        r = random.randint((-(2 ** (2 * self.rho))) + 1, (2 ** (2 * self.rho)) - 1)
        print("r", r)

        # Output c = (m + 2r + 2 \sum_{i \in S}(x_i))
        sum_x_i = 0
        for i in s:
            sum_x_i += pk[i]
        print("sum", sum_x_i)

        return (m + (2 * r) + (2 * sum_x_i)) % pk[0]

    def eval(self, pk, P, c):
        c_prime = P(c)
        return c_prime % pk[0]

    def dec(self, sk, c):
        return (c % sk) % 2

    def __D__(self, p):
        q = random.randrange(0, int((2**self.gamma) / p))
        r = random.randrange(-(2**self.rho) + 1, 2**self.rho)
        return (p * q) + r


if __name__ == "__main__":
    test = VanDijk(100, 1000, 10, 10)
    pk = [
            1159864900974717219462642652227635172877237865623257364869817203338617235757126001139582988772899467120127679433150759155900173965172424591477202078839780869412367482889139835055391616989645100133490183333558496313317651981496839237950729025597429061336472935812620666958297809018047458351868144416307,
            951122382877629164982429034031218119467164795760371553689221773679078971495552537163173741107955904424735015457792007635912735838325567966509121131422842055780378487761268270917395618134136023239890421951172476531585234084431414950906618367700012908697750959442651193692174961980218719160178878466940,
            827550438108775745335623493613439735657370990924454138176398729571038688800756481963645825193998722861141901553423010446605780443898196875261277888767319955741020567126861315798120213575654757387387284747002951325142525959253660085413458331705585876517999676714571498663525615968680993134711496452831,
            617035609567423008350230202908022390751388164319301385789365789818107798346047815268396668414277018638777368064010084625608775021902086633327466988233699175788765152711224549290506966812251017680687377664556764935072939720764561591087182244934506274292700396443212854569868372961795524043215913511829,
            560963368066864962756870352618395880724557837373289760920083029506658995021951393071958052368553037333281951118954001049956341307390914363509201889395119669634421158959198669624086443112692216132976746267974358845990367035513013625313563107014868975018715406357122234724616320022789372288771098908415,
            203738824957240897654775650433602772149893641665445011474876539461749611172067442918458124319407488735468746467093692170249452278392419862653866941288624633974824874746268945333358586096888367073324966307125126417015780393402478335895178453840798496047930892780523252219063203703185076581671368734021,
            397227426122872419382256883791972010469443501252969285278061545922745159208338729466255620969755712291635439996615576070168909629958059597673868874123442807722008435893931788662316837335373099798371923000207421145140038621284430208902175373888333842332255037700809092616840210556325479795776412939991,
            448174558257515580352811177132998088170017900757520815207706439424112832970907306065378912206930127895183015163888206075183143636911431368436860857590553911557042623654684384823655432614169479039249664252351213814300429868873585923046361286963254887942690967030493651936519753271405053363635335301454,
            750385328854053573821669787653017000518569489865034582881045854097464322196326162796505973561317418042030736973375315588645913722814485958740370349415644939153807101710151817282564684015551813238423189016840901983127430263155221926009211145980120134060943564008117781725967345442705435281961676954713,
            199126715051203967211650660341499563117734067249217803278320378898265448012291453600925571342506648333188106670916045569409986195886718433804258737559820210222370536678872301118264337227722323661046420569237664706978492445547227635853684937759124653857527961792092891583564969016718967785846042217287,
            156178209009610253410234534866223643858135372428715117407896928363685325265378211879260175060061843019505302012813456452932966303036740911901285640666601525837601220535435057473346462743361129712820393940119843480074685049658111740474465813028840203352729689016024180101779844503204839624084717746262
          ]
    sk = 1158800203735514989515375466831
    plaintext = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    ciphertext = []
    for m in plaintext:
        ciphertext.append(test.enc(pk, m))

    decrypted = []
    for c in ciphertext:
        decrypted.append(test.dec(sk, c))

    print(plaintext)
    print(ciphertext)
    print(decrypted)
