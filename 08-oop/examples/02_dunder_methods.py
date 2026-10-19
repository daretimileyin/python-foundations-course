"""Example 02 – Dunder (special) methods."""


class Money:
    def __init__(self, amount, currency="NGN"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.currency} {self.amount:,.2f}"

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Can't add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        return self.amount < other.amount


class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs or []

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs


a = Money(1500)
b = Money(2500.5)
print("a =", a)
print("repr(b) =", repr(b))
print("a + b =", a + b)
print("a == Money(1500)?", a == Money(1500))
print("Sorted:", sorted([b, a]))

p = Playlist("Afrobeats", ["Essence", "Calm Down", "Last Last"])
print(f"\n{p.name} has {len(p)} songs")
print("First song:", p[0])
print("'Calm Down' in playlist?", "Calm Down" in p)
for song in p:
    print(" 🎵", song)
