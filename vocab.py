from notes import *

# Unit One
ambulō = VerbVocab.first_conj('ambulō', definition='walk')
aqua = NounVocab('aqua', '-ae', 'F', definition='water')
clāmō = VerbVocab.first_conj('clāmō', definition='shout')
corōna = NounVocab('corōna', '-ae', 'F', definition='crown, wreath')
corōnō = VerbVocab.first_conj('corōnō', definition='crown (v.)')
cum = PrepVocab('cum', 'ablative', definition='with')
cūra = NounVocab('cūra', '-ae', 'F', definition='care, concern, anxiety')
dē = PrepVocab('dē', 'ablative', definition='concerning, about; (down) from')
dō = VerbVocab('dō', 'dare', 'dedī', 'datus', definition='give, grant')
dōnō = VerbVocab.first_conj('dōnō', definition='give, present, reward')
ē = PrepVocab(['ē', 'ex'], 'ablative', definition='out of, from')
enim = Vocab(definition='(postpositive conj.) indeed. of course; for')
et = Vocab(definition='(conj.) and')
et_et = Vocab(definition='(conj.s) both ... and') # et ... et
et = Vocab(definition='(adv.) even')
fāma = NounVocab('fāma', '-ae', 'F', definition='talk, report, rumor, fame, reputation')
fēmina = NounVocab('fēmina', '-ae', 'F', definition='woman')
fōrma = NounVocab('fōrma', '-ae', 'F', definition='form, shape, figure, beauty')
habeō = VerbVocab('habeō', '-ēre', 'habuī', 'habitus', definition='have, hold, possess, consider')
impleō = VerbVocab('impleō', '-ēre', 'implēvī', 'implētus', definition='fill, fill up')
in_acc = PrepVocab('in', 'accusative', definition='into, onto (motion toward)')
in_abl = PrepVocab('in', 'ablative', definition='in, on (place where)')
īnsula = NounVocab('īnsula', '-ae', 'F', definition='island')
nauta = NounVocab('nauta', '-ae', 'M', definition='sailor')
ne = Vocab(definition='(enclitic) when added to first word of clause, indicates question') # -ne
nōn = Vocab(definition='(adv.) not')
optō = VerbVocab.first_conj('optō', definition='desire, wish (for); choose')
patria = NounVocab('patria', '-ae', 'F', definition='native land, country')
pecūnia = NounVocab('pecūnia', '-ae', 'F', definition='money')
poena = NounVocab('poena', '-ae', 'F', definition='penalty, punishment')
poenās_dare = VerbVocab('poenās dō', 'poenās dare', 'poenās dedī', 'poenās datus', definition='to pay a penalty')
poēta = NounVocab('poēta', '-ae', 'M', definition='poet')
porta = NounVocab('porta', '-ae', 'F', definition='gate')
puella = NounVocab('puella', '-ae', 'F', definition='girl')
que = Vocab(definition='(enclitic) and') # -que
rēgīna = NounVocab('rēgīna', '-ae', 'F', definition='queen')
sed = Vocab(definition='(conj.) but')
sum_ = VerbVocab('sum', 'esse', 'fuī', 'futūrus', definition='be, exist')
taeda = NounVocab('taeda', '-ae', 'F', definition='torch')
terreō = VerbVocab('terreō', '-ēre', 'terruī', 'territus', definition='frighten, alarm, terrify')
timeō = VerbVocab('timeō', '-ēre', 'timuī', '--', definition='fear, be afraid (of)')
turba = NounVocab('turba', '-ae', 'F', definition='crowd, uproar')
via = NounVocab('via', '-ae', 'F', definition='way, road, path, street')
videō = VerbVocab('videō', '-ēre', 'vīdī', 'vīsus', definition='see')

# Unit Two
ā = PrepVocab(['ā', 'ab'], 'ablative', definition='(away) from; by (living being)')
ad = PrepVocab('ad', 'accusative', definition='to, towards')
anima = NounVocab('anima', '-ae', 'F', definition='soul, spirit, life force')
āra = NounVocab('āra', '-ae', 'F', definition='altar')
capiō = VerbVocab('capiō', '-ere', 'cēpī', 'captus', definition='take, capture')
cella = NounVocab('cella', '-ae', 'F', definition='storeroom, (small) room') # cell/ar
cēlō = VerbVocab.first_conj('cēlō', definition='hide, conceal')
cōgitō = VerbVocab.first_conj('cōgitō', definition='think, ponder, consider') # cognition
culpa = NounVocab('culpa', '-ae', 'F', definition='guilt, fault') # culpable
dāmnō = VerbVocab.first_conj('dāmnō', definition='condemn, sentence') # damn
dubitō = VerbVocab.first_conj('dubitō', definition='doubt, hesitate') # dubious
glōria = NounVocab('glōria', '-ae', 'F', definition='glory, renown') # []
incipiō = VerbVocab('incipiō', '-ere', 'incēpī', 'inceptus', definition='begin')
incola = NounVocab('incola', '-ae', 'M', definition='inhabitant')
incola_F = NounVocab('incola', '-ae', 'F', definition='inhabitant (occasionally F.)')
incolō = VerbVocab('incolō', '-ere', '-uī', '--', definition='inhabit')
īnsidiae = NounVocab('insidia', '-ae', 'F', definition='ambush, plot, treachery (used only in pl.)') # insidious
invidia = NounVocab('invidia', '-ae', 'F', definition='envy, jealousy')
labōrō = VerbVocab.first_conj('labōrō', definition='work') # labor
lacrima = NounVocab('lacrima', '-ae', 'F', definition='tear (as in teardrop)')
lūna = NounVocab('lūna', '-ae', 'F', definition='moon, moonlight') # lunar
moneō = VerbVocab('moneō', '-ēre', 'monuī', 'monitus', definition='warn, remind') # admonish
mora = NounVocab('mora', '-ae', 'F', definition='delay')
mūtō = VerbVocab.first_conj('mūtō', definition='change, exchange') # mutate
nātūra = NounVocab('nātūra', '-ae', 'F', definition='nature') # []
neque = nec = Vocab(definition='(conj.) nor; neither ... nor')
nihil = NounVocab('nihil', '--', 'N', definition='nothing')
nil = NounVocab('nil', '--', 'N', definition='nothing')
nisī = Vocab(definition='(conj.) unless, if ... not; except')
noxa = NounVocab('noxa', '-ae', 'F', definition='harm, injury') # noxious
nunc = Vocab(definition='(adv.) now')
pellō = VerbVocab('pellō', '-ere', 'pepulī', 'pulsus', definition='push, drive (off)') # pulse
expellō = VerbVocab('expellō', '-ere', 'expepulī', 'expulsus', definition='push out, drive out (ex + pellō)') # expel
per = PrepVocab('per', 'accusative', definition='through')
prōvincia = NounVocab('prōvincia', '-ae', 'F', definition='province') # []
semper = Vocab(definition='(adv.) always')
sententia = NounVocab('sententia', '-ae', 'F', definition='feeling, thought, opinion') # sentient
sentiō = VerbVocab('sentiō', '-īre', 'sēnsī', 'sēnsus', definition='feel, perceive') # sentient
si = Vocab(definition='(conj.) if')
sub_acc = PrepVocab('sub', 'accusative', definition='under (i.e. going under)')
sub_abl = PrepVocab('sub', 'ablative', definition='under (i.e. at/in a place under)')
superō = VerbVocab.first_conj('superō', definition='overcome, conquer') # superior
taceō = VerbVocab('taceō', '-ēre', 'tacuī', 'tacitus', definition='be (or keep) silent')
teneō = VerbVocab('teneō', '-ēre', 'tenuī', 'tentus', definition='hold, keep, possess')
terra = NounVocab('terra', '-ae', 'F', definition='earth, land') # []
unda = NounVocab('unda', '-ae', 'F', definition='wave') # undulate
veniō = VerbVocab('veniō', '-īre', 'vēnī', 'ventus', definition='come')
vīta = NounVocab('vīta', '-ae', 'F', definition='life') # vital

# Unit Three
acerbus = AdjVocab('acerbus', '-a', '-um', definition='bitter, harsh')
ager = NounVocab('ager', 'agrī', 'M', definition='field') # agriculture
audiō = VerbVocab('audiō', '-īre', '-īvī', '-ītus', definition='hear, listen (to)') # []
bellum = NounVocab('bellum', '-ī', 'N', definition='war') # bellerigent
bonus = AdjVocab('bonus', '-a', '-um', definition='good') # []
caecus = AdjVocab('caecus', '-a', '-um', definition='blind, hidden, secret')
campus = NounVocab('campus', '-ī', 'M', definition='plain, level surface') # []
clārus = AdjVocab('clārus', '-a', '-um', definition='bright, clear, famous') # clear
dexter = AdjVocab('dexter', 'dextra', 'dextrum', definition='right (not left), favorable') # dextrous
dextra = NounVocab('dextra', '-ae', 'F', definition='right hand') # dextrous
# ad dextram: to the right
dīligentia = NounVocab('dīligentia', '-ae', 'F', definition='diligence') # []
dōnum = NounVocab('dōnum', '-ī', 'N', definition='gift') # donation
gerō = VerbVocab('gerō', '-ere', 'gessī', 'gestus', definition='conduct, manage, wage') # gestate?
gladius = NounVocab('gladius', '-ī', 'M', definition='sword') # gladiator
laetus = AdjVocab('laetus', '-a', '-um', definition='happy')
līber = AdjVocab('līber', 'lībera', 'līberum', definition='free') # liberty
magnus = AdjVocab('magnus', '-a', '-um', definition='large, big, great') # magnitude
malus = AdjVocab('malus', '-a', '-um', definition='evil, bad, wicked') # malicious
Marcus = NounVocab('Marcus', '-ī', 'M', definition='proper name')
miser = AdjVocab('miser', 'misera', 'miserum', definition='miserable, unhappy, wretched') # miserable
multus = AdjVocab('multus', '-a', '-um', definition='much, many') # multiple
nātus = NounVocab('nātus', '-ī', 'M', definition='son') # natal
nē = Vocab(definition='(conj.) in purpose clauses, in order that ... not; in indirect commands, that ... not')
oculus = NounVocab('oculus', '-ī', 'M', definition='eye') # ocular
ōrō = VerbVocab.first_conj('ōrō', definition='beg (for)')
petō = VerbVocab('petō', '-ere', 'petīvī', 'petītus', definition='seek, ask for (needs ā + abl.)') # petition
portō = VerbVocab.first_conj('portō', definition='carry') # portable
puer = NounVocab('puer', 'puerī', 'M', definition='boy; child') # puerile
pūgnō = VerbVocab.first_conj('pūgnō', definition='fight; with cum + abl., fight against')
pulcher = AdjVocab('pulcher', 'pulchra', 'pulchrum', definition='beautiful') # ?
Rōmānus = AdjVocab('Rōmānus', '-a', '-um', definition='Roman') # []
saxum = NounVocab('saxum', '-ī', 'N', definition='rock, stone')
scrībō = VerbVocab('scrībō', '-ere', 'scrīpsī', 'scrīptus', definition='write') # script
servus = NounVocab('servus', '-ī', 'M', definition='slave') # servant
spectō = VerbVocab.first_conj('spectō', definition='look at') # spectate
ut = Vocab(definition='(conj.) in purpose clauses, in order that; in indirect commands, that')
validus = AdjVocab('validus', '-a', '-um', definition='strong, healthy') # valid
vēlum = NounVocab('vēlum', '-ī', 'N', definition='cloth, covering, sail') # []
# vela dare: set sail
venia = NounVocab('venia', '-ae', 'F', definition='indulgence, favor, kindness, (obliging) disposition')
ventus = NounVocab('ventus', '-ī', 'M', definition='wind') # vent
verbum = NounVocab('verbum', '-ī', 'N', definition='word') # verb
vir = NounVocab('vir', 'virī', 'M', definition='man') # wer

# Unit Four
aeternus = AdjVocab('aeternus', '-a', '-um', definition='eternal') # []
agō = VerbVocab('agō', '-ere', 'ēgī', 'āctus', definition='do (your job), drive, discuss, spend (time), conduct')
altus = AdjVocab('altus', '-a', '-um', definition='high, tall, deep') # altitude
amīcus = AdjVocab('amīcus', '-a', '-um', definition='friendly (+ dative)') # amicable
inimīcus = AdjVocab('inimīcus', '-a', '-um', definition='unfriendly, hostile (+ dative)') # enemy
caelum = NounVocab('caelum', '-ī', 'N', definition='heaven, sky')
cārus = AdjVocab('cārus', '-a', '-um', definition='dear (+ dative)')
cibus = NounVocab('cibus', '-ī', 'M', definition='food')
circum = PrepVocab('circum', 'accusative', definition='around') # circumstantial
dēleō = VerbVocab('dēleō', '-ēre', '-ēvī', '-ētus', definition='destroy')
deus = NounVocab('deus', '-ī', 'M', definition='a god, deity') # []
dea = NounVocab('dea', '-ae', 'F', definition='goddess')
dūcō = VerbVocab('dūcō', '-ere', 'dūxī', 'ductus', definition='lead; consider')
faciō = VerbVocab('faciō', '-ere', 'fēcī', 'factus', definition='make, do')
factum = NounVocab('factum', '-ī', 'N', definition='deed') # fact
fīlius = NounVocab('fīlius', '-ī', 'M', definition='son') # filial
fīlia = NounVocab('fīlia', '-ae', 'F', definition='daughter')
honestus = AdjVocab('honestus', '-a', '-um', definition='respected, honorable, distinguished')
intellegō = VerbVocab('intellegō', '-ere', 'intellēxī', 'intellēctus', definition='understand') # intelligence
legō = VerbVocab('legō', '-ere', 'lēgī', 'lēctus', definition='choose, select; read') # legible
liber = NounVocab('liber', 'librī', 'M', definition='book (NOT līber)') # library
littera = NounVocab('littera', '-ae', 'F', definition='letter (of the alphabet); pl., letter (epistle)')
mēnsa = NounVocab('mēnsa', '-ae', 'F', definition='table')
mittō = VerbVocab('mittō', '-ere', 'mīsī', 'missus', definition='send') # mission
mōnstrō = VerbVocab.first_conj('mōnstrō', definition='show, point out, demonstrate') # []
oppidum = NounVocab('oppidum', '-ī', 'N', definition='town')
perdō = VerbVocab('perdō', '-ere', 'perdidī', 'perditus', definition='destroy, lose, waste')
perīculum = NounVocab('perīculum', '-ī', 'N', definition='danger')
pōnō = VerbVocab('pōnō', '-ere', 'posuī', 'positus', definition='put, place, set aside') # posit
quod = Vocab(definition='(conj.) because')
rēgnum = NounVocab('rēgnum', '-ī', 'N', definition='realm, kingdom')
respondeō = VerbVocab('respondeō', '-ēre', 'respondī', 'respōnsus', definition='answer') # respond
studium = NounVocab('studium', '-ī', 'N', definition='enthusiasm, zeal') # studious
tegō = VerbVocab('tegō', '-ere', 'tēxī', 'tēctus', definition='cover, conceal')
tēctum = NounVocab('tēctum', '-ī', 'N', definition='roof, house')
trādō = VerbVocab('trādō', '-ere', 'trādidī', 'trāditus', definition='hand over, betray') # traitor
umbra = NounVocab('umbra', '-ae', 'F', definition='shadow') # umbra
urna = NounVocab('urna', '-ae', 'F', definition='urn') # []
vērus = AdjVocab('vērus', '-a', '-um', definition='true, real') # veritable
vēre = vērō = Vocab(definition='(adv.) truly, indeed')
videō = VerbVocab('videō', '-ēre', 'vīdī', 'vīsus', definition='see; (in passive) seem, _as well as_ be seen')
vīlla = NounVocab('vīlla', '-ae', 'F', definition='country house, farmhouse')

# Unit Five
ante = PrepVocab('ante', 'accusative', definition='before, in front of') # antecedent
ante = Vocab(definition='(adv.) before, previously')
antīquus = AdjVocab('antīquus', '-a', '-um', definition='ancient') # antique
ardeō = VerbVocab('ardeō', '-ēre', 'arsī', 'arsus', definition='burn, be on fire; desire') # arson
# NOTE: arma, armōrum, N. is never found in the singular
arma = NounVocab('armum', '-ī', 'N', definition='arms, weapons') # []
aurum = NounVocab('aurum', '-ī', 'N', definition='gold') # Au
aureus = AdjVocab('aureus', '-a', '-um', definition='golden, of gold') # Au
autem = Vocab(definition='(postpositive conj.) however, moreover')
bene = Vocab(definition='(adv.) well')
canō = VerbVocab('canō', '-ere', 'cecinī', 'cantus', definition='sing (of)') # cant
cēdō = VerbVocab('cēdō', '-ere', 'cessī', 'cessus', definition='go, move, yield') # cede, cease
accēdō = VerbVocab('accēdō', '-ere', 'accessī', 'accessus', definition='go to, approach') # accede, access
discēdō = VerbVocab('discēdō', '-ere', 'discēssī', 'discessus', definition='go from, depart, leave') # discuss?
dēbeō = VerbVocab('dēbeō', '-ēre', 'dēbuī', 'dēbitus', definition='owe, ought') # debit/debt
dominus = NounVocab('dominus', '-ī', 'M', definition='master, lord') # dominate
dūrus = AdjVocab('dūrus', '-a', '-um', definition='hard, harsh') # durable
ferrum = NounVocab('ferrum', '-ī', 'N', definition='iron, sword') # ferrite
flamma = NounVocab('flamma', '-ae', 'F', definition='flame, fire') # []
imperium = NounVocab('imperium', '-ī', 'N', definition='authority, power, empire') # imperial
imperō = VerbVocab.first_conj('imperō', definition='give (an) order(s), give (a) command(s)') # imperative
# ^ the person ordered is in the dative; the thing ordered is expressed with a purpose clause
interficiō = VerbVocab('interficiō', '-ere', 'interfēcī', 'interfectus', definition='kill') # interfere?
invādō = VerbVocab('invādō', '-ere', 'invāsī', 'invāsus', definition='go into, invade, attack') # []
magister = NounVocab('magister', 'magistrī', 'M', definition='superior, director, master, teacher') # magistrate
medius = AdjVocab('medius', '-a', '-um', definition='middle of, middle') # median
moveō = VerbVocab('moveō', '-ēre', 'mōvī', 'mōtus', definition='move') # []
removeō = VerbVocab('removeō', '-ēre', 'remōvī', 'remōtus', definition='remove, take away, set aside') # [], remote
mox = Vocab(definition='(adv.) soon')
nōscō = VerbVocab('nōscō', '-ere', 'nōvī', 'nōtus', definition='learn, (in perfect) know')
cognōscō = VerbVocab('cognōscō', '-ere', 'cognōvī', 'cognitus', definition='learn, (in perfect) know') # cognitive
novus = AdjVocab('novus', '-a', '-um', definition='new, strange')
numquam = nunquam = Vocab(definition='(adv.) never')
umquam = unquam = Vocab(definition='(adv.) ever')
pius = AdjVocab('pius', '-a', '-um', definition='loyal, dutiful, pious') # []
impius = AdjVocab('impius', '-a', '-um', definition='irreverant, wicked, impious') # []
populus = NounVocab('populus', '-ī', 'M', definition='people') # populus
possum = VerbVocab('possum', 'posse', 'potuī', '--', definition='be able, can')
post = PrepVocab('post', 'accusative', definition='after, behind')
post = Vocab(definition='(adv.) afterwards, after, behind')
postquam = Vocab(definition='(conj.) after (+ indicative)')
quamquam = Vocab(definition='(conj.) although (+ indicative)')
ruīna = NounVocab('ruīna', '-ae', 'F', definition='fall, downfall, ruin, destruction') # []
ruō = VerbVocab('ruō', '-ere', 'ruī', 'rutus', definition='fall, go to ruin, rush') # [], rue?
sine = PrepVocab('sine', 'ablative', definition='without')
socius_adj = AdjVocab('socius', '-a', '-um', definition='allied') # society
socius_n = NounVocab('socius', '-ī', 'M', definition='ally') # society
tamen = Vocab(definition='(adv.) nevertheless')
vīvō = VerbVocab('vīvō', '-ere', 'vīxī', 'vīctus', definition='be alive, live') # vivid
vocō = VerbVocab.first_conj('vocō', definition='call') # vocal

# Unit Six
animal = NounVocab('animal', 'animālis', 'N', True, definition='animal') # []
Athēnae = NounVocab('Athēna', '-ae', 'F', definition='Athens (plural only)')
atque = ac = Vocab(definition='(conj.) and')
aurōra = NounVocab('aurōra', '-ae', 'F', definition='dawn') # aurora
careō = VerbVocab('careō', '-ēre', '-uī', '-itus', definition='lack, be without (+ abl.)')
corpus = NounVocab('corpus', 'corporis', 'N', definition='body') # corpse
dīcō = VerbVocab('dīcō', '-ere', 'dīxī', 'dictus', definition='say, tell, speak') # dictate
diū = Vocab(definition='(adv.) for a long time')
domus = NounVocab('domus', '-ī', 'F', definition='house, home') # domicile
exemplar = NounVocab('exemplar', 'exemplāris', 'N', True, definition='copy, model, example') # []
exemplum = NounVocab('exemplum', '-ī', 'N', definition='example') # []
frāter = NounVocab('frāter', 'frātris', 'M', definition='brother') # fraternal
homō = NounVocab('homō', 'hominis', 'M', definition='human being, man') # hominid
ignis = NounVocab('ignis', 'ignis', 'M', True, definition='fire') # ignite
Italia = NounVocab('Italia', '-ae', 'F', definition='Italy') # []
Iūnō = NounVocab('Iūnō', 'Iūnōnis', 'F', definition='Juno (sister and wife of Jupiter)') # []
Iuppiter = NounVocab('Iuppiter', 'Iovis', 'M', definition='Jupiter (god of the sky)') # []
līberō = VerbVocab.first_conj('līberō', definition='free') # liberate
lūmen = NounVocab('lūmen', 'lūminis', 'N', definition='light') # illuminate
mare = NounVocab('mare', 'maris', 'N', True, definition='sea') # Mare Nostrum
māter = NounVocab('māter', 'mātris', 'F', definition='mother') # maternal
mēns = NounVocab('mēns', 'mentis', 'F', True, definition='mind, disposition, intellect') # mental
mīles = NounVocab('mīles', 'mīlitis', 'M', definition='soldier') # military
moenia = NounVocab('moenia', 'moenis', 'N', True, definition='(city) walls (plural only)')
mōns = NounVocab('mōns', 'montis', 'M', True, definition='mountain') # []
nōn_sōlum_sed_etiam = Vocab(definition='(idiom) not only ... but also') # nōn sōlum ... sed etiam
nox = NounVocab('nox', 'noctis', 'F', True, definition='night') # nocturnal
oppūgnō = VerbVocab.first_conj('oppūgnō', definition='attack, fight against') # oppose
pater = NounVocab('pater', 'patris', 'M', definition='father') # paternal
regō = VerbVocab('regō', '-ere', 'rēxī', 'rēctus', definition='rule') # reign
rēx = NounVocab('rēx', 'rēgis', 'M', definition='king') # T. Rex
Rōma = NounVocab('Rōma', '-ae', 'F', definition='Rome') # []
rūmor = NounVocab('rūmor', 'rūmōris', 'M', definition='rumor, gossip') # []
rūs = NounVocab('rūs', 'rūris', 'N', definition='country (as opposed to city)') # rural
sānus = AdjVocab('sānus', '-a', '-um', definition='sound, healthy, sane') # []
sciō = VerbVocab('sciō', '-īre', '-īvī', '-ītus', definition='know') # scry?
servitūs = NounVocab('servitūs', 'servitūtis', 'F', definition='slavery') # servitude
sīdus = NounVocab('sīdus', 'sīderis', 'N', definition='constellation, star; heaven')
soror = NounVocab('soror', 'sorōris', 'F', definition='sister') # sorority
spargō = VerbVocab('spargō', '-ere', 'sparsī', 'sparsus', definition='scatter, sprinkle, distribute') # sparse
timor = NounVocab('timor', 'timōris', 'M', definition='fear, dread') # tremor
urbs = NounVocab('urbs', 'urbis', 'F', True, definition='city') # urban
vigor = NounVocab('vigor', 'vigōris', 'M', definition='liveliness, activity, vigor') # []
vīs = NounVocab('vīs', 'vīris', 'F', definition='(sg.) force, power; (pl.) strength')
